"""The Hertzsprung-Russell Diagram: luminosity and temperature, spectral classes, giants and dwarfs, cluster diagrams and dating from the turnoff."""
CODE = "science4_astro_hr"
BOOK = {
    "title": "The Hertzsprung-Russell Diagram",
    "subtitle": "Reading stars by brightness and temperature, and dating clusters",
    "chapters": [
        ("A plot of stars", "The Hertzsprung-Russell diagram plots stars by their luminosity against their surface temperature. Each star is one dot on the chart. Patterns in the dots show how stars live and change."),
        ("Temperature and spectral classes", "Hotter stars look blue and cooler stars look red. Astronomers sort stars into spectral classes, O, B, A, F, G, K and M, from hottest to coolest. The Sun is a G-class star."),
        ("Giants and dwarfs", "For a given temperature, a giant star is far brighter than a dwarf, because it has a much larger surface. Most stars lie on a diagonal band called the main sequence, running from hot bright stars to cool dim ones."),
        ("Cluster diagrams", "Stars in a star cluster formed together, from the same cloud, at about the same distance. A cluster diagram therefore shows stars of different masses at one moment, all at the same stage of their own paths."),
        ("Radius and luminosity", "Luminosity depends on both temperature and size. Once you know a star's luminosity and surface temperature, you can work out its radius. This is how astronomers measure stars too far away to see as discs."),
        ("Dating a cluster from its turnoff", "The point where stars leave the main sequence in a cluster is called the turnoff. The brightness of the turnoff tells astronomers roughly how old the cluster is, because the most massive stars leave the main sequence first."),
    ],
    "test": [
        ("What two quantities does the Hertzsprung-Russell diagram compare?",
         [("a", "Luminosity and surface temperature"), ("b", "Mass and colour of planets"), ("c", "Distance and speed"), ("d", "Size and shape of galaxies")], "a"),
        ("Which spectral class is the hottest?",
         [("a", "M"), ("b", "K"), ("c", "O"), ("d", "G")], "c"),
        ("What is the main sequence?",
         [("a", "A list of star names"), ("b", "The path that comets take"), ("c", "A ring around the Sun"), ("d", "The diagonal band where most stars lie")], "d"),
        ("Why are the stars in a cluster useful for dating?",
         [("a", "They are all the same colour by chance"), ("b", "They formed together, so they share a common starting time"), ("c", "They all have exactly the same mass"), ("d", "They are all giants")], "b"),
        ("At the same temperature, which star is brighter?",
         [("a", "The giant, because it has a much larger surface"), ("b", "The dwarf, because it is closer to Earth"), ("c", "The dwarf, because it is hotter"), ("d", "Neither, since brightness depends only on colour")], "a"),
    ],
}
