"""Precipitation Kinetics and the JMAK Equation: how fast new particles form inside a solid alloy, and why timing matters."""
CODE = "engineering5_precip_kinetics"
BOOK = {
    "title": "Precipitation Kinetics and the JMAK Equation",
    "subtitle": "How fast new particles form inside a solid alloy, and why timing matters",
    "chapters": [
        ("Particles inside a solid",
         "Some alloys form tiny particles inside the solid when they are held at the right temperature. These particles strengthen the alloy."),
        ("Nucleation and growth",
         "Precipitation has two stages: new particles nucleate, and then they grow. The rates of both depend on temperature."),
        ("The Avrami equation",
         "The JMAK, or Avrami, equation gives the fraction transformed as a function of time, using an exponent and a rate constant. It gives an S-shaped curve over time."),
        ("Time-temperature-transformation diagrams",
         "TTT diagrams show how long a transformation takes at each temperature. The nose of the curve marks the fastest point."),
        ("Ageing of alloys",
         "Ageing is a heat treatment that lets fine precipitates form and strengthen the alloy. If it goes on too long, the particles coarsen and the strength falls."),
        ("Timing in practice",
         "Engineers choose the ageing time and temperature from the kinetics, so that the alloy reaches its peak strength. Going past peak is called overageing."),
    ],
    "test": [
        ("What is precipitation?",
         [("a", "Rain"), ("b", "Paint dripping"), ("c", "A price rise"), ("d", "New particles forming inside a solid alloy")], "d"),
        ("What does the Avrami equation give?",
         [("a", "The fraction transformed as a function of time"), ("b", "The colour"), ("c", "The cost"), ("d", "The weight")], "a"),
        ("What does the nose of a TTT diagram mark?",
         [("a", "The price"), ("b", "The paint"), ("c", "The fastest point of the transformation"), ("d", "The weight")], "c"),
        ("What is ageing?",
         [("a", "A paint finish"), ("b", "A heat treatment that lets fine precipitates form"), ("c", "A price discount"), ("d", "A bolt type")], "b"),
        ("What is overageing?",
         [("a", "Holding too long, so particles coarsen and strength falls"), ("b", "Going too fast"), ("c", "A paint fault"), ("d", "A price rise")], "a"),
    ],
}
