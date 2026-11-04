"""The Polyconic Projection: classic survey sheets and their gentle curves."""
CODE = "navigation4_polyconic"
BOOK = {
    "title": "The Polyconic Projection",
    "subtitle": "Classic survey sheets and their gentle curves",
    "chapters": [
        ("Cones along each parallel", "The polyconic projection uses a separate cone for each parallel of latitude. Each cone touches the globe along its parallel. The lines of the map curve gently as a result."),
        ("The classic survey sheets", "For many years, national survey maps used the polyconic projection. Its sheets fitted well into a series of maps. Many older maps still use it."),
        ("Its uses", "The polyconic projection works well for areas that run mostly north to south. It keeps distortion small near the middle of each sheet. It was popular for topographic work."),
        ("Scale near the edges", "Scale becomes less accurate near the edges of a sheet. Surveyors keep their work near the middle of each sheet. That keeps the errors low."),
        ("The arrangement of sheets", "Sheets are arranged in a grid, often in rows and columns. Each sheet covers a set area. Careful edge matching keeps the whole series consistent."),
        ("Its limits", "The polyconic projection is neither conformal nor equal-area. Its scale and shape change across a large area. It is less used now that computers offer other projections."),
    ],
    "test": [
        ("How many cones does the polyconic projection use?",
         [("a", "One only"), ("b", "Two only"), ("c", "One for each parallel"), ("d", "None")], "c"),
        ("Which kind of maps used the polyconic projection for many years?",
         [("a", "Classic national survey sheets"), ("b", "Sea charts for sailors only"), ("c", "Star maps"), ("d", "Weather radar")], "a"),
        ("What kind of area suits the polyconic well?",
         [("a", "Mostly the Pacific"), ("b", "Just the poles"), ("c", "Only the Moon"), ("d", "Areas mostly running north to south")], "d"),
        ("Where does scale become less accurate?",
         [("a", "At the centre"), ("b", "Near the edges of a sheet"), ("c", "Nowhere"), ("d", "On the paper only")], "b"),
        ("What is a true limit of the polyconic projection?",
         [("a", "It cannot show any land"), ("b", "Its scale and shape change across a large area"), ("c", "It only shows the sea"), ("d", "It uses a ruler")], "b"),
    ],
}
