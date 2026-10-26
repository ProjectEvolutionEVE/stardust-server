"""Airline Economics: load factor, cost per seat mile, fuel hedging, fleet choice, thin margins and bankruptcies."""
CODE = "flight5_m_airline_econ"
BOOK = {
    "title": "Airline Economics",
    "subtitle": "Full planes, fuel bills and very thin margins",
    "chapters": [
        ("Load factor",
         "Load factor is the share of seats sold on a flight. A plane that is 80% full has a load factor of 80%. Airlines fill seats through pricing, timing and routes. An empty seat earns nothing, but it still costs to fly."),
        ("Cost per seat mile",
         "Airlines track cost per available seat mile, which is the total cost of a flight divided by the seats flown and the distance. It shows how efficiently a fleet runs. Lower costs let an airline price competitively and still earn a profit."),
        ("Fuel hedging",
         "Fuel is one of the largest costs for an airline. Many airlines buy fuel in advance, or use contracts, to limit the damage from price rises. Hedges can also lose money if fuel prices fall."),
        ("Fleet choice",
         "Choosing the right aircraft matters. Newer planes often burn less fuel and need less maintenance. A fleet that suits its routes can cut costs, but buying planes is a large commitment of money."),
        ("Thin margins",
         "Airlines often earn small profits, or losses, after costs. Their margins are thin because fares are competitive and costs are high. A small change in fuel price, load factor or demand can change the result sharply."),
        ("Bankruptcies",
         "Many airlines have gone bankrupt over the decades. Failures often came after fuel spikes, economic shocks or price wars. Strong cash reserves and careful debt help them survive."),
    ],
    "test": [
        ("What is load factor?",
         [("a", "The weight of the plane"), ("b", "The cost of a pilot"), ("c", "The age of a fleet"), ("d", "The share of seats sold on a flight")], "d"),
        ("What does cost per available seat mile show?",
         [("a", "The colour of the seats"), ("b", "How many pilots fly"), ("c", "How efficiently a fleet runs"), ("d", "The number of airports")], "c"),
        ("What does fuel hedging aim to do?",
         [("a", "Limit the damage from fuel price rises"), ("b", "Guarantee a free flight"), ("c", "Remove all airline costs"), ("d", "Ban fuel use")], "a"),
        ("Why are airline margins often thin?",
         [("a", "Airlines never charge for tickets"), ("b", "Planes are free to fly"), ("c", "Fares are competitive and costs are high"), ("d", "Profit is banned")], "c"),
        ("What is one cause of airline bankruptcies?",
         [("a", "Too many passengers"), ("b", "Fuel price spikes, shocks and price wars"), ("c", "Owning too many cash reserves"), ("d", "Using new planes")], "b"),
    ],
}
