"""Strapdown inertial systems: body-fixed sensors, attitude updates, velocity in chosen frames and the computing load."""
CODE = "navigation4_strapdown"
BOOK = {
    "title": "Strapdown Inertial Systems",
    "subtitle": "Sensors fixed to the body, computers doing the rest",
    "chapters": [
        ("Sensors fixed to the body", "A strapdown system fixes its gyros and accelerometers rigidly to the vehicle. Unlike a gimballed platform, the sensors do not stay level by themselves. A computer does that job instead."),
        ("Attitude updates", "The computer tracks the vehicle's orientation by adding up the gyro rotation rates over time. This is the attitude update. Errors in the gyros build up here, so they need to be small."),
        ("Velocity in chosen frames", "The accelerometer readings are turned into a chosen reference frame using the attitude. Gravity is then removed and the result is summed to find velocity. A good choice of frame keeps the sums simple."),
        ("The mechanisation", "The mechanisation is the set of steps that turns sensor readings into position, velocity and attitude. It is repeated many times a second. Its correctness matters as much as the sensors do."),
        ("Advantages", "Strapdown units are smaller, lighter and cheaper than gimballed ones. They have fewer moving parts to wear out. They are used in aircraft, ships, spacecraft and cars."),
        ("The computing load", "The computer must run the mechanisation fast enough to keep up with the sensors. Modern processors make this easy, but it still needs careful design. Shortcuts that save computing can add error."),
    ],
    "test": [
        ("What distinguishes a strapdown system?", [("a", "Its sensors float in a liquid bath"), ("b", "It uses only the stars for its position"), ("c", "It needs no power at all"), ("d", "Its sensors are fixed rigidly to the vehicle")], "d"),
        ("What is an attitude update?", [("a", "Changing the colour of the display"), ("b", "Tracking the vehicle's orientation by summing gyro rotation rates"), ("c", "Sending a message to a satellite"), ("d", "Replacing a worn battery")], "b"),
        ("What is removed from accelerometer readings before summing them to get velocity?", [("a", "Air resistance only"), ("b", "The time of day"), ("c", "Gravity"), ("d", "The sensor's serial number")], "c"),
        ("What is the mechanisation?", [("a", "The set of steps that turns sensor readings into position, velocity and attitude"), ("b", "A type of gearbox in the vehicle"), ("c", "A map of the ocean floor"), ("d", "The paint used on the sensor case")], "a"),
        ("What is an advantage of strapdown units?", [("a", "They never need calibration"), ("b", "They are smaller, lighter and cheaper than gimballed ones"), ("c", "They work only underwater"), ("d", "They need no computer")], "b"),
    ],
}
