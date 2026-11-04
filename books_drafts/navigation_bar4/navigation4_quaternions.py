"""Quaternions for attitude: four-number rotations, composition, normalisation, avoiding gimbal lock and integrating rotation rates."""
CODE = "navigation4_quaternions"
BOOK = {
    "title": "Quaternions for Attitude",
    "subtitle": "Four numbers that describe one turn",
    "chapters": [
        ("Describing a turn", "A rotation in three dimensions can be described in several ways. A quaternion uses four numbers to describe one rotation. It is compact and avoids some awkward problems."),
        ("How rotations combine", "Two rotations combined into one are multiplied as quaternions. The order matters, just as it does for real turns. Getting the order right is essential."),
        ("Keeping the length right", "A rotation quaternion must have length one. Numerical errors make it drift away from length one. Normalising it, which means rescaling it back to length one, keeps it correct."),
        ("Avoiding gimbal lock", "Some angle-based methods lose a direction at certain tilts. This is called gimbal lock. Quaternions do not suffer from it, so they are used for smooth tracking."),
        ("Integrating rotation rates", "A gyro's rotation rates can be added up as quaternion updates each second. This gives the orientation over time. It is the core of a strapdown attitude update."),
        ("Error growth", "Small errors in each update build up over time. Normalising and careful arithmetic keep them small. A navigator watches the attitude error grow and corrects it when outside aids allow."),
    ],
    "test": [
        ("How many numbers does a quaternion use to describe a rotation?", [("a", "Four"), ("b", "Two"), ("c", "Nine"), ("d", "Twelve")], "a"),
        ("What must the length of a rotation quaternion be?", [("a", "Zero"), ("b", "One"), ("c", "Ten"), ("d", "Three hundred and sixty")], "b"),
        ("What does normalising a quaternion do?", [("a", "Doubles its size each step"), ("b", "Turns it into a list of angles"), ("c", "Rescales it back to length one"), ("d", "Deletes the time stamp")], "c"),
        ("What problem do quaternions avoid?", [("a", "Slow processors"), ("b", "Running out of batteries"), ("c", "Magnetic north changing"), ("d", "Gimbal lock")], "d"),
        ("What do quaternion updates add up?", [("a", "A gyro's rotation rates over time"), ("b", "The sum of all satellite clocks"), ("c", "The number of stars seen"), ("d", "The price of the sensor")], "a"),
    ],
}
