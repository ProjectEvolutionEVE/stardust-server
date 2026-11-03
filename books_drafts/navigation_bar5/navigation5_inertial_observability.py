"""Observability of Navigation States: the state vector, measurements, unobservable directions, manoeuvres and gauge freedom."""
CODE = "navigation5_inertial_observability"
BOOK = {
    "title": "Observability of Navigation States",
    "subtitle": "What a filter can and cannot learn from its measurements",
    "chapters": [
        ("The state vector", "A navigation system's state vector holds position, velocity, attitude and sensor errors. The filter estimates these together."),
        ("Measurements", "Measurements such as GNSS position or Doppler velocity give information about some of the states. Not every state is seen directly."),
        ("Unobservable directions", "Some combinations of states may leave every measurement unchanged. Those combinations are called unobservable directions."),
        ("Manoeuvres", "Manoeuvres, such as turns and changes in speed, can make hidden states observable. Steady straight motion often leaves them unseen."),
        ("Design", "Designers check observability when they choose sensors and plan missions. The check shows what the system can and cannot estimate."),
        ("Gauge freedom", "Some navigation problems have gauge freedom. This is a choice of reference that does not change any measurement, so the designer must fix one reference to remove it."),
    ],
    "test": [
        ("What is a state vector?",
         [("a", "A paint"), ("b", "A menu"), ("c", "A list of position, velocity, attitude and errors"), ("d", "A bus")], "c"),
        ("Which of these is an example of a measurement?",
         [("a", "GNSS position"), ("b", "A painting"), ("c", "A song"), ("d", "A recipe")], "a"),
        ("What is an unobservable direction?",
         [("a", "A visible light"), ("b", "A direction on paper"), ("c", "A compass rose"), ("d", "A combination of states that no measurement can reveal")], "d"),
        ("What can make hidden states observable?",
         [("a", "A still table"), ("b", "Manoeuvres such as turns"), ("c", "A closed door"), ("d", "Sleep")], "b"),
        ("What is gauge freedom?",
         [("a", "A choice of reference that does not change the measurements"), ("b", "A fuel tank"), ("c", "A clock"), ("d", "A road")], "a"),
    ],
}
