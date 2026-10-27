"""Calibrating Handheld Analysers: keeping handheld X-ray analysers accurate in the field, and knowing the limits of what they can detect."""
CODE = "mining5_pxrf_cal"
BOOK = {
    "title": "Calibrating Handheld Analysers",
    "subtitle": "Keeping field X-ray readings accurate",
    "chapters": [
        ("Standards", "Handheld X-ray analysers are checked against certified reference standards. A standard has a known chemistry. Reading it at the start of each shift shows whether the instrument is on track."),
        ("Matrix effects", "The surrounding material can change an X-ray reading. This is a matrix effect. Teams correct for it using standards that match the sample type."),
        ("Drift", "Instruments drift over time as parts age and conditions change. Drift can shift readings slowly and without warning. Regular checks catch it before results are affected."),
        ("Field checks", "Field checks include repeat readings and blank samples. Repeated readings show how consistent the instrument is. Blanks show whether contamination is present."),
        ("Detection limits", "Every analyser has a detection limit, below which it cannot reliably see an element. Results near the limit are uncertain. Teams report these values as less than the limit rather than as exact numbers."),
        ("Quality", "Quality control ties all these steps together. It records every standard, check and reading. Good records let anyone see how much a result can be trusted."),
    ],
    "test": [
        ("What are certified reference standards used for?",
         [("a", "Decorating the lab"), ("b", "Making tea"), ("c", "Checking that an analyser reads known chemistry correctly"), ("d", "Weighing people")], "c"),
        ("What is a matrix effect?",
         [("a", "A grid on a map"), ("b", "The surrounding material changing an X-ray reading"), ("c", "A kind of maths test"), ("d", "A bright light")], "b"),
        ("What is drift?",
         [("a", "Slow, unnoticed change in an instrument's readings over time"), ("b", "A type of boat"), ("c", "A wind on the sea"), ("d", "A kind of dance")], "a"),
        ("What is a detection limit?",
         [("a", "The top speed of a car"), ("b", "The height of a fence"), ("c", "The number of staff"), ("d", "The level below which an element cannot be reliably seen")], "d"),
        ("Why do blank samples matter in field checks?",
         [("a", "They make the sample heavier"), ("b", "They change the colour of the rock"), ("c", "They show whether contamination is present"), ("d", "They are never useful")], "c"),
    ],
}
