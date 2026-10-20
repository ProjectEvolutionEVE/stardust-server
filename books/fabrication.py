"""Fabrication: making parts from metal and other materials. Real-world basics; aboard, only what exists."""
CODE = "fabrication"
BOOK = {
    "title": "Fabrication",
    "subtitle": "Turning metal and materials into real parts",
    "chapters": [
        ("What fabrication is",
         "Fabrication is making parts: taking metal and other materials and shaping them into something that does a "
         "job. Smelting gives you metal; fabrication turns that metal into a bracket, a pipe, a panel or a gear."),
        ("Four ways to shape metal",
         "• Casting: melt the metal and pour it into a mould. Good for complicated shapes.\n"
         "• Forging: heat the metal and hammer or press it into shape. Forged parts are strong.\n"
         "• Machining: cut metal away from a solid block with drills, lathes and mills. Good for exact sizes.\n"
         "• Joining: weld, bolt or rivet pieces together into something bigger."),
        ("Picking the right material",
         "Every material has a real density, so the same part weighs very different amounts:\n"
         "• Aluminium about 2,700 kg per cubic metre: light, and easy to work.\n"
         "• Titanium about 4,500: strong for its weight, and it resists corrosion.\n"
         "• Iron about 7,870: strong and cheap, but heavy. Add a little carbon and you get steel.\n"
         "• Copper about 8,960: the one to pick when a part must carry electricity or heat.\n"
         "In a ship, weight matters, so builders look for the lightest material that is strong enough."),
        ("Measure twice, cut once",
         "A good part starts with a good plan: its sizes, the material and the steps, written down before anyone cuts. "
         "That plan is a blueprint. Mistakes are cheap on paper and expensive in metal."),
        ("Heat makes metal grow",
         "Metals expand when they get hot and shrink when they cool. In space, a part can swing from fierce sunlight "
         "to deep shadow, so good designs leave room for that movement. Another space fact: two clean pieces of the "
         "same metal pressed together in a vacuum can stick fast, called cold welding."),
        ("Fabrication aboard",
         "Aboard the Starship, the things players make start as blueprints, designed by players and reviewed by the "
         "team. A blueprint lists each raw material and its amount, and how it's built. You never type in a part's "
         "weight or size: they come from the real densities of its materials."),
    ],
    "test": [
        ("What is pouring melted metal into a mould called?",
         [("a", "Forging"), ("b", "Casting"), ("c", "Machining"), ("d", "Riveting")], "b"),
        ("Which of these metals is the lightest?",
         [("a", "Iron"), ("b", "Copper"), ("c", "Aluminium"), ("d", "Gold")], "c"),
        ("What do you get when you add a little carbon to iron?",
         [("a", "Steel"), ("b", "Bronze"), ("c", "Slag"), ("d", "Glass")], "a"),
        ("What happens to metal when it gets hot?",
         [("a", "It shrinks"), ("b", "Nothing"), ("c", "It expands"), ("d", "It turns to gas at once")], "c"),
        ("Where does a blueprint's weight come from?",
         [("a", "The designer types it in"), ("b", "The real densities of its materials"), ("c", "A guess"), ("d", "The market price")], "b"),
    ],
}
