"""Chart datum and lowest astronomical tide: depth references, soundings, regional choices, mean sea level and tidal range."""
CODE = "navigation4_chart_datum"
BOOK = {
    "title": "Chart Datum and Lowest Astronomical Tide",
    "subtitle": "The zero level for every depth on a chart",
    "chapters": [
        ("The reference for depths", "Charts show depths measured from a chosen reference level, called the chart datum. The datum is chosen so that depths are rarely less than shown. It is a safety choice."),
        ("Lowest astronomical tide", "Lowest astronomical tide is a common chart datum. It is the lowest level the tide is predicted to reach under average conditions. Using it keeps the charted depths on the safe side."),
        ("Soundings", "Soundings are the depth readings shown on the chart. They are referred to the datum. Changing the datum changes every sounding."),
        ("Regional choice", "Different countries choose different datums. Mariners must know which one their chart uses. Mixing datums leads to depth errors."),
        ("Mean sea level", "Mean sea level is the average level of the sea over a long period. It is used as a reference for heights on land. In many places it is not used as the chart datum."),
        ("Tidal range", "The tidal range is the difference between high and low water. A large range means big changes in depth over a tide. Charts and tide tables are read together."),
    ],
    "test": [
        ("What does a chart datum set?", [("a", "The price of the chart"), ("b", "The zero level for the depths on a chart"), ("c", "The colour of the land"), ("d", "The number of islands")], "b"),
        ("Why is lowest astronomical tide often used?", [("a", "It keeps charted depths on the safe side"), ("b", "It is always the highest level"), ("c", "It makes boats float higher"), ("d", "It is the same as the Moon's age")], "a"),
        ("What are soundings?", [("a", "Sounds made by ships"), ("b", "Radio messages between ports"), ("c", "Depth readings shown on the chart"), ("d", "Tides measured in the sky")], "c"),
        ("Why must mariners know which datum a chart uses?", [("a", "Datums change the spelling of place names"), ("b", "Datums set the colour of buoys"), ("c", "Datums decide the ship's name"), ("d", "Mixing datums causes depth errors")], "d"),
        ("What is the tidal range?", [("a", "The difference between high and low water"), ("b", "The time between two tides"), ("c", "The speed of the current"), ("d", "The distance from shore")], "a"),
    ],
}
