"""Fruit Ripening and Ethylene: how fruit soften, sweeten and smell as they ripen, and how ethylene controls the process."""
CODE = "science5_bot_ripening"
BOOK = {
    "title": "Fruit Ripening and Ethylene",
    "subtitle": "Climacteric ripening, ethylene signalling and storage control",
    "chapters": [
        ("Ripening is a change of plan", "Ripening is the set of changes that makes a fruit ready to eat and helps it spread its seeds. Colour, softness, sugar and aroma all change during ripening. The process is tightly controlled by the plant."),
        ("Climacteric fruit", "Some fruits, such as bananas, apples and tomatoes, have a climacteric ripening. Their respiration rises sharply as they ripen. This rise is driven by a burst of ethylene."),
        ("Ethylene signalling", "Ethylene is a plant gas that acts as a hormone. It binds to receptors in the cells and starts a chain of signals. Those signals switch on the genes that drive ripening."),
        ("Softening and sweetening", "As fruit ripen, their cell walls are broken down by enzymes, so the fruit softens. Starch is often turned into sugar, which makes the fruit sweeter. Aroma compounds build up at the same time."),
        ("Controlling ripening", "Ripening can be slowed by cold storage and by blocking ethylene receptors. The chemical 1-MCP is used to block those receptors in some crops. Growers use these tools to hold fruit until it reaches the market."),
        ("Storage management", "Storing fruit together can hurt the fruit if one kind releases lots of ethylene. Careful sorting and temperature control prevent early ripening. Good storage keeps quality high for longer."),
    ],
    "test": [
        ("What is ethylene in a fruit?",
         [("a", "A type of metal"), ("b", "A plant gas that acts as a hormone and starts ripening signals"), ("c", "A kind of bird song"), ("d", "A sweet syrup")], "b"),
        ("Which fruit is a climacteric fruit?",
         [("a", "Cactus"), ("b", "Banana"), ("c", "Grape bunch"), ("d", "Onion")], "b"),
        ("What happens to cell walls during ripening?",
         [("a", "They grow thicker and harder"), ("b", "They turn into metal"), ("c", "Enzymes break them down, so the fruit softens"), ("d", "They dissolve in cold water")], "c"),
        ("What does 1-MCP do to ripening?",
         [("a", "It blocks the ethylene receptors"), ("b", "It adds extra ethylene"), ("c", "It turns fruit into stone"), ("d", "It makes fruit grow larger")], "a"),
        ("Why does storing fruit together need care?",
         [("a", "One ripe kind can release ethylene and make the others ripen too early"), ("b", "Fruit cannot share a room"), ("c", "Fruit must be kept in water"), ("d", "Fruit cannot be cooled at all")], "a"),
    ],
}
