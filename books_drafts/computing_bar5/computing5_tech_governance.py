"""Technology Governance Councils: who decides what, how exceptions are handled, and how fast decisions can move."""
CODE = "computing5_tech_governance"
BOOK = {
    "title": "Technology Governance Councils",
    "subtitle": "Who decides what, how exceptions are handled, and how fast decisions can move",
    "chapters": [
        ("Why governance",
         "Governance sets out how technology decisions are made. Without it, teams make conflicting choices and costs spiral. With too much of it, work stops. The aim is clear rules that let people act."),
        ("Decision rights",
         "Decision rights say who decides what, and they should be written down. When everyone knows the owner of each decision, questions get answered faster. Unclear rights cause delays and arguments."),
        ("Standards",
         "A standard is a shared rule most teams follow, such as a common security practice. Explain the reason behind each standard, so people follow it willingly. Review standards when the world changes."),
        ("Exceptions processes",
         "Sometimes a team needs to step outside a standard. A good exceptions process is a quick, written request with a clear reason. Each exception should have a time limit and a review date."),
        ("Architecture boards",
         "An architecture board reviews big, risky technical choices, not every small decision. Keep its membership small and its answers quick. Its job is to help teams succeed, not to act as a gate."),
        ("Speed versus control, and charters",
         "Too little control causes chaos, and too much stops work. Aim for light rules and quick answers. Write a short charter that states the council's purpose, members, decisions and meeting rhythm."),
    ],
    "test": [
        ("What are decision rights?",
         [("a", "Written rules for who decides what"), ("b", "Voting rights in elections"), ("c", "Rights to parking"), ("d", "Office keys")], "a"),
        ("What is an exceptions process for?",
         [("a", "Routine approval of everything"), ("b", "A written, time-limited way to ask for a deviation from a standard"), ("c", "Skipping all reviews"), ("d", "Hiding deviations")], "b"),
        ("What should an architecture board focus on?",
         [("a", "Office decor"), ("b", "Lunch"), ("c", "Every small line of code"), ("d", "Big, risky technical choices")], "d"),
        ("What balance does good governance aim for?",
         [("a", "Maximum control with no speed"), ("b", "No rules at all"), ("c", "Light rules with quick decisions"), ("d", "Rules nobody reads")], "c"),
        ("What should a governance charter state?",
         [("a", "Purpose, members, decisions and meeting rhythm"), ("b", "The lunch menu"), ("c", "A password"), ("d", "Staff salaries")], "a"),
    ],
}
