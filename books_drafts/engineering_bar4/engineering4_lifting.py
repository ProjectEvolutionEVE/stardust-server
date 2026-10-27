"""Cranes, Hoists and Lifting Gear: safe working load, rated capacity, wire rope, sling angles and lift procedures."""
CODE = 'engineering4_lifting'
BOOK = {
    "title": "Cranes, Hoists and Lifting Gear",
    "subtitle": "Lifting heavy loads safely, within the rated capacity and the procedure",
    "chapters": [
        ("Safe working load",
         "Every crane, hoist and sling has a safe working load, the most it may lift in normal use. It must never be exceeded."),
        ("Rated capacity",
         "The rated capacity depends on the lifting setup, such as boom length and angle. A load that is safe at one reach may be unsafe at another."),
        ("Wire rope",
         "Wire rope wears from bending and rubbing. It must be checked for broken wires, kinks and corrosion before each use."),
        ("Sling angles",
         "The wider the angle between the legs of a sling, the greater the force on each leg. Keep sling angles as small as the job allows."),
        ("Inspection",
         "Lifting gear is inspected regularly, and after any unusual event, by a competent person. Damaged gear is taken out of service."),
        ("Lift procedures",
         "Plan each lift, check the load, clear the area and use a signaller. Following the set procedure prevents most lifting accidents."),
    ],
    "test": [
        ("What is the safe working load?",
         [("a", "The weight of the crane"), ("b", "The lightest weight it can lift"), ("c", "The most it may lift in normal use"), ("d", "The price of the hook")], "c"),
        ("Why is rated capacity tied to the lifting setup?",
         [("a", "Boom length and angle change how much can be lifted safely"), ("b", "Paint changes it"), ("c", "Colour matters"), ("d", "The weather decides it")], "a"),
        ("Why does a wider sling angle increase the force on each leg?",
         [("a", "The rope gets longer"), ("b", "The wire shrinks"), ("c", "The rope gets cold"), ("d", "The legs must carry more of the load as they spread apart")], "d"),
        ("What must be done with damaged lifting gear?",
         [("a", "Use it anyway"), ("b", "Remove it from service"), ("c", "Paint it"), ("d", "Hide it")], "b"),
        ("Who should inspect lifting gear?",
         [("a", "A competent person"), ("b", "Any passer-by"), ("c", "The customer"), ("d", "The wind")], "a"),
    ],
}
