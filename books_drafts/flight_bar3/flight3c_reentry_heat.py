"""Re-entry Heat and Heat Shields: why coming back through a planet's air makes a shield glow, and how shields are built."""
CODE = "flight3c_reentry_heat"
BOOK = {
    "title": "Re-entry Heat and Heat Shields",
    "subtitle": "Why coming back through a planet's air makes a shield glow, and how shields are built",
    "chapters": [
        ("Air as a wall",
         "A craft coming back from space meets the air at very high speed. The air in front of it is squeezed so hard that it becomes extremely hot and glows. Much of that heat goes into the air, but the craft's outer surface still gets very hot."),
        ("Heat shields",
         "A heat shield is the part that takes the worst of the heat. Early capsules used ablative shields, which slowly char and burn away and carry heat off with them. The Space Shuttle protected its underside with tiles of heat-resistant material."),
        ("The angle matters",
         "Coming in too steeply brings a sharp rise in heat and force. Coming in too shallow risks skipping back out into space. A craft must enter within a narrow band of angles, so engineers design for the whole band, not only the ideal path."),
        ("Speed and energy",
         "The faster a craft comes in, the more energy its shield must handle. A craft returning from far away carries much more energy than one coming back from low orbit. The shield is sized to match the trip it is meant to make."),
        ("Weight and cost",
         "A thicker shield keeps the crew safer, but it adds weight. Every kilogram of shield is a kilogram that cannot be cargo or fuel. Designers balance safety against the cost of carrying the shield, and a bad balance costs money one way or the other."),
        ("A pilot's view",
         "In the game, the Starship never flies inside an atmosphere, so you will not feel this heat on its hull. The lesson still holds for any craft: a shield is always a trade of weight against safety, and the design sets the limits of the flight."),
    ],
    "test": [
        ("What makes the glowing gas around a re-entering craft?",
         [("a", "Sunlight on the hull"), ("b", "Plasma from the crew"), ("c", "Air squeezed very hot by the craft's speed"), ("d", "Ice melting on the hull")], "c"),
        ("What does an ablative heat shield do?",
         [("a", "Reflects all light away"), ("b", "Slowly chars and burns away, carrying heat with it"), ("c", "Turns into a radiator"), ("d", "Floats the craft")], "b"),
        ("Why must a re-entry angle stay within a narrow band?",
         [("a", "Too steep burns the shield too hard, and too shallow may skip back out"), ("b", "Too steep makes the craft float"), ("c", "Too shallow freezes the fuel"), ("d", "The angle is only for show")], "a"),
        ("Why does a craft returning from far away need a stronger shield?",
         [("a", "It is older"), ("b", "It has more paint"), ("c", "Gravity is stronger there"), ("d", "It carries more energy into the air")], "d"),
        ("What is the main cost of a thicker heat shield?",
         [("a", "Better radio"), ("b", "Extra weight, which cannot be used as cargo or fuel"), ("c", "Lower speed only"), ("d", "Nothing at all")], "b"),
    ],
}
