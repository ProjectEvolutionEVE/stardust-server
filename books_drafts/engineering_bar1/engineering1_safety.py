"""Workshop Safety: protective gear, tools, heat, pressure and electricity, in general terms for any real workshop."""
CODE = 'engineering1_safety'
BOOK = {
    "title": 'Workshop Safety',
    "subtitle": 'Protective gear, tools, heat, pressure and electricity: the habits that keep hands whole',
    "chapters": [
        ('Plan before you start',
         'A workshop is safe when people plan before they begin. Look at the job, check the tools and the work area, and ask '
         'what could go wrong. Most accidents come from rushing, from skipping a check, or from a messy floor.'),
        ('Protective gear',
         'Wear safety glasses or goggles whenever something could fly, splash or shatter. Wear ear protection near loud '
         'machines, and a dust mask or respirator around dust and fumes. Tie back long hair, and do not wear loose clothing, '
         'jewellery or gloves near anything that spins.'),
        ('Hand tools and power tools',
         'Keep blades sharp and tools in good repair, because a dull blade needs more force and slips more. Use the guards on '
         'machines, and keep your fingers clear of moving parts. Unplug a power tool before you change a blade or bit, and never '
         'carry it by its cord.'),
        ('Heat and hot material',
         'Hot metal looks the same as cold metal, so treat anything that has been heated as hot until it has cooled. Use tongs '
         'and heat-proof gloves, and keep flammable things away from heat. Make sure the air moves freely where heat or fumes are '
         'made, and keep a fire extinguisher close by, knowing how to use it.'),
        ('Pressure and gas',
         'Compressed air can drive dust or chips into skin or eyes, so never point an air line at a person. Check hoses for '
         'damage before use. Gas cylinders and pressure vessels should be secured upright, and everyone should know where the '
         'shut-off valve is.'),
        ('Electricity and water',
         'Keep power tools and cords dry and in good repair. Where you work with mains power outdoors or near water, use a '
         'residual current device (RCD in the UK, GFCI in the US), which cuts the power when it detects a fault. Never work on '
         'live wiring. If something smells hot, sparks or trips the breaker, switch it off and have it checked.'),
    ],
    "test": [
        ("What should you wear when something could fly, splash or shatter?",
         [("a", "Sunglasses"), ("b", "Nothing at all"), ("c", "Slippers"), ("d", "Safety glasses or goggles")], "d"),
        ("What should you do before you change a blade or bit on a power tool?",
         [("a", "Switch it on to test it"), ("b", "Unplug it"), ("c", "Hold it by the cord"), ("d", "Blow on it")], "b"),
        ("Why should you treat metal that has been heated as hot?",
         [("a", "It looks the same as cold metal, so you cannot tell by looking"), ("b", "Hot metal is always heavier"), ("c", "Hot metal always glows"), ("d", "Heat makes metal lighter")], "a"),
        ("What must you never do with a compressed-air line?",
         [("a", "Dry a part you have just washed"), ("b", "Keep the hose in a dry place"), ("c", "Point it at a person's skin or eyes"), ("d", "Check the hose for damage")], "c"),
        ("Which device cuts the power when it detects a fault, to help prevent electric shock?",
         [("a", "A residual current device (RCD or GFCI)"), ("b", "A louder radio"), ("c", "A thicker coat"), ("d", "A ladder")], "a"),
    ],
}
