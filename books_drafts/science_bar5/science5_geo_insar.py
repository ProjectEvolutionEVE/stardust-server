"""Satellite Radar Interferometry (InSAR). How radar phase from two passes of a satellite maps ground movement."""
CODE = "science5_geo_insar"
BOOK = {
    "title": "Satellite Radar Interferometry (InSAR)",
    "subtitle": "Mapping the ground from space with radar",
    "chapters": [
        ("Radar from orbit",
         "A radar satellite sends microwave pulses to the ground and records the echo. Because the pulses can pass through cloud and work day and night, radar can map the surface in almost any weather."),
        ("Radar phase",
         "Each echo has a phase, a measure of where it falls within a wave cycle. If the ground moves toward or away from the satellite between two passes, the phase changes, and that change is the signal that InSAR uses."),
        ("Forming an interferogram",
         "An interferogram is made by subtracting the phase of one radar image from another taken from almost the same place. Fringes in the result show steps of ground movement, each fringe marking a fixed amount of change along the line of sight."),
        ("Atmospheric noise",
         "The air between satellite and ground slows the radar by varying amounts, which adds noise to the phase. Scientists estimate this noise with weather models or with many images, so that it is not mistaken for ground motion."),
        ("Subsidence mapping",
         "InSAR maps subsidence, such as the sinking of a city after groundwater is pumped out. It can cover wide areas that would be hard to survey on foot."),
        ("Time-series methods and limits",
         "Time-series methods combine many images to track each stable point over years. These methods have limits: they work best where the ground reflects radar well, and they measure only motion toward or away from the satellite."),
    ],
    "test": [
        ("What does InSAR measure?",
         [("a", "The taste of river water"), ("b", "The sound of wind"), ("c", "Changes in radar phase that reveal ground movement"), ("d", "The number of birds in a forest")], "c"),
        ("What is an interferogram?",
         [("a", "A chart of market prices"), ("b", "A list of earthquakes by name"), ("c", "A map of cloud colours"), ("d", "A difference between two radar images that shows movement as fringes")], "d"),
        ("Why is radar useful for mapping the ground?",
         [("a", "It works through cloud and day or night"), ("b", "It only works at night"), ("c", "It cannot see the ground at all"), ("d", "It only works in the sea")], "a"),
        ("What does atmospheric noise do to InSAR results?",
         [("a", "It adds errors to the phase that must be estimated and removed"), ("b", "It makes the ground move by itself"), ("c", "It stops the satellite from orbiting"), ("d", "It turns radar into sound")], "a"),
        ("What is a limit of InSAR?",
         [("a", "It cannot measure any motion at all"), ("b", "It measures only motion toward or away from the satellite"), ("c", "It works only on the Moon"), ("d", "It only works for one day")], "b"),
    ],
}
