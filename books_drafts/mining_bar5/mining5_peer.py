"""Peer Review of Technical Reports: how independent experts check a technical report before people rely on it."""
CODE = "mining5_peer"
BOOK = {
    "title": "Peer Review of Technical Reports",
    "subtitle": "Review roles, checklists, independence and trust",
    "chapters": [
        ("Why a second look matters",
         "A technical report can shape a large investment and many lives. A second expert reads it before it is trusted. This is called peer review, and it catches errors the author may not see."),
        ("Review roles",
         "A reviewer may check the data, the method, the maths or the conclusions. Some reviewers look at the whole report, and others check one part. Clear roles mean nothing is missed."),
        ("Checklists",
         "A checklist lists the things that must be true: sources named, units stated, uncertainty shown. Working through the same list each time makes reviews more consistent. A checklist does not replace judgement, but it supports it."),
        ("Independence",
         "A reviewer should have no stake in the outcome of the report. If they worked on the project, or are paid by its owner, the review may not be fair. Independence is what makes the review believable."),
        ("Errors found",
         "Reviews often find wrong units, missing data, and conclusions that go further than the evidence. Finding these early is cheaper than fixing them after a decision. Errors found should be recorded, with what was done about them."),
        ("Reports and trust",
         "A report that has been reviewed is more trusted, but only if the review is honest and the reviewer's name is shown. Readers judge a report partly by how it was checked. Trust is built by many honest reviews over time."),
    ],
    "test": [
        ("What is the purpose of peer review of a technical report?",
         [("a", "To make the report longer"), ("b", "To have a second expert catch errors before the report is trusted"), ("c", "To hide the author's name"), ("d", "To print the report in colour")], "b"),
        ("What is a checklist useful for in review?",
         [("a", "Making reviews more consistent, by stating what must be true"), ("b", "Replacing all judgement"), ("c", "Hiding errors"), ("d", "Counting the pages")], "a"),
        ("Why does a reviewer need independence?",
         [("a", "So the review is fair and not tied to the outcome"), ("b", "So the reviewer can skip the data"), ("c", "So the reviewer can be paid twice"), ("d", "So the report is shorter")], "a"),
        ("Why is an error found in review cheaper to fix than one found later?",
         [("a", "Because errors never cost anything"), ("b", "Because the report is thrown away"), ("c", "Because it is caught before a decision is made on it"), ("d", "Because nobody reads the report")], "c"),
        ("What makes a reviewed report more trusted?",
         [("a", "A cover in bright colours"), ("b", "A missing reference list"), ("c", "A review done by the author alone"), ("d", "An honest review with the reviewer's name shown")], "d"),
    ],
}
