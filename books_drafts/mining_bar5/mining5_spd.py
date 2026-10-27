"""Severe Plastic Deformation: forcing metal through a bent die to refine its grains without changing its shape."""
CODE = "mining5_spd"
BOOK = {
    "title": "Severe Plastic Deformation",
    "subtitle": "Refining grains by shearing metal without changing its size",
    "chapters": [
        ("Heavy working without shape change", "Severe plastic deformation means working a metal very hard so its grains break down into much finer ones. The sample keeps the same overall shape, so the process is different from ordinary rolling or forging."),
        ("Equal channel angular pressing", "In the best known method, a bar is pushed through a die with two channels of equal cross section that meet at an angle. The bar is sheared at the bend, then pushed again, and the grains are broken into finer pieces each pass."),
        ("Ultrafine grains", "After several passes the grains can be less than a micrometre across. This gives the metal much higher strength than it had before."),
        ("Strength and ductility", "The strength gain can be large. Some ductility is lost, though, and the metal must be handled carefully afterwards. Engineers balance the two."),
        ("Scale problems", "Most methods work on small samples, such as a short bar. Making long sheets or large parts this way is harder and costs more. So the process is used for special parts."),
        ("Where it is used", "Medical implants, specialist fasteners and research samples are some uses. The method shows how much a metal can change when its internal structure is reshaped on purpose."),
    ],
    "test": [
        ("What does severe plastic deformation keep the same?",
         [("a", "The overall shape of the sample"), ("b", "The colour of the metal"), ("c", "The melting point of the metal"), ("d", "The weight of the metal in air")], "a"),
        ("What is the best known method in this family?",
         [("a", "Pouring into sand"), ("b", "Boiling in acid"), ("c", "Equal channel angular pressing"), ("d", "Painting the surface")], "c"),
        ("About how big are the grains after several passes?",
         [("a", "Several metres"), ("b", "Less than a micrometre"), ("c", "Visible to the eye as large stones"), ("d", "Bigger than the sample")], "b"),
        ("What is a main limit of the method?",
         [("a", "It works only on gold"), ("b", "It makes metal melt"), ("c", "It needs no tools at all"), ("d", "It is hard and costly to scale up to long sheets or large parts")], "d"),
        ("What is lost as strength rises?",
         [("a", "The shape of the sample"), ("b", "Some ductility"), ("c", "The metal itself"), ("d", "The colour of the metal")], "b"),
    ],
}
