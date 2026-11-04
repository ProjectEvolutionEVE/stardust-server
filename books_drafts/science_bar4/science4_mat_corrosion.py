"""Corrosion and Protection: how metals wear away in their surroundings, and how to stop it."""
CODE = "science4_mat_corrosion"
BOOK = {
    "title": "Corrosion and Protection",
    "subtitle": "How metals rust, and how to stop them",
    "chapters": [
        ("What corrosion is", "Corrosion is the slow wearing away of a material by a chemical reaction with its surroundings. For iron and steel, the common result is rust. Corrosion costs large sums every year because it weakens bridges, pipes and ships."),
        ("Electrochemical corrosion", "Most metal corrosion is electrochemical. One area of metal, the anode, loses electrons and dissolves, while another area, the cathode, takes them up. Water acts as the electrolyte that lets charged ions move, so damp conditions speed corrosion up."),
        ("Passivation", "Some metals form a thin oxide layer that shields the metal beneath. Stainless steel is the best-known example, because its chromium forms a tough film of chromium oxide. If the film is damaged and oxygen can reach the metal, the film can form again and protect it."),
        ("Galvanic couples", "When two different metals touch in a wet place, the more active metal corrodes faster. The galvanic series ranks metals by how readily they corrode in sea water. Designers keep dissimilar metals apart or insulate the joint to limit this."),
        ("Coatings and cathodic protection", "Paint, zinc plating and other coatings keep water and oxygen away from the metal. Cathodic protection makes the whole structure the cathode, so a sacrificial anode, often zinc, magnesium or aluminium, corrodes in its place. Ships, pipelines and buried tanks often use this method."),
        ("Testing corrosion", "Engineers test corrosion in salt spray chambers, in immersion tests and with electrochemical measurements. Tests are only useful if they match real conditions, so the test setup is chosen with care. Results help pick materials and coatings before a structure is built."),
    ],
    "test": [
        ("What is the anode in electrochemical corrosion?",
         [("a", "The area that takes up electrons"), ("b", "The electrolyte"), ("c", "The area of metal that loses electrons and dissolves"), ("d", "The protective coating")], "c"),
        ("Why does stainless steel resist rust?",
         [("a", "A thin chromium oxide film shields the metal"), ("b", "It contains no iron at all"), ("c", "It is coated in plastic"), ("d", "It is always kept dry in a vacuum")], "a"),
        ("What does a sacrificial anode do?",
         [("a", "It makes the steel harder"), ("b", "It repels salt water"), ("c", "It paints the surface"), ("d", "It corrodes in place of the structure it protects")], "d"),
        ("What happens when two different metals touch in a wet place?",
         [("a", "Both stop corroding"), ("b", "The more active metal corrodes faster"), ("c", "They fuse into one metal"), ("d", "Neither is affected by the water")], "b"),
        ("What is the main job of a coating such as paint?",
         [("a", "To add electrons to the metal"), ("b", "To make the metal conduct better"), ("c", "To keep water and oxygen away from the metal"), ("d", "To raise the melting point")], "c"),
    ],
}
