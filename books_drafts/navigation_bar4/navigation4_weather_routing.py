"""Weather Routing and Isochrones: forecasts, equal-time lines, the best path, uncertainty, fuel and the final decision."""
CODE = "navigation4_weather_routing"
BOOK = {
    "title": "Weather Routing and Isochrones",
    "subtitle": "Choosing the fastest and safest path through changing wind and waves",
    "chapters": [
        ("Wind and wave forecasts", "Weather routing starts with forecasts of wind and waves. The forecasts are updated often. Each update can change the best route, so the plan must be checked again and again."),
        ("Isochrones", "An isochrone is a line of equal travel time from a starting point. Each new ring shows how far a ship can get in the next period. The rings show the reach of the ship under the forecast."),
        ("The best path", "The best path links the rings back to the destination. It takes the fastest route that the weather allows. A route may bend around a storm rather than cut straight through it."),
        ("Uncertainty", "Forecasts are less certain further ahead. A route that looks best may depend on a wind that never arrives. Good routing shows a range of likely outcomes, not one answer."),
        ("Fuel", "Rough seas and head winds burn more fuel. A faster route can cost more than a slower one. The best choice balances time against fuel and comfort."),
        ("Decisions", "The master makes the final decision. Routing tools give advice, but the crew watches the real conditions. Safety comes before speed or saving fuel."),
    ],
    "test": [
        ("What starts a weather routing plan?", [("a", "A list of songs"), ("b", "The colour of the hull"), ("c", "A menu for the crew"), ("d", "Forecasts of wind and waves")], "d"),
        ("What is an isochrone?", [("a", "A line of equal travel time from a starting point"), ("b", "A type of storm"), ("c", "A kind of anchor"), ("d", "A sea shanty")], "a"),
        ("Why might a best route bend around a storm?", [("a", "Storms cannot be seen"), ("b", "The weather lets a faster route go around it"), ("c", "Bends are always shorter"), ("d", "Ships cannot turn")], "b"),
        ("Why does uncertainty matter in forecasts?", [("a", "Forecasts never change"), ("b", "Forecasts are only for the land"), ("c", "Forecasts are exact over any time"), ("d", "Forecasts are less certain further ahead")], "d"),
        ("What must a routing plan balance?", [("a", "Paint colour against cargo"), ("b", "Music against the menu"), ("c", "Time against fuel and comfort"), ("d", "Flags against names")], "c"),
    ],
}
