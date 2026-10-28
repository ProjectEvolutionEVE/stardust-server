"""Crystal Plasticity and Texture: how the crystal orientation of each grain decides how a metal deforms."""
CODE = "engineering5_crystal_plast"
BOOK = {
    "title": "Crystal Plasticity and Texture",
    "subtitle": "How the crystal orientation of each grain decides how a metal deforms",
    "chapters": [
        ("Grains in a metal",
         "A metal is made of many small crystals called grains, each with its own orientation. How the grains deform together decides the behaviour of the whole piece."),
        ("Slip systems",
         "Plastic deformation happens mostly by slip, where planes of atoms slide over one another along set directions. Each crystal structure has its own set of slip systems."),
        ("The Schmid factor",
         "The Schmid factor measures how well a slip system lines up with the applied stress. A high factor means slip starts at a lower stress."),
        ("Texture from forming",
         "Rolling or drawing turns many grains to share similar orientations. This shared pattern is called texture, and it makes the metal behave differently in different directions."),
        ("Anisotropy of sheet",
         "A rolled sheet often stretches differently along and across the rolling direction. This anisotropy must be included when forming parts."),
        ("Polycrystal models",
         "These models average the response of many grains with different orientations to predict the bulk behaviour. They connect what happens in one crystal to the whole sheet."),
    ],
    "test": [
        ("What are the small crystals in a metal called?",
         [("a", "Bolts"), ("b", "Beams"), ("c", "Grains"), ("d", "Sheets")], "c"),
        ("What is slip?",
         [("a", "Planes of atoms sliding along set directions"), ("b", "A fall on ice"), ("c", "Paint dripping"), ("d", "A price fall")], "a"),
        ("What does the Schmid factor measure?",
         [("a", "The price"), ("b", "The weight"), ("c", "The colour"), ("d", "How well a slip system lines up with the applied stress")], "d"),
        ("What is texture?",
         [("a", "A fabric"), ("b", "Grains sharing similar orientations"), ("c", "A paint finish"), ("d", "A bolt type")], "b"),
        ("What does a polycrystal model do?",
         [("a", "Averages many grains with different orientations to predict bulk behaviour"), ("b", "Paints the sheet"), ("c", "Counts grains by colour"), ("d", "Sets prices")], "a"),
    ],
}
