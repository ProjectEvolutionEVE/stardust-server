"""Lithography and Patterning at Small Scales: how the tiny patterns on computer chips are made, and what limits them."""
CODE = "science5_mat_lithography"
BOOK = {
    "title": "Lithography and Patterning at Small Scales",
    "subtitle": "How the patterns on a computer chip are printed, and why they are so hard to shrink",
    "chapters": [
        ("Patterning", "Lithography transfers a pattern onto a surface. It is the basis of making computer chips. Many patterning steps are stacked to build a working circuit."),
        ("Photoresists", "A photoresist is a coating that changes when light falls on it. Where it is exposed, its chemistry changes. The pattern in the resist then guides the next step."),
        ("Resolution limits", "The smallest feature that can be printed depends on the wavelength of light, the optics and the chemistry. Shorter wavelengths allow finer detail. Physics sets a hard floor on how small features can be."),
        ("Etching", "Etching removes material that is not protected by the resist. The pattern is transferred into the layer below. Etching can be wet, using liquids, or dry, using plasma."),
        ("Mask design", "A mask holds the pattern to be copied. Designers draw the mask carefully, because every feature must print correctly. Errors in the mask show up on every chip."),
        ("Process control", "Small changes in dose, temperature or timing can change the final pattern. Good process control keeps those changes within tight limits. Consistency is as important as precision."),
    ],
    "test": [
        ("What is lithography in chip making?",
         [("a", "A method to transfer a pattern onto a surface"), ("b", "A way to bake bread"), ("c", "A type of paint"), ("d", "A kind of cloud")], "a"),
        ("What is a photoresist?",
         [("a", "A battery"), ("b", "A glass lens"), ("c", "A light-sensitive coating that changes where it is exposed"), ("d", "A metal wire")], "c"),
        ("What sets the limit on how small a printed feature can be?",
         [("a", "The number of colours used"), ("b", "Wavelength, optics and chemistry"), ("c", "The size of the room"), ("d", "The price of the chip")], "b"),
        ("What does etching do?",
         [("a", "Adds sound"), ("b", "Heats the sample"), ("c", "Paints the sample"), ("d", "Removes material not protected by the resist")], "d"),
        ("Why does process control matter?",
         [("a", "Small changes never matter"), ("b", "It makes patterns random"), ("c", "Small changes in dose, temperature or timing can change the result"), ("d", "It only matters for paper")], "c"),
    ],
}
