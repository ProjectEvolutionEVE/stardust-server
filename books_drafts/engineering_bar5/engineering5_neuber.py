"""Notch Analysis: Neuber's Rule. Estimating the real strain at a sharp notch from the elastic answer."""
CODE = "engineering5_neuber"
BOOK = {
    "title": "Notch Analysis: Neuber's Rule",
    "subtitle": "Estimating the real strain at a sharp notch from the elastic answer",
    "chapters": [
        ("Stress at a notch",
         "A sharp notch raises the elastic stress at its root by the stress concentration factor. Fatigue cracks often start at such points."),
        ("Local yielding",
         "If the notch root yields, the local strain can be much larger than the elastic estimate suggests. To predict life, engineers need the local strain, not just the stress."),
        ("Neuber's approximation",
         "Neuber's rule says that the product of the local stress and local strain equals the square of the elastic stress concentration times the nominal stress and strain. It gives a practical estimate of the local values."),
        ("Notch sensitivity",
         "Some materials are less affected by notches than the elastic factor suggests. Notch sensitivity measures how far the real reduction in strength or life falls short of the full factor."),
        ("Fatigue at notches",
         "Combining Neuber's rule with a strain-life curve predicts how many cycles a notched part can take. This is more realistic than using the elastic stress alone."),
        ("Practical checks",
         "Use the rule for moderate yielding, and check larger yielding against tests. Rounding a notch or increasing its radius lowers the peak stress."),
    ],
    "test": [
        ("What raises the stress at the root of a sharp notch?",
         [("a", "Paint"), ("b", "Cold water"), ("c", "Stress concentration"), ("d", "Sunshine")], "c"),
        ("Why is local strain important at a notch?",
         [("a", "It is never important"), ("b", "If the root yields, local strain can be much larger than the elastic estimate"), ("c", "It shows the colour"), ("d", "It counts bolts")], "b"),
        ("What does Neuber's rule relate?",
         [("a", "Colour to weight"), ("b", "Cost to time"), ("c", "Sound to light"), ("d", "Local stress times local strain to the elastic values")], "d"),
        ("What does notch sensitivity measure?",
         [("a", "How far the real reduction falls short of the full elastic factor"), ("b", "The price of notches"), ("c", "The paint thickness"), ("d", "The number of holes")], "a"),
        ("What lowers the peak stress at a notch?",
         [("a", "Making it sharper"), ("b", "Rounding the notch or increasing its radius"), ("c", "Adding paint"), ("d", "Removing supports")], "b"),
    ],
}
