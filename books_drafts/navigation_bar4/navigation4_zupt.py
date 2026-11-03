"""Zero-velocity updates for walkers: foot-mounted inertial sensors, the stance phase, drift between steps and rescue uses."""
CODE = "navigation4_zupt"
BOOK = {
    "title": "Zero-Velocity Updates for Walkers",
    "subtitle": "Using the moment each foot is planted",
    "chapters": [
        ("Walking with a sensor", "A walker's foot strikes the ground many times each minute. Each time the foot is planted, it is for a short moment at rest. A sensor fixed to the foot can use those moments."),
        ("The stance phase", "The stance phase is the part of the step when the foot touches the ground. During this time the foot's speed is effectively zero. A zero-velocity update uses this fact to correct the sensor."),
        ("The foot-mounted sensor", "A small inertial sensor fixed to the shoe can track a walker's steps. Each stance resets the velocity to zero. This stops the velocity error from building up as it otherwise would."),
        ("Drift between steps", "Between steps the sensor still drifts, mostly in heading and position. Errors grow more slowly than without updates, but they do not vanish. Over long distances the position still drifts."),
        ("Limits", "The method works poorly if the foot slides or if the walker does not plant the foot cleanly. Heading errors are hard to correct without outside aids. Careful sensor placement and good algorithms help."),
        ("Use in rescue", "Foot-mounted sensors are useful for rescue teams in buildings or tunnels where satellite signals do not reach. They help track responders when satellite positioning is missing. Results are best combined with other aids such as maps."),
    ],
    "test": [
        ("What is the stance phase of a step?", [("a", "The moment the foot leaves the ground"), ("b", "The time spent looking at a map"), ("c", "The part of the step when the foot is on the ground"), ("d", "The moment the foot is lifted high")], "c"),
        ("What is assumed to be zero during the stance phase?", [("a", "The velocity of the foot"), ("b", "The sound of the walker"), ("c", "The height of the walker"), ("d", "The number of steps taken")], "a"),
        ("What does a zero-velocity update do?", [("a", "It turns the sensor off until the walker stops"), ("b", "It resets the velocity error each time the foot is planted"), ("c", "It changes the colour of the shoe"), ("d", "It stops all drift in position forever")], "b"),
        ("Why does drift still build up between steps?", [("a", "The shoes are too heavy"), ("b", "The stairs are too steep"), ("c", "The satellites are too far away"), ("d", "Heading and position errors remain")], "d"),
        ("Where are foot-mounted sensors useful?", [("a", "In buildings or tunnels where satellite signals do not reach"), ("b", "On a supersonic jet"), ("c", "In a deep-space probe"), ("d", "On a racing bicycle")], "a"),
    ],
}
