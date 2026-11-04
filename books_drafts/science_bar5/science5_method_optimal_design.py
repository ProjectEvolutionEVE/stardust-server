"""Optimal Experimental Design: design criteria, information matrices, sequential design, adaptive trials, cost-aware design and robustness."""
CODE = "science5_method_optimal_design"
BOOK = {
    "title": "Optimal Experimental Design",
    "subtitle": "Choosing the experiment that teaches the most for the cost",
    "chapters": [
        ("What optimal design aims for",
         "Optimal design chooses the plan that gives the most information for a given cost or number of runs. Before any measurement, the team decides what it most needs to learn. A good plan puts its effort where that answer is most sensitive."),
        ("Design criteria",
         "A design criterion is a rule for judging a plan. Some criteria aim to pin down the main effects, and others to predict new cases well. The right criterion depends on the question, so state it before comparing designs."),
        ("Information matrices",
         "An information matrix is a mathematical summary of how much information a design gives about the unknown values. Designs are compared by how their matrices behave. Larger information means smaller uncertainty in the estimates."),
        ("Sequential design",
         "In sequential design, each step's choice uses the results of earlier steps. The next run is picked where it will teach the most, given what is already known. This often needs fewer runs than fixing the whole plan in advance."),
        ("Adaptive trials and cost-aware design",
         "An adaptive trial is one whose rules allow planned changes based on interim data, set out in advance. Cost-aware design weighs each option by what it costs to run, so cheap runs can be used more often. Rules for stopping and changing must be written before the trial starts."),
        ("Design robustness",
         "Robustness checks whether a design still works well if the assumed values turn out wrong. A plan that only works under one set of guesses is fragile. Testing a few alternative assumptions shows how much the plan can bend."),
    ],
    "test": [
        ("What is the goal of an optimal design?",
         [("a", "To use the most samples possible"), ("b", "To choose a plan that gives the most information for a given cost or number of runs"), ("c", "To avoid measuring anything"), ("d", "To make the plot look smooth")], "b"),
        ("What is an information matrix?",
         [("a", "A table of lab rotas"), ("b", "A list of journals"), ("c", "A shopping list"), ("d", "A mathematical summary of how much information a design gives about the unknown values")], "d"),
        ("What does sequential design mean?",
         [("a", "All runs are chosen at once and never changed"), ("b", "Runs are chosen by flipping a coin"), ("c", "Each step's choice uses the results of earlier steps"), ("d", "Runs are chosen by the sponsor")], "c"),
        ("What is an adaptive trial?",
         [("a", "A trial whose rules allow planned changes based on interim data, set out in advance"), ("b", "A trial with no plan at all"), ("c", "A trial run by a robot only"), ("d", "A trial with no participants")], "a"),
        ("Why check design robustness?",
         [("a", "To make the design more expensive"), ("b", "To avoid writing the design down"), ("c", "To see whether the plan still works well if the assumed values turn out wrong"), ("d", "To remove the need for data")], "c"),
    ],
}
