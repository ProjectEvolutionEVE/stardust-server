"""Living Reviews and Evidence Updating: continuous evidence updates, updating thresholds, version control, evidence grading, decision triggers and communicating changes."""
CODE = "science5_method_living"
BOOK = {
    "title": "Living Reviews and Evidence Updating",
    "subtitle": "Keeping a review current as new evidence arrives",
    "chapters": [
        ("What a living review is",
         "A living review is a systematic review that is updated as new evidence appears, rather than written once and left. It suits fast-moving fields where waiting years for a new review is unhelpful. The review stays useful for as long as it is maintained."),
        ("Updating thresholds",
         "An updating threshold is the point at which new evidence is strong enough to change the review. Set it in advance, so that updates are not driven by whichever result arrives last. Thresholds guard against overreacting to a single study."),
        ("Version control",
         "Version control records each update, with its date and reason. Readers can see what changed and why. A living review without version records is hard to trust."),
        ("Evidence grading",
         "Evidence grading ranks the strength of the evidence behind a conclusion, such as how well designed the studies are. Grades can change as new studies arrive. Show the grade next to each conclusion."),
        ("Decision triggers",
         "A decision trigger is a rule that says when a finding should lead to action, such as a change in guidance. Triggers link the review to the decisions it informs. Agree them with the people who will act on them."),
        ("Communicating changes",
         "When a conclusion changes, say so clearly. Explain what new evidence caused it and how confident the team is. Clear communication keeps users from being confused by reversals."),
    ],
    "test": [
        ("What is a living review?",
         [("a", "A review that is written once and never changed"), ("b", "A review updated as new evidence appears"), ("c", "A review written by robots only"), ("d", "A review kept in a drawer")], "b"),
        ("Why set an updating threshold in advance?",
         [("a", "So the review can be as long as possible"), ("b", "So the lab can avoid all changes"), ("c", "So updates are not driven by whichever result arrives last"), ("d", "So the sponsor can choose the result")], "c"),
        ("What does version control record?",
         [("a", "The price of the printer"), ("b", "The lab's holiday rota"), ("c", "The colour of the cover"), ("d", "Each update, with its date and reason")], "d"),
        ("What is evidence grading?",
         [("a", "Ranking the strength of the evidence behind a conclusion"), ("b", "Marking the students' exams"), ("c", "Sorting samples by size"), ("d", "Setting the price of a study")], "a"),
        ("What is a decision trigger?",
         [("a", "A rule that says when a finding should lead to action"), ("b", "A lab gun"), ("c", "A type of microscope lens"), ("d", "A journal's membership form")], "a"),
    ],
}
