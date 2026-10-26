"""Engineering in Vacuum and Cold: what changes when there is no air to carry heat, and how cold changes metal and seals."""
CODE = 'engineering2_vacuum'
BOOK = {
    "title": 'Engineering in Vacuum and Cold',
    "subtitle": 'What changes without air to carry heat, and how deep cold changes metal and seals',
    "chapters": [
        ('No air to carry heat',
         "On Earth, air carries heat away from a hot part by moving and touching it. In vacuum there is no air to do this, so a part "
         "sheds heat only by radiation. Radiators, with large surfaces facing space, do this job, and a part in sunlight can get very hot."),
        ('Sunlight and shade',
         "A surface in sunlight can get very hot, and in shadow it can fall to a very low temperature. The same part can be hot on one side "
         "and cold on the other. Design for both, and choose coatings: a light, shiny surface reflects sunlight, while a dark surface "
         "absorbs it and also radiates heat away more easily."),
        ('Cold makes some metals brittle',
         "Many ordinary steels become brittle as they get colder, and a sharp knock can crack them. Aluminium, copper and austenitic "
         "stainless steel keep their toughness at low temperatures, which is why they are often chosen for tanks that hold very cold liquids."),
        ('Seals and lubricants',
         "Rubber and plastic seals stiffen in the cold and can lose their grip, so they leak. Oils and greases thicken or freeze. In vacuum, "
         "some oils evaporate, so engineers use dry lubricants such as molybdenum disulfide. Test every seal and lubricant at the coldest "
         "temperature the part will see."),
        ('Clean metal sticks',
         "In air, a thin oxide film usually stops two clean metal faces from welding when pressed together. In vacuum that film can be "
         "missing, so clean metal surfaces can cold weld and stick without any heat. Keep moving faces apart with a coating or a deliberate "
         "gap, and clean them with care."),
        ('Test in real conditions',
         "Test a part at the temperatures, pressure and light it will meet. Account for its expansion when cold, as the book on hot and cold "
         "parts explains, and check that a part that fits when warm still fits and moves when cold."),
    ],
    "test": [
        ("Why does a part in vacuum need radiators?",
         [('a', 'Vacuum is cold'), ('b', 'Vacuum makes metal heavier'), ('c', 'Vacuum draws heat out of the part by suction'), ('d', 'With no air to carry heat away, a part can only shed heat by radiation, so it needs large surfaces')], 'd'),
        ("Which metal keeps its toughness in deep cold, unlike many ordinary steels?",
         [('a', 'Aluminium'), ('b', 'Plain carbon steel'), ('c', 'Cast iron'), ('d', 'Ceramic tile')], 'a'),
        ("What can happen to two clean metal faces pressed together in vacuum?",
         [('a', 'They rust'), ('b', 'They melt'), ('c', 'They can cold weld and stick'), ('d', 'They become magnetic')], 'c'),
        ("What do rubber seals do in deep cold?",
         [('a', 'They grow larger'), ('b', 'They stiffen and can lose their grip, so they leak'), ('c', 'They turn into metal'), ('d', 'They conduct electricity')], 'b'),
        ("Why are dry lubricants used in vacuum?",
         [('a', 'Oils and greases can evaporate in vacuum'), ('b', 'Dry lubricants are cheaper'), ('c', 'Oils are magnetic'), ('d', 'Dry lubricants glow in the dark')], 'a'),
    ],
}
