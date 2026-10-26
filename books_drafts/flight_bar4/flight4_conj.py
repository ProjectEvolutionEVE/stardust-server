"""Conjunction Assessment: how operators judge a close approach between two objects in orbit, and when to dodge."""
CODE = "flight4_conj"
BOOK = {
    "title": "Conjunction Assessment",
    "subtitle": "Judging close approaches and when to dodge",
    "chapters": [
        ("A close approach", "A conjunction is a close approach between two objects in orbit. Operators watch for them every day, because even a small object can do great harm at orbital speed."),
        ("Uncertainty in words", "No one knows a position exactly. Each prediction comes with a cloud of uncertainty, called covariance. A wide cloud means the position is less certain, and a narrow cloud means it is more certain."),
        ("Probability of collision", "Operators combine the two clouds to estimate a probability that the objects will hit. The number is small in most cases, but it can be large when the clouds overlap and the approach is close."),
        ("Threshold decisions", "Each operator sets a threshold, a level of probability above which they will act. When a close approach passes the threshold, the team decides whether to move one object."),
        ("Avoidance burns", "A small burn can move a craft off its path. Teams plan the burn well ahead, check that it does not create a new risk, and then carry it out."),
        ("Sharing data", "Operators share orbit data so that everyone can judge the same approach. Good sharing lets more than one team check the numbers, and it helps prevent surprises."),
    ],
    "test": [
        ("What is a conjunction in orbit?", [("a", "A type of rocket fuel"), ("b", "A planet ring"), ("c", "A close approach between two objects"), ("d", "A radio station")], "c"),
        ("What does covariance describe?", [("a", "The uncertainty around a predicted position"), ("b", "The colour of a satellite"), ("c", "The number of crew"), ("d", "The price of fuel")], "a"),
        ("What does an operator combine to estimate a collision chance?", [("a", "Two cookbooks"), ("b", "Two radio songs"), ("c", "Two spacesuits"), ("d", "The two uncertainty clouds")], "d"),
        ("What is a threshold in this work?", [("a", "A doorway in a station"), ("b", "A probability level above which the team will act"), ("c", "A type of solar panel"), ("d", "A kind of sensor")], "b"),
        ("Why is an avoidance burn checked first?", [("a", "To make the craft heavier"), ("b", "To stop all communication"), ("c", "To make sure it does not create a new risk"), ("d", "To hide the orbit")], "c"),
    ],
}
