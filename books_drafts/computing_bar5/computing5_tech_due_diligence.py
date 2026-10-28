"""Technology Due Diligence: checking the technology behind a company before a deal closes."""
CODE = "computing5_tech_due_diligence"
BOOK = {
    "title": "Technology Due Diligence",
    "subtitle": "Checking what you are buying before a deal closes",
    "chapters": [
        ("Purpose",
         "Technology due diligence checks the technology behind a company before it is bought or invested in. The aim is to find costs and risks that the price does not yet reflect. Findings can change the deal."),
        ("Code and architecture review",
         "Look at how the software is built, how well it is tested and how easily it can change. Ask how long a typical change takes. A system that is hard to change is a hidden cost."),
        ("Security checks",
         "Test the main systems for weaknesses and read past incident reports. Check how data is stored and protected. Gaps here can become expensive after the deal."),
        ("Key-person risk",
         "If vital knowledge sits with one or two people, plan how to keep them and share what they know. Check the contracts of key staff. A deal can lose its value if a key expert leaves."),
        ("Technical debt estimates",
         "Technical debt is the future cost created by shortcuts and old systems. Count the main shortcuts and estimate the time and money needed to fix them. Put a rough number on each one."),
        ("Deal findings",
         "Write up the risks and costs in plain language, with the evidence behind each one. Feed the findings into the price and the integration plan. Clear findings protect both sides."),
    ],
    "test": [
        ("What is the main purpose of technology due diligence?",
         [("a", "To choose office snacks"), ("b", "To check the technology before a deal"), ("c", "To pick new colours"), ("d", "To write a press release")], "b"),
        ("What is technical debt?",
         [("a", "Money owed to a bank"), ("b", "A staff bonus"), ("c", "Future cost created by shortcuts and old systems"), ("d", "A type of code")], "c"),
        ("Why check key-person risk?",
         [("a", "To know if vital knowledge sits with too few people"), ("b", "To count desks"), ("c", "To find the best coffee"), ("d", "To avoid all staff")], "a"),
        ("What should due diligence findings feed?",
         [("a", "Only the lunch menu"), ("b", "Nothing"), ("c", "A joke"), ("d", "The price and the integration plan")], "d"),
        ("Which check looks for weaknesses in a system?",
         [("a", "Security testing"), ("b", "Menu planning"), ("c", "Desk checks"), ("d", "Parking")], "a"),
    ],
}
