"""Meteoroid and Debris Shielding: how a craft takes small hits from fast-moving specks."""
CODE = 'flight4_shielding'
BOOK = {
    "title": "Meteoroid and Debris Shielding",
    "subtitle": "Whipple shields, bumper layers and the windows that get hit",
    "chapters": [
        ("Space is not empty",
         "Tiny bits of rock and old metal drift through orbit. Many are left over from past launches. Even a fleck of paint can dent a window or punch through a thin wall."),
        ("Speed does the damage",
         "A small particle moving at orbital speed carries far more energy than its size suggests. That is why a craft cannot simply be made thick everywhere. The shield has to break the impact up before it reaches the important parts."),
        ("The Whipple shield",
         "In 1946 the astronomer Fred Whipple proposed a simple idea. Place a thin outer sheet a short distance in front of the main wall. When a particle hits the sheet, it breaks into a spray of smaller pieces that spread out and do less harm to the wall behind."),
        ("Bumper layers",
         "Modern craft use several layers, often with a gap or soft cloth between them. Materials such as Nextel and Kevlar catch and spread the spray. Each layer does a small part of the job, and together they protect well without a heavy solid wall."),
        ("Windows and repairs",
         "Space Shuttle windows were pitted by tiny strikes over the years, so the glass was checked and replaced when needed. Holes in the hull are patched using tools and sealing material. The crew treats each repair with care."),
        ("Shielding is about odds",
         "Designers study how often a hit of a given size is likely, and then choose how much protection to carry. Inspection after each mission and a sensible safety margin keep the risk low. The risk is never zero, so the planning never stops."),
    ],
    "test": [
        ("What did Fred Whipple propose?",
         [("a", "A thin outer sheet that breaks particles up before they reach the wall"), ("b", "A thicker solid wall with no gap"), ("c", "Windows with no glass"), ("d", "Engines that run on ice")], "a"),
        ("Why are tiny particles dangerous in orbit?",
         [("a", "They are heavy"), ("b", "They are sticky"), ("c", "They move very fast, so they carry much energy"), ("d", "They glow")], "c"),
        ("What is the job of a bumper layer?",
         [("a", "To make the craft shine"), ("b", "To break up and spread the impact"), ("c", "To store fuel"), ("d", "To cool the engines")], "b"),
        ("What can a fleck of paint do to a window?",
         [("a", "Nothing at all"), ("b", "Repair it"), ("c", "Make it colder"), ("d", "Pit it")], "d"),
        ("Why is shielding a question of odds?",
         [("a", "Designers study how likely hits of each size are"), ("b", "Hits are impossible"), ("c", "Shields never need checking"), ("d", "Windows do not matter")], "a"),
    ],
}
