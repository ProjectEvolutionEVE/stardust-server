"""Torsion and Shaft Design: twist, torque, shear stress in shafts, hollow shafts, angle-of-twist limits and shaft diameter from power."""
CODE = "engineering4_torsion"
BOOK = {
    "title": "Torsion and Shaft Design",
    "subtitle": "Twist, torque, shear stress and shaft diameter",
    "chapters": [
        ("What torsion is",
         "Torsion is twisting. A shaft that drives a load carries torque, and it twists slightly along its length."),
        ("Torque and power",
         "Power equals torque times angular speed. A shaft that carries more power at the same speed must carry more torque."),
        ("Shear stress in shafts",
         "Torsion produces shear stress that is largest at the outer surface of a solid shaft. The stress falls toward the centre."),
        ("Angle of twist",
         "The angle of twist grows with length and torque, and falls with stiffness. Designers set a limit on twist so that gears and bearings stay in line."),
        ("Hollow shafts",
         "A hollow shaft carries most of its strength in its outer wall. It saves weight for the same torque, because the stress near the centre is low anyway."),
        ("Shaft diameter from power",
         "Designers find the shaft diameter from the power, the speed and an allowed stress. They then check the twist and the fatigue life."),
    ],
    "test": [
        ("What is torsion?",
         [("a", "Twisting"), ("b", "Sound"), ("c", "Heat"), ("d", "Colour")], "a"),
        ("How is power related to torque?",
         [("a", "Power equals torque divided by colour"), ("b", "Power equals zero"), ("c", "Power equals sound"), ("d", "Power equals torque times angular speed")], "d"),
        ("Where is shear stress largest in a solid shaft?",
         [("a", "At the centre"), ("b", "At the outer surface"), ("c", "At the ends only"), ("d", "Nowhere")], "b"),
        ("Why set a limit on the angle of twist?",
         [("a", "To make the shaft heavier"), ("b", "So the shaft turns colour"), ("c", "For sound"), ("d", "So gears and bearings stay in line")], "d"),
        ("Why is a hollow shaft efficient?",
         [("a", "It saves weight for the same torque"), ("b", "It is heavier"), ("c", "It cannot twist"), ("d", "It uses no steel")], "a"),
    ],
}
