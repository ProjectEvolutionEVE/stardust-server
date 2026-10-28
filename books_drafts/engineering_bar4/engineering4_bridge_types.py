"""Bridge types: beams, arches, trusses and cables, with load paths, span ranges, bearings and cost per metre."""
CODE = "engineering4_bridge_types"
BOOK = {
    "title": "Bridge Types: Beams, Arches, Trusses and Cables",
    "subtitle": "Span ranges, load paths and how bridges carry their weight",
    "chapters": [
        ("Following the load",
         "Every bridge carries its deck load along a load path to the supports. Some bridges carry the load by bending a beam, others by squeezing an arch or pulling on cables. The shape of the bridge tells you how it moves the load."),
        ("Span ranges",
         "Beams suit short spans, trusses cover medium spans, and arches and cable systems reach much longer distances. Each type has a range where it is the most sensible choice. Span length is one of the first things a designer decides."),
        ("Cable-stayed against suspension",
         "A cable-stayed bridge hangs its deck from straight cables fixed to towers. A suspension bridge drapes a main cable between towers, and hangers carry the deck. Both use cables in tension, but they spread the load differently."),
        ("Arch thrust",
         "An arch pushes sideways on its supports as well as down. This sideways push, called thrust, must be held by strong abutments or a tie. Designers check the thrust before they choose the foundations."),
        ("Deck and bearings",
         "The deck carries the traffic and is held up by the main structure. Bearings sit between the deck and the supports, letting the deck expand, contract and turn slightly. Bearings must be replaced over a bridge's life, so they are designed to be reached."),
        ("Cost per metre of span",
         "Bridge cost is often given per metre of span, but a longer bridge costs far more per metre because the towers, cables and foundations grow. The type chosen balances material, construction method and the length of the crossing."),
    ],
    "test": [
        ("What is a load path?", [("a", "The way the load travels from the deck down to the supports"), ("b", "A walking route across the bridge"), ("c", "A painted line on the road"), ("d", "The list of bridge workers")], "a"),
        ("Which bridge type usually suits the longest spans?", [("a", "A short beam"), ("b", "A small timber footbridge"), ("c", "A paved ditch"), ("d", "A cable system")], "d"),
        ("How does a suspension bridge carry its deck?", [("a", "By being sunk into the ground"), ("b", "By a main cable draped between towers, with hangers holding the deck"), ("c", "By floating on water"), ("d", "By painted supports only")], "b"),
        ("What is arch thrust?", [("a", "The speed of traffic"), ("b", "The noise from the deck"), ("c", "The sideways push an arch puts on its supports"), ("d", "Rain falling on the arch")], "c"),
        ("What do bearings do on a bridge?", [("a", "Store the traffic lights"), ("b", "Make the deck heavier"), ("c", "Let the deck expand, contract and turn slightly"), ("d", "Replace the cables")], "c"),
    ],
}
