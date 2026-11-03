"""Gravity Disturbance in Inertial Systems: local variations in gravity, deflection of the vertical and long-flight errors."""
CODE = "navigation5_gravity_disturbance"
BOOK = {
    "title": "Gravity Disturbance in Inertial Systems",
    "subtitle": "Why the pull of gravity is not quite the same everywhere",
    "chapters": [
        ("Gravity is not uniform", "The pull of gravity varies a little from place to place. The Earth's shape causes most of it, and a reference model allows for that. The extra differences, from mountains and rock density, are called the gravity disturbance."),
        ("Deflection", "The local vertical, the direction gravity pulls, can differ from the direction of the ellipsoid's normal. This difference is called the deflection of the vertical."),
        ("The model", "A gravity model describes these variations on a grid. An inertial system uses the model to predict the local gravity vector."),
        ("Errors", "If the gravity model is wrong, the inertial system gets a position error. Over long flights, these errors grow."),
        ("Correction", "Systems correct for gravity by using the model's values at the current position. Good models and regular updates keep the error small."),
        ("Long flights", "On long flights over oceans and polar regions, gravity errors can become significant. Careful models and gravity surveys help."),
    ],
    "test": [
        ("What causes gravity to vary from place to place?",
         [("a", "The colour of the sky"), ("b", "Cats"), ("c", "Songs"), ("d", "Mountains, rock density and the Earth's shape")], "d"),
        ("What is deflection of the vertical?",
         [("a", "A bent road"), ("b", "A jump"), ("c", "The difference between the gravity direction and the ellipsoid's normal"), ("d", "An insect")], "c"),
        ("What does a gravity model do?",
         [("a", "Describes gravity variations so systems can predict it"), ("b", "Paints maps"), ("c", "Cooks food"), ("d", "Prints tickets")], "a"),
        ("What happens if the gravity model is wrong?",
         [("a", "Nothing happens"), ("b", "The inertial system gets a position error"), ("c", "The sky turns green"), ("d", "The paper tears")], "b"),
        ("Where do gravity errors matter most?",
         [("a", "In a bedroom"), ("b", "In a garden"), ("c", "On long flights over oceans and polar regions"), ("d", "In a kitchen")], "c"),
    ],
}
