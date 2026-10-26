"""Ore Grades: how much metal real mines find in their rock, and why the game's pieces are simpler."""
CODE = 'mining2_grades'
BOOK = {
    "title": "Ore Grades: Real Rock and Pure Pieces",
    "subtitle": "How much metal real mines find in their rock, and why the game's pieces are simpler",
    "chapters": [
        ("What a grade is",
         "An ore's grade is how much metal it holds, usually written as a percentage of weight. For gold, grade is written in grams per tonne. A mine works only the rock whose grade is high enough to pay for the work."),
        ("Real grades are often low",
         "Many copper mines today work rock with less than 1 per cent copper. Many large gold mines work ore with only a few grams of gold in every tonne of rock. One gram per tonne is about one part per million."),
        ("The cut-off grade",
         "The cut-off grade is the lowest grade worth mining. It moves with the price of the metal. When prices rise, more low-grade rock becomes worth digging, and when they fall, some mines close."),
        ("Waste rock and dilution",
         "Real ore is mixed with waste rock, called gangue, which holds little or no metal. Mining takes some waste out along with the ore, and that lowers the grade. Crushing, grinding and separating then remove most of the gangue before smelting."),
        ("The game's pure pieces",
         "The game keeps this simple. Every debris piece is pure ore mineral, so the mineral's formula gives its metal share exactly. Chalcopyrite gives 34.63 per cent copper, with no dilution."),
        ("Why grade matters",
         "A real mine's grade tells you how much metal to expect from each tonne of rock. The game's pieces give the same kind of answer, and you can check any piece with the formula and a calculator."),
    ],
    "test": [
        ("What is an ore's grade?",
         [("a", "Its colour"), ("b", "How much metal it holds"), ("c", "Its shape"), ("d", "Its place in the queue")], "b"),
        ("Roughly how much copper do many modern copper mines work?",
         [("a", "About 50 per cent"), ("b", "Over 90 per cent"), ("c", "Under 1 per cent"), ("d", "None at all")], "c"),
        ("What does cut-off grade mean?",
         [("a", "The price of metal"), ("b", "The highest grade in the world"), ("c", "The depth of a mine"), ("d", "The lowest grade worth mining")], "d"),
        ("What is gangue?",
         [("a", "A kind of engine"), ("b", "Waste rock that holds little or no metal"), ("c", "Pure gold"), ("d", "A bay for ships")], "b"),
        ("Why does each game piece yield exactly its formula's share?",
         [("a", "It is pure ore mineral, with no dilution"), ("b", "It is all gold"), ("c", "The bank measures it"), ("d", "It is printed in the shop")], "a"),
    ],
}
