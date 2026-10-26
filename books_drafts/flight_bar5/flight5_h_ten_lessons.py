"""Ten Lessons of Space Flight: lessons from decades of missions, written as plain rules of good practice."""
CODE = "flight5_h_ten_lessons"
BOOK = {
    "title": "Ten Lessons of Space Flight",
    "subtitle": "Lessons from decades of missions, written as plain rules",
    "chapters": [
        ("Keep margins",
         "Leave room for error in every design. A part that is strong enough on paper may still need spare strength for surprises."),
        ("Test before you fly",
         "Test each part, then test the whole system together. A failure found on the ground is a lesson, not a loss."),
        ("Communicate clearly",
         "Say what you know, what you do not know and what worries you. A clear message can save a mission."),
        ("Be honest",
         "Report problems as they are, even when they are unwelcome. A hidden fault tends to grow."),
        ("Train for the unexpected",
         "Crews and controllers practise emergencies so they can act calmly. Practice turns panic into steps."),
        ("Stay humble",
         "Respect what you do not know, and check your own assumptions. Many of the best teams were quick to admit when they had been wrong."),
    ],
    "test": [
        ("What does 'keep margins' mean?",
         [("a", "Leave room for error"), ("b", "Make parts as thin as possible"), ("c", "Paint the edges"), ("d", "Remove all spares")], "a"),
        ("Why test the whole system together?",
         [("a", "To waste time"), ("b", "To find faults that tests of single parts can miss"), ("c", "To make the craft heavier"), ("d", "To impress visitors")], "b"),
        ("Why report problems honestly?",
         [("a", "To hide them better"), ("b", "To delay a launch"), ("c", "To please the press"), ("d", "Because hidden faults grow bigger")], "d"),
        ("Why do crews practise emergencies?",
         [("a", "For parties"), ("b", "To use up time"), ("c", "So they can act calmly when things go wrong"), ("d", "To see the Moon")], "c"),
        ("What is a failure found on the ground?",
         [("a", "A lesson, not a loss"), ("b", "A total loss"), ("c", "A reason to stop all research"), ("d", "A secret")], "a"),
    ],
}
