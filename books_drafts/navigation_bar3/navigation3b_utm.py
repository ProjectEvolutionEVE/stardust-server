"""The UTM Grid: sixty zones, each six degrees wide, laid across the world so that a place is two numbers in metres."""
CODE = 'navigation3b_utm'
BOOK = {
    "title": "The UTM Grid",
    "subtitle": "Sixty zones, each six degrees wide, with a flat grid of metres in each",
    "chapters": [
        ("A grid for the whole Earth",
         "The Universal Transverse Mercator system, called UTM, splits the world into 60 zones. Each zone is 6 degrees of longitude wide and has its own flat grid measured in metres. Inside a zone, a position is two numbers, which are easier to add and subtract than degrees."),
        ("A map turned on its side",
         "UTM uses a Mercator-style map wrapped round the Earth on its side, so the line where the map touches the globe runs north and south through the middle of each zone. The map stays close to true shape near that line, and distortion grows toward the zone's edges."),
        ("Keeping the error even",
         "To spread the error evenly, the central line of each zone is scaled down slightly, by a factor of 0.9996. Distances along the middle come out a little short, and distances near the zone edges come out a little long, so both sides end up roughly correct."),
        ("Numbering the zones",
         "Zone 1 starts at 180 degrees west, and the numbers run eastward, so zone 60 ends at 180 degrees east. The zones cover the world from 80 degrees south to 84 degrees north. The polar regions use a different system, called UPS."),
        ("Easting and northing",
         "Each position has an easting, its distance east of a false origin on the zone's central line, and a northing, its distance north of the equator. The false origin keeps every number positive, so a point to the west of the centre never has a negative number."),
        ("Less time, less cost",
         "A crew that works in one zone keeps its arithmetic simple and its time on site short. In the game, a craft is billed for every hour it flies, so a plan that cuts wasted flight time saves credits as well as effort."),
    ],
    "test": [
        ("How many UTM zones are there?",
         [("a", "6"), ("b", "12"), ("c", "60"), ("d", "360")], "c"),
        ("How wide is each UTM zone in longitude?",
         [("a", "1 degree"), ("b", "30 degrees"), ("c", "90 degrees"), ("d", "6 degrees")], "d"),
        ("Why is the scale on a zone's central line reduced to 0.9996?",
         [("a", "To spread the distortion so distances are roughly right across the zone"), ("b", "So the zone looks smaller on paper"), ("c", "Because the Earth is shrinking"), ("d", "To make the numbers round")], "a"),
        ("What is a false easting for?",
         [("a", "To hide the zone number"), ("b", "To keep every number in a zone positive"), ("c", "To mark the North Pole"), ("d", "To count satellites")], "b"),
        ("Which zone starts at 180 degrees west?",
         [("a", "Zone 60"), ("b", "Zone 30"), ("c", "Zone 1"), ("d", "Zone 0")], "c"),
    ],
}
