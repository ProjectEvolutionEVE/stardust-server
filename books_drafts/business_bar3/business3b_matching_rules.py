"""Matching Rules (Manager, bar 3, part B): price first, then time, and how an order book decides who trades with whom."""
CODE = "business3b_matching_rules"
BOOK = {
    "title": "Matching Rules",
    "subtitle": "Price first, then time: how an order book decides who trades with whom",
    "chapters": [
        ("Two rules, in order",
         "When a buy order and a sell order meet, the book needs a rule to decide who trades first. Most exchanges use two rules in order: price first, then time. The best price always goes first, and among orders at the same price, the earliest one goes first."),
        ("Price first",
         "A buyer willing to pay more is matched before a buyer willing to pay less. A seller asking less is matched before one asking more. A better price jumps the queue, even when the order that offers it arrived later."),
        ("Then time",
         "Orders at the same price form a queue. The one that arrived first fills first, and later orders wait behind it. At a busy price, the time you joined the queue can matter as much as the price itself."),
        ("Partial fills",
         "An order does not always fill all at once. If a buy for 50 units meets a sell for 20, the 20 trade now, and the other 30 stay on the book to wait for a match. A partial fill is still a real trade."),
        ("The waiting price rules",
         "A trade happens at the price already waiting in the book, not at the price of the newer order. If a sell is resting at 200, a buyer willing to pay 210 buys at 200. The Starship market works this way too, so the buyer keeps the difference."),
        ("Why the rules matter",
         "Knowing the rules tells you what your order will do. A limit order placed at the best price usually fills first. An order placed at the back of a long queue may wait, even when its price is right."),
    ],
    "test": [
        ("Under price-then-time matching, which order fills first?",
         [("a", "The largest order, whatever its price"), ("b", "The best price first, and the earliest order among orders at the same price"), ("c", "The newest order"), ("d", "Whichever trader clicks first")], "b"),
        ("A buy order for 50 units meets a sell order for 20 units. What happens?",
         [("a", "The whole 50 is cancelled"), ("b", "The 20 trade now, and the other 30 wait on the book"), ("c", "All 50 trade at double the price"), ("d", "Nothing trades until the next day")], "b"),
        ("Two sell orders sit at 200, one placed at 9:00 and one at 9:05. Which fills first?",
         [("a", "The 9:05 order, since it is newer"), ("b", "Neither, since both wait for a year"), ("c", "The one with more units"), ("d", "The 9:00 order, since it arrived first")], "d"),
        ("A resting sell order is at 200. A buyer arrives willing to pay 210. At what price do they trade?",
         [("a", "200, the price already waiting on the book"), ("b", "210, the buyer's price"), ("c", "205, halfway between the two"), ("d", "They cannot trade")], "a"),
        ("Why does a better price go ahead of an earlier order at a worse price?",
         [("a", "Because the exchange favours big traders"), ("b", "Because the bank always pays the highest price"), ("c", "Because it was placed later in the day"), ("d", "Because the matching rule puts the best price first")], "d"),
    ],
}
