"""Ptolemy's Geography: the latitude and longitude grid, coordinate tables, distance estimates, errors, influence and lost originals."""
CODE = "navigation4_ptolemy"
BOOK = {
    "title": "Ptolemy's Geography",
    "subtitle": "A grid of latitude and longitude for the known world",
    "chapters": [
        ("A grid for the world", "Ptolemy, an Alexandrian scholar of the second century, wrote a Geography that set out a grid of latitude and longitude. He gave lists of coordinates for many places. His method shaped mapmaking for centuries."),
        ("Latitude and longitude tables", "The tables listed the coordinates of cities, rivers and coasts. Each entry gave a latitude and a longitude in degrees. Users could place these points on a map."),
        ("Distance estimates", "Distances were estimated from travel reports and other sources. The distances were only as good as the reports they came from. Errors in the sources carried into the coordinates."),
        ("Errors", "The tables contained real errors, including places placed too far east or west. Some regions were stretched or squeezed on the grid. Later readers corrected many of these mistakes."),
        ("Influence", "The Geography was copied and translated across Europe and the Islamic world for centuries. Its method of coordinates influenced later maps. Many later mapmakers built on his grid."),
        ("Lost originals", "Ptolemy's original maps have not survived. Later copies of the text were made with maps added by scholars. Scholars still work to reconstruct what the originals showed."),
    ],
    "test": [
        ("Who wrote the Geography that set out a grid of latitude and longitude?", [("a", "Ptolemy, an Alexandrian scholar"), ("b", "A Viking sailor"), ("c", "A Chinese emperor's clerk"), ("d", "A medieval monk in Ireland")], "a"),
        ("What did the coordinate tables list?", [("a", "Prices of goods at each port"), ("b", "Recipes from every region"), ("c", "Latitude and longitude for cities, rivers and coasts"), ("d", "Names of ships in harbour")], "c"),
        ("Why could Ptolemy's distances be wrong?", [("a", "The Earth was flat"), ("b", "They depended on travel reports, which were not always reliable"), ("c", "Ships moved at a fixed speed"), ("d", "Ink faded in the sun")], "b"),
        ("What happened to Ptolemy's original maps?", [("a", "They are kept in every library"), ("b", "They were printed on every ship"), ("c", "They were sent to the Moon"), ("d", "They have not survived")], "d"),
        ("What was the lasting influence of the Geography?", [("a", "It banned maps for a century"), ("b", "Its grid of coordinates shaped later maps"), ("c", "It influenced only food recipes"), ("d", "It was forgotten the next day")], "b"),
    ],
}
