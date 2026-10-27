"""The Ritz Method and Approximate Solutions: guessing a shape with adjustable parts, and letting energy choose the best one."""
CODE = "engineering5_ritz"
BOOK = {
    "title": "The Ritz Method and Approximate Solutions",
    "subtitle": "Finding a good answer by guessing a shape and letting energy pick the best one",
    "chapters": [
        ("Guessing a shape",
         "The Ritz method starts with a trial shape that satisfies the supports, with some adjustable parts. Each adjustable part is a number to be found."),
        ("Energy as the guide",
         "The total energy of the trial shape depends on those numbers. Choosing them to make the energy as low as possible gives the best answer within that family of shapes."),
        ("More terms, better answers",
         "Adding more shape functions gives more freedom, and usually a closer answer. Each extra term helps less than the one before, so the answer settles down."),
        ("Error and bounds",
         "For many problems the Ritz result gives an upper bound on the energy. The true answer is never higher than the trial answer, so a rough result still tells you a limit."),
        ("Comparing with finite elements",
         "Finite element methods split a structure into many small pieces, which is more general. The Ritz method is compact and gives a formula, which is useful for checks and for simple shapes."),
        ("Using it sensibly",
         "Choose trial shapes that look like the expected deformed form. A poor guess converges slowly, so check the result with a second, larger set of terms."),
    ],
    "test": [
        ("What is the first step in the Ritz method?",
         [("a", "Painting the beam"), ("b", "Counting the bolts"), ("c", "Choosing a trial shape with adjustable parts"), ("d", "Measuring the weld")], "c"),
        ("What is the goal when choosing the adjustable parts?",
         [("a", "Make the energy as low as possible"), ("b", "Make the colour bright"), ("c", "Make the shape as tall as possible"), ("d", "Make the cost the highest")], "a"),
        ("What usually happens when more terms are added?",
         [("a", "The answer gets worse"), ("b", "The answer usually gets closer"), ("c", "Nothing ever changes"), ("d", "The beam melts")], "b"),
        ("For many problems, what kind of bound does Ritz give on the energy?",
         [("a", "A lower bound only"), ("b", "An upper bound"), ("c", "No bound at all"), ("d", "A bound on colour")], "b"),
        ("What is a poor trial shape likely to cause?",
         [("a", "Faster convergence"), ("b", "Slow convergence"), ("c", "A perfect answer every time"), ("d", "Zero stress")], "b"),
    ],
}
