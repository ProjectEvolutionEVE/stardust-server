"""Fermi Estimates: estimating the unknowable, breaking a question into factors, ranges, the piano tuners, sanity checks and quick market sizing."""
CODE = "business5_fermi"
BOOK = {
    "title": "Fermi Estimates",
    "subtitle": "Estimating the unknowable, breaking questions into factors, and quick market sizing",
    "chapters": [
        ("Estimating the unknowable", "A Fermi estimate is a quick, rough answer to a question where data is missing. It is named after the physicist Enrico Fermi, who was known for such estimates. The aim is an order of magnitude, not an exact figure."),
        ("Breaking into factors", "Split a big unknown into smaller factors that you can estimate. Multiply the factors together to reach a rough total. Each factor may be off, but errors often cancel out."),
        ("Ranges", "Give a low and a high estimate for each factor, not a single number. The result is then a range, which shows how uncertain the answer is. A range is more honest than a false point."),
        ("The piano tuners", "A classic example asks how many piano tuners work in a city such as Chicago. You can estimate the number of pianos, how often each is tuned, and how many a tuner can do in a year. Multiplying and dividing gives a rough number to test."),
        ("Sanity checks", "After you have an answer, check it against something you know. Does it make sense compared with people, shops, or money? A sanity check catches many big mistakes."),
        ("Quick market sizing", "Businesses use Fermi estimates to size a market before collecting detailed data. Multiply the number of possible customers by how often they buy and by the price. The result shows whether a market is worth a closer look."),
    ],
    "test": [
        ("What is a Fermi estimate?",
         [("a", "An exact measurement"), ("b", "A quick, rough answer where data is missing"), ("c", "A kind of cake"), ("d", "A tax form")], "b"),
        ("What is the aim of a Fermi estimate?",
         [("a", "An exact figure"), ("b", "A guess with no basis"), ("c", "A colour"), ("d", "An order of magnitude")], "d"),
        ("Why give a range instead of one number?",
         [("a", "It shows how uncertain the answer is"), ("b", "It hides the answer"), ("c", "It always doubles the answer"), ("d", "It is required by law")], "a"),
        ("What does a sanity check do?",
         [("a", "Checks the weather"), ("b", "Makes the answer longer"), ("c", "Compares the answer with something known to catch big mistakes"), ("d", "Removes factors")], "c"),
        ("What is quick market sizing?",
         [("a", "Measuring shoe sizes"), ("b", "Multiplying possible customers by how often they buy and by the price"), ("c", "Choosing a logo"), ("d", "Building a ship")], "b"),
    ],
}
