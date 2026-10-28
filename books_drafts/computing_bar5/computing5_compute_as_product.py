"""Selling Compute as a Product: how computing capacity is priced, committed and sold to customers fairly."""
CODE = "computing5_compute_as_product"
BOOK = {
    "title": "Selling Compute as a Product",
    "subtitle": "Pricing computing capacity, committing it and selling it fairly",
    "chapters": [
        ("Unit pricing for compute",
         "Compute is often sold by a unit, such as an hour of processor time or a block of memory. The unit price must cover the cost of the hardware, power and staff. Keep the unit simple, so customers can predict their bills."),
        ("Reserved tiers",
         "A reserved tier is a block of capacity a customer agrees to buy in advance, usually at a lower price. It gives the provider steady income and helps it plan. The customer gains a discount for the commitment."),
        ("Margins",
         "Margin is the share of revenue left after the costs of providing the service. Compute margins depend on how well the hardware is used. Idle hardware costs money without earning any."),
        ("Capacity commitments",
         "A capacity commitment is a promise to have enough hardware ready for a customer. It must be backed by real purchases and lead times. Overpromising leads to failed service and lost trust."),
        ("Customer contracts",
         "Contracts should state what capacity is promised, how it is measured and what happens if it is not delivered. Clear terms prevent disputes. Keep them easy for customers to read."),
        ("Fairness",
         "Fair sharing means no customer can crowd out others without reason. Set clear limits and publish them. Customers judge a provider by how it treats them when capacity is tight."),
    ],
    "test": [
        ("What is a reserved tier?",
         [("a", "A type of printer"), ("b", "A block of capacity bought in advance, usually at a lower price"), ("c", "A staff uniform"), ("d", "A tax on electricity")], "b"),
        ("What does margin measure?",
         [("a", "The number of staff in a team"), ("b", "The length of a contract"), ("c", "The size of an office"), ("d", "The share of revenue left after the costs of providing the service")], "d"),
        ("Why is idle hardware costly?",
         [("a", "It costs money without earning any"), ("b", "It earns money while it sits"), ("c", "It improves margin automatically"), ("d", "It is never counted")], "a"),
        ("What should a capacity commitment be backed by?",
         [("a", "A hope that demand will fall"), ("b", "A promise with no hardware"), ("c", "Real purchases and lead times"), ("d", "A discount to the customer")], "c"),
        ("What makes sharing compute fair?",
         [("a", "Letting one customer take everything"), ("b", "Clear, published limits so no one crowds out others without reason"), ("c", "Hiding the limits"), ("d", "Charging a random price each day")], "b"),
    ],
}
