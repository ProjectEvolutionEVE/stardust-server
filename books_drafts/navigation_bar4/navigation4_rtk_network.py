"""Networked RTK Corrections: positioning help from a network of reference stations."""
CODE = "navigation4_rtk_network"
BOOK = {
    "title": "Networked RTK Corrections",
    "subtitle": "Corrections from a network of reference stations",
    "chapters": [
        ("A network of reference stations", "Networked RTK uses many fixed reference stations spread over an area. Each station knows its exact position. Together they watch the satellites and measure the errors in the signals."),
        ("Interpolated corrections", "Corrections are estimated for places between the stations. The network models how the errors change across the area. A rover receives corrections suited to its own location."),
        ("The virtual reference station", "A virtual reference station is a made-up station near the rover. It is built from the nearby real stations. The rover then works as if it had a station close by."),
        ("The range of a correction", "A correction is useful only within a certain distance of the stations. The further the rover is from them, the less accurate the corrections become. The network sets the area it can serve."),
        ("Its limits", "Networked RTK is limited by the network's coverage and by the data link. Gaps in the network and poor sky views reduce accuracy. Good planning shows where the service works."),
        ("The data link", "The rover receives corrections over a data link, usually a mobile connection. If the link fails, the corrections stop. Reliable data links keep the survey working."),
    ],
    "test": [
        ("What does networked RTK use?",
         [("a", "A single tower"), ("b", "Many fixed reference stations"), ("c", "A balloon"), ("d", "A kite")], "b"),
        ("What do interpolated corrections cover?",
         [("a", "Only the stations themselves"), ("b", "The Sun"), ("c", "Places between the stations"), ("d", "The ocean floor")], "c"),
        ("What is a virtual reference station?",
         [("a", "A video game"), ("b", "A real station on the Moon"), ("c", "A paper map"), ("d", "A made-up station near the rover built from nearby real stations")], "d"),
        ("What happens to accuracy as the rover moves away from the stations?",
         [("a", "It usually gets worse"), ("b", "It gets better"), ("c", "It becomes exact"), ("d", "It disappears")], "a"),
        ("What carries the corrections to the rover?",
         [("a", "A pigeon"), ("b", "A printed book"), ("c", "A data link"), ("d", "The wind")], "c"),
    ],
}
