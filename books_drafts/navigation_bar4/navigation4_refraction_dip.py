"""Refraction and Dip: why the stars and the horizon do not sit exactly where they seem."""
CODE = "navigation4_refraction_dip"
BOOK = {
    "title": "Refraction and Dip",
    "subtitle": "Why the stars and the horizon are not quite where they seem",
    "chapters": [
        ("Why light bends", "Light from a star passes through the air on its way to you. The air is denser near the ground, so the light bends. The star looks a little higher than it really is."),
        ("Refraction tables", "Navigators look up refraction in tables, or work it out from the observed altitude. Refraction is largest near the horizon and almost nothing overhead. The correction is subtracted from the observed altitude."),
        ("The dip of the horizon", "When you measure to the sea horizon, the horizon sits a little below the level of your eye. The higher your eye, the further below it appears. This dip correction is also subtracted."),
        ("Height of eye", "The dip depends on the square root of your height above the sea. Stand higher and the dip grows, but more slowly than the height. Enter the correct height of eye in the tables."),
        ("Temperature and pressure", "Cold, dense air bends light more than warm, thin air. Refraction tables allow for temperature and pressure. Using the wrong values adds a small error to the altitude."),
        ("Applying the corrections", "Apply the corrections in the right order, subtracting refraction and dip from the sextant reading. Keep a note of each correction you use. A clear record makes a check much easier."),
    ],
    "test": [
        ("What happens to a star's apparent height because of refraction?",
         [("a", "It looks lower"), ("b", "It moves sideways"), ("c", "It disappears"), ("d", "It looks higher than it really is")], "d"),
        ("Where is refraction largest?",
         [("a", "Straight overhead"), ("b", "Near the horizon"), ("c", "At the Pole only"), ("d", "At noon only")], "b"),
        ("What happens to the dip of the horizon as eye height grows?",
         [("a", "It shrinks to zero"), ("b", "It stays exactly the same"), ("c", "It grows"), ("d", "It turns into refraction")], "c"),
        ("How is the dip correction applied to a sextant altitude?",
         [("a", "It is subtracted"), ("b", "It is added"), ("c", "It is multiplied by the azimuth"), ("d", "It is ignored at sea")], "a"),
        ("Which air condition makes light bend more?",
         [("a", "Cold, dense air"), ("b", "Warm, thin air"), ("c", "Air with no pressure"), ("d", "Air above a mountain only")], "a"),
    ],
}
