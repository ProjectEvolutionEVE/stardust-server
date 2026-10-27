"""Engineered timber: grain direction, glued laminated beams, moisture, fire, connectors and the cost of wood."""
CODE = "engineering4_timber"
BOOK = {
    "title": "Engineered Timber: Laminated and Glued Wood",
    "subtitle": "Grain, glulam, moisture, fire and connectors",
    "chapters": [
        ("Wood follows its grain",
         "Wood is much stronger along the grain than across it. A timber member is best loaded in the direction its fibres run. Engineers check the grain direction before they trust a piece of wood."),
        ("Glued laminated beams",
         "Glued laminated timber, often called glulam, is made by gluing thin layers of wood together. The layers spread out the natural flaws, so the beam is more even and can be made much longer than a single log. Glulam can be curved into arches and large beams."),
        ("Moisture content",
         "Wood swells when it takes up water and shrinks when it dries. Its strength and stiffness change with moisture content. Designers set the moisture level in the design and keep the timber dry in service."),
        ("Fire behaviour",
         "Large timber sections char on the outside, and the charred layer slows the burning inside. A thick timber beam can keep much of its strength in a fire longer than an unprotected steel beam. Designers plan for this in the fire design."),
        ("Connectors",
         "Timber members are joined with bolts, nails, screws and metal plates. The joint is often the weakest part of a timber structure. Connector design needs as much care as the member itself."),
        ("The cost of timber",
         "The price of timber depends on species, grade, sourcing and transport. Certified and sustainably managed supply can cost more up front but may suit a project's rules. A builder weighs the price of the wood against the time and labour it saves."),
    ],
    "test": [
        ("Along which direction is wood strongest?", [("a", "Across the grain"), ("b", "Along the grain"), ("c", "At right angles to the rings only"), ("d", "Wood has no direction")], "b"),
        ("What is glulam?", [("a", "A type of paint"), ("b", "A metal bolt"), ("c", "Timber made by gluing thin layers of wood together"), ("d", "Wood that has never been dried")], "c"),
        ("What happens to wood when its moisture content changes?", [("a", "It turns to stone"), ("b", "Nothing changes at all"), ("c", "Its strength and stiffness can change"), ("d", "It becomes a metal")], "c"),
        ("How does a thick timber beam behave in a fire?", [("a", "Its outer char slows the burning and it keeps some strength"), ("b", "It burns through at once"), ("c", "It melts like glass"), ("d", "Fire has no effect on wood")], "a"),
        ("Why is the joint often a weak point in timber?", [("a", "Joints are always made of gold"), ("b", "Timber never needs joints"), ("c", "Joints add strength by themselves"), ("d", "Connectors and joints need careful design, and they can be the weakest part")], "d"),
    ],
}
