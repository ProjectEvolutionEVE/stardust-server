"""Insurance and Navigation Risk: premiums, risk ratings, claims, deductibles, navigation warranties and loss records."""
CODE = "navigation4_navigation_insurance"
BOOK = {
    "title": "Insurance and Navigation Risk",
    "subtitle": "How insurers price the risk of sailing, and what a good record is worth",
    "chapters": [
        ("Premiums", "A premium is the price paid for insurance cover. It depends on the risk, the ship's value and its record. A better record can lower the premium."),
        ("Risk ratings", "Insurers rate each ship and voyage by risk. High-risk routes or old ships often cost more to insure. Ratings are based on past losses and known dangers."),
        ("Claims", "A claim is a request to the insurer to pay for a loss. Good records make claims faster and fairer. Claims are checked before they are paid."),
        ("Deductibles", "A deductible is the part of a loss the owner pays first. A higher deductible usually lowers the premium. It makes the owner share the cost of small losses."),
        ("Navigation warranties", "A warranty is a promise written into an insurance contract. A navigation warranty may require the ship to follow certain rules or routes. Breaking a warranty can void the cover."),
        ("Loss records", "Loss records show a ship's past claims and accidents. Insurers use them to judge risk. A clean record helps keep premiums down."),
    ],
    "test": [
        ("What is a premium?", [("a", "The prize for the fastest ship"), ("b", "The price paid for insurance cover"), ("c", "A type of rope"), ("d", "The name of an island")], "b"),
        ("What does a deductible do?", [("a", "It cancels all cover"), ("b", "It pays the crew"), ("c", "It adds cargo"), ("d", "The owner pays the first part of a loss")], "d"),
        ("What can breaking a navigation warranty do?", [("a", "Make the ship faster"), ("b", "Void the cover"), ("c", "Cut the crew's pay"), ("d", "Lower the premium to zero")], "b"),
        ("What do loss records show?", [("a", "A ship's past claims and accidents"), ("b", "The menu of the day"), ("c", "The paint colour"), ("d", "The weather for the year")], "a"),
        ("What does a higher deductible usually do to the premium?", [("a", "Doubles it always"), ("b", "Removes it"), ("c", "Lowers it"), ("d", "Has no effect ever")], "c"),
    ],
}
