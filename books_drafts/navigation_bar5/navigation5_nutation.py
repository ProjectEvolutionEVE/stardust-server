"""Nutation of the Earth's Axis: the 18.6-year cycle, the lunar torque, the sizes of the terms, models, effects on star positions and corrections."""
CODE = "navigation5_nutation"
BOOK = {
    "title": "Nutation of the Earth's Axis",
    "subtitle": "The small wobble that moves the stars",
    "chapters": [
        ("The 18.6-year cycle",
         "Earth's axis wobbles in a small motion called nutation. The largest part repeats about every 18.6 years. The cycle comes from the slow shifting of the Moon's orbit."),
        ("Lunar torque",
         "The Moon and the Sun pull harder on the bulge at Earth's equator than on the rest of the planet. This pull is a torque that tilts the spin axis. The Moon provides most of it."),
        ("Amplitudes",
         "The size of nutation is small. The main term moves the pole about seventeen arc seconds in longitude and about nine in tilt. Smaller terms add tiny extra wobbles, and measuring them needs precise instruments."),
        ("Models",
         "Astronomers model nutation as a sum of many periodic terms. Each term has its own period and its own size. Good models predict the position of the axis very well."),
        ("Effects on star positions",
         "Because the axis moves, the apparent positions of stars shift slightly. Nutation adds a small change to the true equator and the equinox. Star catalogues must take it into account."),
        ("Corrections",
         "Navigators and astronomers correct for nutation when they convert star positions for a given day. Ignoring it causes small but real errors. Modern almanacs include the corrections."),
    ],
    "test": [
        ("About how long is the main cycle of nutation?",
         [("a", "18.6 years"), ("b", "24 hours"), ("c", "365 days"), ("d", "100 years")], "a"),
        ("What causes the lunar torque?",
         [("a", "The wind"), ("b", "The pull of the Moon and Sun on Earth's equatorial bulge"), ("c", "The tides in the sea"), ("d", "The colour of the Sun")], "b"),
        ("What is the size of the main nutation term?",
         [("a", "About 90 degrees"), ("b", "About one day"), ("c", "About 1,000 kilometres"), ("d", "About seventeen arc seconds")], "d"),
        ("How do astronomers model nutation?",
         [("a", "With one wavy line"), ("b", "By drawing pictures"), ("c", "As a sum of many periodic terms"), ("d", "By guessing")], "c"),
        ("Why must star catalogues include nutation corrections?",
         [("a", "To make the books heavier"), ("b", "So star positions are not off by a small but real error"), ("c", "Because stars move quickly"), ("d", "Because the Moon is wet")], "b"),
    ],
}
