"""The Cost of a Positioning Service: the receiver, subscriptions, correction fees, lifecycle cost, replacement and the budget."""
CODE = "navigation4_gnss_service_cost"
BOOK = {
    "title": "The Cost of a Positioning Service",
    "subtitle": "Adding up everything a satellite positioning service costs over its life",
    "chapters": [
        ("The receiver purchase", "A positioning receiver is the first cost. The price depends on accuracy and features. A cheap receiver may not meet the needs of professional work."),
        ("Subscriptions", "Some services charge a subscription to receive corrections. The fee may be monthly or yearly. The subscription should be counted as an ongoing cost."),
        ("Correction fees", "Some correction services charge per use or per hour. These fees add up on busy days. Check the fee structure before choosing a service."),
        ("Lifecycle cost", "The lifecycle cost is the total cost of owning the equipment over its life. It includes purchase, service, fees and repairs. A low price can hide a high lifetime cost."),
        ("Replacement", "Equipment wears out and is replaced after some years. The replacement cost should be planned for in advance. Ignoring it leads to surprise bills."),
        ("The budget", "A budget lists all the costs of the service over a year. It includes one-off costs and ongoing fees. A good budget makes decisions easier."),
    ],
    "test": [
        ("What is the first cost of a positioning service?", [("a", "The office chairs"), ("b", "The paint on the hull"), ("c", "The receiver purchase"), ("d", "The crew's menu")], "c"),
        ("What does a subscription cover?", [("a", "The cargo"), ("b", "Ongoing access to corrections"), ("c", "The naming of the ship"), ("d", "The crew's songs")], "b"),
        ("What is lifecycle cost?", [("a", "The total cost of owning the equipment over its life"), ("b", "The cost of one hour of use"), ("c", "The cost of paint"), ("d", "The price printed on the box")], "a"),
        ("Why plan for replacement?", [("a", "Equipment never wears out"), ("b", "Replacement is free"), ("c", "Equipment wears out and needs replacing"), ("d", "It lowers the budget")], "c"),
        ("What does a budget list?", [("a", "All costs over a year, one-off and ongoing"), ("b", "Only the crew's names"), ("c", "Only the weather"), ("d", "A menu")], "a"),
    ],
}
