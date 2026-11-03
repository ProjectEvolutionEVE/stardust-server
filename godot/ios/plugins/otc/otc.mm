// Security-code AutoFill on the iPhone (Eric 11-03): when a sign-in code arrives by text or email, iOS offers it above
// the keyboard ("From Messages: 123456") and one tap fills the box, as in every other app. Godot's keyboard field never
// tells iOS it wants a one-time code, so iOS never offered it. The sign-in code box is the only field that opens the
// number pad, so whenever Godot's field opens the number pad we mark it as a one-time-code field. Godot sets the field's
// content type itself, so it is set again after Godot opens the field, which is then reloaded.
#import <UIKit/UIKit.h>
#import <objc/runtime.h>
#include <stdio.h>
#include <stdarg.h>

// DIAGNOSTIC 11-03: everything is also written to Documents/otc-log.txt in the app, fetched over the cable afterwards.
static void otc_print(const char *fmt, ...) {
    char buf[1024];
    va_list ap; va_start(ap, fmt); vsnprintf(buf, sizeof buf, fmt, ap); va_end(ap);
    fputs(buf, stderr);
    NSString *dir = NSSearchPathForDirectoriesInDomains(NSDocumentDirectory, NSUserDomainMask, YES).firstObject;
    FILE *f = fopen([[dir stringByAppendingPathComponent:@"otc-log.txt"] UTF8String], "a");
    if (f) { fputs(buf, f); fclose(f); }
}

static BOOL otc_is_code(id self) {
    UIKeyboardType k = [(id<UITextInputTraits>)self keyboardType];
    return k == UIKeyboardTypeNumberPad || k == UIKeyboardTypeASCIICapableNumberPad;
}

static void otc_log(id self, const char *where) {
    UITextView *v = (UITextView *)self;
    otc_print("[otc] %s keyboardType=%ld contentType=%s hidden=%d first=%d frame=%s autocorrect=%ld\n", where,
            (long)v.keyboardType, v.textContentType ? v.textContentType.UTF8String : "nil", v.hidden, v.isFirstResponder,
            NSStringFromCGRect(v.frame).UTF8String, (long)v.autocorrectionType);
}

// iOS offers AutoFill only to a field that is on screen, and Godot keeps its field hidden at zero size. For the code box
// it's shown at 2x2 points with clear text, cursor and background: still invisible, but iOS now treats it as a field.
static void otc_show_for_autofill(UITextView *v, BOOL code) {
    if (code) {   // DIAGNOSTIC 11-03: fully visible white box near the top, to learn whether visibility is what blocks AutoFill
        v.hidden = NO;
        v.frame = CGRectMake(20, 52, 300, 40);
        v.alpha = 1.0;
        v.backgroundColor = UIColor.whiteColor;
        v.textColor = UIColor.blackColor;
        v.tintColor = UIColor.blueColor;
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

static void otc_log_pasteboard(const char *where) {
    UIPasteboard *p = UIPasteboard.generalPasteboard;   // types and hasStrings never trigger the paste prompt
    otc_print("[otc] pasteboard at %s: hasStrings=%d items=%ld types=%s\n", where, p.hasStrings, (long)p.numberOfItems,
            [[p.pasteboardTypes componentsJoinedByString:@","] UTF8String]);
}

static void (*otc_original_paste)(id, SEL, id);
static void otc_paste(id self, SEL _cmd, id sender) {
    otc_log_pasteboard("field paste");
    otc_original_paste(self, _cmd, sender);
    otc_print("[otc] field text after paste: %lu chars\n", (unsigned long)((UITextView *)self).text.length);
}

@interface StardustOneTimeCode : NSObject
@end

@implementation StardustOneTimeCode
+ (void)load {
    Class c = NSClassFromString(@"GDTKeyboardInputView");   // Godot's hidden keyboard field
    otc_print("[otc] load: GDTKeyboardInputView %s\n", c ? "found" : "NOT FOUND");
    if (!c) return;
    otc_original_become_with = (BOOL (*)(id, SEL, NSString *, NSInteger, NSInteger))
        otc_swap(c, @selector(becomeFirstResponderWithString:cursorStart:cursorEnd:), (IMP)otc_become_with);
    otc_print("[otc] hook: becomeFirstResponderWithString %s\n", otc_original_become_with ? "ok" : "MISSING");
    otc_original_paste = (void (*)(id, SEL, id))otc_swap(c, @selector(paste:), (IMP)otc_paste);
    [[NSNotificationCenter defaultCenter] addObserverForName:UIApplicationDidBecomeActiveNotification object:nil queue:nil
        usingBlock:^(NSNotification *n) { otc_log_pasteboard("app active"); }];
}
@end

void stardust_otc_init() {}     // Godot calls these (as C++) when the plugin starts and stops; the work is done in +load
void stardust_otc_deinit() {}
