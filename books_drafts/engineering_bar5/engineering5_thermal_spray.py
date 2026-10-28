"""Thermal Spray Coatings: plasma and flame spraying, particle velocity, porosity, bond strength and coating qualification."""
CODE = "engineering5_thermal_spray"
BOOK = {
    "title": "Thermal Spray Coatings",
    "subtitle": "Spraying molten particles onto a part to build a coating",
    "chapters": [
        ("Spraying hot particles",
         "Thermal spray melts or softens powder or wire in a hot flame or plasma. The hot particles are blown at the part, where they flatten and stick. The coating builds up one pass at a time."),
        ("Plasma and flame",
         "Plasma spraying uses a very hot electric arc gas to melt the particles. Flame spraying burns fuel to do the same job, with less heat. The choice depends on the material and the coating needed."),
        ("Particle velocity",
         "How fast a particle hits the part matters. Faster particles flatten better and make a denser coating. High-velocity methods push particles very fast, which gives strong, dense layers."),
        ("Porosity",
         "Thermal sprayed coatings usually have some pores between the splats. Porosity can help hold lubricant, but it can also let corrosion in. The engineer picks the spray method to match the amount of porosity wanted."),
        ("Bond strength",
         "The coating must bond to the base metal. Roughening the surface and cleaning it well help the bond. A coating that lifts off has failed, so bond tests are an important check."),
        ("Qualifying the coating",
         "Before a coating goes into service, it is tested on sample parts. The tests check thickness, bond, porosity and hardness. Only a process that passes every check is approved for production parts."),
    ],
    "test": [
        ("What does thermal spray do with the powder or wire?",
         [("a", "It freezes it in ice"), ("b", "It dissolves it in water"), ("c", "It leaves it dry on a shelf"), ("d", "It melts or softens it in a hot flame or plasma")], "d"),
        ("What does particle velocity affect?",
         [("a", "How flat and dense the particles become on the part"), ("b", "The colour of the sky"), ("c", "The weight of the operator"), ("d", "The price of the paper")], "a"),
        ("Why can some porosity be useful in a thermal spray coating?",
         [("a", "It makes the coating stronger in all ways"), ("b", "It can help hold lubricant"), ("c", "It stops all corrosion"), ("d", "It removes the need for a bond")], "b"),
        ("What helps the coating bond to the base metal?",
         [("a", "A polished mirror finish"), ("b", "A coat of wax"), ("c", "A roughened, well-cleaned surface"), ("d", "Leaving the surface dirty")], "c"),
        ("What does qualifying a coating mean?",
         [("a", "Naming the coating after a city"), ("b", "Painting the coating red"), ("c", "Skipping all tests"), ("d", "Testing sample parts before the coating goes into service")], "d"),
    ],
}
