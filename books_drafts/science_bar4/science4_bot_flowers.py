"""Flower Anatomy and Plant Identification: the parts of a flower, how botanists read a floral diagram, and how identification keys work."""
CODE = "science4_bot_flowers"
BOOK = {
    "title": "Flower Anatomy and Plant Identification",
    "subtitle": "Floral parts, floral diagrams and telling plants apart",
    "chapters": [
        ("Floral organs",
         "A typical flower has four sets of organs: sepals, petals, stamens and carpels. Sepals protect the bud, petals attract pollinators, stamens make pollen, and carpels hold the ovules. Together they make up the flower’s reproductive system."),
        ("Floral diagrams",
         "A floral diagram is a drawing that shows the number and arrangement of floral parts, as seen from above. Symbols mark each organ type. A diagram gives a compact summary of a flower’s structure."),
        ("Identification keys",
         "A key is a set of paired choices that lead the user, step by step, to a name. Each choice asks about a clear feature, such as leaf shape or flower colour. A good key is clear and avoids guesswork."),
        ("Reproductive strategies",
         "Flowers use many strategies to attract pollinators, such as scent, colour, nectar and shape. Some are wind-pollinated and need no showy parts at all. Each strategy suits the plant’s habitat and its partners."),
        ("Herbarium specimens",
         "A herbarium is a collection of pressed and dried plants kept for study. Specimens record the form of a plant at one moment and a place and date. They are invaluable for identifying plants and tracking change."),
        ("Family recognition",
         "Plant families share features, such as flower arrangement or leaf pattern. Learning these shared features lets a botanist place an unfamiliar plant in a family, then narrow down its name. Family knowledge makes keys faster to use."),
    ],
    "test": [
        ("Which organs make pollen?",
         [("a", "Stamens"), ("b", "Sepals"), ("c", "Petals"), ("d", "Carpels")], "a"),
        ("What does a floral diagram show?",
         [("a", "The smell of a flower"), ("b", "The number and arrangement of floral parts"), ("c", "The price of seeds"), ("d", "The weight of the soil")], "b"),
        ("What is an identification key?",
         [("a", "A set of paired choices that leads step by step to a name"), ("b", "A metal tool for opening seed boxes"), ("c", "A map of the garden"), ("d", "A calendar of flowering")], "a"),
        ("What is a herbarium?",
         [("a", "A bakery for bread"), ("b", "A collection of pressed and dried plants kept for study"), ("c", "A type of fish tank"), ("d", "A farm animal shelter")], "b"),
        ("What do plant families share?",
         [("a", "Identical genomes"), ("b", "The same soil"), ("c", "The same height"), ("d", "Features such as flower arrangement or leaf pattern")], "d"),
    ],
}
