"""Secure Software Development Lifecycle: security in requirements, design reviews, secure coding standards, security testing gates, release sign-off, and training developers."""
CODE = "computing4_secure_sdlc"
BOOK = {
    "title": "Secure Software Development Lifecycle",
    "subtitle": "Building security into every stage of making software",
    "chapters": [
        ("Security in requirements",
         "Security needs are written down with the other requirements from the start. They cover who may see what, how data is protected, and how long it is kept."),
        ("Design reviews",
         "Before building begins, the team reviews the design for weak points. Threat models and checklists help the review find problems while they are still cheap to fix."),
        ("Secure coding standards",
         "The team agrees on rules for checking input, using safe libraries, and handling secrets. Shared rules prevent the common mistakes from being repeated."),
        ("Security testing gates",
         "Automated checks, such as static analysis, dependency scans and security tests, run before code can ship. A failed check stops the release until the problem is fixed."),
        ("Release sign-off",
         "Before a release, someone who is accountable confirms that the known risks are either fixed or accepted. This keeps those decisions visible."),
        ("Training developers",
         "Developers learn the common flaws and how to avoid them. Short, practical training that uses the team's own code works best."),
    ],
    "test": [
        ("When are security needs written down?",
         [("a", "At the start, with the other requirements"), ("b", "After launch only"), ("c", "Never"), ("d", "In a poem")], "a"),
        ("What is a security testing gate?",
         [("a", "A garden gate"), ("b", "A password"), ("c", "An automated check that must pass before release"), ("d", "A user")], "c"),
        ("Why hold a release sign-off?",
         [("a", "To pick colours"), ("b", "To delay lunch"), ("c", "So that known risks are fixed or accepted by someone accountable"), ("d", "It is never needed")], "c"),
        ("What do design reviews look for?",
         [("a", "Weak points before building"), ("b", "Typos in logos"), ("c", "Music"), ("d", "Menus")], "a"),
        ("What kind of training works best?",
         [("a", "Never"), ("b", "Short and practical, using the team's own code"), ("c", "Long and boring"), ("d", "Only in colour")], "b"),
    ],
}
