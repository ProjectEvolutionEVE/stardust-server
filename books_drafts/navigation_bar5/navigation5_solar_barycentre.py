"""The Solar System Barycentre: the Sun's wobble, the centre of mass, timing, the coordinate system, the pulsar link and its uses."""
CODE = "navigation5_solar_barycentre"
BOOK = {
    "title": "The Solar System Barycentre",
    "subtitle": "The balance point of the planets and the Sun",
    "chapters": [
        ("The Sun's wobble",
         "The Sun moves a little around the centre of mass of the solar system. The planets, especially Jupiter, pull on it in turn. The wobble is small compared with the size of the Sun."),
        ("The centre of mass",
         "The barycentre is the point where the total mass of the solar system balances. It is usually near the Sun, but it can lie outside the Sun's surface. It is a balance point, not a solid object."),
        ("Timing",
         "Signals from distant objects reach Earth at slightly different times, depending on where Earth is in its orbit. Astronomers correct arrival times to the barycentre so that the timing is consistent. This correction is part of precise timing work."),
        ("The coordinate system",
         "A barycentric coordinate system places its origin at the centre of mass of the solar system. It gives a fixed frame for measuring the positions of stars and objects. Using it removes much of the effect of Earth's own motion."),
        ("The pulsar link",
         "Pulsars are rapidly spinning neutron stars that send out regular pulses. Their timing is very precise, so astronomers correct the arrival times of the pulses to the barycentre. This is how the pulsar link works."),
        ("Uses",
         "Barycentric timing helps test gravity, search for planets and keep precise time references. The method connects the motion of the planets with the very precise timing of distant stars. It is a practical tool as well as a fine idea."),
    ],
    "test": [
        ("What causes the Sun's wobble?",
         [("a", "The Moon alone"), ("b", "The Sun's own spin"), ("c", "The wind on Earth"), ("d", "The pull of the planets, mostly Jupiter")], "d"),
        ("Where is the barycentre usually?",
         [("a", "On Earth"), ("b", "On the Moon"), ("c", "Near the Sun"), ("d", "At the edge of the galaxy")], "c"),
        ("Why do astronomers correct signal arrival times?",
         [("a", "To make signals louder"), ("b", "So that timing matches the barycentre"), ("c", "To hide the pulsar"), ("d", "To slow down light")], "b"),
        ("What is a pulsar?",
         [("a", "A spinning neutron star that sends out regular pulses"), ("b", "A planet with rings"), ("c", "A comet"), ("d", "A cloud of gas")], "a"),
        ("What is at the origin of a barycentric coordinate system?",
         [("a", "The Moon"), ("b", "The Earth's pole"), ("c", "The surface of the Sun"), ("d", "The centre of mass of the solar system")], "d"),
    ],
}
