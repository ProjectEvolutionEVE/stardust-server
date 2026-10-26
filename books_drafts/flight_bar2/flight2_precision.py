"""Precision Manoeuvres: small, steady corrections, and why the gentlest push usually wins."""
CODE = "flight2_precision"
BOOK = {
    "title": "Precision Manoeuvres",
    "subtitle": "Small, steady corrections, and why gentle usually wins",
    "chapters": [
        ("Small is accurate",
         "A big push feels decisive, but it is the usual cause of an overshoot. If you only need to move a little, ask for a little. In the game that means one tap of the throttle, or a short touch of the stick rather than a long hold."),
        ("Why overshoots happen",
         "Space has almost no air to slow a craft down, so once you turn or speed up, the craft keeps going after you stop asking. A sharp correction carries past the target, and then you have to correct back. Plan where you will stop before you reach the target, not after you pass it."),
        ("Act, then check",
         "Make one small correction, then watch the result for a moment before you make another. Good pilots work in a steady loop of act and check. Small, steady inputs settle faster than a string of large ones."),
        ("Turn first, then go",
         "The side thrusters turn the craft where it sits, which makes them ideal for lining up on a field or the Starship before you move forward. Point the craft at its target first, then add forward speed. A craft that starts out lined up needs far less correction later."),
        ("Heading is not the same as path",
         "When the craft is not under power, it coasts along the direction it was already travelling, not the way its nose points. Under power, it flies where it points. Before you change direction, check both the nose and the path on the screen."),
        ("Practise the small moves",
         "Set the throttle low and fly a slow, straight line past a debris field. Try to keep the field centred with the smallest stick movement you can. Precision is a habit that grows slowly, one gentle input at a time."),
    ],
    "test": [
        ("Why does a sudden, large correction in space often overshoot the target?",
         [("a", "Friction from the stars slows the craft down"), ("b", "Nothing slows the craft much, so it carries past the target"), ("c", "The side thrusters always fail at high speed"), ("d", "Gravity pulls it straight back at once")], "b"),
        ("What is a sound way to make a small move?",
         [("a", "Hold the stick for as long as you can"), ("b", "Turn 90 degrees at full speed"), ("c", "Wait for the scanner to beep before you move"), ("d", "Make one small correction, then check the result")], "d"),
        ("When the craft is not under power, which way does it travel?",
         [("a", "Wherever its nose is pointing"), ("b", "Along the direction it was already travelling"), ("c", "Straight toward the Sun"), ("d", "Back toward the Starship")], "b"),
        ("What are the side thrusters best used for when you are lining up?",
         [("a", "Carrying you forward fast"), ("b", "Opening the hold"), ("c", "Turning the craft in place before you move forward"), ("d", "Measuring the distance to the Sun")], "c"),
        ("What is a good way to practise precision?",
         [("a", "Fly fast past every field you can find"), ("b", "Keep a slow, straight line and centre a field with small stick moves"), ("c", "Hold the stick down until the bars refill"), ("d", "Warp back and forth between two rings")], "b"),
    ],
}
