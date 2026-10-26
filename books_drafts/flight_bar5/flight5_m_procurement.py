"""Buying Well: specifying needs, bids, evaluation, supplier checks, terms, and managing delivery."""
CODE = "flight5_m_procurement"
BOOK = {
    "title": "Buying Well",
    "subtitle": "From a clear need to a delivery that works",
    "chapters": [
        ("Specify the need",
         "Good buying starts with a clear statement of what is needed, why, and by when. A vague request invites vague offers. Describe the result you want, and the standards it must meet."),
        ("Invite bids",
         "A bid is a supplier's written offer to do the work at a price. Invite several bids so you can compare them. Give every bidder the same information so the comparison is fair."),
        ("Evaluate",
         "Judge each bid against the same criteria: price, quality, time, experience and risk. Score them openly. Do not pick on price alone when quality or delivery matters more."),
        ("Check suppliers",
         "Check each supplier's references, finances, insurance and past delivery record. A cheap bid from a weak supplier can cost more in the end. Ask to see examples of similar work."),
        ("Agree the terms",
         "Write down the price, the schedule, the standards, payment dates and what happens if things go wrong. Clear terms protect both sides. Read them before signing."),
        ("Manage delivery",
         "Track progress against the plan, check the work as it is delivered and record any problems in writing. Act early on delays. Good management is what turns a signed contract into a result."),
    ],
    "test": [
        ("What should good buying start with?",
         [("a", "The cheapest supplier"), ("b", "A signed contract"), ("c", "A clear statement of the need"), ("d", "A rumour")], "c"),
        ("What is a bid?",
         [("a", "A payment made in advance"), ("b", "A supplier's written offer to do the work at a price"), ("c", "A type of tax"), ("d", "A complaint")], "b"),
        ("Why invite several bids?",
         [("a", "So the buyer can avoid all suppliers"), ("b", "So prices can be raised"), ("c", "So no record is needed"), ("d", "So offers can be compared fairly")], "d"),
        ("Why should you not pick a supplier on price alone?",
         [("a", "Price is always wrong"), ("b", "The law forbids price comparisons"), ("c", "Quality, time and experience can matter more than price"), ("d", "Prices never differ")], "c"),
        ("What should a supplier check include?",
         [("a", "References, finances, insurance and past delivery record"), ("b", "The supplier's favourite colour"), ("c", "The weather where they live"), ("d", "Their shoe size")], "a"),
    ],
}
