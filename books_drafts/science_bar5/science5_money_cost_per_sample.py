"""Cost per Sample in High-Throughput Labs: throughput economics, batch costs, automation investment, quality costs, pricing and capacity planning."""
CODE = "science5_money_cost_per_sample"
BOOK = {
    "title": "Cost per Sample in High-Throughput Labs",
    "subtitle": "How many samples a lab can process, and what each one really costs",
    "chapters": [
        ("Throughput economics",
         "Throughput is the number of samples a lab can process in a given time. Cost per sample is the total cost of running the lab divided by the number of samples it processes. Raising throughput usually lowers the cost of each sample, as long as quality holds."),
        ("Batch costs",
         "A batch cost is a cost shared by a group of samples processed together, such as a set-up run or a calibration. Running larger batches spreads these costs. Batches that are too large can cause delays or errors, so the best size needs checking."),
        ("Automation investment",
         "Automation can save time and staff effort, but machines must be bought and set up first. The cost of a robot can take years to repay. Compare the purchase, service and training costs with the time it will save each month."),
        ("Quality costs",
         "Quality costs are the costs of repeating work, checking results and fixing errors. A lab that makes fewer errors spends less on repeats. Count these costs in the true cost of each sample, not only the bench time."),
        ("Pricing per sample",
         "A lab that sells its services must set a price per sample that covers its real costs. Price too low and the lab loses money. Price too high and clients take their work elsewhere. Review prices as costs and volumes change."),
        ("Capacity planning",
         "Capacity planning asks how much work the lab can take on, and when it will need more space, staff or machines. Track the busiest instruments to find bottlenecks. Plan expansions before the queue becomes too long."),
    ],
    "test": [
        ("What does cost per sample measure?",
         [("a", "How many staff work in the lab"), ("b", "The price of the lab building"), ("c", "The total cost of running a lab divided by the samples it processes"), ("d", "The number of journals the lab reads")], "c"),
        ("What is a batch cost?",
         [("a", "A cost shared by a group of samples processed together"), ("b", "A cost for one sample only"), ("c", "A cost paid to a sponsor"), ("d", "A cost for lost keys")], "a"),
        ("Why might automation cost more at first?",
         [("a", "Machines must be bought and set up before they save time"), ("b", "Machines are free to lease"), ("c", "Automation adds no training"), ("d", "Automation stops all errors at once")], "a"),
        ("What are quality costs?",
         [("a", "The cost of new furniture"), ("b", "The price of coffee"), ("c", "Donations to the library"), ("d", "Costs of repeating work, checking and fixing errors")], "d"),
        ("What does capacity planning help a lab decide?",
         [("a", "Which colour to paint the walls"), ("b", "How much work the lab can take on, and when it needs more space or machines"), ("c", "Which journal to pick"), ("d", "Which film to watch")], "b"),
    ],
}
