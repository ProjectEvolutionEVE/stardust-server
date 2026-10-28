"""X-Ray and Neutron Diffraction Stress Measurement: lattice spacing, the sin-squared psi method, penetration and calibration."""
CODE = "engineering5_x_ray_residual"
BOOK = {
    "title": "X-Ray and Neutron Diffraction Stress Measurement",
    "subtitle": "Reading stress from the spacing between atoms",
    "chapters": [
        ("Atoms as a ruler",
         "Metal is made of crystals, and the atoms sit in regular rows. When a part is stressed, those rows move a little closer or farther apart. Diffraction measures that spacing, and the change in spacing gives the strain, and from it the stress."),
        ("Why diffraction works",
         "A beam of X-rays or neutrons bounces off the crystal planes at a set angle. The angle at which the bounced beams add up depends on the spacing between the planes. By measuring the angle, the engineer measures the spacing."),
        ("Tilting to find the stress",
         "The sin-squared psi method tilts the sample to several angles and measures the spacing at each one. The slope of the result shows the stress in the surface. This method is the standard approach for many shop measurements."),
        ("How deep each beam reaches",
         "X-rays reach only a few micrometres into most metals, so they measure the surface. Neutrons pass through centimetres of metal and measure deep inside a part. Choosing between them is a question of where in the part the stress matters."),
        ("A reference that must be right",
         "Every measurement needs a stress-free reference spacing. Without one, the answer is only a relative value. Calibration uses a sample of the same alloy, prepared without stress, so the numbers can be trusted."),
        ("Cost and care",
         "X-ray stress measurement is quick and often done on the shop floor, but it needs care with radiation safety. Neutron measurements need a reactor or accelerator source and cost much more, so teams use them only where depth matters most."),
    ],
    "test": [
        ("What changes when a metal part is stressed, in the crystal rows?",
         [("a", "The atoms change colour"), ("b", "The spacing between the rows gets slightly larger or smaller"), ("c", "The rows vanish"), ("d", "The metal melts")], "b"),
        ("Which beam reaches deeper into a metal part?",
         [("a", "X-rays"), ("b", "Both reach the same depth"), ("c", "Neutrons"), ("d", "Neither reaches inside")], "c"),
        ("What is the sin-squared psi method?",
         [("a", "Melting the surface to test it"), ("b", "Weighing the part"), ("c", "Counting the grains by eye"), ("d", "Tilting the sample and measuring spacing at several angles")], "d"),
        ("Why does a measurement need a stress-free reference spacing?",
         [("a", "Without it the answer is only a relative value"), ("b", "It makes the X-ray tube last longer"), ("c", "It changes the colour of the beam"), ("d", "It is needed only for neutrons")], "a"),
        ("Why do teams use neutron measurements only where depth matters most?",
         [("a", "They damage the part"), ("b", "They need a large source and cost much more"), ("c", "They cannot measure stress at all"), ("d", "They work only on plastics")], "b"),
    ],
}
