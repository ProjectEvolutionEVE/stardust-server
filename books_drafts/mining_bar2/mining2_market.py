"""What Ore Is Worth: the starting prices of the ores on the market, per lot, and why prices change."""
CODE = 'mining2_market'
BOOK = {
    "title": "What Ore Is Worth",
    "subtitle": "The starting prices of the main ores, per lot, and why prices change",
    "chapters": [
        ("Prices are per lot",
         "The market prices ore by the lot, not by the piece. One lot is the smallest order: iron ore and copper ore come in 100 kg lots, silver ore in 10 kg lots, and native gold and industrial diamond in 1 kg lots."),
        ("The starting prices",
         "At the start, a 100 kg lot of iron ore costs 200 credits, and a 100 kg lot of copper ore costs 600. A 10 kg lot of silver ore starts at 300. Native gold starts at 200 per kg, and industrial diamond at 100 per kg."),
        ("Comparing per kilogram",
         "Divide the lot price by the kilograms in the lot to compare ores. At the starting prices, iron ore is about 2 credits a kilogram and copper ore 6. Silver is 30 a kilogram, industrial diamond 100, and native gold 200."),
        ("The near-flawless diamond",
         "The near-flawless diamond is priced per stone, not per kilogram. Its starting price is 250,000 credits, with a floor of 125,000. It is kept apart from industrial diamond."),
        ("Floors",
         "Every item has a floor, which is half its starting price. Nothing trades below its floor. Iron ore's floor is 100 credits per lot, and native gold's floor is 100 credits per kg."),
        ("Prices move",
         "The prices here are starting prices. Trades move them over time, and the game's designers may change any number. Check the Market terminal at your desk for today's prices."),
    ],
    "test": [
        ("What is the smallest order of copper ore?",
         [("a", "1 kg"), ("b", "10 kg"), ("c", "100 kg"), ("d", "1 tonne")], "c"),
        ("What is the starting price of a 100 kg lot of copper ore?",
         [("a", "200"), ("b", "600"), ("c", "300"), ("d", "2,000")], "b"),
        ("Roughly what does iron ore cost per kilogram at the start?",
         [("a", "200 credits"), ("b", "0.2 credits"), ("c", "2 credits"), ("d", "20 credits")], "c"),
        ("Which of these has the highest starting price per kilogram?",
         [("a", "Native gold"), ("b", "Silver ore"), ("c", "Copper ore"), ("d", "Iron ore")], "a"),
        ("What is a floor price?",
         [("a", "The highest price"), ("b", "The price at midnight"), ("c", "The bank's fee"), ("d", "The lowest price anything trades at, half the start")], "d"),
    ],
}
