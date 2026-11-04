"""Stellar Evolution from Birth to Death: the main sequence, red giants, helium burning, white dwarfs, supernovae and stellar lifetimes."""
CODE = "science4_astro_stellar_life"
BOOK = {
    "title": "Stellar Evolution from Birth to Death",
    "subtitle": "From the main sequence to white dwarfs and supernovae",
    "chapters": [
        ("Birth on the main sequence", "A star forms from a collapsing cloud of gas and dust. Once its core is hot enough to fuse hydrogen into helium, the star settles onto the main sequence. This is the long, steady middle of its life."),
        ("Burning hydrogen", "Most of a star's life is spent fusing hydrogen in its core. A more massive star burns through its fuel much faster, so it has a shorter life. A small star burns slowly and lasts far longer."),
        ("Red giants", "When core hydrogen runs out, the core contracts and heats up. The outer layers swell and cool, and the star becomes a red giant."),
        ("Helium burning", "In a more massive star, the core can become hot enough to fuse helium into carbon and oxygen. A sun-like star does not reach the temperature needed to fuse carbon, so its story ends earlier."),
        ("White dwarfs", "A sun-like star sheds its outer layers as a glowing shell of gas. The hot core that remains is a white dwarf. A white dwarf slowly cools over an extremely long time."),
        ("Supernovae and lifetimes", "A massive star ends its life in a supernova, a huge explosion. A star's lifetime depends mainly on its mass. Massive stars live only a few million years, while small red dwarfs can keep shining for trillions of years."),
    ],
    "test": [
        ("Where does a star spend most of its life?",
         [("a", "As a white dwarf"), ("b", "As a red giant"), ("c", "In a supernova"), ("d", "On the main sequence, fusing hydrogen in its core")], "d"),
        ("What happens to the core of a sun-like star when its hydrogen runs out?",
         [("a", "It becomes a black hole at once"), ("b", "It fills with water"), ("c", "It contracts and heats up while the outer layers swell"), ("d", "It stops shining and disappears")], "c"),
        ("What is a white dwarf?",
         [("a", "The hot, dense core left after a sun-like star sheds its outer layers"), ("b", "A cold planet made of ice"), ("c", "A moon of Jupiter"), ("d", "A sunspot")], "a"),
        ("Which kind of star has the shortest life?",
         [("a", "A massive star"), ("b", "A small red dwarf"), ("c", "A sun-like star"), ("d", "A brown dwarf")], "a"),
        ("Which is the best description of a red giant?",
         [("a", "A small, hot, blue star"), ("b", "A large, cool, swollen star that forms after core hydrogen runs out"), ("c", "A cloud of dust in space"), ("d", "A planet with a ring")], "b"),
    ],
}
