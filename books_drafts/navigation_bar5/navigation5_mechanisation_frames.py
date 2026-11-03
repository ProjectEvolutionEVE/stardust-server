"""Mechanisation in Different Frames: Earth-fixed, local level and inertial frames, transformations and numerical care."""
CODE = "navigation5_mechanisation_frames"
BOOK = {
    "title": "Mechanisation in Different Frames",
    "subtitle": "Choosing the frame that makes the sums easiest",
    "chapters": [
        ("Choosing a frame", "Navigation equations can be written in different reference frames. The inertial, Earth-fixed and local level frames each suit different tasks."),
        ("The local level frame", "The local level frame has north, east and down axes at the vehicle's position. Velocity and attitude are easy to read in this frame."),
        ("The Earth-fixed frame", "The Earth-fixed frame turns with the Earth. Positions are simple to state here, but the frame's rotation adds extra terms to the equations."),
        ("The inertial frame", "The inertial frame does not rotate, so the sensors measure simply here. Positions must be converted to the Earth frame before they are used."),
        ("Transformations", "Converting between frames uses rotation matrices or quaternions. Each step adds a little computing and a chance of error."),
        ("Numerical issues", "Problems arise near the poles, where longitude becomes unstable, and rounding can build up over long runs. A careful choice of frame and method avoids both."),
    ],
    "test": [
        ("What do the axes of a local level frame point to?",
         [("a", "The inertial frame's stars"), ("b", "A sofa"), ("c", "North, east and down at the vehicle's position"), ("d", "A railway station")], "c"),
        ("What is true of the Earth-fixed frame?",
         [("a", "It does not rotate"), ("b", "It is a colour"), ("c", "It has no positions"), ("d", "It turns with the Earth")], "d"),
        ("What does the inertial frame do?",
         [("a", "Does not rotate"), ("b", "Rotates fast"), ("c", "Spins a plate"), ("d", "Changes colour")], "a"),
        ("What is used to convert between frames?",
         [("a", "Pencils"), ("b", "Bread"), ("c", "Rotation matrices or quaternions"), ("d", "Cars")], "c"),
        ("Where do longitude problems mainly arise?",
         [("a", "At the equator"), ("b", "Near the poles"), ("c", "In cities"), ("d", "At sea")], "b"),
    ],
}
