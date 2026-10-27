"""Gyroscopic Precession and Rotor Moments: why a spinning rotor pushes sideways when it is turned, and how that load reaches the bearings of ships and aircraft."""
CODE = "engineering5_gyro_precess"
BOOK = {
    "title": "Gyroscopic Precession and Rotor Moments",
    "subtitle": "Why a spinning rotor turns sideways, and the loads it puts on its bearings",
    "chapters": [
        ("Angular momentum", "A spinning rotor has angular momentum, which is its moment of inertia times its spin rate. This momentum points along the spin axis. It keeps that direction unless a torque acts to change it."),
        ("Precession", "If you push the spinning axis sideways, the rotor does not simply tip over. It turns about a third axis at right angles to both. This slow turning is called precession."),
        ("The precession rate", "For a rotor spinning at a steady rate, the precession rate is the applied torque divided by the angular momentum. A stronger spin means a slower precession for the same torque. A bigger torque means a faster one."),
        ("Loads on bearings", "A rotor that is turned on a moving vehicle creates a gyroscopic moment. This moment pushes on the bearings and the frame. Designers must allow for it, or the bearings wear quickly or fail."),
        ("Ships and aircraft", "A ship that rolls and pitches can cause its turbines or flywheels to load their bearings in unusual ways. Aircraft engines spinning fast also add a moment when the aircraft pitches or yaws. Engineers check these loads for each design."),
        ("Designing for it", "Rotor design includes the mass, the spin rate, the mount stiffness and the expected turning rates. The aim is to keep the moments within the bearing rating. Tests on a rig confirm the design before it goes to sea or into the air."),
    ],
    "test": [
        ("What does a spinning rotor's angular momentum point along?", [("a", "Across the spin axis only"), ("b", "Along the spin axis"), ("c", "Straight down at all times"), ("d", "Nowhere")], "b"),
        ("What is precession?", [("a", "A fast spin about the same axis"), ("b", "A type of paint"), ("c", "A way to store fuel"), ("d", "Slow turning about a third axis when the spin axis is pushed")], "d"),
        ("For a steady spin, what sets the precession rate?", [("a", "The colour of the rotor"), ("b", "The temperature of the room only"), ("c", "The applied torque divided by the angular momentum"), ("d", "The length of the cable")], "c"),
        ("What loads does a turning rotor put on its bearings?", [("a", "Gyroscopic moments that push on the bearings and frame"), ("b", "None at all"), ("c", "Only electrical loads"), ("d", "Only the weight of the paint")], "a"),
        ("What does a stronger spin do for the same torque?", [("a", "Makes the precession faster"), ("b", "Has no effect at all"), ("c", "Reverses the spin direction"), ("d", "Makes the precession slower")], "d"),
    ],
}
