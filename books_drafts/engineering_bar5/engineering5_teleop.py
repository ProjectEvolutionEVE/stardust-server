"""Teleoperation Latency and Force Feedback: time delay, stability, force reflection, operator performance and bilateral control."""
CODE = "engineering5_teleop"
BOOK = {
    "title": "Teleoperation Latency and Force Feedback",
    "subtitle": "Remote control, time delay and feeling what the robot feels",
    "chapters": [
        ("Remote control",
         "Teleoperation means a person controls a robot from a distance. The operator's commands travel to the robot, and information about the scene travels back. The quality of this link decides how well the task goes."),
        ("Time delay",
         "Latency is the delay between an operator's command and the robot's response, including the trip for the data. Long delays make the operator wait and move too far. Latency can make the whole control loop feel sluggish or unsafe."),
        ("Stability",
         "Delayed feedback can make the control loop oscillate, or even go unstable. Engineers design controllers that remain stable despite the delay. Passivity-based methods are one way to keep the loop well behaved."),
        ("Force reflection",
         "Force reflection sends the contact force felt by the robot back to the operator's hand. The operator can then feel how hard the robot is pressing. This makes delicate remote work far easier."),
        ("Bilateral control",
         "Bilateral control means that motion and force pass both ways between the operator and the robot. The operator's device both commands the robot and receives its feel. This is the basis of most force-feedback teleoperation."),
        ("Operator performance",
         "Latency and poor feedback tend to slow the operator and increase errors. Designers test systems with real operators and measure completion time and mistakes. Good feedback makes the task feel natural and keeps mistakes low."),
    ],
    "test": [
        ("What is teleoperation latency?",
         [("a", "The colour of the console"), ("b", "The length of a lunch break"), ("c", "The price of cable"), ("d", "The delay between an operator's command and the robot's response")], "d"),
        ("Why can time delay cause instability?",
         [("a", "It makes the paint dry"), ("b", "Delayed feedback can make the loop oscillate or go unstable"), ("c", "It cools the motor"), ("d", "It saves power")], "b"),
        ("What is force reflection?",
         [("a", "Sending the contact force felt by the robot back to the operator's hand"), ("b", "Mirrors on the wall"), ("c", "A paint method"), ("d", "A light show")], "a"),
        ("What is bilateral control?",
         [("a", "One-way control only"), ("b", "Control with paint"), ("c", "Two-way control, where motion and force pass both ways between operator and robot"), ("d", "A timer")], "c"),
        ("How does latency usually affect operator performance?",
         [("a", "It always improves it"), ("b", "It makes the robot taller"), ("c", "It removes all errors"), ("d", "It tends to slow the operator and increase errors")], "d"),
    ],
}
