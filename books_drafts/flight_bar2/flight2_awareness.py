"""Situational Awareness: keeping a clear picture of where you are, what is around you and what happens next."""
CODE = "flight2_awareness"
BOOK = {
    "title": "Situational Awareness",
    "subtitle": "Knowing what is around you, what it means, and what comes next",
    "chapters": [
        ("Three levels",
         "Situational awareness is knowing what is around you, what it means, and what is likely to happen next. Researchers often describe it in three levels: noticing what is there, understanding it, and projecting what comes next. Each level builds on the one before."),
        ("A scan, not a stare",
         "Do not fix your eyes on one thing. Good pilots move their attention across the whole screen: the bars, the scanner, the approach number and the info line. A short, regular scan catches changes that one long look would miss."),
        ("Check the rim and the radar",
         "The gold rim on the stick and the radar scope show things your eyes and ears may miss. Check them now and then, even while you are busy with one target. They are cheap to glance at and easy to forget."),
        ("Ask what comes next",
         "Do not only ask what is happening now. Ask what will happen in a minute: the approach number will reach its stopping point, a field will be close, or a bar will fall below 65%. Plan for the next event as well as the current one."),
        ("Notice what has gone quiet",
         "A good pilot also notices what has changed or stopped changing. A number that is frozen when it should be moving, or a bar that is falling faster than before, can each mean something. A quiet moment is not always a calm one."),
        ("Keep the picture tidy",
         "Too much on the screen can hide what matters. Keep your attention on the few things that affect your next move, and set the rest aside for now. A clear picture is easier to act on than a full one."),
    ],
    "test": [
        ("What are the three levels of situational awareness commonly described?",
         [("a", "Speed, height and fuel"), ("b", "Sight, sound and touch"), ("c", "Start, middle and end"), ("d", "Noticing, understanding and projecting what comes next")], "d"),
        ("What is the trouble with staring at one thing for too long?",
         [("a", "It makes the scanner louder"), ("b", "It misses changes elsewhere on the screen"), ("c", "It fills the hold"), ("d", "It stops the autopilot")], "b"),
        ("Which of these is a sound thing to scan regularly?",
         [("a", "The colour of the walls"), ("b", "Only the Sun"), ("c", "The hold's lid"), ("d", "The bars, the scanner, the approach number and the info line")], "d"),
        ("What does the third level, projecting, mean?",
         [("a", "Fixing what is broken"), ("b", "Painting the radar scope"), ("c", "Working out what is likely to happen next"), ("d", "Counting the pieces in a field")], "c"),
        ("Which situation most deserves a closer look?",
         [("a", "A reading that stops changing when you expect it to"), ("b", "A status line that reads DOCKED"), ("c", "A full bar after a good rest"), ("d", "An empty hold before you start collecting")], "a"),
    ],
}
