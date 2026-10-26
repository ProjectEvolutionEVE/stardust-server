"""Map Design for Clear Reading: making a map that people can read quickly and trust."""
CODE = 'navigation3b_map_design'
BOOK = {
    "title": "Map Design for Clear Reading",
    "subtitle": "Making a map that people can read quickly and trust",
    "chapters": [
        ("Start with the question",
         "A map answers a question for its reader. Decide what the reader needs first: the way to a place, the depth of the water, or the spread of a crop. Everything on the map should help that answer, and anything that does not should go."),
        ("Order the information",
         "Use a clear order of importance. The main features are the boldest, and background details such as grids and faint roads are lighter. The reader's eye should go first to the subject, then to the labels, and last to the background."),
        ("Colour with care",
         "Use a small number of colours, and give each one a meaning. A range from light to dark shows amounts. Clearly different colours show separate categories. Roughly 8 men in 100 have some kind of colour vision difference, so add labels or patterns rather than relying on colour alone."),
        ("Labels and the legend",
         "Label the important places directly, so the reader does not have to hunt through a key. The legend explains every symbol and colour, in the same style as the map. Text must be large enough to read at the size the map will be shown or printed."),
        ("Scale and direction",
         "A scale bar is more useful than a ratio alone, because it stays true when the map is enlarged or reduced. A north arrow shows which way is up. Any map that people use to walk, sail or fly needs both."),
        ("Test it on a reader",
         "Show the map to someone who did not make it. Ask them to find one place, and to say what one colour means. If they cannot, change the map, not the reader."),
    ],
    "test": [
        ("What should a map designer decide first?",
         [("a", "The colour of the frame"), ("b", "The question the reader needs answered"), ("c", "The price of the paper"), ("d", "The size of the font only")], "b"),
        ("Why does a scale bar work better than a written ratio alone?",
         [("a", "It stays true when the map is enlarged or reduced"), ("b", "It makes the map heavier"), ("c", "It hides the north arrow"), ("d", "It is always printed in colour")], "a"),
        ("Roughly how many men in 100 have some kind of colour vision difference?",
         [("a", "About 1"), ("b", "About 8"), ("c", "About 50"), ("d", "About 90")], "b"),
        ("Why should a map not rely on red and green alone to show two categories?",
         [("a", "Because red and green are the cheapest inks"), ("b", "Because red maps cannot be printed"), ("c", "Because green means danger everywhere"), ("d", "Because some readers cannot tell those colours apart, so labels or patterns are needed")], "d"),
        ("What is the best quick test of a map design?",
         [("a", "Count the colours"), ("b", "Weigh the paper"), ("c", "Show it to someone who did not make it, and ask them to find a place and explain a colour"), ("d", "Print it at night")], "c"),
    ],
}
