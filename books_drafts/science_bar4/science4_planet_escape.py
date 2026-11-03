"""Atmospheric Escape and Loss: thermal escape, Jeans escape, solar wind stripping, hydrogen loss, the Mars and Venus cases, and how escape is measured."""
CODE = "science4_planet_escape"
BOOK = {
    "title": "Atmospheric Escape and Loss",
    "subtitle": "How planetary atmospheres leak into space",
    "chapters": [
        ("What escape means", "A gas molecule escapes a planet if it moves fast enough to leave the planet's gravity behind. Light gases escape more easily than heavy ones, because the same heat gives them higher speeds."),
        ("Thermal escape", "Hot molecules in the upper atmosphere can move faster than the escape speed. This thermal escape is a slow leak, and it happens on every planet with an atmosphere."),
        ("Jeans escape", "Jeans escape describes molecules leaving from the outer edge of an atmosphere, where collisions are rare. The rate depends on the temperature there and on the mass of the molecule."),
        ("Solar wind stripping", "The solar wind is a stream of charged particles from the Sun. On planets without a strong magnetic field, it can strip gas from the top of the atmosphere."),
        ("Hydrogen loss", "Hydrogen is so light that it escapes faster than heavier gases. Over long periods, planets lose much of their original hydrogen."),
        ("Mars and Venus", "Mars has lost much of its air over time, partly through solar wind stripping. Venus keeps a dense carbon dioxide atmosphere. Spacecraft that count particles leaving the planets help scientists measure these escape rates."),
    ],
    "test": [
        ("What does a molecule need to escape a planet's gravity?",
         [("a", "Heavy weight"), ("b", "A slow speed"), ("c", "A telescope"), ("d", "Enough speed to exceed the escape speed")], "d"),
        ("Which kind of gas escapes most easily?",
         [("a", "Heavy gases such as xenon"), ("b", "Cold, heavy gases"), ("c", "Light gases such as hydrogen"), ("d", "Liquid water")], "c"),
        ("What is thermal escape?",
         [("a", "A rocket launch"), ("b", "Hot molecules moving faster than escape speed leak out of the upper atmosphere"), ("c", "A volcano eruption"), ("d", "A type of storm")], "b"),
        ("What can the solar wind do to a planet's atmosphere?",
         [("a", "Strip gas from it when there is no strong magnetic field"), ("b", "Make it colder by adding snow"), ("c", "Turn it into water"), ("d", "Build mountains")], "a"),
        ("What has happened to Mars' atmosphere?",
         [("a", "It grew thicker each year"), ("b", "It stayed the same forever"), ("c", "It lost much of its gas over time"), ("d", "It turned into rings of ice")], "c"),
    ],
}
