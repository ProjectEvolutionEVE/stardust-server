"""Hand-Arm and Whole-Body Vibration Exposure: how much shaking a body can take at work, how it is measured, and how tools and seats are designed to protect it."""
CODE = "engineering5_vibration_exposure"
BOOK = {
    "title": "Hand-Arm and Whole-Body Vibration Exposure",
    "subtitle": "How much shaking is too much, how it is measured, and how to design it out",
    "chapters": [
        ("Two kinds of exposure", "Hand-arm vibration comes from tools held in the hands, such as grinders and drills. Whole-body vibration comes through a seat or floor, such as a driver on a vehicle or an operator on a large machine. The two are measured and limited in different ways."),
        ("Magnitude and frequency", "Vibration is measured as acceleration in metres per second squared, with a frequency weighting that matches how the body responds at each frequency. The weighted value tells you how harsh the motion feels to the person. A higher weighted value means a shorter safe time."),
        ("Exposure action and limit values", "The European Vibration Directive sets two levels for each kind of exposure. The action value is the daily level that triggers steps to reduce exposure. The limit value is the level that must never be exceeded. Both are stated as an eight-hour equivalent, called A(8)."),
        ("Measuring the dose", "The daily dose depends on how strong the vibration is and how long the worker is exposed. Measurements are taken on the tool or seat while it is used in normal work. Several short tasks are combined into one eight-hour figure, so a task done for less time still counts."),
        ("Designing it out", "The best protection is a quieter, smoother machine. Designers add damping, isolate handles with resilient mounts, and balance rotating parts. A good seat uses suspension matched to the body's weight and the road or floor it runs over."),
        ("Work practice matters too", "Rotating jobs between workers shortens each person's dose. Good maintenance keeps tools sharp and balanced, since a worn tool shakes more. Health checks catch early signs such as tingling and numbness in the fingers, so action can be taken before lasting harm builds up."),
    ],
    "test": [
        ("What is the EU daily action value for hand-arm vibration, measured as A(8)?", [("a", "0.5 metres per second squared"), ("b", "2.5 metres per second squared"), ("c", "5 metres per second squared"), ("d", "1.15 metres per second squared")], "b"),
        ("What does the action value trigger?", [("a", "The end of the working day"), ("b", "A new tool purchase only"), ("c", "A ban on all machines"), ("d", "Steps to reduce exposure")], "d"),
        ("What does A(8) mean?", [("a", "Eight tools in use at once"), ("b", "Eight percent of the frequency range"), ("c", "The exposure equivalent over an eight-hour day"), ("d", "The number of safety checks per year")], "c"),
        ("Which design step reduces the vibration a worker feels?", [("a", "Using resilient mounts to isolate the handle"), ("b", "Painting the handle a brighter colour"), ("c", "Making the tool heavier with loose parts"), ("d", "Running the tool faster to smooth it out")], "a"),
        ("Why does rotating jobs between workers help?", [("a", "It lowers the strength of the vibration"), ("b", "It removes the need for maintenance"), ("c", "It changes the frequency weighting"), ("d", "It shortens each person daily dose")], "d"),
    ],
}
