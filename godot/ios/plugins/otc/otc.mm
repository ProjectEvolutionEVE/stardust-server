// Security-code AutoFill on the iPhone (Eric 11-03): when a sign-in code arrives by text or email, iOS offers it above
// the keypad ("From Messages: 123456") and one tap fills the box, as in every other app.
//
// iOS offers codes only to a standard text field (UITextField) marked as a one-time-code field. Godot types through its
// own hidden UITextView, which iOS never offers a code to, even when marked and visible (checked on Eric's iPhone, 11-03).
// So when Godot opens the number pad (only the sign-in code box uses it), a standard field takes the keypad instead:
// invisible, marked as a one-time-code field. What it receives (typed, pasted or AutoFilled) is passed on to Godot's
// field as if typed, so the code box fills; at 6 digits the keypad closes. When Godot closes its keypad, so does ours.
#import <UIKit/UIKit.h>
#import <objc/runtime.h>
#include <stdio.h>
#include <stdarg.h>

// Messages go to the device console (xcrun devicectl device process launch --console). To log to a file on the phone
// for a test, also append to Documents/otc-log.txt here and fetch it with xcrun devicectl device copy from.
static void otc_print(const char *fmt, ...) {
    va_list ap; va_start(ap, fmt); vfprintf(stderr, fmt, ap); va_end(ap);
}

@interface StardustCodeField : UITextField
@property (nonatomic, weak) UITextView *godot;      // Godot's own keyboard field, the one the game listens to
@property (nonatomic, copy) NSString *sent;          // what has already been passed on to Godot
@end

static StardustCodeField *otc_field;
static BOOL otc_taking;                              // true while our field takes the keypad over from Godot's
static BOOL (*otc_original_become_with)(id, SEL, NSString *, NSInteger, NSInteger);
static BOOL (*otc_original_resign)(id, SEL);

@implementation StardustCodeField
- (void)changed {
    NSString *now = self.text ?: @"";
    NSString *was = self.sent ?: @"";
    // pass the difference on to Godot as typing: delete what changed, then type the rest
    NSUInteger same = 0;
    while (same < now.length && same < was.length && [now characterAtIndex:same] == [was characterAtIndex:same]) same++;
    for (NSUInteger i = same; i < was.length; i++) [self.godot deleteBackward];
    if (now.length > same) [self.godot insertText:[now substringFromIndex:same]];
    self.sent = now;
    otc_print("[otc] code field: %lu characters passed to Godot\n", (unsigned long)now.length);
    if (now.length >= 6) [self resignFirstResponder];   // all 6 in: the keypad goes away
}
@end

static BOOL otc_is_code(id view) {
    UIKeyboardType k = [(id<UITextInputTraits>)view keyboardType];
    return k == UIKeyboardTypeNumberPad || k == UIKeyboardTypeASCIICapableNumberPad;
}

static BOOL otc_become_with(id self, SEL _cmd, NSString *s, NSInteger a, NSInteger b) {
    BOOL r = otc_original_become_with(self, _cmd, s, a, b);
    if (!otc_is_code(self)) return r;
    UITextView *g = (UITextView *)self;
    if (!otc_field) {
        otc_field = [[StardustCodeField alloc] initWithFrame:CGRectMake(0, 0, 1, 1)];
        otc_field.keyboardType = UIKeyboardTypeNumberPad;
        otc_field.textContentType = UITextContentTypeOneTimeCode;
        otc_field.autocorrectionType = UITextAutocorrectionTypeNo;
        otc_field.textColor = UIColor.clearColor;
        otc_field.tintColor = UIColor.clearColor;
        otc_field.backgroundColor = UIColor.clearColor;
        [otc_field addTarget:otc_field action:@selector(changed) forControlEvents:UIControlEventEditingChanged];
    }
    if (otc_field.superview != g.superview) {
        [otc_field removeFromSuperview];
        [g.superview addSubview:otc_field];
    }
    otc_field.godot = g;
    otc_field.text = s ?: @"";
    otc_field.sent = otc_field.text;
    otc_taking = YES;
    BOOL took = [otc_field becomeFirstResponder];
    otc_taking = NO;
    otc_print("[otc] code box: standard field took the keypad=%d\n", took);
    return r;
}

static BOOL otc_resign(id self, SEL _cmd) {
    if (!otc_taking && otc_field.isFirstResponder && otc_field.godot == self) {
        otc_print("[otc] Godot closed its keypad: closing ours\n");
        [otc_field resignFirstResponder];
    }
    return otc_original_resign(self, _cmd);
}

static IMP otc_swap(Class c, SEL sel, IMP imp) {
    Method m = class_getInstanceMethod(c, sel);
    if (!m) return NULL;
    IMP old = method_getImplementation(m);
    if (!class_addMethod(c, sel, imp, method_getTypeEncoding(m)))
        method_setImplementation(m, imp);
    return old;
}

@interface StardustOneTimeCode : NSObject
@end

@implementation StardustOneTimeCode
+ (void)load {
    Class c = NSClassFromString(@"GDTKeyboardInputView");   // Godot's hidden keyboard field
    if (!c) { otc_print("[otc] Godot's keyboard field not found\n"); return; }
    otc_original_become_with = (BOOL (*)(id, SEL, NSString *, NSInteger, NSInteger))
        otc_swap(c, @selector(becomeFirstResponderWithString:cursorStart:cursorEnd:), (IMP)otc_become_with);
    otc_original_resign = (BOOL (*)(id, SEL))otc_swap(c, @selector(resignFirstResponder), (IMP)otc_resign);
    otc_print("[otc] ready: open=%d close=%d\n", otc_original_become_with != NULL, otc_original_resign != NULL);
}
@end

void stardust_otc_init() {}     // Godot calls these (as C++) when the plugin starts and stops; the work is done in +load
void stardust_otc_deinit() {}
