"""Robotic Drilling and Bolting: machines that drill and bolt the rock while people work from a safe distance, with sensors and collision avoidance."""
CODE = "mining5_robot_drill"
BOOK = {
    "title": "Robotic Drilling and Bolting",
    "subtitle": "Sensors, positioning, collision avoidance, productivity and safety",
    "chapters": [
        ("Machines at the face",
         "Robotic drill rigs can drill holes and install rock bolts with little direct human work at the face. People stay in safer areas while the machine does the job. The rig follows a plan loaded from the mine survey."),
        ("Sensors",
         "Sensors on the rig measure the boom position, the rock contact and the drill feed. They also watch for fault conditions such as overheating. Good sensing lets the machine stop before a problem grows."),
        ("Positioning",
         "The rig knows where it is by using surveyed reference points and onboard measurement. Accurate positioning puts each hole where the plan calls for it. Small errors compound, so checks are frequent."),
        ("Collision avoidance",
         "The boom can strike the walls, roof or other machines. Collision avoidance uses zones and sensors to stop motion before contact. Operators can see the boom's path on screen before it moves."),
        ("Productivity",
         "Robots can work through shifts with fewer breaks, which raises the number of holes per shift. Productivity also depends on setup, rock conditions and maintenance. The gains are measured against the old method on the same ground."),
        ("Safety and retrofit",
         "Keeping people away from the drilling area is a major safety gain. Many existing rigs can be retrofitted with sensors and control systems, which costs less than buying new. A safety case shows that the change reduces risk."),
    ],
    "test": [
        ("What do robotic drill rigs do?",
         [("a", "Serve drinks in the canteen"), ("b", "Mine gold with bare hands"), ("c", "Sort mail"), ("d", "Drill holes and install bolts with little direct human work at the face")], "d"),
        ("What is collision avoidance for?",
         [("a", "Making the boom hit the roof on purpose"), ("b", "Stopping the boom before it strikes walls, roof or machines"), ("c", "Painting the rig"), ("d", "Measuring the rain")], "b"),
        ("Why are positioning checks frequent?",
         [("a", "Because small errors can add up across many holes"), ("b", "Because the rig forgets its name"), ("c", "Because the sun moves the rock"), ("d", "Because drills need a hug")], "a"),
        ("What does retrofitting mean for an existing rig?",
         [("a", "Adding sensors and control systems to it"), ("b", "Throwing it away"), ("c", "Painting it blue only"), ("d", "Moving it to the sea")], "a"),
        ("What does a safety case show?",
         [("a", "That the rig is the fastest in the world"), ("b", "That the miners can leave the site"), ("c", "That the change reduces risk"), ("d", "That the paint is dry")], "c"),
    ],
}
