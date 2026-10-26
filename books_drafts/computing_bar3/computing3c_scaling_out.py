"""Scaling Up or Scaling Out: two ways to handle more work, and what each one costs."""
CODE = "computing3c_scaling_out"
BOOK = {
    "title": "Scaling Up or Scaling Out",
    "subtitle": "Two ways to handle more work, and what each one costs",
    "chapters": [
        ("More work, more capacity",
         "As a system gets busier, it needs more capacity to keep up. Scaling means adding that capacity. There are two main ways to do it."),
        ("Scaling up",
         "Scaling up, also called vertical scaling, means using one bigger machine with more memory or a faster processor. It is simple, and the program does not need to change. A single machine has a top size, though, and bigger machines cost much more for each unit of power."),
        ("Scaling out",
         "Scaling out, also called horizontal scaling, means adding more machines that share the work. It can keep growing for longer, and one failed machine hurts less. The program must be built so that many machines can work together."),
        ("The bill grows too",
         "Every machine adds to the monthly bill, so scaling is a money decision as well as a technical one. Ask what each extra machine adds in capacity, and compare that price with the gain. If the income per player is lower than the server cost per player, growth loses money."),
        ("Measure before you buy",
         "Find out where the slowness really is before adding anything. Often one slow step, such as a missing cache or a search with no index, is the real cause. Fixing that first can cost far less than a bigger machine."),
        ("Plan the next step",
         "Good plans set a trigger, such as adding a machine when the busiest one passes three quarters full. Write the trigger down and review it every month. Growth then comes as a plan, not as a surprise bill."),
    ],
    "test": [
        ("What is scaling up?",
         [("a", "Adding more machines that share the work"), ("b", "Using one bigger machine with more memory or a faster processor"), ("c", "Painting the walls"), ("d", "Turning the system off")], "b"),
        ("What is a limit of scaling up?",
         [("a", "It can never make anything faster"), ("b", "It needs the players to change their game"), ("c", "A single machine has a top size, and bigger machines cost much more per unit"), ("d", "It stops all the money")], "c"),
        ("What does scaling out mean?",
         [("a", "Adding more machines that share the work"), ("b", "Deleting old files"), ("c", "Making one machine bigger"), ("d", "Printing a bigger screen")], "a"),
        ("Why does every extra machine matter to the budget?",
         [("a", "It always pays for itself"), ("b", "It removes the bill"), ("c", "It only costs money once, ever"), ("d", "It adds to the monthly bill, so its cost must be compared with the gain")], "d"),
        ("What should you do before buying a bigger machine?",
         [("a", "Measure where the slowness really is"), ("b", "Buy the most expensive one"), ("c", "Turn off the logs"), ("d", "Sell the storage")], "a"),
    ],
}
