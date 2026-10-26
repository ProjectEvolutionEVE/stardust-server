"""Shipping Economics: charter rates, voyage costs, freight cycles, flags of convenience, marine insurance and cases."""
CODE = "flight5_m_shipping_econ"
BOOK = {
    "title": "Shipping Economics",
    "subtitle": "Ships, charters, cycles and the cost of moving goods",
    "chapters": [
        ("Chartering a ship",
         "A ship can be chartered, which means hired by the trip or by the time. A voyage charter pays for one journey. A time charter pays for a set period, and the charterer decides where the ship goes within agreed limits."),
        ("Voyage costs",
         "Running a ship costs fuel, crew, port fees, maintenance, insurance and capital. Fuel is often the largest single voyage cost, so fuel prices move freight rates quickly."),
        ("Freight cycles",
         "Shipping rates rise when demand for transport grows faster than the fleet, and fall when new ships flood the market. Ships take years to build, so the cycle can be long and sharp."),
        ("Flags of convenience",
         "A ship may be registered under a flag of a country other than its owner's. Flags of convenience can offer lower costs and simpler rules. Critics say they can weaken safety and labour standards."),
        ("Marine insurance",
         "Ships and cargo are insured against loss or damage at sea. Insurance is a major cost and a major safeguard. Insurers look at the route, the age of the ship and the record of the crew."),
        ("Cases",
         "Container shipping grew fast from the 1960s, cutting the cost of moving goods. Over time, shipping lines merged and sized up, so a small group of firms now handles much of world trade."),
    ],
    "test": [
        ("What is a voyage charter?",
         [("a", "A bank loan"), ("b", "A type of share"), ("c", "Hire of a ship for one journey"), ("d", "A harbour fee")], "c"),
        ("What is often the largest single voyage cost?",
         [("a", "Fuel"), ("b", "Paint"), ("c", "Flags"), ("d", "Tickets")], "a"),
        ("Why can freight rates swing sharply?",
         [("a", "Ships never move"), ("b", "Rates are fixed by law"), ("c", "Ships take years to build, so supply responds slowly"), ("d", "Ports charge nothing")], "c"),
        ("What is a flag of convenience?",
         [("a", "A signal for a storm"), ("b", "A ship registered under the flag of a country other than its owner's"), ("c", "A type of cargo"), ("d", "A club badge")], "b"),
        ("What does marine insurance cover?",
         [("a", "Holiday trips for sailors"), ("b", "Port building"), ("c", "Fuel prices"), ("d", "Loss or damage to ships and cargo at sea")], "d"),
    ],
}
