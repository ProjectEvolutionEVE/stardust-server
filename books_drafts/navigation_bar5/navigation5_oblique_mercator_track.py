"""The Oblique Mercator for Satellite Tracks: mapping strips of imagery along an orbit."""
CODE = "navigation5_oblique_mercator_track"
BOOK = {
    "title": "The Oblique Mercator for Satellite Tracks",
    "subtitle": "Tilting the map to follow an orbit",
    "chapters": [
        ("Where satellites travel", "A satellite in a near-polar orbit traces a path over the ground, called its ground track. The track is close to a great circle that is tilted from the equator."),
        ("Rotating the cylinder", "An ordinary Mercator wraps a cylinder around the equator. The oblique version tilts the cylinder so that it hugs the track instead."),
        ("Following the orbit", "Because the projection follows the track, a strip of imagery stays nearly straight. Distortion stays low along the path."),
        ("Mapping imagery", "Landsat imagery is commonly processed in the Space Oblique Mercator projection, which suits strips of images collected along an orbit."),
        ("Scale", "The scale is exact along the central line and grows away from it. Mapmakers keep the scale error within a set range."),
        ("Putting it into software", "Software uses the orbit's inclination and the satellite's path to set the projection's parameters. Careful checks of those parameters prevent large offsets."),
    ],
    "test": [
        ("What is a ground track?",
         [("a", "The path over the ground traced by a satellite's position"), ("b", "A railway line"), ("c", "A mountain range"), ("d", "A weather front")], "a"),
        ("What is different about the oblique Mercator?",
         [("a", "It uses a cube"), ("b", "It has no scale"), ("c", "Its cylinder is tilted to follow a path"), ("d", "It maps only the poles")], "c"),
        ("Which imagery is commonly processed with the Space Oblique Mercator?",
         [("a", "Old paper maps"), ("b", "Photographs of cats"), ("c", "Landsat satellite imagery"), ("d", "Cave drawings")], "c"),
        ("Where is the scale exact in this projection?",
         [("a", "At the poles only"), ("b", "At the edges"), ("c", "Nowhere"), ("d", "Along the central line")], "d"),
        ("What sets the projection's parameters for a satellite strip?",
         [("a", "The colour of the sky"), ("b", "The orbit's inclination and path"), ("c", "The number of cities"), ("d", "The price of paper")], "b"),
    ],
}
