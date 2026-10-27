"""Digital Image Correlation Strain Mapping: mapping strain over a surface from camera images."""
CODE = "engineering5_dic"
BOOK = {
    "title": "Digital Image Correlation Strain Mapping",
    "subtitle": "Mapping strain over a surface from camera images",
    "chapters": [
        ("Watching a surface move",
         "Digital image correlation uses cameras to follow the pattern on a surface as the part is loaded. The movement of the pattern gives the displacement of the surface."),
        ("Speckle patterns",
         "A random speckle pattern is sprayed or printed on the surface, so that each small area looks unique. The software tracks those patches from one image to the next."),
        ("Camera calibration",
         "The cameras must be calibrated so that pixels can be turned into real distances. A calibration target of known size is used for this."),
        ("Displacement fields",
         "Matching the patches across images gives a displacement at many points on the surface. Taking differences between nearby points gives the strain."),
        ("Strain maps",
         "The result is a colour map of strain across the surface. It shows where strain is high, which helps find weak spots."),
        ("Validating models",
         "Comparing the measured strain map with the model's prediction checks the model. Differences point to missing physics or wrong inputs."),
    ],
    "test": [
        ("What does a speckle pattern give the surface?",
         [("a", "A paint colour"), ("b", "A price"), ("c", "Unique patches the software can track"), ("d", "A weight")], "c"),
        ("What is camera calibration for?",
         [("a", "Changing colour"), ("b", "Turning pixels into real distances"), ("c", "Counting visitors"), ("d", "Setting prices")], "b"),
        ("How is strain found from the displacements?",
         [("a", "By taking differences between nearby points"), ("b", "By guessing"), ("c", "By weighing the part"), ("d", "By the date")], "a"),
        ("What does a strain map show?",
         [("a", "The paint"), ("b", "The sales"), ("c", "The date"), ("d", "Where strain is high across the surface")], "d"),
        ("What does comparing a measured strain map with a model check?",
         [("a", "The model"), ("b", "The paint"), ("c", "The price"), ("d", "The camera brand")], "a"),
    ],
}
