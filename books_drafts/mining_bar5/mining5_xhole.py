"""Cross-Hole Electromagnetic Imaging: sending electric signals from one drill hole to another to image the rock between them."""
CODE = "mining5_xhole"
BOOK = {
    "title": "Cross-Hole Electromagnetic Imaging",
    "subtitle": "Transmitters, receivers and mapping conductive bodies between holes",
    "chapters": [
        ("Two holes, one picture",
         "In cross-hole imaging, a transmitter sits in one drill hole and a receiver sits in another. The signal travels through the rock between them. What arrives tells us about what the signal passed through."),
        ("Transmitter and receiver",
         "The transmitter sends an electromagnetic pulse, and the receiver measures its strength and timing. Many transmitter and receiver positions are used, so the rock is covered from many directions."),
        ("Tomography",
         "The readings are combined by a computer, which works like a medical scanner. It builds a picture of the electrical properties across the plane between the holes. Places that conduct more well show up clearly."),
        ("Conductive bodies",
         "Sulphide minerals, graphite and wet clay conduct electricity well. A conductive body between holes can be a mineral deposit or a fault zone. The image shows where it is, though not always what it is."),
        ("Field layouts",
         "Holes are placed in lines or fans, and the spacing decides what can be seen. Deeper and wider layouts need stronger transmitters. Good planning saves time and avoids gaps in the image."),
        ("Resolution and modelling",
         "Resolution is best near the holes and gets coarser with distance. Modelling tests what the data would look like for a given shape, and the model is adjusted until it fits the measurements. The final image is only as good as the model behind it."),
    ],
    "test": [
        ("Where is the transmitter placed in cross-hole imaging?",
         [("a", "In a drill hole"), ("b", "On a satellite"), ("c", "In the mine office"), ("d", "Under the sea")], "a"),
        ("What does the receiver measure?",
         [("a", "The strength and timing of the pulse"), ("b", "The taste of the mud"), ("c", "The number of trucks"), ("d", "The price of the hole")], "a"),
        ("What do conductive bodies include?",
         [("a", "Dry sand only"), ("b", "Clean air"), ("c", "Sulphide minerals, graphite and wet clay"), ("d", "Glass windows")], "c"),
        ("Where is resolution best in a cross-hole survey?",
         [("a", "Far from all the holes"), ("b", "Only at the surface"), ("c", "Nowhere at all"), ("d", "Near the holes")], "d"),
        ("What is modelling used for?",
         [("a", "To print the report in colour"), ("b", "To test what data a shape would give and adjust until it fits"), ("c", "To count the drill crew"), ("d", "To choose a lunch menu")], "b"),
    ],
}
