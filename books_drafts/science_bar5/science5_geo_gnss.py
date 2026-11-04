"""GNSS Geodesy and Ground Deformation. How satellite positioning reveals the slow and sudden movement of the ground."""
CODE = "science5_geo_gnss"
BOOK = {
    "title": "GNSS Geodesy and Ground Deformation",
    "subtitle": "Measuring how the ground moves with satellite positioning",
    "chapters": [
        ("Satellites and positions",
         "Global Navigation Satellite Systems, such as GPS, let a receiver find its position using signals from orbiting satellites. For geodesy, receivers are fixed to the ground, and their positions are measured again and again over the years."),
        ("Station networks",
         "A network of continuous GNSS stations records the position of each site every day. Dense networks show how the ground moves across a whole region, not just at one spot."),
        ("Strain rates",
         "Strain rate describes how fast the ground is stretched, squeezed or sheared. By comparing the motion of nearby stations, scientists map the strain rate and find where it builds up."),
        ("Coseismic offsets",
         "When an earthquake occurs, stations on either side of a fault can jump suddenly. These coseismic offsets reveal the size and direction of the slip on the fault at depth."),
        ("Reference frames",
         "All positions must be given in a reference frame, a model of the Earth's shape and motion that defines the coordinates. Care is needed to use the same frame across all measurements, or small errors will appear as ground motion."),
        ("Detecting slow slip",
         "Some faults slip slowly over days or weeks without a large earthquake. GNSS can detect this slow slip in the steady movement of nearby stations, and so reveal a process that seismometers may miss."),
    ],
    "test": [
        ("What is GNSS used for in ground deformation studies?",
         [("a", "Measuring the taste of soil"), ("b", "Measuring the position of fixed ground stations over time"), ("c", "Counting the stars at night"), ("d", "Weighing the atmosphere")], "b"),
        ("What does strain rate describe?",
         [("a", "How fast the ground is stretched, squeezed or sheared"), ("b", "The colour of rock"), ("c", "The number of birds on a cliff"), ("d", "The temperature of ocean water")], "a"),
        ("What are coseismic offsets?",
         [("a", "Ocean waves that follow a storm"), ("b", "Layers of ash in a cave"), ("c", "Plants that grow on a slope"), ("d", "Sudden jumps of stations on either side of a fault during an earthquake")], "d"),
        ("Why must a single reference frame be used?",
         [("a", "So that all measurements share one set of coordinates and small errors are not mistaken for motion"), ("b", "So that the ground stays still"), ("c", "So that rivers flow faster"), ("d", "So that earthquakes stop")], "a"),
        ("What can GNSS detect that seismometers may miss?",
         [("a", "The taste of seawater"), ("b", "The shape of clouds"), ("c", "Slow slip on a fault over days or weeks"), ("d", "The colour of minerals")], "c"),
    ],
}
