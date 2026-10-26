"""Case Study: Schiaparelli on Mars, 2016. A lander that was meant to test the way down to the surface, and the sensor data that went wrong."""
CODE = "flight5_schiaparelli"
BOOK = {
    "title": "Case Study: Schiaparelli on Mars",
    "subtitle": "Entry, wrong data, an early cutoff, and a crash",
    "chapters": [
        ("A test of the way down",
         "Schiaparelli was a European lander carried to Mars in 2016. Its job was to test the way down to the surface, including the parachute, the heat shield and the braking rockets. It was a test flight for a later and larger mission."),
        ("Entry",
         "The lander entered the thin air of Mars at high speed and slowed by heat shield, parachute and then rockets. Each stage had to hand over to the next at exactly the right moment. The sequence was complex and unforgiving."),
        ("Wrong data",
         "Sensor readings made during the descent gave the lander a wrong picture of its height and motion. The data made it seem that the craft had already reached the surface. This is the kind of error that is hard to spot in the moment."),
        ("Early cutoff",
         "Believing that it had landed, the craft shut off its braking rockets early. It was still high above the ground at that point. The lander then fell the rest of the way."),
        ("Findings",
         "The inquiry looked at how the sensor data was checked and how the system responded to errors. It found that a single wrong input had too much effect on the decisions the craft took. Changes were made to how such data is tested and cross-checked."),
        ("Lessons",
         "A system that trusts its sensors too much can act on a false picture. Good design checks each reading against others and allows for a wrong one. A captain should ask how the team would know if its own instruments were wrong."),
    ],
    "test": [
        ("What was Schiaparelli sent to do?",
         [("a", "Orbit Jupiter"), ("b", "Bring samples to Earth"), ("c", "Test the way down to the surface of Mars"), ("d", "Fly past the Sun")], "c"),
        ("What did the craft's sensor data wrongly suggest?",
         [("a", "That it had already reached the surface"), ("b", "That it had reached Venus"), ("c", "That its parachute was pink"), ("d", "That the radio had broken")], "a"),
        ("What did the lander do too early?",
         [("a", "It opened the parachute"), ("b", "It shut off its braking rockets"), ("c", "It sent its photos"), ("d", "It turned on its lights")], "b"),
        ("What did the inquiry find about how errors were handled?",
         [("a", "The craft had no sensors at all"), ("b", "Errors were always ignored by design"), ("c", "The problem was caused by the weather"), ("d", "One wrong input had too much effect on the decisions")], "d"),
        ("What is a key lesson of this case?",
         [("a", "Sensors should never be used"), ("b", "Descents should always be fast"), ("c", "A system that trusts its sensors too much can act on a false picture"), ("d", "Heat shields are not needed")], "c"),
    ],
}
