"""Electrifying Mine Power Supply: bringing grid power to a mine, with substations, harmonics, redundancy and the path away from diesel."""
CODE = "mining5_electrify"
BOOK = {
    "title": "Electrifying Mine Power Supply",
    "subtitle": "Substations, grid links, harmonics, redundancy and planning",
    "chapters": [
        ("Power for the whole site",
         "A mine uses a lot of power for drills, pumps, ventilation and processing. Many remote mines still run on diesel generators. Bringing in grid power can cut running costs and emissions."),
        ("Substations",
         "A substation steps the voltage down to levels that equipment can use. It also protects the network with switchgear. Each substation must be sized for the full load of the site, including future growth."),
        ("Grid links",
         "A grid link is the line that connects the mine to the public network. Its capacity, reliability and cost depend on the distance and the local grid. Early talks with the utility are important."),
        ("Harmonics",
         "Large drives and rectifiers can distort the electrical waveform. This distortion is called harmonics, and it can heat equipment and disturb sensitive gear. Filters and careful design keep harmonics within limits."),
        ("Redundancy",
         "A mine cannot stop when the power fails, because pumps and ventilation must keep running. Redundant lines, transformers and backup generators keep critical loads alive. The level of backup should match the risk."),
        ("Planning",
         "Electrification is planned in stages, with diesel displaced step by step. Each stage is checked for cost and reliability. Good planning means the lights stay on through the change."),
    ],
    "test": [
        ("What does a substation do?",
         [("a", "It grows crops"), ("b", "It stores rock samples"), ("c", "It steps voltage down to levels equipment can use"), ("d", "It makes music")], "c"),
        ("What is a grid link?",
         [("a", "A chain on a fence"), ("b", "A link in a report"), ("c", "A hyperlink on a website"), ("d", "The line that connects the mine to the public network")], "d"),
        ("What are harmonics in a power supply?",
         [("a", "Musical notes from the generator"), ("b", "Distortion of the electrical waveform"), ("c", "Extra water in the cables"), ("d", "A type of diesel")], "b"),
        ("Why does a mine need redundancy in power?",
         [("a", "Pumps and ventilation must keep running when power fails"), ("b", "So the mine can stop more often"), ("c", "So the lights are brighter"), ("d", "So the grid is cheaper")], "a"),
        ("How is electrification usually planned?",
         [("a", "In stages, with diesel displaced step by step"), ("b", "All at once with no checks"), ("c", "By switching off all power at once"), ("d", "By asking the cook")], "a"),
    ],
}
