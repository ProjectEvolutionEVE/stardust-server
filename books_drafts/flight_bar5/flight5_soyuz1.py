"""Case Study: Soyuz 1, 1967. A rushed flight, a string of faults, and the lessons the Soviet programme took from them."""
CODE = "flight5_soyuz1"
BOOK = {
    "title": "Case Study: Soyuz 1, 1967",
    "subtitle": "A rushed flight, a string of faults, and what changed afterwards",
    "chapters": [
        ("A rushed flight",
         "Soyuz 1 was launched in April 1967 under heavy schedule pressure, with one cosmonaut, Vladimir Komarov, aboard. The new spacecraft was still being tested when the date was set. Many people knew it was not ready, and the launch went ahead."),
        ("A string of faults",
         "In orbit, one of the solar panels did not open fully, so the craft had less power than planned. The attitude control system also gave trouble, and Komarov had to fly the craft by hand with limited means. The mission was cut short and a return was ordered for the next day."),
        ("The return",
         "On the way down, the main parachute did not open as it should. The backup system also failed to work properly, and the capsule hit the ground at a speed far too high for survival. Komarov died in the landing."),
        ("What the crash showed",
         "The accident showed that a schedule cannot replace testing. Every fault had a known risk, and the risks had been stacked on top of each other. A complex craft needs each system checked before anyone is asked to fly it."),
        ("Changes afterwards",
         "The Soviet programme slowed its pace and tightened its test rules. Parachute and landing systems were reviewed closely, and the lessons were applied to later Soyuz flights. The name of Soyuz continued, but the flights that followed were far more carefully prepared."),
        ("A lesson for any captain",
         "A captain who is pushed to act before the ship is ready carries that risk for the whole crew. The right answer is to say clearly what is not yet tested, and to hold the date until it is. Honest reporting of doubts is part of the job, not a sign of weakness."),
    ],
    "test": [
        ("In what year did the Soyuz 1 flight take place?",
         [("a", "1957"), ("b", "1977"), ("c", "1967"), ("d", "1987")], "c"),
        ("What was one of the faults the crew of Soyuz 1 faced in orbit?",
         [("a", "A solar panel did not fully open"), ("b", "The hatch was painted the wrong colour"), ("c", "The radio played music"), ("d", "The food ran out on the first day")], "a"),
        ("What went wrong on the way down?",
         [("a", "The engines started too early"), ("b", "The main parachute did not open as it should"), ("c", "The craft landed in the sea"), ("d", "The heat shield was never fitted")], "b"),
        ("What main lesson does the case draw about schedules?",
         [("a", "A fixed date is always the safest plan"), ("b", "Testing can be shortened when there is pressure"), ("c", "Only the first flight of a new design needs testing"), ("d", "A schedule cannot replace proper testing of every system")], "d"),
        ("What did the programme do afterwards?",
         [("a", "It closed the Soyuz name for good"), ("b", "It ended all crewed flights"), ("c", "It tightened test rules and reviewed the landing systems"), ("d", "It moved all launches to the night")], "c"),
    ],
}
