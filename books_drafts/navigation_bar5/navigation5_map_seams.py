"""Seams and Hemisphere Splits: where a whole-world map must be cut, and how to keep the data whole across the cut."""
CODE = "navigation5_map_seams"
BOOK = {
    "title": "Seams and Hemisphere Splits",
    "subtitle": "Where the cut goes, and how to keep features whole",
    "chapters": [
        ("The seam problem", "A projection that covers the whole globe must be cut somewhere, or it stretches. The cut makes a seam, where the edges of the map do not match."),
        ("Polar caps", "Many cylindrical and conic maps need separate maps for the north and south polar caps. The caps are drawn apart and joined at a set boundary."),
        ("Cut lines", "Where possible, a cut line passes through open ocean or sparse land. A good choice splits as few features as it can."),
        ("Continuity", "When a feature crosses a seam, the software must keep its shape and attributes continuous. Otherwise a road or river appears broken at the edge."),
        ("Handling data", "Data that cross a cut must be duplicated, clipped and rejoined with care. Tests check that nothing is lost or counted twice."),
        ("Design", "The designer decides where the seams fall and how they look. A clear label on the cut helps readers understand the map."),
    ],
    "test": [
        ("Why does a whole-globe map need a seam?",
         [("a", "The paper is round"), ("b", "The sea is salty"), ("c", "The Earth is hollow"), ("d", "A flat map cannot show the whole sphere without a cut or stretching")], "d"),
        ("What is a polar cap map?",
         [("a", "A separate map drawn for a pole"), ("b", "A map of hats"), ("c", "A map of clouds"), ("d", "A map of rivers in winter")], "a"),
        ("Where should a cut line ideally pass?",
         [("a", "Through the largest city"), ("b", "Through the middle of a mountain range"), ("c", "Through open ocean where possible"), ("d", "Through the North Pole only")], "c"),
        ("What must software keep continuous across a seam?",
         [("a", "The map's title"), ("b", "The shape and attributes of a feature"), ("c", "The paper size"), ("d", "The map's name")], "b"),
        ("What is a good check after handling data across a cut?",
         [("a", "Check that nothing is lost or doubled"), ("b", "Add a new colour"), ("c", "Print a poster"), ("d", "Delete the seam")], "a"),
    ],
}
