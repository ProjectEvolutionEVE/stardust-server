"""Inspection: finding flaws before they fail, with methods that test a part without breaking it."""
CODE = 'engineering2_inspection'
BOOK = {
    "title": 'Inspection: Finding Flaws Before They Fail',
    "subtitle": 'Non-destructive methods for checking a part without breaking it',
    "chapters": [
        ('Inspect before you trust',
         "Inspection checks that a part is sound before anyone relies on it. Many faults hide inside metal or under paint, where the "
         "eye cannot see them. Non-destructive testing, or NDT, finds them without cutting or breaking the part."),
        ('Look first: visual inspection',
         "The first check is the eye, with good light and a magnifier. Look for cracks, dents, rust, scoring, bent parts and loose "
         "fittings. A borescope, a thin flexible camera, lets you look inside pipes and engines through a small opening."),
        ('Dye penetrant',
         "A coloured or fluorescent liquid is spread over a clean surface. It is drawn into any crack that breaks the surface. After "
         "the surface is wiped clean, a developer draws the liquid back out, so the crack shows. This works on most non-porous "
         "materials, but not on cracks sealed below the surface."),
        ('Magnetic particle',
         "In magnetic metals such as steel, a magnetic field is set up in the part. Iron particles dusted on the surface gather at any "
         "crack, because the crack disturbs the field. It is quick, and good for surface cracks and cracks just below the surface."),
        ('Ultrasound',
         "A probe sends high-frequency sound into the metal. Echoes come back from the far wall and from any flaw in between, and the "
         "timing of the echoes shows where the flaw is. The same timing measures wall thickness, which reveals corrosion from inside."),
        ('Keep records',
         "Write down what was checked, by which method, what was found, and when. A trend of growing cracks or thinning walls means a "
         "part is due for replacement before it fails. Repeat the same test the same way, so that changes can be seen."),
    ],
    "test": [
        ("What does NDT stand for?",
         [('a', 'Non-destructive testing'), ('b', 'Non-dangerous tools'), ('c', 'Normal data transfer'), ('d', 'New drawing type')], 'a'),
        ("What does dye penetrant testing show?",
         [('a', 'Heat trapped inside a part'), ('b', 'The weight of a part'), ('c', 'Cracks that break the surface'), ('d', 'The colour of the metal')], 'c'),
        ("What does an ultrasonic check rely on?",
         [('a', 'Light from a lamp'), ('b', 'Sound echoes that come back from the far wall and from any flaws'), ('c', 'The smell of the metal'), ('d', 'Electric current in the air')], 'b'),
        ("Which method suits magnetic metals such as steel?",
         [('a', 'Dye penetrant only'), ('b', 'Taste testing'), ('c', 'A look by eye with no light'), ('d', 'Magnetic particle inspection')], 'd'),
        ("Why keep inspection records?",
         [('a', 'To spot trends, such as growing cracks or thinning walls, before a part fails'), ('b', 'To save paper'), ('c', 'To sell the metal'), ('d', 'They are never useful')], 'a'),
    ],
}
