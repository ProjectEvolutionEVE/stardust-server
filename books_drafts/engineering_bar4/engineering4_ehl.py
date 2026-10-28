"""Elastohydrodynamic Lubrication: contact pressure, oil film formation in gears and rolling bearings, film thickness and lubricant choice."""
CODE = "engineering4_ehl"
BOOK = {
    "title": "Elastohydrodynamic Lubrication",
    "subtitle": "Oil films in gears and rolling bearings",
    "chapters": [
        ("Contact pressure",
         "In gears and rolling bearings, the contact area is tiny and the pressure there is very high. At that pressure the oil's thickness rises, and the metal surfaces deform a little."),
        ("Film formation",
         "Oil is drawn into the contact and forms a thin film that keeps the metal surfaces apart. The film is only a few micrometres thick."),
        ("Film thickness",
         "Film thickness depends on speed, viscosity and load, and on how the viscosity rises under pressure. A thicker film keeps the surfaces apart, but only up to a point."),
        ("Gears and rolling bearings",
         "These parts rely on this film. Their designs check the film thickness against the roughness of the surfaces."),
        ("Lubricant choice",
         "A lubricant with the right viscosity forms the right film. Too thin and the film breaks down. Too thick and it adds drag and heat."),
        ("Why the surfaces survive",
         "The film carries the load, so the metal rarely touches metal. That prevents pitting and wear."),
    ],
    "test": [
        ("Where does elastohydrodynamic lubrication matter most?",
         [("a", "Gears and rolling bearings"), ("b", "Paint"), ("c", "Sails"), ("d", "Hats")], "a"),
        ("What does the oil film do?",
         [("a", "Makes sound"), ("b", "Melts parts"), ("c", "Adds colour"), ("d", "Keeps the metal surfaces apart")], "d"),
        ("What does film thickness depend on?",
         [("a", "Colour"), ("b", "Speed, viscosity and load"), ("c", "Music"), ("d", "Weather")], "b"),
        ("What happens if the lubricant is too thin?",
         [("a", "A better film forms"), ("b", "Less heat"), ("c", "A stronger oil"), ("d", "The film may break and metal touches metal")], "d"),
        ("What does a good film prevent?",
         [("a", "Pitting and wear"), ("b", "Growth"), ("c", "Sunshine"), ("d", "Music")], "a"),
    ],
}
