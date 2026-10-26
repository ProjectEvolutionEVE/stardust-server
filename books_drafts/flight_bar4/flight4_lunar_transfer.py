"""Getting to the Moon: the trans-lunar burn, free-return paths, lunar orbit insertion and the return home."""
CODE = "flight4_lunar_transfer"
BOOK = {
    "title": "Getting to the Moon",
    "subtitle": "From Earth orbit to lunar orbit and back",
    "chapters": [
        ("The trans-lunar burn", "A craft in Earth orbit must first be pushed out toward the Moon. This burn is called trans-lunar injection. After it, the craft coasts out on a long path while the Moon's pull bends it."),
        ("Free-return paths", "A free-return path loops around the Moon and comes back to Earth without a major burn. Apollo 13 used one after its service module was damaged, so the crew could get home with the path itself as the safety net."),
        ("Lunar orbit insertion", "Near the Moon, the craft must slow down to be captured. The burn that does this is called lunar orbit insertion. Apollo missions used it to enter orbit before a landing."),
        ("Apollo's choices", "Apollo chose lunar orbit rendezvous. A lander went down to the surface while the command module stayed in orbit. This saved fuel and weight, and it made the mission possible with the rockets of the time."),
        ("Modern cheap routes", "Modern planners can use slow, low-fuel routes for some missions. These routes take longer but can carry more payload. The best choice depends on the cargo and the time the mission can spend on the way."),
        ("Return corridors", "A craft coming back from the Moon must enter Earth's air within a narrow band of angles. Too steep and it burns up; too shallow and it skips off the air. The return corridor is that safe band."),
    ],
    "test": [
        ("What is trans-lunar injection?", [("a", "A radio call"), ("b", "The burn that pushes a craft out toward the Moon"), ("c", "A type of spacesuit"), ("d", "A landing on Mars")], "b"),
        ("What is a free-return path?", [("a", "A loop around the Moon that comes back to Earth without a major burn"), ("b", "A path that never returns"), ("c", "A path inside the Moon"), ("d", "A road on the Moon")], "a"),
        ("Which mission used a free-return path after damage?", [("a", "Sputnik 1"), ("b", "Voyager 1"), ("c", "Apollo 13"), ("d", "Hubble")], "c"),
        ("What is lunar orbit insertion?", [("a", "A way to dig holes"), ("b", "A spacesuit repair"), ("c", "A colour test"), ("d", "The burn that slows a craft down so it is captured by the Moon")], "d"),
        ("Why does a return corridor matter?", [("a", "It sets the time of dinner"), ("b", "The craft must enter Earth's air at a safe angle"), ("c", "It colours the parachute"), ("d", "It moves the Moon")], "b"),
    ],
}
