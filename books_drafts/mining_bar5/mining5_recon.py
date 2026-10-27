"""Mine Reconciliation: comparing what the model predicted with what was actually mined and milled, and learning from the gap."""
CODE = "mining5_recon"
BOOK = {
    "title": "Mine Reconciliation: Predicted Versus Mined",
    "subtitle": "Model against mill, grade control, bias and corrective action",
    "chapters": [
        ("Checking the plan",
         "Every mine plan starts with a model of the ore. Reconciliation asks a simple question: did the ore turn out as the model said? It compares the predicted tonnes and grade with what was mined and milled."),
        ("Model against mill",
         "The mill keeps accurate records of the ore it processes. These records are compared with the block model for the same period. Any gap between the two shows where the model needs attention."),
        ("Grade control",
         "Grade control sampling is done close to the mining face, just before ore is dug. It guides which material goes to the mill and which goes to waste. Good grade control makes the reconciliation more trustworthy."),
        ("Factors that create gaps",
         "Gaps can come from many sources. Sampling error, changes in mining method, recovery in the mill and mistakes in the model can all add to them. Looking at each source separately shows what caused the gap."),
        ("Bias and corrective action",
         "A bias is a gap that always points the same way, such as the model always overestimating grade. A bias must be corrected at its source, for example by changing the estimation method or the sampling. Random gaps need different care."),
        ("Reporting",
         "Reconciliation results go into regular reports for managers and engineers. A clear report states the size of each gap and what is being done about it. Honest reporting builds trust in future plans."),
    ],
    "test": [
        ("What does mine reconciliation compare?",
         [("a", "The colour of the mine office"), ("b", "The number of trucks in the car park"), ("c", "The salaries of two departments"), ("d", "Predicted tonnes and grade against what was mined and milled")], "d"),
        ("Where is grade control sampling done?",
         [("a", "In a far-away city"), ("b", "Close to the mining face, before the ore is dug"), ("c", "Inside the mill after processing"), ("d", "In the sky")], "b"),
        ("What is a bias in reconciliation?",
         [("a", "A gap that always points in the same direction"), ("b", "A gap that never happens"), ("c", "A gap caused by a sunny day"), ("d", "A gap that fixes itself")], "a"),
        ("How should a bias be corrected?",
         [("a", "At its source, such as the estimation method or the sampling"), ("b", "By ignoring it in every report"), ("c", "By changing the name of the mine"), ("d", "By mining faster only")], "a"),
        ("What should a reconciliation report state?",
         [("a", "Only the best month of the year"), ("b", "The name of the favourite tool"), ("c", "The size of each gap and what is being done about it"), ("d", "Nothing about the gaps")], "c"),
    ],
}
