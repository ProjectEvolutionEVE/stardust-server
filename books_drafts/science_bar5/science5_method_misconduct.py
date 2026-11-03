"""Detecting Scientific Misconduct and Data Forensics: statistical anomalies, image integrity checks, duplicate detection, investigation procedures, false accusations and reported outcomes."""
CODE = "science5_method_misconduct"
BOOK = {
    "title": "Detecting Scientific Misconduct and Data Forensics",
    "subtitle": "How honest labs check their own work, and how fair investigations proceed",
    "chapters": [
        ("What misconduct means",
         "Scientific misconduct includes fabricating data, falsifying results and plagiarising work. Honest mistakes are different, and they are corrected by openly fixing the record. Clear definitions help a lab tell the two apart."),
        ("Statistical anomalies",
         "Some patterns in data are unusual enough to deserve a closer look, such as results that are too uniform or too neat. An anomaly is a reason to check, not proof of wrongdoing. Ordinary explanations come first."),
        ("Image integrity checks",
         "Image checks look for duplicated regions, cropping or unexplained adjustments in figures and micrographs. Raw image files and their history are the best evidence. Labs should keep raw files for this reason."),
        ("Duplicate detection",
         "Duplicate detection looks for the same data, text or images appearing where they should not. Automated tools can scan large sets of papers. A match needs human review before any conclusion is drawn."),
        ("Investigation procedures",
         "A fair investigation has written steps, an independent panel, and a chance for the person involved to respond. Evidence is preserved, and decisions are recorded. Procedures protect both the field and the accused."),
        ("False accusations and reported outcomes",
         "A false accusation can ruin a career, so cases must be checked carefully before they are made public. Investigations should report their outcomes, including when the concern was not upheld. Honest closure matters as much as the finding."),
    ],
    "test": [
        ("Which of these is scientific misconduct?",
         [("a", "Fixing a typo in a published paper openly"), ("b", "Fabricating data and presenting it as real"), ("c", "Asking a colleague to check a figure"), ("d", "Keeping raw files for later review")], "b"),
        ("What is a statistical anomaly?",
         [("a", "A reason to check the data further, not proof of wrongdoing"), ("b", "A proof of fraud"), ("c", "A type of lab glass"), ("d", "A fixed rule for all studies")], "a"),
        ("Why do labs keep raw image files?",
         [("a", "To make the files bigger"), ("b", "To give the best evidence of how a figure was made"), ("c", "To avoid publishing"), ("d", "To store coffee recipes")], "b"),
        ("What is an important feature of a fair investigation?",
         [("a", "The accused is never allowed to respond"), ("b", "Evidence is destroyed after one day"), ("c", "Written steps, an independent panel and a chance to respond"), ("d", "Decisions are kept secret from everyone for ever")], "c"),
        ("Why must a false accusation be avoided?",
         [("a", "Because it can ruin a career unfairly"), ("b", "Because it makes the lab richer"), ("c", "Because it improves the data"), ("d", "Because it speeds up journals")], "a"),
    ],
}
