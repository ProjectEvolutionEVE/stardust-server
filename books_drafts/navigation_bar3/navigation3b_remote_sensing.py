"""Seeing from Orbit: Remote Sensing. Mapping the ground with a sensor that never touches it."""
CODE = 'navigation3b_remote_sensing'
BOOK = {
    "title": "Seeing from Orbit: Remote Sensing",
    "subtitle": "Mapping the ground with a sensor that never touches it",
    "chapters": [
        ("Measuring from a distance",
         "Remote sensing means measuring the ground from far away, usually from an aircraft or a satellite. The sensor never touches the land. It records light or radio waves that have come from the surface, and turns them into a picture or a set of numbers."),
        ("Passive and active",
         "A passive sensor records energy that already exists, such as sunlight reflected from the ground or heat the ground gives off. An active sensor sends out its own signal, such as radar or a laser, and listens for the echo. Active sensors can work at night and through some cloud."),
        ("Four kinds of resolution",
         "Resolution has four parts. Spatial resolution is the size of one pixel on the ground. Spectral resolution is how many bands of light the sensor records. Temporal resolution is how often it passes over the same place. Radiometric resolution is how finely it measures brightness."),
        ("The same time of day",
         "Many mapping satellites fly in orbits that pass a place at about the same local time on each visit. The sun then lights the ground from a similar angle, which makes images easy to compare from one season to the next."),
        ("Reading a scene",
         "Water absorbs most of the light that reaches it, so it looks dark. Bare soil reflects more. Healthy plants glow strongly in near-infrared light. Analysts read these patterns to tell crops, forest, water and bare ground apart."),
        ("A free view of the past",
         "Some long-running satellite programmes, such as the Landsat series, have produced free images for decades. That allows the same place to be compared across many years. Good planning starts with the data already in hand before anyone pays for a new flight."),
    ],
    "test": [
        ("What is remote sensing?",
         [("a", "Measuring the ground from a distance, without touching it"), ("b", "Sending letters by radio"), ("c", "Cooking with solar power"), ("d", "Mining by hand")], "a"),
        ("Which of these is an active sensor?",
         [("a", "A camera that records sunlight"), ("b", "A thermometer in a field"), ("c", "A telescope that only reads starlight"), ("d", "A radar that sends out its own signal and listens for the echo")], "d"),
        ("What is spatial resolution?",
         [("a", "How many colours an image has"), ("b", "How often a satellite passes overhead"), ("c", "The size of one pixel on the ground"), ("d", "The brightness of the sun")], "c"),
        ("Why do some mapping satellites pass a place at about the same local time?",
         [("a", "So they can avoid clouds"), ("b", "Because the Earth stops spinning"), ("c", "So the sun lights the ground from a similar angle, which makes images easy to compare"), ("d", "To save fuel only")], "c"),
        ("Why does healthy vegetation stand out in near-infrared images?",
         [("a", "It is the hottest thing on the ground"), ("b", "Its leaves reflect strongly in near-infrared light"), ("c", "It turns black at night"), ("d", "It is made of metal")], "b"),
    ],
}
