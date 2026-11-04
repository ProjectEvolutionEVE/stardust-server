"""Creep and High-Temperature Failure: the slow stretching of materials under steady load, and how engineers predict it."""
CODE = "science5_mat_creep"
BOOK = {
    "title": "Creep and High-Temperature Failure",
    "subtitle": "Why parts that hold for years can slowly stretch and fail",
    "chapters": [
        ("What creep is", "Creep is slow deformation under a steady load at high temperature. It can happen over months or years, even when the stress is below what would break the part quickly. Hot parts are most at risk."),
        ("Three stages", "A creep curve usually has three stages. In primary creep, the rate slows. In secondary creep, the rate is roughly steady. In tertiary creep, the rate speeds up toward failure."),
        ("The Norton law", "The Norton law is an empirical model. It says the steady creep rate rises with stress raised to a power. It is a simple tool for comparing materials and conditions."),
        ("Mechanisms", "At high temperature, atoms and dislocations can get past obstacles more easily. Diffusion lets atoms move, and dislocation climb lets dislocations step around barriers. These processes drive creep."),
        ("Rupture", "Eventually the material breaks. This final failure is called rupture. Rupture time depends on temperature, stress and the material."),
        ("Life prediction", "Engineers test at high temperature and stress to predict how long a part will last. Results are scaled and checked to guide design and inspection. Good prediction keeps turbines and boilers safe."),
    ],
    "test": [
        ("What is creep?",
         [("a", "Slow deformation under steady load at high temperature"), ("b", "Fast breaking at room temperature"), ("c", "A layer of rust"), ("d", "A cold weld")], "a"),
        ("How many classic stages of creep are usually described?",
         [("a", "One"), ("b", "Two"), ("c", "Four"), ("d", "Three")], "d"),
        ("What is the Norton law used for?",
         [("a", "Measuring light"), ("b", "Measuring sound"), ("c", "Describing how the steady creep rate depends on stress"), ("d", "Measuring weight")], "c"),
        ("What processes let atoms and dislocations get past obstacles in creep?",
         [("a", "Magnetism"), ("b", "Diffusion and dislocation climb"), ("c", "Lightning"), ("d", "Ice formation")], "b"),
        ("Why do engineers test at high temperature and stress?",
         [("a", "To make parts glow"), ("b", "To make parts cheaper"), ("c", "To predict how long parts will last"), ("d", "To remove paint")], "c"),
    ],
}
