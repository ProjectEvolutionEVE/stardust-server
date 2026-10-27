"""Muon Tomography Through Rock: using natural cosmic particles that pass through hills and mountains to image the density inside."""
CODE = "mining5_muon"
BOOK = {
    "title": "Muon Tomography Through Rock",
    "subtitle": "Cosmic muons, density images and their limits",
    "chapters": [
        ("Particles from space",
         "Cosmic rays strike the top of the air and make showers of particles. Muons are among the particles that reach the ground in large numbers. They pass through rock that stops most other particles."),
        ("Scattering",
         "As a muon passes through rock, it is pushed slightly off its path by the nuclei it meets. Dense rock scatters muons more than light rock does. By measuring how far each muon bends, we learn something about the material it crossed."),
        ("Density images",
         "Detectors record the paths of many muons from many directions. Computers combine these paths into a picture of density inside the hill or ore body. Dense ore shows up as a bright area, and an empty void shows up as a dark one."),
        ("Sites",
         "The method has been used on volcanoes, old tunnels and ancient monuments, and it can look for dense ore bodies or hidden cavities. Each site needs its own detectors and its own planning. The rock above the target sets how deep the method can see."),
        ("Detector arrays",
         "Detectors are often placed in layers, one above the other, so the paths of each muon can be tracked. The larger and better placed the array, the more muons it can count. Cost rises as the array grows."),
        ("Limits",
         "Muon imaging needs long exposure to collect enough counts, so it is slow. Its resolution is coarse compared with a drill core. It works best as a broad first look that guides where to drill next."),
    ],
    "test": [
        ("What kind of particle is used in muon tomography?",
         [("a", "A particle made in the drill bit"), ("b", "A particle from the mine lamp"), ("c", "A particle from the radio"), ("d", "A particle that comes from space and reaches the ground")], "d"),
        ("What does a muon's scattering tell us?",
         [("a", "The name of the mine"), ("b", "Something about the density of the material it crossed"), ("c", "The price of gold"), ("d", "The age of the miner")], "b"),
        ("What shows up as a dark area in a muon density image?",
         [("a", "A void with little material"), ("b", "Dense ore"), ("c", "A steel beam"), ("d", "A road")], "a"),
        ("What is a main limit of muon imaging?",
         [("a", "It needs long exposure, so it is slow"), ("b", "It cannot detect any rock at all"), ("c", "It only works at night"), ("d", "It needs a diamond drill")], "a"),
        ("How is muon imaging best used?",
         [("a", "As a replacement for every drill hole"), ("b", "As a way to count workers"), ("c", "As a broad first look that guides where to drill"), ("d", "As a cooking method")], "c"),
    ],
}
