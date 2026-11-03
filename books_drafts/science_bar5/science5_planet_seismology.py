"""Planetary Seismology from Landers: how a lander's seismometer listens to a planet's quakes and reads its interior."""
CODE = "science5_planet_seismology"
BOOK = {
    "title": "Planetary Seismology from Landers",
    "subtitle": "Listening to quakes on other worlds to learn what lies beneath",
    "chapters": [
        ("Listening to a planet", "A seismometer is an instrument that records tiny shakes in the ground. On a planet with quakes, it turns the ground into a record that can be read like a book about the interior."),
        ("Seismic sources", "Quakes on Mars can come from the cooling and shrinking of the crust, or from the stress of the surface changing over time. Each source leaves its own kind of wave signature."),
        ("Marsquake detection", "The InSight lander, which operated on Mars from 2018 to 2022, recorded many marsquakes with its seismometer. Its work showed that quakes on Mars are common enough to study well."),
        ("Seismometer design", "A lander seismometer must sit very still and be shielded from wind, temperature changes and the lander's own movement. Engineers protect it with a cover and a buried or shielded placement."),
        ("Interior models", "Seismic waves travel at different speeds through different materials. By timing their arrivals at the seismometer, scientists can estimate the thickness of the crust and the size of the core."),
        ("Event statistics and noise", "Counting quakes over time shows how active a planet is. Instrument noise, from the wind and the lander itself, hides small quakes, so scientists must separate real signals from noise before they draw conclusions."),
    ],
    "test": [
        ("What does a seismometer record?",
         [("a", "The temperature of the air"), ("b", "Tiny shakes in the ground"), ("c", "The brightness of stars"), ("d", "The chemistry of clouds")], "b"),
        ("Which lander recorded many marsquakes between 2018 and 2022?",
         [("a", "Viking"), ("b", "Pathfinder"), ("c", "InSight"), ("d", "Phoenix")], "c"),
        ("How do seismic waves reveal a planet's interior?",
         [("a", "They travel at different speeds through different materials"), ("b", "They always travel in straight lines through air"), ("c", "They make the planet change colour"), ("d", "They stop at the surface every time")], "a"),
        ("Why must a lander seismometer be shielded?",
         [("a", "So it can glow in the dark"), ("b", "To keep it from wind, temperature changes and the lander's own movement"), ("c", "To stop it recording any data"), ("d", "To make it heavier")], "b"),
        ("Why do scientists separate signals from noise?",
         [("a", "Because noise is always the most interesting part"), ("b", "Because a real quake signal must be told apart from instrument noise before conclusions are drawn"), ("c", "Because quakes never happen on Mars"), ("d", "Because noise helps the instrument")], "b"),
    ],
}
