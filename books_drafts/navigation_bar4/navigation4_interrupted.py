"""Interrupted and Pseudocylindrical Maps: world maps that cut the sea to save the land."""
CODE = "navigation4_interrupted"
BOOK = {
    "title": "Interrupted and Pseudocylindrical Maps",
    "subtitle": "World maps that cut the sea to save the land",
    "chapters": [
        ("Flattening a globe", "Every flat world map must stretch or tear parts of the globe. Pseudocylindrical maps spread the meridians across the page. The result often looks like a curved oval."),
        ("The sinusoidal design", "The sinusoidal projection is one of the oldest equal-area world maps. Its lines of latitude are straight, and its meridians curve. It keeps areas right but distorts shapes away from the centre line."),
        ("Interruptions to reduce distortion", "An interrupted map cuts the sea areas so the land can be laid flat with less stretch. Each piece is placed separately. This lowers distortion over the continents."),
        ("Mollweide and Goode", "The Mollweide projection is an equal-area oval map. Goode's homolosine is an interrupted equal-area map. Both give good results when comparing areas."),
        ("The compromise", "Every equal-area map pays a price in shape. Shapes near the edges can look odd. Choose the map that suits the task you are doing."),
        ("Reading them", "Read these maps with care. Areas are accurate, but shapes away from the centre are not. Check the labels and the scale before you measure."),
    ],
    "test": [
        ("What does a pseudocylindrical map do?",
         [("a", "It draws the world as a cube"), ("b", "It spreads the meridians across the page"), ("c", "It prints only one country"), ("d", "It hides the sea")], "b"),
        ("Which of these is an equal-area oval map?",
         [("a", "Mercator"), ("b", "Gnomonic"), ("c", "Polyconic"), ("d", "Mollweide")], "d"),
        ("What does an interrupted map do?",
         [("a", "It cuts the sea areas so the land has less stretch"), ("b", "It removes all coastlines"), ("c", "It makes the map three-dimensional"), ("d", "It shows only the Moon")], "a"),
        ("What is the sinusoidal design known for?",
         [("a", "Keeping colours right"), ("b", "Showing the sky"), ("c", "Keeping areas right"), ("d", "Showing the poles")], "c"),
        ("What is the usual trade-off of an equal-area map?",
         [("a", "Areas go wrong"), ("b", "The map is too small"), ("c", "Shapes can look odd near the edges"), ("d", "It cannot be printed")], "c"),
    ],
}
