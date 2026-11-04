"""Pricing Analytical Services and Testing: building a fair price for lab testing from its real costs, and comparing it with the market."""
CODE = "science5_money_analytic_pricing"
BOOK = {
    "title": "Pricing Analytical Services and Testing",
    "subtitle": "Cost build-up, sample throughput, price tiers, quality guarantees, client pricing and market comparisons",
    "chapters": [
        ("Cost build-up", "A cost build-up adds up all the costs of a service, such as staff time, consumables, equipment use and overhead. The total gives the base price before any margin is added. A price that skips a cost will lose money on every job."),
        ("Sample throughput", "Sample throughput is the number of samples a lab can process in a set time. High throughput spreads fixed costs across more samples and lowers the cost of each one. Planning throughput is central to setting a sensible price."),
        ("Price tiers", "A price tier sets a different price for different volumes or categories of work. Larger orders can earn a lower price, and urgent work can carry a higher one. Tiers make pricing clear and fair to different kinds of client."),
        ("Quality guarantees", "A quality guarantee is a promise that results meet stated accuracy and turnaround times. It is a commitment the lab must be able to keep. Price should reflect the quality the lab promises, and the cost of the checks needed to keep it."),
        ("Client pricing", "Client pricing sets the price each customer pays, based on the cost build-up, the tiers and the market. Clear price lists and clear terms help clients decide quickly. Pricing should be reviewed as costs change."),
        ("Market comparisons", "Compare your prices with those of other labs offering similar services. A comparison shows whether your price is competitive, too high or too low. It should not drive the price alone, since your costs and quality may differ."),
    ],
    "test": [
        ("What is a cost build-up?",
         [("a", "Stacking boxes in a store"), ("b", "A plan for a building"), ("c", "Adding up all the costs of a service to find its base price"), ("d", "A form for paying tax")], "c"),
        ("What is sample throughput?",
         [("a", "The number of colours in the lab"), ("b", "The number of samples a lab can process in a set time"), ("c", "The weight of the samples"), ("d", "The price of gas")], "b"),
        ("What does a price tier do?",
         [("a", "Sets the colour of the price list"), ("b", "Sets the time of day for testing"), ("c", "Sets the number of staff"), ("d", "Sets a different price for different volumes or categories of work")], "d"),
        ("What is a quality guarantee for a lab?",
         [("a", "A promise that results meet stated accuracy and turnaround times"), ("b", "A promise of a free lunch"), ("c", "A warranty on paper"), ("d", "A bank guarantee")], "a"),
        ("Why compare your prices with the market?",
         [("a", "Market prices are irrelevant to a lab"), ("b", "To check that your price is fair and competitive for the service"), ("c", "To hide your prices from clients"), ("d", "Because markets never change")], "b"),
    ],
}
