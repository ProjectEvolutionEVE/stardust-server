"""Total Cost of Security Controls: the full lifetime cost of a security measure, including staff time and false alarms."""
CODE = "computing5_security_controls_cost"
BOOK = {
    "title": "Total Cost of Security Controls",
    "subtitle": "The full lifetime cost of a security measure, beyond its price tag",
    "chapters": [
        ("Control lifecycle costs",
         "A control costs money from the day it is chosen until the day it is retired. Those costs include planning, setup, running and eventual replacement. A price tag shows only the first step."),
        ("Staff time",
         "People must set up, run and respond to security controls. Their time is a real cost, often larger than the software price. Count the hours each year, not just the day of purchase."),
        ("Tool licences",
         "Many security tools are priced by user, device or volume, and prices may rise at renewal. Track licence counts and renewal dates. Unused licences add cost with no benefit."),
        ("The cost of false alarms",
         "A control that raises many false alarms wastes time and can cause real alerts to be missed. Count the time spent checking false alarms as a cost. Tuning a control can cut this cost."),
        ("Audit fees",
         "Some controls exist to satisfy audits, and the audits themselves cost money. Preparing evidence takes staff time. Plan for these costs when deciding which controls to keep."),
        ("Prioritising controls",
         "Rank controls by how much risk they reduce for their total cost. Start with the cheapest, most effective ones. Review the ranking as threats and costs change."),
    ],
    "test": [
        ("What is the full cost of a security control?",
         [("a", "Only its purchase price"), ("b", "Its cost across its life, including staff time and renewals"), ("c", "The cost of the office chairs"), ("d", "The cost of one coffee")], "b"),
        ("Why is staff time a real cost?",
         [("a", "Staff time is always free"), ("b", "Staff time is only counted in a bank"), ("c", "Staff time is never measured"), ("d", "People must set up, run and respond to controls")], "d"),
        ("What do false alarms cost?",
         [("a", "The time spent checking them, and risk of missing real alerts"), ("b", "Nothing at all"), ("c", "A bonus for staff"), ("d", "A free holiday")], "a"),
        ("Why track licence renewal dates?",
         [("a", "Renewal dates have no effect"), ("b", "Renewals are always free"), ("c", "Prices may rise at renewal and unused licences add cost"), ("d", "Licences never expire")], "c"),
        ("How should controls be ranked?",
         [("a", "By the colour of their boxes"), ("b", "By how much risk they reduce for their total cost"), ("c", "By the alphabet only"), ("d", "By the length of their names")], "b"),
    ],
}
