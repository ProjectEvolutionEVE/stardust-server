"""Geocoding: Addresses to Coordinates. How an address becomes a point, how sure we can be, and why privacy matters."""
CODE = "navigation4_geocoding"
BOOK = {
    "title": "Geocoding: Addresses to Coordinates",
    "subtitle": "Turning a street address into a point on the map, and handling it with care",
    "chapters": [
        ("Address parts", "An address has parts: a house number, a street, a town and a postal code. Each part helps the software narrow the search. A missing or misspelled part can send the match somewhere else."),
        ("Matching", "Geocoding compares the address with reference data, such as a list of address points or a street network. The best match gives a coordinate. Several close matches may need a person to choose."),
        ("Reference data", "The quality of a geocoder depends on its reference data. Old or incomplete data gives weaker matches. New streets and new houses may not appear at all."),
        ("Confidence", "Most geocoders report a confidence score with each result. A high score means a close, clear match. A low score means the point should be checked before anyone relies on it."),
        ("Errors", "Common errors include mixed-up street names, ambiguous towns and rural addresses placed at the road. A point can also land at the centre of a large parcel. Checking results against a map helps catch these."),
        ("Privacy", "An address is personal information. Store only what you need, and protect it. Do not share addresses in ways that could identify a person who did not agree."),
    ],
    "test": [
        ("What is geocoding?", [("a", "Turning an address into a coordinate"), ("b", "Painting a map in colour"), ("c", "Counting the people in a town"), ("d", "Printing a timetable")], "a"),
        ("Which of these is an address part?", [("a", "A colour scheme"), ("b", "A sound file"), ("c", "A house number"), ("d", "A data cable")], "c"),
        ("What does a high confidence score mean?", [("a", "The address is wrong"), ("b", "The match is close and clear"), ("c", "The map is out of date"), ("d", "The result is hidden")], "b"),
        ("What reference data does a geocoder compare against?", [("a", "A cookbook"), ("b", "A list of songs"), ("c", "A weather report"), ("d", "Address points or a street network")], "d"),
        ("Why should addresses be handled with care?", [("a", "They are always wrong"), ("b", "They never change"), ("c", "They are only numbers"), ("d", "They are personal information")], "d"),
    ],
}
