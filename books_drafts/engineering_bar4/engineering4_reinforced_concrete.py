"""Reinforced concrete: why concrete needs steel inside it, how cover protects the bars, and what a frame costs."""
CODE = "engineering4_reinforced_concrete"
BOOK = {
    "title": "Reinforced Concrete: Steel Inside Stone",
    "subtitle": "Tension zones, cover, cracking, curing and cost",
    "chapters": [
        ("Why steel goes inside",
         "Concrete is strong when it is squeezed, but weak when it is pulled. Steel bars are strong in tension, so they are placed where the concrete would be stretched. Together the two materials carry both squeezing and pulling loads."),
        ("Tension zones",
         "When a beam bends, one side is squeezed and the other side is stretched. Engineers place the steel on the stretched side, called the tension zone. Bars in the wrong place add weight and do little good."),
        ("Cover over the bars",
         "Cover is the layer of concrete between the outside face and the steel. It shields the steel from water and air, which can cause rust. Too little cover lets rust grow and push the concrete apart."),
        ("Cracking",
         "Concrete cracks, and that is normal, because its tensile strength is low. The steel keeps small cracks narrow and stops them opening up. Designers limit crack width so that water cannot reach the bars easily."),
        ("Curing",
         "Curing is keeping fresh concrete moist and at a steady temperature while it gains strength. Concrete that dries out too fast is weaker and cracks more. Good curing costs a little time and gives a longer-lasting frame."),
        ("Steel against concrete",
         "In a frame, steel is usually more expensive per tonne than concrete, but it allows slimmer members and longer spans. The right mix of the two is a trade between material cost, labour and the space the building needs."),
    ],
    "test": [
        ("Why is steel placed inside concrete?", [("a", "To make the concrete cheaper"), ("b", "Steel stops concrete from setting"), ("c", "To change the colour of the concrete"), ("d", "Concrete is weak in tension, and steel is strong in tension")], "d"),
        ("Where is the steel placed in a bending beam?", [("a", "On the squeezed side only"), ("b", "On the stretched side, the tension zone"), ("c", "In the middle of the concrete"), ("d", "Nowhere in the beam")], "b"),
        ("What is cover in reinforced concrete?", [("a", "The paint on the surface"), ("b", "The roof of the building"), ("c", "The concrete layer between the outside face and the steel"), ("d", "A type of formwork")], "c"),
        ("What does curing do?", [("a", "Dries the concrete out fast"), ("b", "Adds steel to the mix"), ("c", "Keeps fresh concrete moist and steady while it gains strength"), ("d", "Removes the cover")], "c"),
        ("Why is steel's cost weighed against concrete in a frame?", [("a", "Steel allows slimmer members and longer spans, so the mix is a trade"), ("b", "Steel never costs anything"), ("c", "Concrete is always more expensive"), ("d", "Frames use no materials")], "a"),
    ],
}
