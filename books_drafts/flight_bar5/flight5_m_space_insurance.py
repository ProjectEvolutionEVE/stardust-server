"""Space Insurance Markets: launch and in-orbit cover, claims, premiums, losses, rates and how they change after failures."""
CODE = "flight5_m_space_insurance"
BOOK = {
    "title": "Space Insurance Markets",
    "subtitle": "Covering the risks of launch and life in orbit",
    "chapters": [
        ("Two kinds of cover",
         "Launch insurance covers the risk of loss during the rocket's ascent. In-orbit insurance covers a satellite once it is working in space. Each has its own risks, its own terms and its own price."),
        ("Claims",
         "A claim is a request for payment after a loss. In space, a claim might follow a launch failure or a satellite that stops working. Insurers check the cause and the terms before paying."),
        ("Premiums",
         "A premium is the price of the cover, usually a share of the insured value. It depends on the rocket or satellite's record, the design, the orbit and the length of cover. Newer designs with little history can be harder to price."),
        ("Losses",
         "Large losses in the space market have happened over the decades, such as launch failures and satellites that failed in orbit. Each loss is paid by the insurers, who then review their rates."),
        ("Rates",
         "Insurance rates for space have moved up and down with the claims record. After a run of losses, rates tend to rise. When launches succeed for a long time, rates tend to ease."),
        ("How prices change",
         "A good record lowers the cost of cover, and a bad one raises it. Customers who can show testing, backup systems and a clear design often get better terms. Insurers and customers both gain from honest, careful planning."),
    ],
    "test": [
        ("What does in-orbit insurance cover?",
         [("a", "A car on the road"), ("b", "A house on Earth"), ("c", "A satellite once it is working in space"), ("d", "A ship in harbour")], "c"),
        ("What is a claim?",
         [("a", "A request for payment after a loss"), ("b", "A type of satellite"), ("c", "A fee for a launch site"), ("d", "A map of orbit")], "a"),
        ("What is a premium?",
         [("a", "A prize for a launch"), ("b", "A fine for late launch"), ("c", "The price of the cover, often a share of the insured value"), ("d", "A satellite part")], "c"),
        ("What tends to happen to rates after a run of losses?",
         [("a", "Rates always fall to zero"), ("b", "Rates tend to rise"), ("c", "Rates are removed"), ("d", "Rates are fixed for ever")], "b"),
        ("What helps a customer get better insurance terms?",
         [("a", "Hiding test results"), ("b", "Skipping backup systems"), ("c", "Asking for no cover"), ("d", "A good record, testing and clear, careful design")], "d"),
    ],
}
