"""The Shape of the Earth: why the Earth bulges at the middle, and the geoid that sea level follows."""
CODE = 'navigation3b_geoid'
BOOK = {
    "title": "The Shape of the Earth",
    "subtitle": "Why the Earth bulges, and the geoid that heights are measured from",
    "chapters": [
        ("Not quite a ball",
         "The Earth spins, and the spin makes it bulge around the middle. Measured through the poles, the Earth is a little flatter than a perfect ball. Scientists call this shape an oblate spheroid."),
        ("How big is the bulge",
         "The radius through the equator is about 6,378 km, and the radius through the poles is about 6,357 km. The difference of roughly 21 km is small next to the whole planet, but it is far too large to ignore in careful work."),
        ("The geoid",
         "The geoid is the surface that gravity keeps level everywhere. Water would settle onto it if the oceans could reach under the land. It is lumpy, because rock of different density pulls on gravity by different amounts. Mean sea level sits close to it."),
        ("Heights need a reference",
         "A hill's height is measured up from the geoid, not from a perfect sphere. Two maps that use different reference surfaces can disagree about how high a mountain is. Surveyors avoid this by agreeing on one reference and writing it down."),
        ("Why a navigator cares",
         "Over a short walk the curve hardly shows. Over a long flight or a large survey, the bulge and the lumps move where a straight line really ends up. Good maps build the true shape in, rather than treating the Earth as a simple ball."),
        ("The same thinking elsewhere",
         "Any body that spins takes a shape set by its spin and its mass. A mapmaker of another world starts the same way: work out the true shape first, then measure from it."),
    ],
    "test": [
        ("What is the shape of the Earth, more exactly?",
         [("a", "A perfect sphere"), ("b", "A flat disc"), ("c", "An oblate spheroid, a little flattened at the poles"), ("d", "A cube")], "c"),
        ("About how much bigger is the equatorial radius than the polar radius?",
         [("a", "About 21 km"), ("b", "About 210 km"), ("c", "About 2,100 km"), ("d", "About 21 metres")], "a"),
        ("What is the geoid?",
         [("a", "A kind of map projection"), ("b", "The surface that gravity keeps level, close to mean sea level"), ("c", "The line of the equator"), ("d", "A survey instrument")], "b"),
        ("Why can two maps with different reference surfaces disagree about a mountain's height?",
         [("a", "Because mountains grow every year"), ("b", "Because the paper shrinks"), ("c", "Because the Moon pulls the mountain up"), ("d", "Because they measure height up from different reference surfaces")], "d"),
        ("Why does the geoid have lumps?",
         [("a", "Because rock of different density pulls on gravity by different amounts"), ("b", "Because the Moon bites at it"), ("c", "Because of volcanoes only"), ("d", "Because water flows uphill")], "a"),
    ],
}
