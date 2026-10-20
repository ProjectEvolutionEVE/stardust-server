"""Ceramics & Glassmaking (10-20): clay, firing and glass, the real basics."""
import minerals as MN

CODE = "ceramics"
_Q = MN.MINERALS["quartz"]

BOOK = {
    "title": "Ceramics & Glassmaking",
    "subtitle": "Clay, fire and glass: some of the oldest crafts there are",
    "chapters": [
        ("What a ceramic is",
         "A ceramic is a hard material made by heating earthy minerals until they bond. Pottery, bricks, tiles and "
         "furnace linings are all ceramics. They are hard, they take great heat, and they don't rust."),
        ("Clay and firing",
         "Wet clay can be shaped by hand. Dried, it is fragile. Fired in a kiln, it changes for good and becomes "
         "hard: low-fired earthenware is porous, while stoneware and porcelain, fired hotter, become dense and "
         "watertight."),
        ("Bricks that take the heat",
         "Refractory bricks and clays line furnaces because they stay strong at temperatures that would melt most "
         "metals. That is why, on the planet, the roots of smelting begin with stone and clay furnaces."),
        ("Glass from sand",
         f"Glass is mostly silica, the same SiO₂ as {_Q['name'].lower()}. Pure silica melts only at about "
         "1,700 °C, so glassmakers add soda to lower the melting point and lime to keep the glass from dissolving in "
         "water. Cooled quickly, the melt sets without crystals: that is glass."),
        ("Glass in the fields",
         "Our debris fields already hold natural glass. Impact glass formed when huge collisions melted rock that "
         "cooled too fast to crystallise. It is found in the fields as a mineral of its own."),
        ("What the game does today",
         "This book is background knowledge. A player who wants a kiln or a glass furnace designs it as a blueprint "
         "and sends it to the review team. The game does not yet run firing or glassmaking as steps of its own."),
    ],
    "test": [
        ("Which of these is a ceramic?",
         [("a", "A brick"), ("b", "A copper wire"), ("c", "Water"), ("d", "Gold")], "a"),
        ("What makes clay hard for good?",
         [("a", "Freezing it"), ("b", "Firing it in a kiln"), ("c", "Painting it"), ("d", "Wetting it")], "b"),
        ("What is glass mostly made of?",
         [("a", "Iron"), ("b", "Silica (SiO₂)"), ("c", "Sulfur"), ("d", "Salt")], "b"),
        ("Why do glassmakers add soda?",
         [("a", "To lower the melting point"), ("b", "For colour only"), ("c", "To make it heavier"), ("d", "For taste")], "a"),
        ("On the planet, what do the first furnaces start from?",
         [("a", "Glass"), ("b", "Stone and clay"), ("c", "Gold"), ("d", "Ice")], "b"),
    ],
}
