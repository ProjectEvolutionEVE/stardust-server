"""Foams and cellular materials: open and closed cells, density scaling, energy absorption, packaging foam and cell shape."""
CODE = "engineering4_cellular"
BOOK = {
    "title": "Foams and Cellular Materials",
    "subtitle": "Open and closed cells, density and energy absorption",
    "chapters": [
        ("Cells inside a solid",
         "A cellular material is a solid full of small cells, like a sponge or a honeycomb. Much of its volume is gas inside the cells. This makes it very light for its size."),
        ("Open and closed cells",
         "In open-cell foam the cell walls are broken or missing, so gas flows through connected pores. In closed-cell foam each cell is sealed off from its neighbours. Closed cells help keep water out, while open cells let air and water pass."),
        ("Density scaling",
         "As density rises, a cellular material becomes stiffer and stronger. The relation is often close to a power law of density."),
        ("Energy absorption",
         "Foams absorb energy by crushing in a steady way at a nearly constant stress. This makes them useful for crash pads and impact protection. A foam that crushes too early or too late gives poor protection."),
        ("Packaging foam",
         "Packaging foam protects goods by crushing to absorb a drop or a bump. The right density and thickness depend on the weight of the goods and the drop height. Packaging engineers test the foam against the expected impacts."),
        ("How cell shape sets stiffness",
         "The shape of the cells sets how stiff the material is in each direction. Regular honeycomb cells are stiff in their plane, and random foam cells are more even in all directions. Changing cell shape is one way to tune a material."),
    ],
    "test": [
        ("What is a closed-cell foam?", [("a", "A foam that is always liquid"), ("b", "A foam with no gas in it"), ("c", "A foam made of metal bars"), ("d", "A foam whose cells are sealed off from each other")], "d"),
        ("What happens to a cellular material as its density rises?", [("a", "It becomes weightless"), ("b", "It becomes stiffer and stronger"), ("c", "It turns into gas"), ("d", "It stops carrying any load")], "b"),
        ("Why are foams useful for crash pads?", [("a", "They are very hard and never crush"), ("b", "They bounce the energy back at full strength"), ("c", "They absorb energy by crushing at a nearly steady stress"), ("d", "They cannot absorb anything")], "c"),
        ("What is packaging foam designed to do?", [("a", "Melt in transit"), ("b", "Stop goods from being packed"), ("c", "Crush to absorb the drops and bumps that goods receive"), ("d", "Keep goods frozen")], "c"),
        ("How does cell shape affect a material?", [("a", "It sets how stiff the material is in each direction"), ("b", "It changes only the colour"), ("c", "It has no effect at all"), ("d", "It makes the material heavier by a set amount")], "a"),
    ],
}
