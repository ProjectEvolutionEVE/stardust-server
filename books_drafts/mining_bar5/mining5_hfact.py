"""Human Factors in Major Hazards: error types, fatigue, interface design, procedures, training and audit."""
CODE = 'mining5_hfact'
BOOK = {
    "title": "Human Factors in Major Hazards",
    "subtitle": "Error types, fatigue, interface design, procedures and audit",
    "chapters": [
        ("People inside the system",
         "Human factors is the study of how people perform in their work and where they go wrong. In major hazard sites, one slip can have large effects. Designing for people is part of designing for safety."),
        ("Types of error",
         "Slips happen when a person does the right thing in the wrong way, such as pressing the wrong button. Mistakes happen when the plan itself is wrong. Violations happen when a rule is broken on purpose. Each type needs a different fix."),
        ("Fatigue",
         "Fatigue slows reactions, weakens judgment and makes slips more likely. Long shifts and poor rest raise the risk, even for skilled workers. Rosters should allow enough rest, and workers should be able to say when they are too tired."),
        ("Interface design",
         "An interface is any point where a person meets a control, a screen or a sign. Clear layouts, obvious labels and sensible defaults reduce errors. A control that is easy to confuse with another is a hazard waiting to happen."),
        ("Procedures and training",
         "Procedures set out how a task should be done. They work best when they are short, tested on site and written for the people who use them. Training builds the skill, and practice keeps it fresh."),
        ("Auditing the human side",
         "An audit checks whether the human factors controls are working in practice. Watch the job, talk to the workers, and compare what happens with what is written. Gaps found early are cheaper to fix than gaps found after an incident."),
    ],
    "test": [
        ("What is a slip?",
         [("a", "A right plan carried out in the wrong way"), ("b", "A deliberate breach of a rule"), ("c", "A planned shift change"), ("d", "A correct action with no result")], "a"),
        ("What is a violation?",
         [("a", "A slip of the tongue"), ("b", "A fire drill"), ("c", "A rule broken on purpose"), ("d", "A repair done in daylight")], "c"),
        ("How does fatigue affect a worker?",
         [("a", "It sharpens judgment"), ("b", "It slows reactions and makes slips more likely"), ("c", "It has no effect on skilled people"), ("d", "It speeds up every task")], "b"),
        ("What makes an interface safer?",
         [("a", "Controls that look alike"), ("b", "Hiding the controls behind other equipment"), ("c", "Removing every label"), ("d", "Clear labels and layouts that are hard to confuse")], "d"),
        ("Why should procedures be tested on site?",
         [("a", "So they match how the work is really done"), ("b", "So they are longer"), ("c", "So they can be sold"), ("d", "So no training is needed")], "a"),
    ],
}
