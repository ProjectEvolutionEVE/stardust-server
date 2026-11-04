"""Kriging for Spatial Interpolation: estimating values between measured points, the variogram, and the limits of the method."""
CODE = "navigation4_kriging"
BOOK = {
    "title": "Kriging for Spatial Interpolation",
    "subtitle": "Estimating values between measurements, and knowing how sure the estimate is",
    "chapters": [
        ("Spatial correlation", "Measurements that are close together tend to be alike. Kriging uses this idea. It assumes that nearby points tell you more about a spot than distant ones do."),
        ("The variogram", "A variogram shows how similarity falls off with distance. It is fitted to the measured data. The fitted curve tells kriging how much weight to give each nearby point."),
        ("Prediction error", "Kriging gives an estimate at each point and an error for that estimate. The error is largest where there are few measurements. A map of the errors is as useful as the map of values."),
        ("Sampling", "Where you take samples matters. Spread points evenly and cover the area of interest. Clustered samples can give a misleading picture of the rest of the land."),
        ("Uses", "Kriging is used in mining, soil science, groundwater and environmental monitoring. It helps estimate where ore or pollution might be found. It can guide where to take the next sample."),
        ("Limits", "Kriging assumes the pattern of change is steady across the area. It needs enough data to fit a variogram. It cannot know what happens between points in ways the data does not show."),
    ],
    "test": [
        ("What idea does kriging use?", [("a", "Every point is random"), ("b", "Distance never matters"), ("c", "Only the highest value counts"), ("d", "Nearby points tend to be alike")], "d"),
        ("What does a variogram show?", [("a", "The colour of the land"), ("b", "How similarity falls off with distance"), ("c", "The number of roads"), ("d", "The hardness of a rock")], "b"),
        ("Where is kriging's error usually largest?", [("a", "Where there are few measurements"), ("b", "Where there are many measurements"), ("c", "At the centre of a lake"), ("d", "On the coastline only")], "a"),
        ("Why does sample spacing matter?", [("a", "Spacing has no effect"), ("b", "Samples must be the same colour"), ("c", "Clustered samples can mislead about the rest of the land"), ("d", "It only affects the printing")], "c"),
        ("Which field uses kriging?", [("a", "Cooking"), ("b", "Mining"), ("c", "Sailing songs"), ("d", "Ballet")], "b"),
    ],
}
