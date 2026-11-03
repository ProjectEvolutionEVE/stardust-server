"""Lock-In in Ring Laser Gyros: the dead band, backscatter, dither and the bias error that lock-in causes."""
CODE = "navigation5_ring_laser_lockin"
BOOK = {
    "title": "Lock-In in Ring Laser Gyros",
    "subtitle": "When a laser gyro goes quiet at slow rotation",
    "chapters": [
        ("The ring laser gyro", "A ring laser gyroscope sends two laser beams around a closed loop, one clockwise and one anticlockwise. Rotation changes the beat frequency between the two beams."),
        ("Dead band", "At low rotation rates the two beams can lock together, and the beat frequency drops to zero. This region is called the dead band, or lock-in."),
        ("Backscatter", "Light scattered back from the mirrors can couple the two beams and cause lock-in. Careful mirror design reduces this effect."),
        ("Dither", "Dither is a small mechanical vibration that rocks the gyro back and forth quickly. It stops the beams from staying locked for long."),
        ("Bias", "Lock-in causes a bias error at low rotation rates. Dither and calibration reduce that bias."),
        ("Cost", "Dither adds cost and complexity, but it makes the gyro far more useful. Designers balance that cost against performance."),
    ],
    "test": [
        ("In which direction do the two beams in a ring laser gyro travel?",
         [("a", "In circles on paper"), ("b", "In a straight line"), ("c", "In opposite directions around a closed loop"), ("d", "Through sand")], "c"),
        ("What is the dead band?",
         [("a", "A music band"), ("b", "A low-rate region where the beams lock together"), ("c", "A belt"), ("d", "A radio")], "b"),
        ("What couples the beams and causes lock-in?",
         [("a", "Backscatter from the mirrors"), ("b", "Heat from sand"), ("c", "Noise from songs"), ("d", "Snow")], "a"),
        ("What is dither?",
         [("a", "A type of rock"), ("b", "A dance"), ("c", "A bird"), ("d", "A small vibration that rocks the gyro back and forth")], "d"),
        ("What does lock-in cause?",
         [("a", "A faster laser"), ("b", "A bias error at low rotation rates"), ("c", "A new colour"), ("d", "A bigger map")], "b"),
    ],
}
