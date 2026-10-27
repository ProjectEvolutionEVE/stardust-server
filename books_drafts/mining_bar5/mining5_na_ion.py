"""Sodium-Ion Battery Materials: batteries that use abundant sodium instead of lithium, their trade-offs, and their roles."""
CODE = "mining5_na_ion"
BOOK = {
    "title": "Sodium-Ion Battery Materials",
    "subtitle": "Cheap, common sodium in place of lithium, with trade-offs",
    "chapters": [
        ("Why sodium", "Sodium is far more common in the Earth's crust than lithium, and it is cheap to mine and process. A sodium-ion battery uses sodium ions in place of lithium ions, with a similar design."),
        ("Cathodes", "Sodium-ion cathodes are often layered oxides or Prussian white type compounds. They store sodium ions in their structure as the cell charges and discharges."),
        ("Hard carbon anodes", "Sodium does not fit well into ordinary graphite, so the anode is often hard carbon. Its disordered structure has spaces that hold sodium ions."),
        ("Energy density", "Sodium-ion cells usually store less energy per kilogram than lithium cells. This makes them less suited to heavy electric cars, though they are attractive for other uses."),
        ("Cycling", "The cells must keep working over many charge cycles. Makers choose materials that resist cracking and keep their structure stable as sodium moves in and out."),
        ("Where they fit", "Sodium-ion batteries suit grid storage, cheap portable power and situations where cost matters more than the smallest size. They add choice to the wider battery market."),
    ],
    "test": [
        ("Why is sodium attractive for batteries?",
         [("a", "It is common and cheap"), ("b", "It is very rare"), ("c", "It is a liquid at room temperature"), ("d", "It is made of gold")], "a"),
        ("What is often used as the anode in sodium-ion cells?",
         [("a", "Solid ice"), ("b", "Clear glass"), ("c", "Hard carbon"), ("d", "Cotton wool")], "c"),
        ("What is the usual trade-off of sodium-ion cells?",
         [("a", "They cost a fortune"), ("b", "Less energy stored per kilogram"), ("c", "They never charge"), ("d", "They are made of wood")], "b"),
        ("Which kind of use suits sodium-ion batteries?",
         [("a", "Making bread"), ("b", "Growing trees"), ("c", "Printing paper"), ("d", "Grid storage")], "d"),
        ("What do cathodes do as the cell cycles?",
         [("a", "Turn into sugar"), ("b", "Store sodium ions in their structure"), ("c", "Glow red"), ("d", "Melt into sand")], "b"),
    ],
}
