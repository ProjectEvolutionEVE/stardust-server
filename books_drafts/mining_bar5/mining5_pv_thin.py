"""Thin-Film Photovoltaics: cadmium telluride and CIGS solar layers, the rare metals they rely on, and why recycling matters."""
CODE = "mining5_pv_thin"
BOOK = {
    "title": "Thin-Film Photovoltaics: CdTe and CIGS",
    "subtitle": "Solar layers a few micrometres thick, and the metals they need",
    "chapters": [
        ("Thin layers, less material", "Thin-film solar cells put a semiconductor only a few micrometres thick onto glass or metal. They use far less material than silicon wafers and can be made on large areas."),
        ("Cadmium telluride", "Cadmium telluride, or CdTe, is a thin-film absorber with a band gap that suits sunlight well. It is made in large volumes and is one of the most widely sold thin-film technologies."),
        ("CIGS", "CIGS is a copper, indium, gallium and selenium compound. Its composition can be tuned to adjust the band gap. Lab cells reach efficiencies in the low twenties of percent."),
        ("Tellurium and indium", "Tellurium is a rare byproduct of copper refining. Indium is also limited, as seen in other applications. The supply of these metals shapes how much can be built."),
        ("Manufacturing", "Thin films are deposited by vapour and sputtering methods in large vacuum systems. Each layer must be even, and a single flaw can lower output."),
        ("Recycling", "Makers and governments plan to recover the metals from end-of-life modules. Recycling reduces the need for new mining and keeps valuable metals in use."),
    ],
    "test": [
        ("How thick is a thin-film absorber layer?",
         [("a", "A few metres"), ("b", "A few kilometres"), ("c", "A few micrometres"), ("d", "A few centimetres of paper")], "c"),
        ("What does CdTe stand for?",
         [("a", "Cadmium telluride"), ("b", "Carbon dioxide tin"), ("c", "Copper dust titanium"), ("d", "Cobalt diesel tin")], "a"),
        ("What metals make up CIGS?",
         [("a", "Gold and silver only"), ("b", "Iron and lead only"), ("c", "Zinc and sugar"), ("d", "Copper, indium, gallium and selenium")], "d"),
        ("Where does tellurium mainly come from?",
         [("a", "From the surface of the moon"), ("b", "As a rare byproduct of copper refining"), ("c", "From salt mines only"), ("d", "From rain water")], "b"),
        ("Why is recycling thin-film modules valuable?",
         [("a", "It makes the modules heavier"), ("b", "It makes them blue"), ("c", "It removes all light"), ("d", "It recovers scarce metals and reduces new mining")], "d"),
    ],
}
