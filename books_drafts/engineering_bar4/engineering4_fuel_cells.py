"""Fuel Cells and Electrochemical Conversion: membrane electrodes, reactions in a cell, efficiency, catalysts, hydrogen supply and cost."""
CODE = "engineering4_fuel_cells"
BOOK = {
    "title": "Fuel Cells and Electrochemical Conversion",
    "subtitle": "Membranes, reactions, catalysts and cost per kilowatt-hour",
    "chapters": [
        ("The membrane electrode",
         "The core of a fuel cell is a membrane between two electrodes. The membrane lets ions pass through while keeping the gases apart."),
        ("Reactions in a cell",
         "At the anode, hydrogen gives up electrons. At the cathode, oxygen takes them up and combines with the ions to form water. The electrons flow through the outside circuit as electricity."),
        ("Efficiency",
         "Real fuel cells run below their theoretical limit because of losses. Under load, the cell voltage sits well below the ideal voltage."),
        ("Catalysts",
         "Platinum-based catalysts speed up the reactions at the electrodes. Catalysts add cost, so designers use only as much as they need."),
        ("Hydrogen supply",
         "The cell needs a steady, clean hydrogen supply. Impurities can poison the catalyst and reduce its life."),
        ("Cost per kilowatt-hour",
         "The cost of power from a fuel cell depends on the stack, the fuel and the lifetime. Compare the full cost over the whole life."),
    ],
    "test": [
        ("What is the membrane's job in a fuel cell?",
         [("a", "Lets ions pass and keeps the gases apart"), ("b", "Makes paint"), ("c", "Plays sound"), ("d", "Holds seats")], "a"),
        ("What is formed at the cathode in a hydrogen fuel cell?",
         [("a", "Gold"), ("b", "Oil"), ("c", "Glass"), ("d", "Water")], "d"),
        ("What do catalysts do?",
         [("a", "Slow the cell"), ("b", "Speed up the reactions at the electrodes"), ("c", "Paint the electrodes"), ("d", "Heat the air")], "b"),
        ("Why do real fuel cells fall below their ideal performance?",
         [("a", "Paint on the cell"), ("b", "Music"), ("c", "Losses in the cell"), ("d", "Weather")], "c"),
        ("What can impurities in the hydrogen do?",
         [("a", "Poison the catalyst"), ("b", "Improve the catalyst"), ("c", "Cool the cell"), ("d", "Make paint")], "a"),
    ],
}
