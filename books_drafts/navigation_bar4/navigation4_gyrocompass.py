"""The Gyrocompass: a fast-spinning wheel that settles toward true north."""
CODE = "navigation4_gyrocompass"
BOOK = {
    "title": "The Gyrocompass",
    "subtitle": "A spinning wheel that finds true north",
    "chapters": [
        ("The spinning wheel", "A gyrocompass uses a wheel spinning very fast on an axis. A spinning wheel resists being turned and keeps its axis pointing in a fixed direction. This property is the heart of the instrument."),
        ("Earth's rotation", "The Earth turns, and a gyrocompass is set up so that Earth's rotation makes it settle with its axis pointing toward true north. It finds north by working with the planet's spin. It does not need a magnet."),
        ("Damping", "Without damping, the wheel would swing back and forth about north. Damping devices remove that swinging and let the compass settle. Good damping keeps the reading steady."),
        ("Speed and latitude error", "A ship that is moving changes the way the gyro settles. This causes a speed and latitude error, and its size depends on the ship's speed and latitude. Navigators allow for it in their corrections."),
        ("Errors at sea", "Rolling, pitching and changes of course can also disturb the gyro for a while. These errors fade as the compass settles again. A careful sailor knows when to trust it."),
        ("Checking against the sky", "A gyrocompass can be checked against celestial sights or a known bearing. Regular checks show whether the compass is holding true. A gyrocompass is a fine servant, but it is still checked."),
    ],
    "test": [
        ("What keeps a gyrocompass wheel pointing in one direction?",
         [("a", "A magnet"), ("b", "Its fast spin"), ("c", "Water pressure"), ("d", "The Moon")], "b"),
        ("What makes a gyrocompass settle toward north?",
         [("a", "The ship's paint"), ("b", "Wind"), ("c", "The Sun's heat"), ("d", "Earth's rotation")], "d"),
        ("What is damping for?",
         [("a", "To make the wheel spin faster"), ("b", "To make the compass louder"), ("c", "To stop the compass swinging back and forth"), ("d", "To heat the compass")], "c"),
        ("What causes the speed and latitude error?",
         [("a", "The ship's speed and latitude"), ("b", "The colour of the hull"), ("c", "The number of sailors"), ("d", "The phase of the Moon")], "a"),
        ("How should a navigator check a gyrocompass?",
         [("a", "Ignore it in fog"), ("b", "Compare it with celestial sights or a known bearing"), ("c", "Turn it off for good"), ("d", "Replace it every hour")], "b"),
    ],
}
