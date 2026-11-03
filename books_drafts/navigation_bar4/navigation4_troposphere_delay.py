"""The Tropospheric Delay: water vapour and dry air slowing the signal in the lowest layer of air."""
CODE = "navigation4_troposphere_delay"
BOOK = {
    "title": "The Tropospheric Delay",
    "subtitle": "Water vapour and air slowing the signal",
    "chapters": [
        ("Water vapour and dry air", "The troposphere is the lowest layer of the atmosphere. It holds water vapour and dry air. Both slow radio signals, so both cause a delay."),
        ("The zenith delay", "The zenith delay is the delay for a signal coming straight from above. Most of it comes from dry air. The rest comes from water vapour, which varies much more from place to place."),
        ("The mapping function", "Signals arriving from low angles pass through more air. A mapping function scales the zenith delay to each satellite's angle. This keeps the correction right at every height above the horizon."),
        ("Weather models", "Weather models give pressure, temperature and humidity. These values help calculate the delay. Good weather data gives better corrections."),
        ("The wet component", "The wet component comes from water vapour. It is harder to predict than the dry part. It can change quickly with the weather."),
        ("Uses in meteorology", "GNSS receivers can estimate the amount of water vapour in the air. Meteorologists use these estimates in forecasts. The tropospheric delay becomes useful data as well as an error."),
    ],
    "test": [
        ("What is the troposphere?",
         [("a", "The highest layer of space"), ("b", "The lowest layer of the atmosphere"), ("c", "A kind of sea"), ("d", "A type of rock")], "b"),
        ("Which part of the zenith delay is the larger?",
         [("a", "The part from the Moon"), ("b", "The part from the sea"), ("c", "The part from the trees"), ("d", "The dry air part")], "d"),
        ("What does a mapping function do?",
         [("a", "It makes maps bigger"), ("b", "It counts clouds"), ("c", "It scales the delay to each satellite's angle"), ("d", "It draws roads")], "c"),
        ("What do weather models provide?",
         [("a", "Football scores"), ("b", "Star names"), ("c", "Pressure, temperature and humidity"), ("d", "Musical notes")], "c"),
        ("Why is the wet component harder to predict?",
         [("a", "It is made of rock"), ("b", "It changes quickly with the weather"), ("c", "It is always zero"), ("d", "It is made of paper")], "b"),
    ],
}
