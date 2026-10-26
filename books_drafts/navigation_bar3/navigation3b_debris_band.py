"""Charting a Debris Band: surveying a ring of debris field by field, and keeping the map honest."""
CODE = 'navigation3b_debris_band'
BOOK = {
    "title": "Charting a Debris Band",
    "subtitle": "Surveying a ring of debris field by field, and keeping the map honest",
    "chapters": [
        ("A band of many fields",
         "Each ring of the debris belt holds many debris fields. The game lays them out in cells about 3 km across, around the pilot and only inside a ring's band. A survey of a band is a survey of many cells, not of one big field."),
        ("At least one massive field per ring",
         "Every ring has at least one massive field. It is the same for every player, and it shrinks as it is mined. Once it is completely mined out, it re-spawns somewhere else in the same ring, so a ring never runs out of large rock."),
        ("Sweep in lanes",
         "A careful survey sweeps a band in parallel lanes, spaced so that what one lane covers overlaps the next. Gaps between lanes leave fields unseen. Search teams and mapmakers use the same method on the ground."),
        ("Keep a record",
         "Mark each field as you find it: where it lies, what it holds, and whether it has been mined out. A mined-out field is marked as cleared. A record stops a crew from searching the same ground twice."),
        ("Mark it for the return",
         "A beacon placed at a field saves its position, so a pilot can warp straight back to it after unloading. Beacons are built by players, and the game sets no limit on how many. A map that marks a good field saves the time of finding it again."),
        ("Plan for the ring",
         "A field returns to its ring after it is mined out, so a surveyor can plan ahead. Keep the map up to date and note the cleared fields. A survey that is out of date sends the crew to empty ground."),
    ],
    "test": [
        ("How large are the cells the game lays debris fields out in, around the pilot?",
         [("a", "About 3 km"), ("b", "About 300 km"), ("c", "About 30 metres"), ("d", "About 3 light years")], "a"),
        ("What happens to a massive debris field once it is completely mined out?",
         [("a", "It is deleted for good"), ("b", "It re-spawns somewhere else in the same ring"), ("c", "It moves to another star"), ("d", "It turns into gold")], "b"),
        ("Why does a careful survey sweep a band in parallel lanes that overlap?",
         [("a", "So no ground is left unseen between the lanes"), ("b", "So the crew can sing"), ("c", "To use more fuel"), ("d", "To make the map look striped")], "a"),
        ("What does a beacon do?",
         [("a", "Blocks other players"), ("b", "Shows the time of day"), ("c", "Saves a field's position so a pilot can warp straight back to it after unloading"), ("d", "Pays out credits")], "c"),
        ("How should a survey record a field that has been mined out?",
         [("a", "Leave it unmarked"), ("b", "Erase the whole record"), ("c", "Mark it as the largest field"), ("d", "Mark it as cleared, so the crew does not search it again")], "d"),
    ],
}
