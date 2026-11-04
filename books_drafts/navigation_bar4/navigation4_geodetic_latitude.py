"""Geodetic and Geocentric Latitude: two angles that look alike but are not the same."""
CODE = "navigation4_geodetic_latitude"
BOOK = {
    "title": "Geodetic and Geocentric Latitude",
    "subtitle": "Two angles that look alike but are not",
    "chapters": [
        ("Two kinds of latitude", "Latitude can be measured in two ways. One follows the normal to the ellipsoid. The other follows the line from the centre of the Earth. The two angles are usually close, but they are not the same."),
        ("The normal to the ellipsoid", "The normal is the line perpendicular to the surface at a point. Surveys and GPS use geodetic latitude, which is measured along the normal. Most maps and datums use this latitude."),
        ("The difference in angle", "The difference between the two latitudes is largest at about forty-five degrees. It is zero at the equator and at the poles. The difference is small, but it matters for precise work."),
        ("The Earth's radius at a point", "The distance from the centre of the Earth changes with latitude. Near the equator it is larger, and near the poles it is smaller. This is part of why the two latitudes differ."),
        ("Conversion", "You can convert between the two latitudes with a formula that uses the shape of the ellipsoid. The conversion is simple once the shape is known. Software does the calculation for you."),
        ("Datum consistency", "Make sure all your data use the same latitude type and datum. Mixing the two can shift a point by a visible amount. Consistency keeps your coordinates trustworthy."),
    ],
    "test": [
        ("Which latitude is measured along the normal to the ellipsoid?",
         [("a", "Geocentric latitude"), ("b", "Geodetic latitude"), ("c", "Magnetic latitude"), ("d", "Solar latitude")], "b"),
        ("Where is the difference between the two latitudes largest?",
         [("a", "At the equator"), ("b", "At the poles"), ("c", "About forty-five degrees"), ("d", "On the Greenwich meridian")], "c"),
        ("What is the normal to the ellipsoid?",
         [("a", "A line perpendicular to the surface"), ("b", "A line along the equator"), ("c", "A line from the Sun"), ("d", "A line through the poles only")], "a"),
        ("Why does the Earth's radius change with latitude?",
         [("a", "The Earth is hotter at the poles"), ("b", "The Earth is flatter at the poles"), ("c", "The Moon pulls the Earth"), ("d", "Rivers change its size")], "b"),
        ("What is the risk of mixing the two latitude types?",
         [("a", "The map gets brighter"), ("b", "The compass stops working"), ("c", "The ship sinks"), ("d", "A point can shift by a visible amount")], "d"),
    ],
}
