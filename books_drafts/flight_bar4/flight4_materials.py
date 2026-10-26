"""Materials in Space: which metals and plastics survive vacuum, bright sunlight, atomic oxygen and hot-cold cycles."""
CODE = "flight4_materials"
BOOK = {
    "title": "Materials in Space",
    "subtitle": "Choosing what survives vacuum and temperature swings",
    "chapters": [
        ("Light and strong", "Spacecraft need materials that are strong but light. Aluminium and titanium are common metals. Each has its own strengths and weaknesses for the job."),
        ("Composites", "Composites are made from fibres set in a resin. Carbon fibre composites are light and very stiff, and they are widely used for panels and frames."),
        ("Vacuum outgassing", "In a vacuum, some materials slowly release gas trapped inside them. This is called outgassing. The gas can cloud lenses or coat sensors, so engineers pick low-outgassing materials."),
        ("Atomic oxygen", "In low Earth orbit, a thin layer of single oxygen atoms can wear down some plastics and coatings. Engineers choose materials or coatings that can resist this slow erosion."),
        ("Thermal cycling", "A craft swings between hot sunlight and cold shadow many times a day. Materials expand and shrink with each swing, and joints can crack if the materials do not match well."),
        ("Cold welding", "In a vacuum, two clean metal surfaces pressed together can bond with no heat at all. This is called cold welding. Engineers keep moving parts apart with lubricants or surface coatings."),
    ],
    "test": [
        ("What is outgassing?", [("a", "A type of rocket engine"), ("b", "A bright light"), ("c", "Trapped gas slowly released in a vacuum"), ("d", "Air cooling in a tent")], "c"),
        ("What can atomic oxygen in low orbit do?", [("a", "Wear down some plastics and coatings"), ("b", "Make metal hot to touch"), ("c", "Turn the craft into a ship"), ("d", "Give the crew air")], "a"),
        ("What is cold welding?", [("a", "Welding ice to a wall"), ("b", "Painting metal blue"), ("c", "Cooling a welder"), ("d", "Two clean metal surfaces bonding in a vacuum with no heat")], "d"),
        ("Why can thermal cycling crack joints?", [("a", "The joints are made of paper"), ("b", "Materials expand and shrink with each swing, and mismatched ones can crack"), ("c", "The sun is always cold"), ("d", "Joints do not move")], "b"),
        ("What is a composite?", [("a", "A type of spacesuit"), ("b", "A kind of tea"), ("c", "Fibres set in a resin, such as carbon fibre"), ("d", "A paper map")], "c"),
    ],
}
