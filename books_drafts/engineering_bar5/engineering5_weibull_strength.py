"""Weibull Statistics of Brittle Strength: why a bigger brittle part is more likely to contain a weak spot."""
CODE = "engineering5_weibull_strength"
BOOK = {
    "title": "Weibull Statistics of Brittle Strength",
    "subtitle": "Why a bigger brittle part is more likely to contain a weak spot",
    "chapters": [
        ("Brittle materials vary",
         "Ceramics and glass break at flaws, and no two pieces have exactly the same flaws. Their strength is therefore a spread of values, not one number."),
        ("Size effects",
         "A larger part has more flaws, so it is more likely to break at a lower stress. This is the size effect."),
        ("The weakest link",
         "A brittle part behaves like a chain. It fails at its weakest link, which is the largest flaw under the highest stress."),
        ("The Weibull modulus",
         "The Weibull modulus describes how spread out the strengths are. A high modulus means the strengths cluster tightly, and a low one means they scatter widely."),
        ("Testing ceramics and glass",
         "Many specimens are broken in test, and their strengths are plotted to fit a Weibull distribution. The fit gives the modulus and a characteristic strength."),
        ("Design allowables",
         "Designers choose an allowable stress with a low chance of failure, based on the fitted distribution and the size of the part. Ceramic parts are designed with this statistical margin."),
    ],
    "test": [
        ("Why do brittle materials show a spread of strengths?",
         [("a", "They never break"), ("b", "They are very heavy"), ("c", "They are all the same colour"), ("d", "They have different flaws")], "d"),
        ("What is the size effect?",
         [("a", "Size changes colour"), ("b", "Size has no effect"), ("c", "Bigger parts are more likely to contain a weak spot"), ("d", "Bigger parts are always stronger")], "c"),
        ("What does the weakest link idea mean?",
         [("a", "A brittle part fails at its largest flaw under the highest stress"), ("b", "Strong parts never fail"), ("c", "All links are equal"), ("d", "Chains are painted")], "a"),
        ("What does a high Weibull modulus mean?",
         [("a", "Strengths scatter widely"), ("b", "Strengths cluster tightly"), ("c", "The part is very heavy"), ("d", "The part is painted")], "b"),
        ("What is a design allowable?",
         [("a", "A stress chosen with a low chance of failure"), ("b", "A paint colour"), ("c", "A sale price"), ("d", "A test date")], "a"),
    ],
}
