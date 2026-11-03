"""Realising the Terrestrial Reference Frame: how a frame becomes a set of stations and versions."""
CODE = "navigation4_itrf"
BOOK = {
    "title": "Realising the Terrestrial Reference Frame",
    "subtitle": "How a frame becomes a set of stations",
    "chapters": [
        ("What a reference frame is", "A reference frame is a system for giving positions on the Earth. It has an origin, axes and a scale. Everyone who uses positions needs to share one."),
        ("A frame as a set of stations", "The frame is made real by a set of stations with known coordinates. Each station is a fixed point, often a marked pillar. The stations define the frame in practice."),
        ("Realisations", "A realisation is one version of the frame, based on a set of measurements. Over time, better measurements produce new realisations. Each one has a date and a version."),
        ("The origin and scale", "The origin of the frame is meant to be the centre of mass of the Earth. The scale is set by very precise length measurements. Both are central to the frame."),
        ("Connection to satellites", "Satellites orbit around the Earth's centre of mass. Their orbits help define the origin and keep the frame tied to the planet. Satellite laser ranging is one way this is done."),
        ("The user's choice of realisation", "Users must choose which realisation to use. Using the wrong one can shift a position by an amount that matters. Always state the realisation and epoch you use."),
    ],
    "test": [
        ("What is a reference frame?",
         [("a", "A system for giving positions on the Earth"), ("b", "A paint for maps"), ("c", "A type of camera"), ("d", "A kind of rock")], "a"),
        ("How is the frame made real in practice?",
         [("a", "By one painted line"), ("b", "By the weather"), ("c", "By a set of stations with known coordinates"), ("d", "By the ocean tides")], "c"),
        ("What is a realisation?",
         [("a", "A paper map"), ("b", "One version of the frame, based on measurements"), ("c", "A satellite's name"), ("d", "A kind of sextant")], "b"),
        ("What should a user always state?",
         [("a", "The name of the surveyor"), ("b", "The realisation and epoch used"), ("c", "The weather at the time"), ("d", "The price of the equipment")], "b"),
        ("What helps tie the frame to the planet?",
         [("a", "Wind speed"), ("b", "Sea colour"), ("c", "Sunspots"), ("d", "Satellite orbits around the Earth's centre of mass")], "d"),
    ],
}
