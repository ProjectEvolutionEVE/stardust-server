"""Monoliths, Modular Monoliths and Microservices: deployment units, module boundaries, team size and coupling, data ownership, the costs of distribution, and choosing a shape."""
CODE = "computing4_monolith_micro"
BOOK = {
    "title": "Monoliths, Modular Monoliths and Microservices",
    "subtitle": "Choosing how to split a system, and what each choice costs",
    "chapters": [
        ("Deployment units",
         "A monolith ships as one deployment unit. Microservices ship as many separate units, and each one owns a part of the system."),
        ("Module boundaries",
         "A modular monolith keeps clear modules inside one deployable unit. The boundaries in the code are real, so a later split is easier."),
        ("Team size and coupling",
         "Splitting work between teams works best when each service can change without asking others. If services are tightly coupled, they behave like one monolith with a network in the middle."),
        ("Data ownership",
         "Each service should own its data. A shared database ties services together, and it makes every change to it risky."),
        ("The costs of distribution",
         "Distributed systems add network calls, new ways to fail, more monitoring, versioning and operations work. These cost time and money."),
        ("Choosing a shape",
         "Many teams start with a well-structured monolith. They split off a part only when there is a clear reason, such as a need to scale it or a boundary between teams."),
    ],
    "test": [
        ("How does a monolith ship?",
         [("a", "As many unrelated pieces"), ("b", "As a poem"), ("c", "Never"), ("d", "As one deployment unit")], "d"),
        ("What does a modular monolith keep?",
         [("a", "Clear modules inside one unit"), ("b", "No structure at all"), ("c", "A separate database for each function"), ("d", "Only pictures")], "a"),
        ("Why should services own their data?",
         [("a", "A shared database ties services together"), ("b", "Data is free"), ("c", "Data is never used"), ("d", "Data is for sales")], "a"),
        ("What do distributed systems add?",
         [("a", "Network calls, failure modes and operations work"), ("b", "Less work"), ("c", "Fewer failures"), ("d", "Free coffee")], "a"),
        ("When should a team split off a part?",
         [("a", "Always"), ("b", "When there is a clear reason, such as scaling or a team boundary"), ("c", "Never"), ("d", "At random")], "b"),
    ],
}
