"""Projecting the Ellipsoid: why the Earth is not a ball, and how Mercator's idea carries over to the real shape."""
CODE = "navigation5_ellipsoidal_mercator"
BOOK = {
    "title": "Projecting the Ellipsoid",
    "subtitle": "The real shape of the Earth, and how maps must follow it",
    "chapters": [
        ("The Earth is not a ball", "The Earth is slightly flattened, bulging at the equator and squashed at the poles. A sphere is a simple model, but a more exact model is an ellipsoid."),
        ("Wider at the equator", "The equatorial radius is about 21 kilometres longer than the polar radius. Earth's spin is the main cause of the bulge."),
        ("The ellipsoidal Mercator", "Mercator's aim was to keep angles true. The same aim can be carried over to an ellipsoid. The formulas are harder, but they keep the map's angles right on the real shape."),
        ("Series", "The exact formulas are long, so mapmakers use series. A series is a sum of terms that get smaller, and a few terms give very accurate results."),
        ("Accuracy", "Using the ellipsoid instead of the sphere reduces errors over long distances and at high latitudes. Some error always remains, and mapmakers measure it."),
        ("Surveyors' use", "Surveyors and geodesists use ellipsoid formulas to measure land and set coordinates. Their work depends on matching the real shape closely."),
    ],
    "test": [
        ("Which shape is the Earth closest to, for mapping?",
         [("a", "A perfect sphere"), ("b", "An ellipsoid, flattened at the poles"), ("c", "A cube"), ("d", "A cone")], "b"),
        ("Why is the Earth wider at the equator than between the poles?",
         [("a", "The Earth spins, so it bulges at the equator"), ("b", "The poles are heavier"), ("c", "The Moon pulls the poles in"), ("d", "The oceans are deeper at the poles")], "a"),
        ("What is a series expansion used for in these projections?",
         [("a", "Painting maps by hand"), ("b", "Storing a map as a photograph"), ("c", "Drawing the coastline"), ("d", "Writing a formula as a sum of simple terms")], "d"),
        ("Why do surveyors use ellipsoid formulas instead of sphere formulas?",
         [("a", "Sphere formulas are faster to print"), ("b", "Ellipsoids cannot be measured"), ("c", "Ellipsoid formulas match Earth's shape better"), ("d", "Spheres have no equator")], "c"),
        ("What does a map's scale factor compare?",
         [("a", "A distance on the map with the true distance on the ground"), ("b", "The map's price with its size"), ("c", "Two colours on the legend"), ("d", "Time taken to print with time taken to draw")], "a"),
    ],
}
