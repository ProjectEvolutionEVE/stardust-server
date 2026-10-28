"""Computational Fluid Dynamics: Simulating Flow. Solving flow on a computer, and checking the answer against real tests."""
CODE = 'engineering4_cfd'
BOOK = {
    "title": "Computational Fluid Dynamics: Simulating Flow",
    "subtitle": "Solving flow on a computer, and checking the answer against real tests",
    "chapters": [
        ("Meshing",
         "The space around a part is cut into many small cells, called the mesh. A finer mesh gives more detail, but it takes longer to solve."),
        ("Boundary conditions",
         "The inputs at the edges of the problem, such as inlet speed, wall behaviour and outlet pressure, define the case. Wrong boundary conditions give wrong answers, however good the mesh."),
        ("Convergence",
         "The solver repeats its calculation until the answers stop changing by much. Checking convergence shows whether the result has settled."),
        ("Validation against tests",
         "A simulation is compared with measurements from a test of a similar case. Agreement builds trust in the model."),
        ("Reporting results",
         "A good report states the mesh, the settings, the convergence and the uncertainty. Readers can then judge how far to trust the result."),
        ("The time cost of runs",
         "Fine meshes and long runs need powerful computers and many hours. Planning the size of the run saves time and money."),
    ],
    "test": [
        ("What is meshing in CFD?",
         [("a", "Painting the part"), ("b", "Cutting the space around the part into many small cells"), ("c", "Building a wire fence"), ("d", "Running a sound check")], "b"),
        ("What do boundary conditions define?",
         [("a", "The paint"), ("b", "The staff"), ("c", "The lunch menu"), ("d", "The inputs at the edges of the problem, such as inlet speed")], "d"),
        ("What does convergence check?",
         [("a", "Whether the answers have settled"), ("b", "Whether the paint is dry"), ("c", "Whether the sun has risen"), ("d", "Whether the staff have arrived")], "a"),
        ("What must a simulation be compared against?",
         [("a", "A painting"), ("b", "A joke"), ("c", "Measurements from a test of a similar case"), ("d", "A rumour")], "c"),
        ("What does a finer mesh usually mean?",
         [("a", "Less detail"), ("b", "More detail but a longer run"), ("c", "No change at all"), ("d", "A smaller file, always")], "b"),
    ],
}
