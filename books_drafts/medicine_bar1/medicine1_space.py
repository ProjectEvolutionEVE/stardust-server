"""Medicine, bar 1: The Body in Space. Real effects of living in low gravity and radiation, and how crews keep well."""
CODE = 'medicine1_space'
BOOK = {
    "title": 'The Body in Space',
    "subtitle": 'How low gravity, fluid shifts and radiation change the body, and how crews keep well',
    "chapters": [
        ('Built for gravity',
         'The human body was shaped by life on Earth, where gravity pulls on it all day long. Muscles and bones are kept in shape by that steady pull. Take the pull away, and the body starts to change.'),
        ('Muscle loss',
         'In low gravity the muscles that hold posture and move the legs have less work to do, so they get smaller and weaker over time. Daily strength exercise is the main way crews keep their muscles in good shape.'),
        ('Bone loss',
         'Bones stay strong partly because of the load they carry. In space, bones lose some of their mineral and density, most in the legs and hips, and the loss continues for as long as the body stays in low gravity. Regular strength exercise helps slow it.'),
        ('Fluid shifts',
         'On Earth, gravity pulls body fluid down into the legs. In space, fluid drifts up toward the head and chest. Many people notice a puffy face and a stuffy nose at first, and the body slowly adjusts over several days.'),
        ('Radiation',
         'Beyond Earth\'s atmosphere and magnetic field, space carries more radiation from the Sun and from cosmic rays. Ships reduce the dose with shielding, such as thick walls and stored supplies including water, and with careful planning of how long people spend in the most exposed places.'),
        ('Sleep, rhythm and exercise',
         'The body keeps a daily rhythm called the circadian rhythm, set mostly by light. A ship may have no sunrise, so crews keep a steady sleep schedule and a set daily routine. On the International Space Station, astronauts exercise about two hours a day to fight muscle and bone loss.'),
    ],
    "test": [
        ('What happens to muscles in low gravity without exercise?',
         [('a', 'They grow larger'), ('b', 'They get smaller and weaker'), ('c', 'Nothing changes'), ('d', 'They become stronger')], 'b'),
        ('Where does body fluid tend to move in space?',
         [('a', 'Out through the skin'), ('b', 'It disappears'), ('c', 'Toward the head and chest'), ('d', 'Down into the legs')], 'c'),
        ('What helps protect a ship\'s crew from radiation?',
         [('a', 'Thin windows'), ('b', 'Bright lights'), ('c', 'Loud music'), ('d', 'Shielding, such as thick walls and stored supplies')], 'd'),
        ('What is the body\'s daily rhythm called?',
         [('a', 'The circadian rhythm'), ('b', 'The fluid shift'), ('c', 'A cosmic ray'), ('d', 'The bone marrow')], 'a'),
        ('About how long do astronauts on the International Space Station exercise each day?',
         [('a', 'They do not exercise'), ('b', 'About 15 minutes'), ('c', 'About 2 hours'), ('d', 'About 12 hours')], 'c'),
    ],
}
