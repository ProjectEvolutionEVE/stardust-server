"""Supply Chains (Manager, bar 3, part B): the path from raw material to customer, its lead times, bottlenecks and buffers."""
CODE = "business3b_supply_chains"
BOOK = {
    "title": "Supply Chains",
    "subtitle": "From the mine to the customer: each link, its delays and its bottlenecks",
    "chapters": [
        ("The chain",
         "A supply chain is the whole path a product takes from raw material to customer. It runs through miners or farms, processors, makers, shippers, sellers and buyers. Each link adds value, and each link adds time."),
        ("Lead times",
         "Lead time is the delay between placing an order and receiving the goods. A long lead time ties up cash, because you pay before you sell. Shorter lead times let you hold less stock."),
        ("Bottlenecks",
         "A bottleneck is the slowest link, and it limits the whole chain. Adding capacity elsewhere does not help while one step is always full. Find the bottleneck before you spend money to speed up anything else."),
        ("One source or many",
         "Relying on one supplier is cheap until that supplier fails. Several sources cost more to manage, but they protect you from a single failure. It is a risk choice, like any other."),
        ("Stock as a buffer",
         "Stock held between links is a buffer. It protects against delays, but it costs money to store and ties up cash. Keep enough buffer to cover the risk you face, and no more."),
        ("Map your own chain",
         "List every link for one product, with its time and cost. Mark the bottleneck and any single point of failure. On the Starship, a chain might run from a debris field to the cargo hold, then to a smelter, and then to a buyer. The map shows where a small change would help most."),
    ],
    "test": [
        ("What is a supply chain?",
         [("a", "The whole path a product takes from raw material to the customer"), ("b", "A chain that holds up a bridge"), ("c", "A list of bank accounts"), ("d", "A single factory")], "a"),
        ("What is lead time?",
         [("a", "The time a shop stays open"), ("b", "The time a product stays on a shelf"), ("c", "The delay between placing an order and receiving the goods"), ("d", "The time a loan takes to repay")], "c"),
        ("What is a bottleneck?",
         [("a", "The fastest link in a chain"), ("b", "A type of storage"), ("c", "The slowest link, which limits the whole chain"), ("d", "A bonus paid to suppliers")], "c"),
        ("Why can relying on one supplier be risky?",
         [("a", "Because one supplier is always the cheapest"), ("b", "Because the law forbids two suppliers"), ("c", "Because it makes the chain faster"), ("d", "Because if that supplier fails, you may have nothing to sell")], "d"),
        ("What does stock held between links do?",
         [("a", "It removes every delay"), ("b", "It makes each link faster"), ("c", "It acts as a buffer against delays, but ties up cash"), ("d", "It is always free to store")], "c"),
    ],
}
