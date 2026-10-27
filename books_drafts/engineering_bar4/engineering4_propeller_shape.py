"""Propeller Blade Shape and Efficiency: pitch, slip, the efficiency curve, blade choices, noise and matching to an engine."""
CODE = "engineering4_propeller_shape"
BOOK = {
    "title": "Propeller Blade Shape and Efficiency",
    "subtitle": "Pitch, slip, blade choices and matching to the engine",
    "chapters": [
        ("What a propeller does",
         "A propeller turns rotation into thrust by pushing water backward. Each blade is a twisted wing that makes lift in the water, and the lift pulls the ship forward."),
        ("Pitch and slip",
         "Pitch is the distance a blade would move forward in one turn if it moved through a solid. Slip is the gap between that distance and the real distance the ship moves, because water is not solid."),
        ("The efficiency curve",
         "A propeller's efficiency depends on its speed and load. Each design works best in a narrow band. Designers match the propeller to the speed the ship spends most of its time at."),
        ("Blade shape choices",
         "Blade outline, thickness and tip shape change efficiency, noise and cavitation. Wider blades carry more load, but they can cavitate more."),
        ("Noise",
         "Propeller noise comes from blades passing the hull, from cavitation, and from turbulence at the blade tips. Quiet designs matter for research and naval vessels."),
        ("Matching to the engine",
         "The propeller and the engine must work together. The engine should run in its best range at the chosen propeller load. A mismatch wastes fuel or stalls the engine."),
    ],
    "test": [
        ("What does a propeller produce?",
         [("a", "Heat"), ("b", "Thrust, by pushing water backward"), ("c", "Sound only"), ("d", "Electricity")], "b"),
        ("What is slip?",
         [("a", "A type of blade"), ("b", "The engine speed"), ("c", "The difference between the pitch distance and the real distance moved"), ("d", "The colour of the hull")], "c"),
        ("What does a propeller's efficiency depend on?",
         [("a", "Its colour"), ("b", "The crew size"), ("c", "The colour of the sea"), ("d", "Its speed and load")], "d"),
        ("What is a drawback of wider blades?",
         [("a", "They cannot carry load"), ("b", "They can cavitate more"), ("c", "They are always quieter"), ("d", "They stop lift")], "b"),
        ("What does a mismatch between propeller and engine cause?",
         [("a", "Wasted fuel or a stalled engine"), ("b", "Brighter paint"), ("c", "More crew"), ("d", "A shorter hull")], "a"),
    ],
}
