"""Acoustic Emission Monitoring: listening for the small bursts of sound that cracks and deformation make in a structure under load."""
CODE = "engineering5_acoustic_em"
BOOK = {
    "title": "Acoustic Emission Monitoring",
    "subtitle": "Listening for cracks, locating sources and watching pressure vessels",
    "chapters": [
        ("Listening to cracks", "When a material cracks or deforms, it releases short bursts of elastic waves. This is acoustic emission, and sensors on the surface can pick it up."),
        ("Source location", "Sensors hear a burst at slightly different times. The small time differences between sensors let the source be located, much like finding where thunder came from."),
        ("Sensor arrays", "Several sensors spread over a vessel let engineers locate sources across the whole structure, not only near one sensor."),
        ("Signal features", "The size, shape and frequency content of a burst give clues to what caused it. Crack growth and rubbing can look different in the data."),
        ("Noise rejection", "Pumps, rain, valves and other sources make noise. The noise must be filtered out or rejected, so that the real bursts stand out."),
        ("Monitoring pressure vessels", "Watching a vessel under load can give early warning of growing cracks. This helps decide when a closer inspection is needed."),
    ],
    "test": [
        ("What is acoustic emission?", [("a", "Short bursts of elastic waves from a material under stress"), ("b", "A type of music played in plants"), ("c", "A kind of paint for vessels"), ("d", "A leak in a tap")], "a"),
        ("How is a source located?", [("a", "By guessing from the sound"), ("b", "From the small time differences between sensors"), ("c", "By weighing the vessel"), ("d", "By reading the colour of the surface")], "b"),
        ("Why use an array of sensors?", [("a", "To cover the whole structure"), ("b", "To make the sound louder"), ("c", "To make the structure colder"), ("d", "To cut the cable")], "a"),
        ("What must be done with pump and rain noise?", [("a", "It must be recorded as a crack"), ("b", "It must be painted over"), ("c", "It must be used as a power source"), ("d", "It must be filtered out so that real bursts stand out")], "d"),
        ("What can monitoring a pressure vessel give?", [("a", "Early warning of growing cracks"), ("b", "A new paint job"), ("c", "A lower price for steel"), ("d", "A longer lunch break")], "a"),
    ],
}
