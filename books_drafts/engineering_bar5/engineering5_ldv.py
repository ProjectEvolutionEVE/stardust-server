"""Laser Doppler Velocimetry: measuring the velocity at one point in a flow, including fast, swirling turbulent flow."""
CODE = "engineering5_ldv"
BOOK = {
    "title": "Laser Doppler Velocimetry",
    "subtitle": "Point measurements, Doppler shift and turbulent flow",
    "chapters": [
        ("A point measurement", "Laser Doppler Velocimetry, or LDV, measures the velocity at one small point in a flow. It gives a detailed reading over time at that point, rather than a whole map."),
        ("The Doppler shift", "Light scattered from a moving particle changes frequency slightly. This change is the Doppler shift, and it tells the speed of the particle."),
        ("Fringe patterns", "Two laser beams cross and form a pattern of bright and dark fringes. A particle crossing the fringes flashes light at a rate that gives its speed."),
        ("Seeding", "As in other flow methods, the fluid needs small particles that follow it well. Without enough particles, the measurement has gaps."),
        ("Turbulent flow", "LDV can measure fast, swirling flow at a point. This suits studies of turbulence, where the velocity changes quickly from moment to moment."),
        ("Accuracy", "The result is only as good as the particle supply through the measuring point. Too few particles can limit the accuracy, especially in slow or sparse flows."),
    ],
    "test": [
        ("What does LDV measure?", [("a", "Velocity at a single point"), ("b", "The mass of a tank"), ("c", "The colour of pipes"), ("d", "The length of cables")], "a"),
        ("What is the Doppler shift?", [("a", "A sound from a bell"), ("b", "A type of paint for pipes"), ("c", "A brand of seal"), ("d", "A change in light frequency from a moving particle")], "d"),
        ("What forms the fringe pattern?", [("a", "Two crossing laser beams"), ("b", "A mirror on a stand"), ("c", "A glass of water"), ("d", "A piece of cloth")], "a"),
        ("Where does LDV suit studies best?", [("a", "In empty space"), ("b", "On paper charts"), ("c", "In turbulent flow at a point"), ("d", "In cold storage")], "c"),
        ("What can limit LDV accuracy?", [("a", "A warm room"), ("b", "Too few particles passing through the measuring point"), ("c", "A long cable"), ("d", "Too many lights in the room")], "b"),
    ],
}
