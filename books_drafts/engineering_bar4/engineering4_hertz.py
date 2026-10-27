"""Contact Stress: Hertz theory for point and line contact, peak pressure, subsurface stress and a hand check of a contact."""
CODE = "engineering4_hertz"
BOOK = {
    "title": "Contact Stress: Hertz Theory",
    "subtitle": "Point and line contact, peak pressure and subsurface stress",
    "chapters": [
        ("Point and line contact",
         "Two curved bodies touching at a point, like a ball on a plate, or along a line, like a roller in a race, carry their load through a small area. The shape of the two bodies sets how large the contact area is."),
        ("Peak pressure",
         "Hertz theory gives the peak pressure in that small area. The peak can be very high even under a modest load."),
        ("Subsurface stress",
         "In a rolling contact, the highest shear stress lies a little below the surface, not at it. This is why fatigue can start below the surface and form pits."),
        ("Ball and roller design",
         "Designers use contact stress to choose ball and roller sizes, their curvature and their materials. A small change in size or curve can change the peak stress a lot."),
        ("Checking a contact by hand",
         "A simple Hertz check uses the load, the curvatures and the elastic moduli to estimate the contact size and the peak pressure. Engineers do this before any detailed analysis."),
        ("Limits",
         "Hertz theory assumes smooth, elastic, small contacts. Rough surfaces and large loads need more detailed analysis."),
    ],
    "test": [
        ("What is point contact?",
         [("a", "Two curved bodies touching at a point"), ("b", "A paint"), ("c", "A sound"), ("d", "A bag")], "a"),
        ("Where is the highest shear stress in a rolling contact?",
         [("a", "At the surface"), ("b", "A little below the surface"), ("c", "In the air"), ("d", "Nowhere")], "b"),
        ("What does Hertz theory estimate?",
         [("a", "The colour"), ("b", "The sound"), ("c", "The weather"), ("d", "The peak pressure in a contact area")], "d"),
        ("Why does subsurface fatigue matter?",
         [("a", "It improves paint"), ("b", "It cools the air"), ("c", "It can start pitting"), ("d", "It adds sound")], "c"),
        ("What does Hertz theory assume?",
         [("a", "Smooth, elastic, small contacts"), ("b", "Rough and huge contacts"), ("c", "Painted and loud contacts"), ("d", "Random contacts")], "a"),
    ],
}
