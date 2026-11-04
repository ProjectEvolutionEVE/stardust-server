"""Mars Surface Mineralogy from Orbit: spectral remote sensing, clays, sulphates, iron oxides, dust cover, orbiter instruments and mineral maps."""
CODE = "science4_planet_mars_minerals"
BOOK = {
    "title": "Mars Surface Mineralogy from Orbit",
    "subtitle": "Reading minerals from clays to iron oxides",
    "chapters": [
        ("Reading light from afar", "Spectrometers in orbit measure the light reflected from a planet's surface at many wavelengths. Each mineral leaves its own pattern in that reflected light, like a fingerprint."),
        ("Clays", "Clay minerals form when water reacts with rock, so finding them points to past water. Several kinds of clay have been found in the oldest terrains on Mars."),
        ("Sulphates", "Sulphate minerals form when water evaporates and leaves salts behind. Some sulphate deposits on Mars point to wetter conditions in the past."),
        ("Iron oxides", "Iron oxides, which are forms of rust, give Mars its red colour. Different kinds of iron oxide show up as different features in the reflected light."),
        ("Dust cover", "Fine dust covers much of Mars and can hide the minerals below. Scientists look where the dust is thin, or measure at many wavelengths, to see through it."),
        ("Mapping minerals", "Instruments on orbiting spacecraft map where each mineral lies across the planet. These maps help choose landing sites and show how the planet changed over time."),
    ],
    "test": [
        ("What do orbiting spectrometers measure?",
         [("a", "The temperature of the air only"), ("b", "The sound of the wind"), ("c", "Light reflected from the surface at many wavelengths"), ("d", "The weight of rocks")], "c"),
        ("What do clay minerals usually indicate?",
         [("a", "Lava flows only"), ("b", "Past reaction with water"), ("c", "Frozen oxygen"), ("d", "Solar flares")], "b"),
        ("How do sulphate minerals form?",
         [("a", "When water evaporates and leaves salts behind"), ("b", "From volcanic gases only"), ("c", "In the upper atmosphere"), ("d", "By melting ice in a fire")], "a"),
        ("What gives Mars its red colour?",
         [("a", "Red sand from space"), ("b", "Ice crystals"), ("c", "Carbon"), ("d", "Iron oxides")], "d"),
        ("Why does dust matter when mapping minerals?",
         [("a", "It makes spacecraft fly faster"), ("b", "It hides minerals below, so scientists must look where dust is thin or use many wavelengths"), ("c", "It adds gold to the surface"), ("d", "It stops all radio contact")], "b"),
    ],
}
