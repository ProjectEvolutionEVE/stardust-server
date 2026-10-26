"""Welding: joining metal by melting, the main processes, and how the heat changes the metal around the joint."""
CODE = 'engineering3b_welding'
BOOK = {
    "title": 'Welding: Joining Metal by Melting',
    "subtitle": 'Arc, wire and gas welding, and how the heat changes the metal around the joint',
    "chapters": [
        ('Welding melts the joint',
         'Welding joins two pieces of metal by melting their edges, usually with an extra filler metal, so the pieces fuse into one. When the pool cools and goes solid, the joint can be as strong as the metal around it. Brazing and soldering differ, because they melt only a filler and leave the base metal solid.'),
        ('Arc welding',
         'In arc welding, an electric arc between an electrode and the work melts the metal. Stick welding uses a coated electrode whose coating makes a protective gas. MIG welding feeds a wire through a gun, with a shielding gas that keeps the air off the molten pool.'),
        ('TIG for fine work',
         'TIG welding uses a tungsten electrode that does not melt, and a filler rod added by hand. It makes neat, precise joints in thin metal, and in metals such as aluminium and stainless steel. It is slower than MIG, so it is chosen for quality rather than speed.'),
        ('Oxy-fuel: a gas flame',
         'Oxy-fuel welding burns a fuel gas with pure oxygen to make a very hot flame. It is a good tool for cutting thick steel and for some repairs. It spreads more heat into the work than an arc does, so it suits jobs where that is acceptable.'),
        ('The heat-affected zone',
         'Heat from welding changes the metal beside the joint, in a band called the heat-affected zone. There the grain may grow coarse, the metal may harden or soften, and it may become more brittle. Good welders keep that band small by controlling the heat and the speed of the weld.'),
        ('Distortion and inspection',
         'Welding heats one side more than the other, so parts bend or warp as they cool. Clamps, a sensible order of welds and small tacks help hold them straight. Check every weld for cracks, porosity (gas bubbles) and undercut, a groove left along the edge, by eye, by dye penetrant or by X-ray.'),
    ],
    "test": [
        ('What does welding do to the pieces being joined?',
         [('a', 'Glues them together'), ('b', 'Cuts them apart'), ('c', 'Freezes them solid'), ('d', 'Melts their edges so they fuse into one')], 'd'),
        ('In MIG welding, what is the shielding gas for?',
         [('a', 'To cool the wire'), ('b', 'To keep air away from the molten pool'), ('c', 'To paint the joint'), ('d', 'To make the metal harder')], 'b'),
        ('Which welding process uses a tungsten electrode that does not melt?',
         [('a', 'Stick welding'), ('b', 'MIG welding'), ('c', 'TIG welding'), ('d', 'Oxy-fuel cutting')], 'c'),
        ('What is the heat-affected zone?',
         [('a', 'The band of metal beside a weld whose properties change with the heat'), ('b', 'The bright light of the arc'), ('c', 'The tank that holds the gas'), ('d', 'The tip of the electrode')], 'a'),
        ('What is porosity in a weld?',
         [('a', 'A coat of paint on the joint'), ('b', 'Gas bubbles trapped in the weld'), ('c', 'A crack wider than a hair'), ('d', 'A clamp left on by mistake')], 'b'),
    ],
}
