"""Camera Calibration and Lens Models: intrinsic parameters, distortion models, calibration targets, reprojection error and accuracy."""
CODE = "engineering5_camera_cal"
BOOK = {
    "title": "Camera Calibration and Lens Models",
    "subtitle": "Intrinsic parameters, distortion and how close the numbers are",
    "chapters": [
        ("Why calibrate",
         "A camera does not see the world exactly as it is. Its lens bends light a little, and its sensor has a fixed size and centre. Calibration measures these properties so that the camera's pictures can be turned into true measurements."),
        ("Intrinsic parameters",
         "The intrinsic parameters describe the camera itself. They include the focal length and the point where the optical axis meets the sensor. These numbers stay fixed for a given lens and sensor."),
        ("Distortion models",
         "Real lenses bend straight lines, so they curve near the edge of the picture. Radial distortion pushes points outward or inward from the centre. Tangential distortion comes from a lens that is not perfectly aligned with the sensor. Models describe both with a few numbers."),
        ("Calibration targets",
         "Calibration uses a target of known size, such as a printed checkerboard. The camera photographs the target from several angles. Software finds the corners and works out the camera's numbers from where they appear."),
        ("Reprojection error",
         "Reprojection error is the gap, in pixels, between where a known point should appear in the image and where it actually appears. A small error means the calibration fits well. A large error means something is wrong in the model or the data."),
        ("Accuracy in practice",
         "A calibrated camera measures only as well as its calibration allows. Engineers check the accuracy with a test object of known size. They recalibrate when a lens is changed, bumped or refocused."),
    ],
    "test": [
        ("What do intrinsic parameters describe?",
         [("a", "The price of the camera"), ("b", "The focal length and the centre point inside the camera"), ("c", "The colour of its case"), ("d", "The owner")], "b"),
        ("What is radial distortion?",
         [("a", "Spin of the sensor"), ("b", "Dust on the lens"), ("c", "Light from the sun"), ("d", "Lens bending that makes straight lines curve near the edge")], "d"),
        ("What is commonly used as a calibration target?",
         [("a", "A painted wall"), ("b", "A mirror"), ("c", "A printed pattern of known size, such as a checkerboard"), ("d", "A clock")], "c"),
        ("What is reprojection error?",
         [("a", "The gap in pixels between where a point should appear and where it does appear"), ("b", "The cost of film"), ("c", "A bug in the paint"), ("d", "The lens cap")], "a"),
        ("Why does accuracy matter in calibration?",
         [("a", "So the camera looks good"), ("b", "So measurements from images match real distances"), ("c", "So the price is fixed"), ("d", "So the case fits")], "b"),
    ],
}
