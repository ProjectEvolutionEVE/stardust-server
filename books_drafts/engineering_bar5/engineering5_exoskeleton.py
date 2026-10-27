"""Exoskeleton Mechanics and Load Transfer: joint alignment, actuator torque, load paths, human-machine interfaces and testing to standards."""
CODE = "engineering5_exoskeleton"
BOOK = {
    "title": "Exoskeleton Mechanics and Load Transfer",
    "subtitle": "Wearable frames that share the load with the body",
    "chapters": [
        ("What an exoskeleton is",
         "An exoskeleton is a wearable frame with motors or springs that help the body move or carry a load. It fits outside the body and follows its movements. Its design must be safe and comfortable for the person wearing it."),
        ("Joint alignment",
         "The exoskeleton's joints must line up with the wearer's human joints. A poor match causes rubbing, pinching and wasted effort. Designers use adjustable parts so the device fits many body sizes."),
        ("Actuator torque",
         "The actuators provide a turning effort, called torque, at each joint. This assistive torque takes some of the load off the wearer's muscles. The amount must be set carefully, so the device helps without forcing the body."),
        ("Load paths",
         "A load path is the route that forces take through the structure, from the carried weight down to the ground or into the wearer. The frame must carry the forces along a clear route, without putting the wearer at risk."),
        ("Human-machine interface",
         "The human-machine interface is where the wearer and the device connect and communicate. It includes straps, cuffs, controls and sensors. A good interface is comfortable, clear and quick to fit."),
        ("Testing to standards",
         "Exoskeletons are tested against recognised safety standards, such as ISO 13482 for personal care robots. Tests check strength, stability, controls and the safety of the wearer. Records of the tests support the claims made for the device."),
    ],
    "test": [
        ("What must the joints of an exoskeleton line up with?",
         [("a", "The colour of the frame"), ("b", "The price"), ("c", "The human joints it sits beside"), ("d", "The room")], "c"),
        ("What does actuator torque do in an exoskeleton?",
         [("a", "Provides assistive turning effort at a joint"), ("b", "Changes the paint"), ("c", "Measures sound"), ("d", "Counts steps")], "a"),
        ("What is a load path?",
         [("a", "A walking trail"), ("b", "A road map"), ("c", "A paint line"), ("d", "The route forces take through the structure to the ground or the wearer")], "d"),
        ("Why are exoskeletons tested to standards?",
         [("a", "To make them cheaper to paint"), ("b", "To show they are safe and meet agreed requirements"), ("c", "To change their colour"), ("d", "To make them lighter")], "b"),
        ("What is a human-machine interface?",
         [("a", "A paint roller"), ("b", "A sound wave"), ("c", "The place where the wearer and the device connect and communicate"), ("d", "A bicycle")], "c"),
    ],
}
