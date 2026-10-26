"""Lidar: Mapping with Laser Pulses. Timing light to measure the ground, even through trees."""
CODE = 'navigation3b_lidar'
BOOK = {
    "title": "Lidar: Mapping with Laser Pulses",
    "subtitle": "Timing light to measure the ground, even through trees",
    "chapters": [
        ("Timing a pulse",
         "Lidar, short for light detection and ranging, sends out thousands of laser pulses every second. It times how long each pulse takes to come back. Light travels about 300,000 km each second, and the pulse covers the distance twice, so the time gives the range once it is halved."),
        ("A simple sum",
         "If a return takes one millionth of a second, a round trip of about 300 metres has been made, so the target is about 150 metres away. Halve the travel, then multiply by the speed of light, and the distance follows."),
        ("Where the aircraft is",
         "To place each point, the system must know exactly where the aircraft is and which way the laser points. GPS gives the position, and an inertial unit gives the tilt and the turn. Together they fix each point in space."),
        ("Several returns from one pulse",
         "One pulse can hit a treetop, then a branch, then the ground. Many systems record several returns from each pulse. The last return is often from the ground, so a surveyor can see the land under a forest."),
        ("A cloud of points",
         "The result is a point cloud, millions of points each with its own position. From it, software builds a bare-earth model that removes trees and buildings, and a surface model that keeps them."),
        ("Strengths and limits",
         "Lidar works in darkness, because it makes its own light, and it measures height well. It does not record colour unless a camera is flown with it, and heavy rain or fog can weaken the returns. Choose it when height and shape matter most."),
    ],
    "test": [
        ("What does lidar measure distance with?",
         [("a", "Sound waves only"), ("b", "The weight of the aircraft"), ("c", "The colour of the ground"), ("d", "The time a laser pulse takes to return")], "d"),
        ("If a laser return takes one microsecond, about how far away is the target?",
         [("a", "About 150 metres"), ("b", "About 150 kilometres"), ("c", "About 3 metres"), ("d", "About 300,000 kilometres")], "a"),
        ("Why can lidar show the ground under a forest?",
         [("a", "It sees through solid rock"), ("b", "It only works at noon"), ("c", "It records several returns, and the last one is often from the ground"), ("d", "Trees are transparent to lasers")], "c"),
        ("What do GPS and an inertial unit provide on a lidar aircraft?",
         [("a", "The position, and the tilt and turn of the sensor"), ("b", "The weather report"), ("c", "The flight menu"), ("d", "The colour of the sky")], "a"),
        ("What is a point cloud?",
         [("a", "A cloud shaped like a point"), ("b", "A single photo"), ("c", "A rain forecast"), ("d", "A collection of millions of points, each with a position")], "d"),
    ],
}
