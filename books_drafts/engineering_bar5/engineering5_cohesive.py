"""Cohesive Zone Models for Cracks: modelling a crack as a band where the material pulls itself apart gradually."""
CODE = "engineering5_cohesive"
BOOK = {
    "title": "Cohesive Zone Models for Cracks",
    "subtitle": "Modelling a crack as a band where the material gives way gradually",
    "chapters": [
        ("The idea",
         "A cohesive zone model treats a crack path as a thin band where forces still hold the two faces together. As the faces separate, those forces fall to zero, so the crack opens smoothly."),
        ("Traction-separation laws",
         "The relation between the pull across the faces and the amount they separate is a traction-separation law. Its shape, its peak and the area under it set the strength and the energy needed to open the crack."),
        ("Process zones",
         "The band of damaged material in front of a crack tip is called the process zone. The cohesive zone is a simple model of that region, which real materials do show."),
        ("Crack initiation in bonded joints",
         "In a glued joint, stress peaks at the edge of the bond. A cohesive model can predict when the bond starts to separate and how the damage spreads from there."),
        ("Simulating growth",
         "Cohesive elements can be placed along likely crack paths in a finite element model. As the load grows, they fail one by one, so the model shows the crack growing."),
        ("Care with the inputs",
         "The results depend on the chosen law and its parameters, so these must be matched to test data, such as a peel or fracture test. A nice picture from an unchecked law proves little."),
    ],
    "test": [
        ("What does a cohesive zone model treat a crack as?",
         [("a", "A colour"), ("b", "A bridge deck"), ("c", "A thin band where forces hold the faces together"), ("d", "A cloud")], "c"),
        ("What is a traction-separation law?",
         [("a", "A recipe"), ("b", "A relation between the pull across the faces and how far they separate"), ("c", "A tax rule"), ("d", "A sound")], "b"),
        ("Where is the process zone?",
         [("a", "Far away from the crack"), ("b", "In the band of damaged material in front of the crack tip"), ("c", "In the paint"), ("d", "Inside the bolt")], "b"),
        ("In a glued joint, where does the stress peak?",
         [("a", "On the top surface only"), ("b", "Nowhere"), ("c", "At the edge of the bond"), ("d", "In the paint")], "c"),
        ("What must the law's inputs be matched to?",
         [("a", "Test data, such as a peel or fracture test"), ("b", "The weather"), ("c", "The price of fuel"), ("d", "A poem")], "a"),
    ],
}
