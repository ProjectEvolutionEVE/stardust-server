"""Rigging and Load Paths: following the force from the hook to the load, and planning each lift."""
CODE = 'engineering4_rigging'
BOOK = {
    "title": "Rigging and Load Paths",
    "subtitle": "Following the force from the hook to the load, and planning each lift",
    "chapters": [
        ("Load path thinking",
         "Force travels from the load through the slings and hooks to the crane. Knowing that path shows where the stress goes and which parts carry the most."),
        ("Centre of gravity",
         "The centre of gravity is the point where the load's weight acts. The hook must sit above it, or the load will tilt when lifted."),
        ("Sling geometry",
         "Sling length, angle and attachment points decide how the load is held. Changing one changes the forces on every leg."),
        ("Lift plans",
         "A lift plan records the load weight, the crane, the rigging and the route. It is written before the lift and checked again on the day."),
        ("Checking every link",
         "Every shackle, hook and link is inspected before use. One weak link can cause the failure of the whole lift."),
        ("Teamwork on the lift",
         "One signaller gives the signals, and everyone keeps clear of the load. Clear communication prevents most accidents on a lift."),
    ],
    "test": [
        ("What is the centre of gravity?",
         [("a", "The middle of the shop"), ("b", "The point where a load's weight acts"), ("c", "The top of the crane"), ("d", "The place for lunch")], "b"),
        ("Why must the hook sit above the centre of gravity?",
         [("a", "To paint the load"), ("b", "To save rope"), ("c", "To make the load louder"), ("d", "So the load hangs level instead of tilting")], "d"),
        ("What does a lift plan record?",
         [("a", "The load weight, the crane, the rigging and the route"), ("b", "The menu"), ("c", "The holidays"), ("d", "The rent")], "a"),
        ("What can one weak link cause?",
         [("a", "A better lift"), ("b", "A new colour"), ("c", "The failure of the whole lift"), ("d", "Cheaper rope")], "c"),
        ("Who gives the signals in a lift?",
         [("a", "Everyone at once"), ("b", "The customer"), ("c", "The crane itself"), ("d", "One signaller")], "d"),
    ],
}
