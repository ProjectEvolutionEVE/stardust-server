// Security-code AutoFill on the iPhone (Eric 11-03): when a sign-in code arrives by text or email, iOS offers it above
// the keyboard ("From Messages: 123456") and one tap fills the box, as in every other app. Godot's keyboard field never
// tells iOS it wants a one-time code, so iOS never offered it. The sign-in code box is the only field that opens the
// number pad, so whenever Godot's field opens the number pad we mark it as a one-time-code field.
#import <UIKit/UIKit.h>
#import <objc/runtime.h>

static BOOL (*otc_original_become)(id, SEL);

static BOOL otc_become(id self, SEL _cmd) {
    UIKeyboardType k = [(id<UITextInputTraits>)self keyboardType];
    BOOL code = (k == UIKeyboardTypeNumberPad || k == UIKeyboardTypeASCIICapableNumberPad);
    [(UITextView *)self setTextContentType:(code ? UITextContentTypeOneTimeCode : nil)];
    return otc_original_become(self, _cmd);
}

@interface StardustOneTimeCode : NSObject
@end

@implementation StardustOneTimeCode
+ (void)load {
    Class c = NSClassFromString(@"GDTKeyboardInputView");   // Godot's hidden keyboard field
    if (!c) return;
    Method m = class_getInstanceMethod(c, @selector(becomeFirstResponder));
    otc_original_become = (BOOL (*)(id, SEL))method_getImplementation(m);
    if (!class_addMethod(c, @selector(becomeFirstResponder), (IMP)otc_become, method_getTypeEncoding(m)))
        method_setImplementation(m, (IMP)otc_become);
}
@end

void stardust_otc_init() {}     // Godot calls these (as C++) when the plugin starts and stops; the work is done in +load
void stardust_otc_deinit() {}
