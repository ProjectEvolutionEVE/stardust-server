"""Wheel odometry: encoder counts, wheel radius, slip, scale error, heading sources and combining with other sensors."""
CODE = "navigation4_wheel_odometry"
BOOK = {
    "title": "Wheel Odometry",
    "subtitle": "Counting turns, and what can go wrong",
    "chapters": [
        ("Counting wheel turns", "Wheel odometry measures distance by counting how far the wheels turn. An encoder on each wheel gives counts, and these are turned into distance. The method is simple and cheap."),
        ("The wheel radius", "The distance for each turn depends on the wheel's radius. If the radius is wrong, every distance is wrong by the same fraction. Measuring the wheel carefully is a basic step."),
        ("Slip", "A wheel can spin without the vehicle moving forward as expected, for example on ice or loose sand. This is called slip. Slip makes wheel counts overstate the distance travelled."),
        ("Scale error", "Scale error comes from the radius, the counts and the slip. It adds up over time, much as a bias does. A long trip can show a large distance error."),
        ("Heading", "Wheel encoders do not show heading directly. Heading can come from a gyro or a compass, or from the difference between the two wheels. Each choice has its own error."),
        ("Combining sensors", "Wheel odometry is often combined with gyros, satellite positioning or maps. Each sensor fills gaps left by the others. The combined result is more reliable than any one of them alone."),
    ],
    "test": [
        ("What does a wheel encoder count?", [("a", "The number of passengers"), ("b", "Litres of fuel used"), ("c", "Hours since sunrise"), ("d", "Turns of the wheel")], "d"),
        ("What happens to every distance if the wheel radius is wrong?", [("a", "Distances are always exactly right"), ("b", "Only the first metre is wrong"), ("c", "Each distance is wrong by the same fraction"), ("d", "The error disappears after one turn")], "c"),
        ("What is slip?", [("a", "A wheel that falls off the axle"), ("b", "A wheel turning without the vehicle moving forward as expected"), ("c", "A small bolt used in the wheel"), ("d", "The sound made by a moving tyre")], "b"),
        ("Why does scale error get worse on long trips?", [("a", "It builds up over time, much as a bias does"), ("b", "It shrinks as the trip goes on"), ("c", "It only happens when the vehicle stops"), ("d", "It is fixed by a longer wheelbase")], "a"),
        ("Where can heading come from besides the wheels?", [("a", "The colour of the road"), ("b", "A gyro or a compass"), ("c", "The number of trees nearby"), ("d", "The weight of the cargo")], "b"),
    ],
}
