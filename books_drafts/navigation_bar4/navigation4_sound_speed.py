"""Sound speed in water: temperature, salinity and pressure, speed profiles, ray bending, depth error and casts."""
CODE = "navigation4_sound_speed"
BOOK = {
    "title": "Sound Speed in Water",
    "subtitle": "How the sea changes the speed of sound",
    "chapters": [
        ("Sound in water", "Sound travels faster in water than in air. Its speed depends on temperature, salinity and pressure. These three set the sound speed profile."),
        ("Temperature, salinity and pressure", "Warmer water carries sound faster. Saltier water does too, and deeper water is under more pressure, which also speeds sound. Each factor matters in its own way."),
        ("The speed profile", "The speed profile is the sound speed at each depth. It changes as the water layers change. Surveys measure it with probes called casts."),
        ("Ray bending", "Sound rays bend toward slower water. A change of speed with depth therefore bends the path of the sound. Echo sounders must account for this bending."),
        ("Depth error", "If the speed profile is wrong, the depths computed from echo time are wrong too. A small speed error can give a large depth error in deep water. Correction is therefore essential."),
        ("Casts and correction", "A sound speed cast lowers a probe through the water and records the speed. The results are entered into the sounder's correction. Casts are repeated as the water changes."),
    ],
    "test": [
        ("What three things does sound speed in water depend on?", [("a", "Colour, taste and smell"), ("b", "Wind, waves and rain"), ("c", "Temperature, salinity and pressure"), ("d", "Boat speed, sun and moon")], "c"),
        ("Which change makes sound travel faster in water?", [("a", "Colder water"), ("b", "Less salt in the water"), ("c", "Warmer water"), ("d", "A dark sky above")], "c"),
        ("What is a speed profile?", [("a", "A list of ship speeds"), ("b", "Sound speed at each depth"), ("c", "A chart of fish sizes"), ("d", "The speed of the wind")], "b"),
        ("Which way do sound rays bend?", [("a", "Straight up at all times"), ("b", "In circles around the sounder"), ("c", "Toward faster water"), ("d", "Toward slower water")], "d"),
        ("What is a cast?", [("a", "A probe lowered through the water that records sound speed"), ("b", "A net for catching fish"), ("c", "A type of fishing rod"), ("d", "A broken chart")], "a"),
    ],
}
