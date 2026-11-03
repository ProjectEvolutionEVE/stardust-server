"""Protein Structure Determination by Cryo-EM: freezing proteins, picking their images and building three-dimensional models that are checked."""
CODE = "science5_bio_cryoem"
BOOK = {
    "title": "Protein Structure Determination by Cryo-EM",
    "subtitle": "Freezing single proteins, collecting their images and building three-dimensional models",
    "chapters": [
        ("Seeing single molecules", "Cryo-electron microscopy images proteins that are frozen in a thin layer of ice. Each image shows many copies of a protein seen from different angles, and the images are combined to build a three-dimensional structure."),
        ("Vitrification", "Vitrification means freezing a sample so fast that water turns to glass-like ice instead of forming crystals. The protein keeps its natural shape, which is the main reason cryo-EM can reveal structures."),
        ("Particle picking", "Particle picking finds the images of individual protein particles among the noise in a micrograph. Software does most of this work, but a person must check that the picks are real proteins."),
        ("Three-dimensional reconstruction", "Many two-dimensional views of the same protein are combined into a three-dimensional map. Each view adds information, so the reconstruction becomes more detailed as more particles are used."),
        ("Resolution and model building", "Resolution describes how fine a detail the map can show. Once the map is good enough, scientists build an atomic model of the protein by fitting the amino acid chains into the density."),
        ("Validation", "Validation checks that the model fits the data and is chemically sensible. A model that looks good but breaks basic chemistry rules is not trusted, however pretty it appears."),
    ],
    "test": [
        ("What is vitrification?",
         [("a", "Turning glass into sand"), ("b", "Melting a sample"), ("c", "Painting a sample"), ("d", "Freezing a sample so fast that ice forms without crystals, keeping its structure")], "d"),
        ("What is particle picking?",
         [("a", "Picking up fruit"), ("b", "Locating the images of individual protein particles in micrographs"), ("c", "Choosing a microscope colour"), ("d", "Removing dust from a computer")], "b"),
        ("What is three-dimensional reconstruction in cryo-EM?",
         [("a", "Printing a three-dimensional toy"), ("b", "Making a two-dimensional drawing"), ("c", "Combining many two-dimensional views to build a three-dimensional model of the protein"), ("d", "Measuring the mass of the microscope")], "c"),
        ("What does resolution describe?",
         [("a", "How fine a detail the map can show"), ("b", "How heavy the sample is"), ("c", "How many colours the map has"), ("d", "How long the sample takes to freeze")], "a"),
        ("Why is validation important?",
         [("a", "To prove the model is pretty"), ("b", "To make the sample bigger"), ("c", "To check that the model fits the data and is chemically sensible"), ("d", "To stop the microscope")], "c"),
    ],
}
