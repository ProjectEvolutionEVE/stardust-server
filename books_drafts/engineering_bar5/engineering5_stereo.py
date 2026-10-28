"""Stereo Vision and Depth Estimation: epipolar geometry, disparity, baseline choice, depth error and matching algorithms."""
CODE = "engineering5_stereo"
BOOK = {
    "title": "Stereo Vision and Depth Estimation",
    "subtitle": "Two eyes, disparity and how far away things are",
    "chapters": [
        ("Two views",
         "Two cameras placed side by side see the same scene from slightly different places. Our own two eyes work the same way. Comparing the two views lets a system judge how far away each part of the scene is."),
        ("Epipolar geometry",
         "The geometry of two cameras limits where a point can appear in the second image. It must lie on a line called an epipolar line. Matching along this line, instead of across the whole image, makes the search much faster."),
        ("Disparity",
         "Disparity is the shift in position of the same point between the two images. Near objects shift more than far ones. Measuring disparity for every point gives a depth map of the scene."),
        ("Baseline choice",
         "The baseline is the distance between the two cameras. A wider baseline gives a larger disparity for the same distance, so depth is measured more precisely. But a wider baseline also makes matching harder, so designers balance the two."),
        ("Depth error",
         "The depth error grows with distance. A small error in disparity becomes a large error in depth when the object is far away. Engineers plan the baseline and the lens so that the working range keeps the error acceptable."),
        ("Matching algorithms",
         "Matching finds which point in one image corresponds to which in the other. Simple block matching is fast, while more careful methods cope better with poor lighting and plain surfaces. The choice depends on the speed and quality the task needs."),
    ],
    "test": [
        ("What is disparity?",
         [("a", "The colour of the lens"), ("b", "The battery level"), ("c", "The shift in position of the same point between the two images"), ("d", "The hard drive size")], "c"),
        ("How is depth found from a stereo pair?",
         [("a", "From disparity, focal length and baseline"), ("b", "From the price of the cameras"), ("c", "From the colour of the cameras"), ("d", "From the time on a clock")], "a"),
        ("What does a wider baseline do?",
         [("a", "Lowers the light"), ("b", "Makes the cameras cheaper"), ("c", "Adds paint"), ("d", "Improves depth precision at a given distance")], "d"),
        ("What is an epipolar line?",
         [("a", "A fishing line"), ("b", "A line along which a point in one image must appear in the other"), ("c", "A cable"), ("d", "A road marking")], "b"),
        ("What happens to depth error as objects get farther away?",
         [("a", "It falls"), ("b", "It stays at zero"), ("c", "It grows"), ("d", "It turns into colour")], "c"),
    ],
}
