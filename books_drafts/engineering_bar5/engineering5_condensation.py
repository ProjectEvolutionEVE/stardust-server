"""Film Condensation Theory: how vapour turns to liquid on a cold surface, Nusselt's film model, and how to raise heat transfer."""
CODE = "engineering5_condensation"
BOOK = {
    "title": "Film Condensation Theory",
    "subtitle": "Nusselt film theory, drainage and dropwise condensation",
    "chapters": [
        ("Vapour turning to liquid", "When vapour touches a cold surface, it condenses and releases its heat. This heat release is what a condenser is built to carry away."),
        ("Nusselt film theory", "Nusselt's theory, published in 1916, treats the condensate as a smooth film draining down the surface. It predicts the heat transfer from that film."),
        ("Condensate drainage", "The film thickens as it runs down the surface. How well it drains controls how much heat passes through it."),
        ("Dropwise condensation", "On some surfaces the liquid forms separate drops rather than a film. Heat transfer can be much higher this way, because the bare surface is exposed between drops."),
        ("Enhancing heat transfer", "Engineers use special coatings and fins to encourage drops or to thin the film. Both aim to raise the heat transfer."),
        ("Condenser design", "The design must handle the film, the drainage and the heat load together. Leaving out one of these gives a poor condenser."),
    ],
    "test": [
        ("What happens when vapour touches a cold surface?", [("a", "It freezes into solid blocks"), ("b", "It turns into paint"), ("c", "It condenses and releases heat"), ("d", "It grows roots into the surface")], "c"),
        ("What did Nusselt's theory assume?", [("a", "A smooth film draining down the surface"), ("b", "A film that flies off the surface"), ("c", "A painted cloud over the surface"), ("d", "A sweet liquid spread on the surface")], "a"),
        ("What is dropwise condensation?", [("a", "A drink served cold"), ("b", "Liquid forming drops rather than a film"), ("c", "A type of drill bit"), ("d", "A drop of rain falling in a bucket")], "b"),
        ("How do engineers enhance heat transfer?", [("a", "By painting the surface black"), ("b", "By shutting the windows of the plant"), ("c", "By adding sugar to the liquid"), ("d", "With coatings and fins that encourage drops or thin the film")], "d"),
        ("What must condenser design handle?", [("a", "Only the colour of the tubes"), ("b", "Only the paint on the shell"), ("c", "The film, drainage and heat load together"), ("d", "Nothing at all")], "c"),
    ],
}
