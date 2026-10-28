"""Software Supply Chain Security: build provenance, signed artefacts, dependency pinning, compromised build systems, verifying third-party code, and industry frameworks."""
CODE = "computing4_supply_chain"
BOOK = {
    "title": "Software Supply Chain Security",
    "subtitle": "Trusting what goes into the software you ship or run",
    "chapters": [
        ("Build provenance",
         "Provenance is the record of how a piece of software was built: the source used, the builder, and the steps taken. It lets users check what went into the file they received."),
        ("Signed artefacts",
         "Signing ties a software file to its publisher. Users check the signature before they trust a download."),
        ("Dependency pinning",
         "Pinning fixes each dependency to a known version, so that an update cannot slip in unnoticed. Lock files are the usual tool for this."),
        ("Compromised build systems",
         "An attacker who controls the build can insert code that never appears in the source. Hardened and isolated build machines reduce this risk."),
        ("Verifying third-party code",
         "Teams review new dependencies before adopting them, check their maintainers and their history, and watch for unexpected changes."),
        ("Industry frameworks",
         "Frameworks such as SLSA, and guidance from NIST, set out levels and practices for improving supply chain security."),
    ],
    "test": [
        ("What does build provenance record?",
         [("a", "Who ate lunch"), ("b", "The weather"), ("c", "How an artefact was built"), ("d", "Colour")], "c"),
        ("What does signing do?",
         [("a", "Binds an artefact to its publisher"), ("b", "Makes files bigger"), ("c", "Deletes files"), ("d", "Plays sound")], "a"),
        ("What does pinning prevent?",
         [("a", "Downloads"), ("b", "Coding"), ("c", "Unexpected updates to a dependency"), ("d", "Sleep")], "c"),
        ("Why is a compromised build dangerous?",
         [("a", "It can insert code that the source does not show"), ("b", "It is always slow"), ("c", "It makes coffee"), ("d", "It never runs")], "a"),
        ("Which of these is a supply chain framework?",
         [("a", "Morse"), ("b", "Tarot"), ("c", "Origami"), ("d", "SLSA")], "d"),
    ],
}
