"""Creep: slow stretching at high heat, creep curves, time and temperature, rupture tests and margins for hot parts."""
CODE = "engineering4_creep"
BOOK = {
    "title": "Creep: Slow Stretching at High Heat",
    "subtitle": "Creep curves, time, temperature and rupture",
    "chapters": [
        ("Metals that stretch slowly",
         "Under a steady load at high temperature, a metal slowly stretches over time, even if the stress is well below its normal strength. This slow deformation is called creep. It is a key limit for hot parts."),
        ("Creep curves",
         "A creep curve plots strain against time under constant load and temperature. It has a fast early stage, a steady middle stage, and a final stage where the rate speeds up. The final stage ends in rupture."),
        ("Time and temperature",
         "Higher temperature speeds up creep a great deal. A part that is safe for years at a moderate temperature may fail in a short time when hotter. Designers therefore set a temperature limit along with the stress limit."),
        ("Turbines and boilers",
         "Turbine blades and boiler tubes run hot for many years under steady load. Creep can make them stretch until they touch other parts or crack. Engineers choose alloys and cooling to keep creep within limits."),
        ("Rupture tests",
         "Rupture tests hold a sample at a set temperature and stress until it breaks, and record the time to failure. The results give the strength a material can keep for a chosen life. Test results form the basis of creep design data."),
        ("Design margins for hot parts",
         "Designers keep a margin between the working stress and the stress that would cause rupture in the design life. They also allow for uncertain temperatures and load swings. A margin is what keeps a hot part safe over its whole life."),
    ],
    "test": [
        ("What is creep?", [("a", "Slow stretching of a metal under steady load at high temperature"), ("b", "Rapid melting of a metal"), ("c", "Rust on the surface"), ("d", "A type of paint")], "a"),
        ("What does a creep curve plot?", [("a", "Voltage against paint"), ("b", "Price against weight"), ("c", "Colour against sound"), ("d", "Strain against time under constant load and temperature")], "d"),
        ("What happens to creep as temperature rises?", [("a", "It stops completely"), ("b", "It speeds up a great deal"), ("c", "It reverses"), ("d", "It has no effect")], "b"),
        ("What do rupture tests record?", [("a", "The shape of the test lab"), ("b", "The number of workers"), ("c", "The time to failure at a set temperature and stress"), ("d", "The price of the sample")], "c"),
        ("Why do designers keep a margin for hot parts?", [("a", "To avoid testing"), ("b", "To make the part heavier"), ("c", "To stay safe over the design life, allowing for uncertain temperatures and loads"), ("d", "To remove all loads")], "c"),
    ],
}
