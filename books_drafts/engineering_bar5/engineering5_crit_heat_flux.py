"""Boiling Curve and Critical Heat Flux: how a hot surface boils in a liquid, and the limit beyond which it can overheat."""
CODE = "engineering5_crit_heat_flux"
BOOK = {
    "title": "Boiling Curve and Critical Heat Flux",
    "subtitle": "Nucleate and film boiling, and the limit of safe heat removal",
    "chapters": [
        ("Boiling on a hot surface", "When a hot surface sits in a liquid, boiling removes heat from it. The way the liquid boils changes as the surface gets hotter."),
        ("The boiling curve", "The boiling curve plots the heat flux against the surface temperature. It shows several regimes, including nucleate and film boiling."),
        ("Nucleate boiling", "In nucleate boiling, bubbles form at sites on the surface and rise away. They remove heat very well, which keeps the surface temperature moderate."),
        ("Critical heat flux", "At a maximum heat flux, the bubbles merge into a vapour film that covers the surface. The vapour is a poor conductor, so the surface temperature jumps."),
        ("Surface effects", "Surface roughness and how well the liquid wets the surface both change the critical heat flux. A change in the surface can therefore change the safe limit."),
        ("Safe heat removal", "Designers keep the heat flux well below the critical value, with a margin. This avoids the sudden temperature rise that can damage equipment."),
    ],
    "test": [
        ("What does the boiling curve plot?", [("a", "Bread against butter"), ("b", "Heat flux against surface temperature"), ("c", "Weight against colour"), ("d", "Price against the weather")], "b"),
        ("What happens in nucleate boiling?", [("a", "The surface is painted by the liquid"), ("b", "Nothing forms on the surface"), ("c", "Bubbles form at sites and remove heat very well"), ("d", "Ice forms on the surface")], "c"),
        ("What happens at critical heat flux?", [("a", "Bubbles merge into a vapour film and the surface temperature jumps"), ("b", "The liquid freezes solid"), ("c", "The surface turns blue"), ("d", "The pump stops working")], "a"),
        ("What affects critical heat flux?", [("a", "The colour of a lunchbox"), ("b", "The number of chairs in the room"), ("c", "The length of the road outside"), ("d", "Surface roughness and wetting")], "d"),
        ("How do designers keep heat removal safe?", [("a", "Run the surface hotter"), ("b", "Keep heat flux well below the critical value, with a margin"), ("c", "Remove all the liquid"), ("d", "Ignore the boiling curve")], "b"),
    ],
}
