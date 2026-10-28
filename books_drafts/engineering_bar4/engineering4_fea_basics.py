"""Finite Element Analysis: meshing a part, setting loads and supports, and checking that the answer can be trusted."""
CODE = "engineering4_fea_basics"
BOOK = {
    "title": "Finite Element Analysis: Meshing a Part",
    "subtitle": "Elements, loads, supports and checking the answer",
    "chapters": [
        ("What the method does",
         "Finite element analysis cuts a part into many small pieces called elements. Each element follows simple rules, and the computer joins them at shared corners called nodes. Together the pieces give an estimate of how the whole part bends, stretches and carries load."),
        ("Building the mesh",
         "The mesh is the net of elements laid over the part. Fine elements give better answers near sharp corners and holes, where stress rises quickly. Coarse elements are quicker to run, so engineers use fine mesh only where it matters."),
        ("Loads and supports",
         "Every model needs loads, such as forces and pressures, and supports that hold the part in place. A wrong support can make a model look stiff when it is not. Engineers check that the supports match how the part is really fixed."),
        ("Checking convergence",
         "Convergence means the answer stops changing much when the mesh gets finer. Engineers refine the mesh in steps and watch the peak stress. If the peak keeps climbing at a sharp corner, the answer has not converged there yet."),
        ("Reading the stress plot",
         "A stress plot uses colours to show where the material works hardest. Peaks at sharp corners can be real, or they can be a sign of a poor mesh or a wrong model. A good engineer asks which one it is before changing the design."),
        ("Simulation and the test",
         "A simulation is only as good as the physical test that backs it. Engineers compare the model with a bench test or a load test on a real part. Each test costs time and money, so a well-checked model saves physical prototypes and gives a clearer picture of risk."),
    ],
    "test": [
        ("What do the small pieces in a finite element model get called?", [("a", "Nodes only"), ("b", "Layers"), ("c", "Elements"), ("d", "Bolts")], "c"),
        ("Where does stress usually rise most quickly in a part?", [("a", "At sharp corners and holes"), ("b", "In the middle of a flat plate"), ("c", "On the paint"), ("d", "At the mesh edge only")], "a"),
        ("What does convergence mean in a finite element model?", [("a", "The model has no supports"), ("b", "The computer runs out of memory"), ("c", "The part gets heavier"), ("d", "The answer stops changing much as the mesh gets finer")], "d"),
        ("Why must supports in a model match the real part?", [("a", "Supports change the colour of the plot"), ("b", "A wrong support can make the model look stiffer than the real part"), ("c", "Supports are not needed in any model"), ("d", "Supports set the size of the elements")], "b"),
        ("Why is a physical test still valuable when a simulation exists?", [("a", "Simulations never give any numbers"), ("b", "Tests replace the need for a mesh"), ("c", "A test checks that the model matches a real part"), ("d", "Tests are only for paint")], "c"),
    ],
}
