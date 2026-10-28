"""Limit Cycles and Nonlinear Oscillators: self-sustaining oscillations that settle to a fixed size, with the van der Pol oscillator and brake squeal as examples."""
CODE = "engineering5_limit_cycle"
BOOK = {
    "title": "Limit Cycles and Nonlinear Oscillators",
    "subtitle": "Oscillations that sustain themselves and settle to a fixed size",
    "chapters": [
        ("Self-excited oscillation", "Some systems set up their own oscillation. There is no outside rhythm pushing them. Energy comes from a steady source, and the motion settles into a repeating pattern."),
        ("Limit cycles", "A limit cycle is a closed repeating path in the state of a system. Nearby motions move toward it, or away from it. The size and shape of the cycle are set by the system itself, not by the starting motion."),
        ("The van der Pol oscillator", "The van der Pol oscillator was studied by the Dutch engineer Balthasar van der Pol in the 1920s. It has a damping term that adds energy at small swings and removes it at large swings. The result is a steady oscillation of a fixed size."),
        ("Brake squeal", "Brake squeal is a high-pitched noise from brake pads. Friction that falls as speed rises can act like negative damping. This feeds energy into a vibration of the pads and rotor, which can settle into a limit cycle."),
        ("Telling them apart", "Linear models cannot show limit cycles. A limit cycle is a nonlinear effect. Engineers look for it by testing the system at different starting sizes and watching where the motion settles."),
        ("Designing against noise", "Designers can add damping, change the friction behaviour, or shift the natural frequencies. The aim is to remove the energy source or break the cycle. Tests on the real parts confirm the cure."),
    ],
    "test": [
        ("What is a limit cycle?", [("a", "A bicycle part"), ("b", "A type of gear"), ("c", "A closed repeating path that nearby motions move toward"), ("d", "A cooling pipe")], "c"),
        ("What is self-excited oscillation?", [("a", "Oscillation sustained by a steady energy source inside the system"), ("b", "Oscillation that needs an outside rhythm to start"), ("c", "Oscillation in a vacuum only"), ("d", "Oscillation that never settles")], "a"),
        ("Which engineer studied the van der Pol oscillator in the 1920s?", [("a", "Isaac Newton"), ("b", "Johannes Kepler"), ("c", "James Watt"), ("d", "Balthasar van der Pol")], "d"),
        ("Why is brake squeal linked to limit cycles?", [("a", "Brakes never move"), ("b", "Friction that falls as speed rises can feed energy into the brake vibration"), ("c", "Brakes use no friction"), ("d", "Brake pads are made of glass")], "b"),
        ("Why can a linear model not show a limit cycle?", [("a", "Because linear models have no equations"), ("b", "Because linear models are too large"), ("c", "Because limit cycles only happen in water"), ("d", "Because limit cycles are a nonlinear effect")], "d"),
    ],
}
