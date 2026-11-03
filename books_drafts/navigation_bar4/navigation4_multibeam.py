"""Multibeam echo sounders: beam fans, swath coverage, footprints, motion sensors, backscatter and processing."""
CODE = "navigation4_multibeam"
BOOK = {
    "title": "Multibeam Echo Sounders",
    "subtitle": "A fan of sound beams across the seabed",
    "chapters": [
        ("A fan of beams", "A multibeam echo sounder sends out many sound beams at once, spread across a fan. Each beam measures a depth. Together they cover a wide strip of seabed in one pass."),
        ("Swath coverage", "The strip of seabed covered in one pass is called the swath. A wide swath means fewer passes. Surveys use the swath width to plan the spacing of survey lines."),
        ("Beam footprint", "Each beam hits the seabed in a small patch called the footprint. The footprint grows with depth. Deeper water gives coarser detail."),
        ("Motion sensors", "The ship rolls, pitches and heaves, so the beams point in changing directions. Motion sensors record these movements. The data are used to correct the depths."),
        ("Backscatter", "Backscatter is the sound that bounces back from the seabed. Its strength depends on the sediment and rock. It can show what kind of seabed is below."),
        ("Processing", "Raw multibeam data are processed to remove errors and combine the soundings. Sound speed and tide corrections are applied. The end product is a detailed depth map."),
    ],
    "test": [
        ("What does a multibeam echo sounder send out?", [("a", "One laser pointing straight down"), ("b", "A single radio pulse to the sky"), ("c", "Many sound beams spread across a fan"), ("d", "A cloud of bubbles")], "c"),
        ("What is a swath?", [("a", "A type of anchor"), ("b", "A bag used for sampling"), ("c", "A sound made by the hull"), ("d", "The strip of seabed covered in one pass")], "d"),
        ("What makes the footprint of a beam larger?", [("a", "Warmer water"), ("b", "Greater depth"), ("c", "A lighter ship"), ("d", "A brighter screen")], "b"),
        ("Why are motion sensors used?", [("a", "To correct depths for the ship's roll, pitch and heave"), ("b", "To keep the crew warm"), ("c", "To count the fish"), ("d", "To measure the wind speed")], "a"),
        ("What does backscatter show?", [("a", "The number of ships nearby"), ("b", "The date of the survey"), ("c", "The colour of the sky"), ("d", "What kind of seabed is below")], "d"),
    ],
}
