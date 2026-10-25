"""Materials and Their Strengths: metals, ceramics and plastics, and how strong, stiff and heavy each one is."""
CODE = 'engineering1_materials'
BOOK = {
    "title": 'Materials and Their Strengths',
    "subtitle": 'Metals, ceramics and plastics: how strong, stiff and heavy each one is',
    "chapters": [
        ('Three families of material',
         'Most of what engineers build from is one of three families. Metals, such as iron, copper and aluminium, can be '
         'bent and shaped, and they usually bend before they break. Ceramics, such as brick, tile and glass, are very hard '
         'but brittle. Plastics are light and easy to shape.'),
        ('Strength, stiffness and weight',
         'Strength is how much load a material can take before it breaks or bends for good. Stiffness is how much it '
         'resists bending or stretching under the same load. Weight is density: the mass of one cubic metre. A good '
         'design balances all three, and it rarely maximises just one.'),
        ('Metals',
         'Iron is 7,874 kg per cubic metre in the Raw Materials Catalogue, and steel, which is mostly iron, is about the '
         'same. Aluminium is about 2,700, roughly a third of steel, which is why it is used where weight matters. '
         'Titanium, at about 4,507, is strong for its weight and resists rust. Metals are tough, which means they can '
         'take a sharp blow and still hold together.'),
        ('Ceramics: hard and heat-proof',
         'Ceramics such as brick, fired clay and glass stay strong at temperatures that would soften most metals, and '
         'they do not rust. Many are stiffer than steel. Their weak point is brittleness: they handle squeezing well, but '
         'they crack under a sudden blow or a pull. Basalt, the dark volcanic rock in our debris fields, is about 2,900 kg '
         'per cubic metre and is also used as a building stone.'),
        ('Plastics: light and easy to shape',
         'Plastics are long chains of molecules. Polyethylene, the plastic in bags and bottles, is about 950 kg per cubic '
         'metre, so it floats on water. Plastics are cheap and easy to mould, but they are far less stiff than metal, and '
         'many soften when they get hot.'),
        ('Choosing for the job',
         'Pick the material for what the part must do. A part that moves wants low weight and enough strength. A part that '
         'carries a load wants strength and stiffness. A part that sits near heat wants a material that stays strong when '
         'hot. Work out the weight from the densities before you build, not after.'),
    ],
    "test": [
        ("Which family of material is usually tough enough to bend before it breaks?",
         [("a", "Ceramics"), ("b", "Plastics"), ("c", "Metals"), ("d", "Gases")], "c"),
        ("What is density?",
         [("a", "How hard a material is"), ("b", "Mass per cubic metre"), ("c", "How hot it can get"), ("d", "How well it conducts electricity")], "b"),
        ("Which of these weighs about a third as much as steel for the same volume?",
         [("a", "Aluminium"), ("b", "Gold"), ("c", "Lead"), ("d", "Tungsten")], "a"),
        ("Why are ceramics a poor choice for a part that takes sharp blows?",
         [("a", "They are too heavy to lift"), ("b", "They conduct electricity too well"), ("c", "They float on water"), ("d", "They are brittle and can crack under a sudden blow")], "d"),
        ("What happens to polyethylene, the plastic in bags, when you put it in water?",
         [("a", "It sinks at once"), ("b", "It dissolves"), ("c", "It floats, because it is less dense than water"), ("d", "It turns into steel")], "c"),
    ],
}
