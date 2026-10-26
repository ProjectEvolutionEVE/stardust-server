"""Floating-Point Numbers: why 0.1 plus 0.2 is not quite 0.3, and how to keep money exact."""
CODE = "computing3c_floating_point"
BOOK = {
    "title": "Floating-Point Numbers",
    "subtitle": "Why 0.1 plus 0.2 is not quite 0.3, and how to keep money exact",
    "chapters": [
        ("Numbers in a box",
         "A computer stores a number in a fixed number of bits. Whole numbers fit exactly, up to a limit. Many decimal fractions do not fit exactly, so the computer stores the closest value it can."),
        ("Floating point",
         "A floating-point number is stored as a sign, a set of significant digits and a power of two. The point can float to a different place, so one format covers very large and very small numbers. The price is that some values are only approximate."),
        ("Almost, but not quite",
         "Many decimal fractions, such as 0.1, cannot be written exactly in binary. Just as one third cannot be written exactly in decimal. So 0.1 plus 0.2 gives 0.30000000000000004 in most programming languages. The answer is close, but not exact."),
        ("Comparing with care",
         "Do not test two floating-point results for exact equality after doing maths. Compare them within a small allowed gap instead. This is the usual rule in careful code."),
        ("Keeping money exact",
         "For money, store whole cents, or whole credits, as integers. Adding whole numbers is exact, so 10 cents plus 20 cents is always 30 cents. Do any rounding once, at the end, under clear rules."),
        ("Why it matters",
         "A tiny error in one sum is harmless. Millions of such sums, or a rule that depends on exact equality, can cause real surprises. Knowing the limits of the box helps you avoid them."),
    ],
    "test": [
        ("Why does 0.1 plus 0.2 not give exactly 0.3 in most languages?",
         [("a", "Because the computer is broken"), ("b", "Because 0.1 cannot be stored exactly in binary, so the sum is slightly off"), ("c", "Because 0.3 is a whole number"), ("d", "Because addition does not work on fractions")], "b"),
        ("What does a floating-point number store?",
         [("a", "A picture"), ("b", "A list of names"), ("c", "A date"), ("d", "A sign, significant digits and a power of two")], "d"),
        ("What is the safest way to store money in a ledger?",
         [("a", "Random fractions"), ("b", "Pictures of coins"), ("c", "Whole cents or whole credits, kept as integers"), ("d", "Binary decimals with no set limit")], "c"),
        ("Why should two floating-point results not be tested for exact equality?",
         [("a", "Because they are always equal"), ("b", "Because they are never numbers"), ("c", "Because a tiny rounding gap can make equal-looking values differ"), ("d", "Because equality is banned by law")], "c"),
        ("When is the best time to round money?",
         [("a", "Never"), ("b", "Only on Sundays"), ("c", "Before every single step, so the error grows"), ("d", "Once, at the end, under clear rules")], "d"),
    ],
}
