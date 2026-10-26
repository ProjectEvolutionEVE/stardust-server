"""Iron Ores: the two iron ores in our fields, how to tell them apart, and what their iron becomes."""
CODE = 'mining2_iron'
BOOK = {
    "title": "Iron Ores: Hematite and Magnetite",
    "subtitle": "The two iron ores in our fields, how to tell them apart, and what their iron becomes",
    "chapters": [
        ("The two iron ores",
         "Our fields hold two iron ores, and both sit in the plentiful band. Iron ore (hematite) has the formula Fe₂O₃ and gives about 70 per cent of its weight as iron. Iron ore (magnetite) has the formula Fe₃O₄ and gives about 72 per cent."),
        ("Hematite and its streak",
         "Hematite is one of the main iron ores used around the world. Rub it across unglazed tile and it leaves a reddish-brown streak, even when the lump looks black or grey. That streak is one of the best ways to pick it out."),
        ("Magnetite is magnetic",
         "Magnetite is the iron ore that a magnet pulls at. Its streak is black. Lodestone, a natural form of magnetite, was used in some of the earliest compasses."),
        ("Why iron matters",
         "Most of the steel we build with is iron mixed with a small amount of carbon. Steel is strong enough for ships, bridges and the frames of machines. Both of these ores are a way to get the iron that steel is made from."),
        ("Iron ore in the game",
         "Each piece is pure ore mineral, so its formula gives its share. Hematite yields 69.94 per cent iron by weight and magnetite 72.36 per cent, and the rest of each piece is slag. Iron ore is common, so you will meet it in many fields."),
        ("Iron-nickel is a different piece",
         "Iron-nickel metal is a separate common piece. It is already metal, so it does not need smelting the way an ore does. The game takes it as about 90 per cent iron and 10 per cent nickel."),
    ],
    "test": [
        ("Roughly what share of its weight does hematite give as iron?",
         [("a", "About 10 per cent"), ("b", "About 70 per cent"), ("c", "About 35 per cent"), ("d", "All of it")], "b"),
        ("What colour is the streak left by hematite on unglazed tile?",
         [("a", "White"), ("b", "Black"), ("c", "Reddish-brown"), ("d", "Green")], "c"),
        ("Which of these iron ores is magnetic?",
         [("a", "Hematite"), ("b", "Gold"), ("c", "Chalcopyrite"), ("d", "Magnetite")], "d"),
        ("Steel is iron mixed with a small amount of what?",
         [("a", "Carbon"), ("b", "Gold"), ("c", "Ice"), ("d", "Sand")], "a"),
        ("In the game, which iron ore gives the bigger share of iron by weight?",
         [("a", "Hematite"), ("b", "Magnetite"), ("c", "They are equal"), ("d", "Neither gives iron")], "b"),
    ],
}
