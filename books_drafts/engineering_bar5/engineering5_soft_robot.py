"""Soft Robotics and Elastomer Actuators: pneumatic actuators, material models, bending geometry, control and applications."""
CODE = "engineering5_soft_robot"
BOOK = {
    "title": "Soft Robotics and Elastomer Actuators",
    "subtitle": "Robots made of flexible material that bend and squeeze",
    "chapters": [
        ("What soft robots are",
         "Soft robots are built from flexible materials such as rubber-like elastomers, rather than rigid metal. They bend, stretch and squeeze, which lets them adapt to shapes and surfaces that rigid robots cannot handle."),
        ("Pneumatic actuators",
         "Many soft actuators are driven by pressurised air. Air is pumped into chambers inside the elastomer, and the chambers swell and move the body. Air is light and safe, which suits soft devices."),
        ("Material models",
         "Elastomers stretch a great deal and respond in a curved, nonlinear way. Engineers use special material models to predict how they will behave under load. Simple linear rules often fail for these materials."),
        ("Bending geometry",
         "A soft actuator bends because of its shape. Stiffer and softer layers, or a strain-limiting layer, make pressure curl the body in a chosen direction. Designers shape the chambers to get the motion they need."),
        ("Control",
         "Controlling a soft robot is harder than controlling a rigid one, because its shape changes in complex ways. Engineers use sensors and models to estimate its pose, and they adjust the air pressure to reach the target."),
        ("Applications",
         "Soft robots suit gentle tasks, such as handling delicate foods, fruit or medical models. They are also used in grippers and wearable devices. Their safety around people is a major reason for their use."),
    ],
    "test": [
        ("What drives many pneumatic soft actuators?",
         [("a", "Electric motors"), ("b", "Pressurised air inside chambers"), ("c", "Steam"), ("d", "Oil")], "b"),
        ("What gives a soft actuator its bending motion?",
         [("a", "Its colour"), ("b", "Its weight"), ("c", "A magnet on the tip"), ("d", "Stiffer and softer layers, or strain-limiting layers, so pressure makes it curl")], "d"),
        ("What kind of material do soft actuators often use?",
         [("a", "Cast iron"), ("b", "Glass"), ("c", "Elastomers such as silicone rubber"), ("d", "Concrete")], "c"),
        ("Why is material modelling hard for soft robots?",
         [("a", "Elastomers stretch a lot and respond in a nonlinear way"), ("b", "They are too small to measure"), ("c", "They do not move"), ("d", "They are made of wood")], "a"),
        ("What is one application of soft robotics?",
         [("a", "Building steel bridges"), ("b", "Gentle handling of delicate objects"), ("c", "Mining coal at depth"), ("d", "Printing money")], "b"),
    ],
}
