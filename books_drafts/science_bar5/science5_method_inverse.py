"""Inverse Problems and Regularisation: ill-posed problems, regularisation terms, Tikhonov methods, resolution matrices, noise and stability and geophysical examples."""
CODE = "science5_method_inverse"
BOOK = {
    "title": "Inverse Problems and Regularisation",
    "subtitle": "Working backwards from measurements to causes, and keeping the answer sensible",
    "chapters": [
        ("What an inverse problem is",
         "An inverse problem starts from measurements and asks what caused them. Seismic waves, medical scans and satellite images all work this way. The forward problem, predicting measurements from causes, is usually the easy direction."),
        ("Ill-posed problems",
         "A problem is ill-posed when a small change in the data can cause a large change in the answer, or when many different answers fit the data equally well. Most real inverse problems are ill-posed. They need extra guidance to give a sensible result."),
        ("Regularisation terms",
         "A regularisation term is an extra penalty that favours stable, sensible answers. It adds a cost for solutions that are wild or unlikely. The penalty must be chosen with the physics of the problem in mind."),
        ("Tikhonov methods",
         "A Tikhonov method is a regularisation method that adds a penalty on the size of the solution. The penalty weight controls the balance between fitting the data and keeping the answer smooth. It is one of the most widely used methods for ill-posed problems."),
        ("Resolution and noise",
         "A resolution matrix shows how well the estimated model matches the true one. Poor resolution means nearby features blur together. Noise in the data can be amplified by the inversion, so the answer can become unstable."),
        ("Geophysical examples",
         "In geophysics, inverse methods turn surface measurements into maps of rock below ground. The chosen regularisation shapes what the map shows. Results should always be checked against independent data where possible."),
    ],
    "test": [
        ("What makes a problem ill-posed?",
         [("a", "It is too easy"), ("b", "A small change in the data can cause a large change in the answer, or the answer is not unique"), ("c", "It has no data"), ("d", "It uses only one number")], "b"),
        ("What is a regularisation term?",
         [("a", "An extra penalty that favours stable, sensible answers"), ("b", "A legal rule"), ("c", "A sampling rate"), ("d", "A computer's warranty")], "a"),
        ("What is a Tikhonov method?",
         [("a", "A dance step"), ("b", "A survey form"), ("c", "A regularisation method that adds a penalty on the size of the solution"), ("d", "A microscope brand")], "c"),
        ("What is a resolution matrix?",
         [("a", "A table of lab coats"), ("b", "A score for the paper"), ("c", "A list of journals"), ("d", "A matrix showing how well the estimated model matches the true one")], "d"),
        ("Why do inverse problems care about noise?",
         [("a", "Noise improves every answer"), ("b", "Noise is a type of sample"), ("c", "Noise can be amplified and make the answer unstable"), ("d", "Noise is always removed by the instrument")], "c"),
    ],
}
