"""Machine Vision for Mapping Outcrops: building 3D models and rock maps from overlapping photos, checked by geologists on the ground."""
CODE = "mining5_ml_outcrop"
BOOK = {
    "title": "Machine Vision for Mapping Outcrops",
    "subtitle": "Photogrammetry, labelled images, classification and drone maps",
    "chapters": [
        ("Photos that become models",
         "Photogrammetry builds a three-dimensional model from many overlapping photographs. The same point seen in several photos is located in space. The result is a textured model of a rock face."),
        ("Image labels",
         "A computer learns to recognise rock types from images that people have labelled. A geologist marks which pixels show granite, which show shale and so on. The quality of the labels sets the quality of the learning."),
        ("Classification",
         "Once trained, the program sorts new images into rock classes. It can cover an outcrop far faster than a person walking it. Its answers are a first draft that a geologist must still check."),
        ("Structure from images",
         "Layers, joints and folds can be measured on the three-dimensional model. Each plane is given a direction and a dip. This turns a picture into structural data that can be used in design."),
        ("Drone maps",
         "Drones fly the overlapping photos over areas that are hard to reach on foot. Flight lines and camera settings are planned in advance. Good flights give sharp images with enough overlap."),
        ("Validation",
         "Every map must be validated against field checks. A geologist visits chosen points and compares what is seen with what the model says. The model is trusted only where the checks agree."),
    ],
    "test": [
        ("What does photogrammetry build from photographs?",
         [("a", "A three-dimensional model of the surface"), ("b", "A sound recording"), ("c", "A new kind of paint"), ("d", "A train timetable")], "a"),
        ("Why are image labels important?",
         [("a", "They set the quality of what the computer learns"), ("b", "They make the photos heavier"), ("c", "They replace the camera"), ("d", "They are only for decoration")], "a"),
        ("What do drone flights need for good results?",
         [("a", "Flights at midnight only"), ("b", "No planning at all"), ("c", "Sharp images with enough overlap between photos"), ("d", "Cameras without lenses")], "c"),
        ("What can be measured on the three-dimensional model?",
         [("a", "The taste of the rock"), ("b", "The price of the drone"), ("c", "The name of the pilot"), ("d", "Layers, joints and folds, with their direction and dip")], "d"),
        ("How is a machine map trusted?",
         [("a", "Because the computer says so"), ("b", "Only where field checks by a geologist agree with it"), ("c", "Because it is printed in colour"), ("d", "Because it is larger than other maps")], "b"),
    ],
}
