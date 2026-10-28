"""Anthropometric Data for Design: body size percentiles, reach envelopes, clearances, population sampling and design limits."""
CODE = "engineering5_anthropometry"
BOOK = {
    "title": "Anthropometric Data for Design",
    "subtitle": "Designing for real body sizes, from the smallest to the largest",
    "chapters": [
        ("Why body size matters",
         "Anthropometry is the measurement of the human body. Designers use these measurements to decide the size of seats, handles, doors and controls. A product that ignores body size may be uncomfortable or unsafe for many people."),
        ("Percentiles",
         "A percentile tells you the share of people at or below a given size. The 5th percentile is a small size that only one person in twenty falls below. The 95th percentile is a large size that only one person in twenty exceeds."),
        ("Designing for a range",
         "Designers rarely use the average person. Instead they design for a range of percentiles, so the product fits a wide span of users. Choosing the range is a judgement about who will use the product and what they must reach."),
        ("Reach envelopes",
         "A reach envelope is the area a person can comfortably reach with their hands or feet. Controls placed inside this area are easy to use. Controls placed outside it cause strain, slips and mistakes."),
        ("Clearances",
         "A clearance is the room left so that a body or a part can move without hitting anything. Clearances are needed around doors, seats, hatches and tools. Designers add enough room for the largest user and the clothing they wear."),
        ("Population sampling",
         "The body data must come from a sample that represents the people who will use the product. A sample from the wrong group gives misleading sizes. Engineers check the source of every dataset before relying on it."),
    ],
    "test": [
        ("What is a percentile in body-size data?",
         [("a", "A type of paint"), ("b", "A price"), ("c", "The share of people at or below a given size"), ("d", "A speed")], "c"),
        ("Why do designers use a range of percentiles rather than an average?",
         [("a", "So a design fits a wide range of people"), ("b", "So the cost falls"), ("c", "So the paint is even"), ("d", "So the sizes are printed in red")], "a"),
        ("What is a reach envelope?",
         [("a", "A paint tin"), ("b", "A letter"), ("c", "A spacing rule for doors"), ("d", "The area a person can reach comfortably with their hands or feet")], "d"),
        ("What is a clearance in design?",
         [("a", "A sale"), ("b", "Room left so a body or part can move without hitting anything"), ("c", "A paint shade"), ("d", "A cable")], "b"),
        ("Why does population sampling matter for body-size data?",
         [("a", "It sets the colour"), ("b", "It sets the price"), ("c", "The sample must represent the people who will use the product"), ("d", "It sets the weight")], "c"),
    ],
}
