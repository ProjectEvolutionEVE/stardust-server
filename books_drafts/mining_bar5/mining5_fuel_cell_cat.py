"""Fuel Cell Catalysts: platinum catalysts that drive oxygen reduction in a fuel cell, how carbon supports and degradation matter, and how cost is cut."""
CODE = "mining5_fuel_cell_cat"
BOOK = {
    "title": "Fuel Cell Catalysts",
    "subtitle": "The platinum layer that makes a fuel cell work, and how to make less of it do more",
    "chapters": [
        ("What a catalyst does", "A catalyst speeds up a chemical reaction without being used up. In a hydrogen fuel cell, the catalyst helps hydrogen and oxygen react to make electricity and water."),
        ("Oxygen reduction", "At the cathode, oxygen must gain electrons, a step called oxygen reduction. This step is slow, so the cathode needs an effective catalyst, usually platinum."),
        ("Platinum loading", "Platinum is rare and costly, so makers measure the loading, the amount of platinum per square centimetre. Less loading lowers cost, but it must not slow the cell too much."),
        ("Carbon supports", "Tiny platinum particles sit on carbon supports. The carbon spreads the platinum and keeps it in place. The support must conduct electricity and resist corrosion."),
        ("Degradation", "Over time, the carbon support can corrode, and platinum particles can dissolve and grow larger. Both reduce the power the cell can deliver."),
        ("Testing and cost", "Catalysts are tested in small rotating disc cells before they go into full stacks. Makers aim to cut platinum use while keeping the cell reliable for many hours of running."),
    ],
    "test": [
        ("What does a catalyst do in a fuel cell?",
         [("a", "Burns the fuel"), ("b", "Cools the water"), ("c", "Melts the cell"), ("d", "Speeds up the reaction without being used up")], "d"),
        ("What is the usual cathode catalyst in fuel cells?",
         [("a", "Sugar"), ("b", "Platinum"), ("c", "Plastic"), ("d", "Paper")], "b"),
        ("What is platinum loading?",
         [("a", "The amount of platinum per square centimetre"), ("b", "The weight of a car"), ("c", "The price of gold"), ("d", "The colour of a cell")], "a"),
        ("What is the role of the carbon support?",
         [("a", "It turns into oxygen"), ("b", "It stores water"), ("c", "It spreads the platinum and holds it in place"), ("d", "It makes sound")], "c"),
        ("What happens to the platinum particles over time?",
         [("a", "They can dissolve and grow larger"), ("b", "They turn into wood"), ("c", "They float away as gas"), ("d", "They become sugar")], "a"),
    ],
}
