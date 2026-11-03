// Security-code AutoFill on the iPhone (Eric 11-03): when a sign-in code arrives by text or email, iOS offers it above
// the keyboard ("From Messages: 123456") and one tap fills the box, as in every other app. Godot's keyboard field never
// tells iOS it wants a one-time code, so iOS never offered it. The sign-in code box is the only field that opens the
// number pad, so whenever Godot's field opens the number pad we mark it as a one-time-code field. Godot sets the field's
// content type itself, so it is set again after Godot opens the field, which is then reloaded.
#import <UIKit/UIKit.h>
#import <objc/runtime.h>
#include <stdio.h>

static BOOL otc_is_code(id self) {
    UIKeyboardType k = [(id<UITextInputTraits>)self keyboardType];
    return k == UIKeyboardTypeNumberPad || k == UIKeyboardTypeASCIICapableNumberPad;
}

static void otc_log(id self, const char *where) {
    UITextView *v = (UITextView *)self;
    fprintf(stderr, "[otc] %s keyboardType=%ld contentType=%s hidden=%d first=%d frame=%s autocorrect=%ld\n", where,
            (long)v.keyboardType, v.textContentType ? v.textContentType.UTF8String : "nil", v.hidden, v.isFirstResponder,
            NSStringFromCGRect(v.frame).UTF8String, (long)v.autocorrectionType);
}

// iOS offers AutoFill only to a field that is on screen, and Godot keeps its field hidden at zero size. For the code box
// it's shown at 2x2 points with clear text, cursor and background: still invisible, but iOS now treats it as a field.
static void otc_show_for_autofill(UITextView *v, BOOL code) {
    if (code) {
        v.hidden = NO;
        v.frame = CGRectMake(0, 0, 2, 2);
        v.alpha = 0.02;
        v.backgroundColor = UIColor.clearColor;
        v.textColor = UIColor.clearColor;
        v.tintColor = UIColor.clearColor;
    } else {
        v.hidden = YES;
        v.frame = CGRectZero;
    }
}

static BOOL (*otc_original_become_with)(id, SEL, NSString *, NSInteger, NSInteger);
static BOOL otc_become_with(id self, SEL _cmd, NSString *s, NSInteger a, NSInteger b) {
    if (otc_is_code(self))
        [(UITextView *)self setTextContentType:UITextContentTypeOneTimeCode];
    otc_show_for_autofill((UITextView *)self, otc_is_code(self));
    otc_log(self, "before");
    BOOL r = otc_original_become_with(self, _cmd, s, a, b);
    otc_show_for_autofill((UITextView *)self, otc_is_code(self));
    if (otc_is_code(self) && ![((UITextView *)self).textContentType isEqualToString:UITextContentTypeOneTimeCode]) {
        [(UITextView *)self setTextContentType:UITextContentTypeOneTimeCode];
        [(UITextView *)self reloadInputViews];
    }
    otc_log(self, "after");
    return r;
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
    fprintf(stderr, "[otc] load: GDTKeyboardInputView %s\n", c ? "found" : "NOT FOUND");
    if (!c) return;
    otc_original_become_with = (BOOL (*)(id, SEL, NSString *, NSInteger, NSInteger))
        otc_swap(c, @selector(becomeFirstResponderWithString:cursorStart:cursorEnd:), (IMP)otc_become_with);
    fprintf(stderr, "[otc] hook: becomeFirstResponderWithString %s\n", otc_original_become_with ? "ok" : "MISSING");
}
@end

void stardust_otc_init() {}     // Godot calls these (as C++) when the plugin starts and stops; the work is done in +load
void stardust_otc_deinit() {}
