"""Port Charges and Pilotage Fees: port dues, pilotage, tug charges, the tonnage basis, the cost of a voyage and disputes."""
CODE = "navigation4_port_dues"
BOOK = {
    "title": "Port Charges and Pilotage Fees",
    "subtitle": "The charges a ship pays to enter, leave and use a port",
    "chapters": [
        ("Port dues", "Port dues are charges paid for using a port. They are often based on the ship's gross tonnage. They help cover the port's costs and upkeep."),
        ("Pilotage", "A pilot guides a ship in and out of port, or through difficult waters. Pilotage is charged for this service. Local pilots know the water and its hazards."),
        ("Tug charges", "Tugs help ships turn and dock. The charge depends on the size of the tug and the time used. Tugs are often needed for large ships in tight spaces."),
        ("The tonnage basis", "Many charges use the tonnage of the ship. Gross tonnage measures the volume of enclosed spaces. The basis of each charge should be stated in advance."),
        ("The voyage's cost", "Port charges are part of the cost of each voyage. They add to fuel, crew and cargo costs. Planning should include them from the start."),
        ("Disputes", "Disputes arise when a charge seems wrong. The agent checks the invoice against the published rules. Written records help settle disputes quickly."),
    ],
    "test": [
        ("What are port dues?", [("a", "Fees for sailing songs"), ("b", "Prizes for speed"), ("c", "Charges for using a port"), ("d", "Costs of paint")], "c"),
        ("What does a pilot do?", [("a", "Cooks the meals"), ("b", "Sells the cargo"), ("c", "Paints the hull"), ("d", "Guides a ship through difficult waters")], "d"),
        ("What do many port charges use as a basis?", [("a", "The ship's tonnage"), ("b", "The colour of the ship"), ("c", "The number of gulls"), ("d", "The name of the captain")], "a"),
        ("What are tugs used for?", [("a", "Carrying passengers"), ("b", "Helping ships turn and dock"), ("c", "Painting the water"), ("d", "Measuring the wind")], "b"),
        ("What helps settle a charge dispute?", [("a", "Guessing"), ("b", "Ignoring the invoice"), ("c", "Shouting"), ("d", "Written records")], "d"),
    ],
}
