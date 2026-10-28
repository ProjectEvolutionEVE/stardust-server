"""Teleoperation of Underground Machines: an operator controls a machine from a safe surface station, with attention to delay, cameras, fallback and safety."""
CODE = "mining5_teleop"
BOOK = {
    "title": "Teleoperation of Underground Machines",
    "subtitle": "Latency, cameras, operator stations, fallback and the safety case",
    "chapters": [
        ("Driving from a safe place",
         "Teleoperation lets a person control a machine from a station away from the danger. Cameras and sensors give the operator a view of the work. The machine carries out the commands in the mine."),
        ("Latency",
         "Latency is the delay between a command and the machine's response. Long delays make precise control hard and can lead to overshooting. Networks must be designed to keep the delay small and steady."),
        ("Cameras",
         "Cameras must show the work clearly in dust, low light and heat. Several views help the operator judge distance and position. Lens cleaning and lighting need regular attention."),
        ("Operator stations",
         "The operator station gives the controls, screens and a comfortable seat. It should reduce fatigue and avoid confusion. Good layout makes the operator's job safer and more accurate."),
        ("Fallback",
         "If the link fails, the machine must stop safely or move to a known safe state. Fallback plans tell the operator and the crew what to do next. Testing fallbacks is as important as testing the normal run."),
        ("Training and the safety case",
         "Operators are trained on the machine, on the network and on the fallback steps. A safety case shows that the whole system, people included, keeps risk low enough. Training and the safety case are reviewed together."),
    ],
    "test": [
        ("What is teleoperation?",
         [("a", "Sending letters by post"), ("b", "Controlling a machine from a station away from the danger"), ("c", "Talking to the machine as a friend"), ("d", "Running the machine in water")], "b"),
        ("What is latency?",
         [("a", "The delay between a command and the machine's response"), ("b", "The weight of the machine"), ("c", "The colour of the cable"), ("d", "The number of cameras")], "a"),
        ("Why must cameras be cleaned and lit with care?",
         [("a", "Because dust, low light and heat can hide the work"), ("b", "Because clean cameras are heavier"), ("c", "Because lights make the rock move"), ("d", "Because cameras fly")], "a"),
        ("What should happen if the link to the machine fails?",
         [("a", "The machine keeps going at full speed"), ("b", "The operator goes to sleep"), ("c", "The machine stops safely or moves to a known safe state"), ("d", "The machine turns off the lights")], "c"),
        ("What does a safety case cover?",
         [("a", "Only the price of the cable"), ("b", "Only the colour of the cab"), ("c", "Only the weather on the surface"), ("d", "The whole system, people included, and whether risk is low enough")], "d"),
    ],
}
