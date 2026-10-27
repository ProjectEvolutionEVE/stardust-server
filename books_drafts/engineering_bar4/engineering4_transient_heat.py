"""Transient Heating: How Fast Parts Warm Up. Lumped heat capacity, time constants, heating curves and a quick hand check."""
CODE = 'engineering4_transient_heat'
BOOK = {
    "title": "Transient Heating: How Fast Parts Warm Up",
    "subtitle": "Heating and cooling curves, time constants and a quick hand check",
    "chapters": [
        ("Lumped heat capacity",
         "If a part is small and its temperature is nearly even throughout, it can be treated as one lump with a single temperature. This simple model is often good enough."),
        ("Time constants",
         "The time constant is the time a part takes to cover about 63% of the gap to its final temperature. It depends on the part's mass, its heat capacity and how easily heat reaches its surface."),
        ("Heating and cooling curves",
         "A heating or cooling curve starts steep and flattens as the part nears the temperature of its surroundings. In the lumped model, the curve is exponential."),
        ("Thermal shock",
         "A sudden temperature change can crack a brittle part, because the outside and inside expand at different rates. Slowing the change reduces the risk."),
        ("Checking a design by hand",
         "A quick estimate using the time constant gives a sanity check before a full analysis. A rough answer that looks wrong is a sign to look again."),
        ("Why it matters",
         "Heat-up time sets process speed, energy use and safety. Good estimates save time in the design stage."),
    ],
    "test": [
        ("What does the lumped model assume?",
         [("a", "The part is on fire"), ("b", "The part is a liquid"), ("c", "The part has nearly one even temperature"), ("d", "The part is painted")], "c"),
        ("What is the time constant?",
         [("a", "The time to cover about 63% of the gap to the final temperature"), ("b", "The time of the lunch break"), ("c", "The length of a shift"), ("d", "The year")], "a"),
        ("What is thermal shock?",
         [("a", "A shock to the ears"), ("b", "A loud bang"), ("c", "A gust of wind"), ("d", "A sudden temperature change that can crack a brittle part")], "d"),
        ("What shape does a heating curve take in the lumped model?",
         [("a", "A straight line"), ("b", "It starts steep and flattens as it nears the surroundings' temperature"), ("c", "A spiral"), ("d", "A loop")], "b"),
        ("What is a quick hand check for?",
         [("a", "A rough estimate before a full analysis"), ("b", "Replacing all tests"), ("c", "Painting parts"), ("d", "Cutting metal")], "a"),
    ],
}
