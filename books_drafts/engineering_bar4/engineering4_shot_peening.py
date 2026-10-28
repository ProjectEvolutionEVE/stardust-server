"""Shot peening and surface compression: shot media, coverage checks, compressive layers, fatigue gains, Almen strip tests and cost."""
CODE = "engineering4_shot_peening"
BOOK = {
    "title": "Shot Peening and Surface Compression",
    "subtitle": "Shot media, coverage and the compressive layer",
    "chapters": [
        ("Blasting the surface",
         "Shot peening throws small hard particles at a surface to dent it. Each dent pushes the surface outward and leaves the layer below in compression. The result is a surface that resists fatigue cracks."),
        ("Shot media",
         "The shot can be steel, cast iron or ceramic beads, chosen by size and hardness. The media size and speed set how deep the compressive layer goes. Clean, uniform shot gives a repeatable result."),
        ("Coverage checks",
         "Coverage is the share of the surface that has been dented by the shot. Inspectors check coverage by eye or with a magnifier, often using a dye. Full coverage is needed for a reliable result."),
        ("Compressive layers",
         "The peened layer is held in compression by the material below it. This layer is what slows fatigue cracks. The depth of the layer depends on the shot and the process settings."),
        ("Fatigue gains",
         "Shot peening can raise the fatigue life of springs, gears and welded parts a great deal. The gain depends on the material, the stress and the depth of the layer. Peening is one of the most useful ways to raise fatigue life."),
        ("Almen strip tests and cost",
         "An Almen strip is a thin steel strip that bends when peened, and the bend shows the peening intensity. Engineers use it to set and check the process. Peening costs media, machine time and checks, which are weighed against the fatigue gain."),
    ],
    "test": [
        ("What does shot peening do to the surface?", [("a", "Paints the surface"), ("b", "Melts the surface smooth"), ("c", "Dents it, leaving the layer below in compression"), ("d", "Adds sugar to the metal")], "c"),
        ("What is coverage in shot peening?", [("a", "The price of the shot"), ("b", "The thickness of the paint"), ("c", "The share of the surface that has been dented by the shot"), ("d", "The number of machines")], "c"),
        ("Why does a compressive layer help a part?", [("a", "It slows fatigue cracks from starting"), ("b", "It makes the part melt faster"), ("c", "It makes the part easier to paint"), ("d", "It adds weight")], "a"),
        ("What is an Almen strip?", [("a", "A wire for electric lamps"), ("b", "A strip of paper for wrapping parts"), ("c", "A plastic ruler"), ("d", "A thin steel strip that bends when peened, showing the peening intensity")], "d"),
        ("What can shot peening raise a lot?", [("a", "The price of the part"), ("b", "The fatigue life of springs, gears and welded parts"), ("c", "The weight of the packaging"), ("d", "The number of colours")], "b"),
    ],
}
