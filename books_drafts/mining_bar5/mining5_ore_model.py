"""Numerical Modelling of Ore-Forming Systems: computer models of heat, fluid and chemistry that help predict where ore forms."""
CODE = "mining5_ore_model"
BOOK = {
    "title": "Numerical Modelling of Ore-Forming Systems",
    "subtitle": "Computer models of heat, fluid and chemistry",
    "chapters": [
        ("Coupled heat, fluid and chemistry", "An ore-forming system is driven by heat, flowing fluid and chemical reactions working together. A good model links all three. Modelling one alone usually gives a wrong picture."),
        ("Mesh design", "A numerical model divides the rock into a grid of small cells called a mesh. Finer cells give more detail but need far more computing power. Designers place fine cells where change is fastest, such as near faults."),
        ("Reactive transport", "Reactive transport models track how dissolved chemicals move and react as fluid flows. They show where minerals dissolve and where they settle. This is how a model can point to a zone where ore could build up."),
        ("Calibration", "Calibration adjusts model settings until the results match real measurements, such as temperatures and mineral ages. A calibrated model is more trustworthy. Calibration must not simply force the model to match, because that hides real errors."),
        ("Predictive limits", "Every model has limits set by the data, the mesh and the assumptions. Predictions far from measured points are less certain. A careful team states where its model is strong and where it is weak."),
        ("Validation", "Validation tests a model against data it was not tuned to fit. If the model predicts a new drill result correctly, confidence grows. Failed validation tells the team to improve the model, not to ignore the failure."),
    ],
    "test": [
        ("What three processes does a good ore model link together?",
         [("a", "Music, art and sport"), ("b", "Sun, wind and rain"), ("c", "Heat, fluid flow and chemical reactions"), ("d", "Cars, roads and bridges")], "c"),
        ("What is a mesh in a numerical model?",
         [("a", "A type of fishing net"), ("b", "A grid of small cells that divides the rock"), ("c", "A kind of computer screen"), ("d", "A metal wire fence")], "b"),
        ("What does calibration do?",
         [("a", "It adjusts model settings until results match real measurements"), ("b", "It paints the model"), ("c", "It deletes all the data"), ("d", "It sells the model")], "a"),
        ("Why is validation useful?",
         [("a", "It proves every model right"), ("b", "It replaces the need for measurements"), ("c", "It makes the mesh bigger"), ("d", "It tests the model against data it was not tuned to fit")], "d"),
        ("Why are far-away predictions less certain?",
         [("a", "Distance changes the chemistry of gold"), ("b", "Models cannot count"), ("c", "They rest on less data and more assumptions"), ("d", "Far points are always wrong")], "c"),
    ],
}
