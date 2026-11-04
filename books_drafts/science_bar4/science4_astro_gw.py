"""Gravitational-Wave Astronomy: detectors, inspiral signals, binary black holes, neutron star mergers, noise sources and multi-messenger events."""
CODE = "science4_astro_gw"
BOOK = {
    "title": "Gravitational-Wave Astronomy",
    "subtitle": "Ripples in spacetime, detectors, mergers and noise",
    "chapters": [
        ("Ripples in spacetime", "Gravitational waves are ripples in spacetime, produced when massive objects accelerate. Einstein predicted them in his general theory of relativity."),
        ("Detectors", "LIGO uses two L-shaped detectors, with laser beams travelling along long arms. A passing wave stretches one arm and squeezes the other by tiny amounts, and the lasers measure the difference."),
        ("Inspiral signals", "Two orbiting objects slowly spiral together, losing energy as they send out gravitational waves. The signal rises in pitch and loudness until the objects merge."),
        ("Binary black holes", "The first detection, in 2015, came from two black holes merging about 1.3 billion light-years away. Many more black hole mergers have been seen since."),
        ("Neutron star mergers", "In 2017, detectors saw two neutron stars merge, and telescopes saw the event in many kinds of light. Observing one event through both gravitational waves and light is called multi-messenger astronomy."),
        ("Noise sources", "Detectors are disturbed by seismic shaking, heat and other noise. Scientists filter the data carefully to pull the faint signals out of the noise."),
    ],
    "test": [
        ("What are gravitational waves?",
         [("a", "Ripples in spacetime produced by accelerating massive objects"), ("b", "Sound waves in air"), ("c", "Light from the Sun"), ("d", "Waves in the sea")], "a"),
        ("What shape are the arms of LIGO's detectors?",
         [("a", "Circular"), ("b", "Triangular"), ("c", "L-shaped, with laser beams in long arms"), ("d", "Spiral")], "c"),
        ("What was the first detection in 2015?",
         [("a", "A neutron star merger"), ("b", "A supernova"), ("c", "A pulsar"), ("d", "Two black holes merging")], "d"),
        ("What does multi-messenger astronomy mean?",
         [("a", "Sending text messages to telescopes"), ("b", "Observing one event with gravitational waves and light together"), ("c", "Listening only to radio stations"), ("d", "Using a single mirror")], "b"),
        ("What happens to an inspiral signal as the objects get closer?",
         [("a", "It gets quieter"), ("b", "It disappears at once"), ("c", "It rises in pitch and loudness"), ("d", "It stops moving")], "c"),
    ],
}
