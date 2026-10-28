"""Dissimilar Metal Joints and Galvanic Pairs: joining different metals, transition inserts, galvanic attack at the joint, thermal mismatch and test coupons."""
CODE = "engineering5_weld_dissimilar"
BOOK = {
    "title": "Dissimilar Metal Joints and Galvanic Pairs",
    "subtitle": "Joining two different metals without inviting corrosion",
    "chapters": [
        ("Two metals, one joint",
         "Many products need two different metals joined together. A steel frame may meet an aluminium panel, for example. Joining them is harder than joining two pieces of the same metal."),
        ("Galvanic pairs",
         "When two metals touch in a wet or salty place, one can corrode faster than it would alone. The metals form a galvanic pair, and the less noble one suffers most. The galvanic series lists how metals rank in this respect."),
        ("Transition inserts",
         "A transition insert is a thin piece of a third metal placed between two dissimilar ones. It helps the join bond and reduces the step between the two metals. Inserts are chosen with care, so they do not add a new galvanic problem."),
        ("Thermal mismatch",
         "Metals expand by different amounts when heated. At a joint, this mismatch sets up stress that can crack the weld or loosen it over many heating cycles. Designers plan for it from the start."),
        ("Keeping water out",
         "Seals, coatings and insulating layers keep water from bridging the two metals. A joint that stays dry corrodes far less. Good design makes it easy to keep the joint dry in service."),
        ("Test coupons",
         "A test coupon is a small sample joined the same way as the real part. It is put through heat, wet and load tests before the full run. The cost of a coupon is small next to the cost of a failed joint in the field."),
    ],
    "test": [
        ("What is a galvanic pair?",
         [("a", "Two plastic sheets"), ("b", "Two identical bolts"), ("c", "Two metals that touch in a wet place so one corrodes faster"), ("d", "A pair of gloves")], "c"),
        ("What does a transition insert do?",
         [("a", "It melts the two metals together"), ("b", "It paints the joint"), ("c", "It removes the need for a joint"), ("d", "It eases the join between two dissimilar metals")], "d"),
        ("Why is thermal mismatch a concern at a joint?",
         [("a", "Metals expand by different amounts, which sets up stress"), ("b", "Metals always shrink the same amount"), ("c", "Heat makes metals lighter"), ("d", "Heat has no effect on joints")], "a"),
        ("How does keeping a joint dry help?",
         [("a", "Water makes the joint stronger"), ("b", "Water cannot bridge the two metals, so corrosion slows"), ("c", "Water hardens the metal"), ("d", "Water changes the metal type")], "b"),
        ("What is a test coupon?",
         [("a", "A discount voucher"), ("b", "A type of bolt"), ("c", "A small sample joined the same way as the real part"), ("d", "A paint sample card")], "c"),
    ],
}
