"""Medicine, bar 2: Cells and Tissues. How cells group into tissues, and how tissues build the organs of bar 1."""
CODE = "medicine2_cells"
BOOK = {
    "title": "Cells and Tissues",
    "subtitle": "The smallest working units of the body, and how they group into tissues and organs",
    "chapters": [
        ("The smallest working unit",
         "Every living thing is built from cells. A cell is the smallest unit that can do all the jobs of life: it takes in materials, releases energy and makes new copies of itself. A human body contains tens of trillions of cells."),
        ("Inside a cell",
         "Each cell has an outer membrane that controls what comes in and what goes out. The nucleus holds the cell's instructions, written in a chemical called DNA. Small parts called mitochondria release energy from food, and other parts each do a job of their own."),
        ("Cells that work as a team",
         "Cells of one kind that work together form a tissue. The body has four main kinds: epithelial tissue covers surfaces, connective tissue supports and joins, muscle tissue contracts to produce movement, and nervous tissue carries signals."),
        ("From tissues to organs",
         "Several kinds of tissue working together form an organ, such as the heart or the stomach. Organs that work as a group form a system, such as the circulatory or digestive system. Each level depends on the one below it."),
        ("Cells that are replaced",
         "Many cells wear out and are replaced all the time. Red blood cells live for about four months, and the outer layer of skin is renewed every few weeks. Many nerve cells in the brain are not replaced in the same way."),
        ("Why cells matter to medicine",
         "Many illnesses begin in cells: a cell can be damaged, infected or stop working properly. Knowing how cells, tissues and organs fit together helps doctors work out which part of the body is affected and why. This is the base for the other body books."),
    ],
    "test": [
        ("What is the smallest unit that can carry out all the jobs of life?",
         [("a", "A tissue"), ("b", "An organ"), ("c", "A cell"), ("d", "A system")], "c"),
        ("Which part of a cell holds its instructions?",
         [("a", "The nucleus"), ("b", "The outer membrane"), ("c", "The mitochondria"), ("d", "The tissue")], "a"),
        ("Which kind of tissue carries signals around the body?",
         [("a", "Muscle tissue"), ("b", "Epithelial tissue"), ("c", "Connective tissue"), ("d", "Nervous tissue")], "d"),
        ("Roughly how long do red blood cells live?",
         [("a", "About one day"), ("b", "About four months"), ("c", "About ten years"), ("d", "About one week")], "b"),
        ("What is a whole organ, such as the stomach, made of?",
         [("a", "One single cell"), ("b", "Several kinds of tissue working together"), ("c", "Blood alone"), ("d", "Air and water")], "b"),
    ],
}
