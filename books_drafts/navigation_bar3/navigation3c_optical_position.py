"""Finding Your Place by Looking: optical navigation, where a camera's view of a known body against the stars fixes the craft's position."""
CODE = "navigation3c_optical_position"
BOOK = {
    "title": "Finding Your Place by Looking",
    "subtitle": "Optical navigation: a camera, a known target and the stars behind it",
    "chapters": [
        ("A camera as a navigator",
         "A camera can help find a craft's position, not only its pointing. The method is to photograph a known target, such as a planet, a moon or a small body, against the background of stars. The stars form a fixed frame, and the target's place in the picture shows where the craft is relative to it."),
        ("Angles, not distances",
         "Each image gives angles, not distances. The angle between the target and the stars tells the navigator which way the target lies from the craft. Two images taken at different times, or two targets seen together, can be combined to work out where the craft must be."),
        ("Finding the centre",
         "The navigator finds a body's centre from the shape of its edge, which is called the limb. A full disc gives a clear centre. A crescent or a lumpy asteroid is harder, so the picture must be matched against a model of the body's shape."),
        ("Size and distance",
         "How much an image tells you depends on the size of the target and how far away it is. A big body that is close fills many pixels and gives a sharp fix. A small body that is far away fills only a few, and gives only a rough one."),
        ("Keeping it honest",
         "Measured angles carry error from blur, from an imperfect model of the target, and from the camera's own alignment. Navigators record the uncertainty with each fix, rather than treating one point as certain."),
        ("Flying on your own pictures",
         "Optical navigation is most useful far from Earth, where radio signals take a long time to travel. A craft that can work out its position from its own pictures can keep flying correctly even when the ground cannot help in time."),
    ],
    "test": [
        ("What does a camera mainly give a navigator in optical navigation?",
         [("a", "The craft's colour"), ("b", "Angles between a known target and the background stars"), ("c", "The weight of the cargo"), ("d", "The time of the next launch")], "b"),
        ("Why are distant stars useful in the background of an image?",
         [("a", "They give off heat that the camera can measure"), ("b", "They always move in the same direction as the craft"), ("c", "They are the same as the target"), ("d", "They are a fixed frame of reference that hardly shifts over short times")], "d"),
        ("Which kind of target gives the sharpest fix?",
         [("a", "A close, large body that fills many pixels"), ("b", "A distant small body that fills only a few pixels"), ("c", "A faint star the camera cannot see"), ("d", "Any target at all, since the result never changes")], "a"),
        ("What is the limb of a planet?",
         [("a", "Its night side"), ("b", "Its magnetic field"), ("c", "Its edge, as it appears in the picture"), ("d", "Its path round the Sun")], "c"),
        ("Why should a navigator record the uncertainty with each optical fix?",
         [("a", "Because the camera always gives a perfect answer"), ("b", "Because blur, the target's shape and the camera's alignment all add error"), ("c", "Because the stars change their names"), ("d", "Because it makes the picture look nicer")], "b"),
    ],
}
