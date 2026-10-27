"""Injection Moulding: Plastic Parts at Scale. The moulding cycle, the mould, and the cost of a shot."""
CODE = 'engineering4_injection_mould'
BOOK = {
    "title": "Injection Moulding: Plastic Parts at Scale",
    "subtitle": "The moulding cycle, the mould, and the cost per shot",
    "chapters": [
        ("The moulding cycle",
         "Plastic pellets melt in a heated barrel. A screw pushes the melt into a closed mould, where it cools and sets. The mould then opens, the part is ejected, and the cycle starts again."),
        ("Mould design",
         "The mould is usually two steel halves with channels for cooling water. Its design sets the shape of the part, where the two halves meet, and how the finished part comes out."),
        ("Gates",
         "The gate is the small opening where melt enters the cavity. Its position affects how the melt flows, how the part looks, and where a mark is left. Gates are placed with care."),
        ("Cooling time",
         "Cooling is often the longest part of the cycle. Thick sections take longer to cool, so good design keeps walls about the same thickness. Shorter cooling means more parts per hour."),
        ("Shrinkage",
         "Plastic shrinks as it cools, so the mould cavity is made a little larger than the finished part. The amount of shrinkage differs between plastics, and the designer must allow for it."),
        ("Cost per shot and payback",
         "A steel mould costs a lot to make, but each shot is cheap. The mould pays back once enough parts have been made to cover its cost. Planned volume decides whether the mould is worth it."),
    ],
    "test": [
        ("Where does the plastic melt before it is injected?",
         [("a", "Inside the mould cavity"), ("b", "In a heated barrel"), ("c", "In the cooling channels"), ("d", "On the ejector pin")], "b"),
        ("What is the gate?",
         [("a", "The door to the factory"), ("b", "The cooling water pipe"), ("c", "The ejector pin"), ("d", "The small opening where melt enters the cavity")], "d"),
        ("Why is the mould cavity made slightly larger than the finished part?",
         [("a", "Plastic shrinks as it cools"), ("b", "Plastic grows when heated"), ("c", "The part is sanded later"), ("d", "The mould wears down")], "a"),
        ("What often sets the length of a moulding cycle?",
         [("a", "The time to open the door"), ("b", "The time paint takes to dry"), ("c", "Cooling time"), ("d", "The time to print a label")], "c"),
        ("When does a steel mould usually pay back its cost?",
         [("a", "On the first shot"), ("b", "Once enough parts are made to cover its cost"), ("c", "Never"), ("d", "Only after it is scrapped")], "b"),
    ],
}
