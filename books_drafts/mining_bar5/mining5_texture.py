"""Crystallographic Texture: how rolling and drawing line up crystal grains, why that makes metal behave differently in different directions."""
CODE = "mining5_texture"
BOOK = {
    "title": "Crystallographic Texture",
    "subtitle": "When the grains line up, the metal behaves differently in each direction",
    "chapters": [
        ("Grains with a preferred direction", "In a metal made of many grains, each grain has its own orientation. When the grains tend to point the same way, the metal has a texture. Texture is a hidden property that shapes how the metal behaves."),
        ("How rolling creates texture", "Rolling a sheet squeezes and stretches the grains in a set pattern. Over many passes, the grains turn toward a few preferred orientations, which are called rolling textures."),
        ("Anisotropy", "A textured sheet is anisotropic: it has different strength and stretch in different directions. A sheet can be stiffer across the rolling direction than along it, for example."),
        ("Earing in deep drawing", "When a flat disc is drawn into a cup, a textured sheet can form wavy edges called ears. These ears must be trimmed away, which wastes metal. Drink cans are a familiar example of the problem."),
        ("Measuring texture", "Texture is measured with X-ray pole figures or with electron backscatter diffraction, which maps each grain. The results show where the grains point and how strong the preference is."),
        ("Controlling texture", "Annealing, the rolling plan and the amount of each reduction all shape the texture. Makers tune these steps so the sheet forms well and behaves as the design needs."),
    ],
    "test": [
        ("What is texture in a metal?",
         [("a", "The colour of the surface"), ("b", "Grains tending to point the same way"), ("c", "The temperature of the metal"), ("d", "The shape of the box it is stored in")], "b"),
        ("What is anisotropy?",
         [("a", "Having the same properties in every direction"), ("b", "Being liquid at room temperature"), ("c", "Having no weight"), ("d", "Having different properties in different directions")], "d"),
        ("What are the wavy edges that form when a textured sheet is drawn into a cup?",
         [("a", "Bubbles"), ("b", "Stripes"), ("c", "Ears"), ("d", "Cracks in glass")], "c"),
        ("Which method maps the orientation of each grain?",
         [("a", "Electron backscatter diffraction"), ("b", "Hand weighing"), ("c", "Taste testing"), ("d", "Sound listening")], "a"),
        ("Which step can be used to control texture?",
         [("a", "Painting"), ("b", "Freezing the sheet in ice"), ("c", "Annealing"), ("d", "Dropping the sheet in sand")], "c"),
    ],
}
