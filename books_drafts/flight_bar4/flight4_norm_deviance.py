"""Normalisation of Deviance: how small, accepted drifts from the rules build up, and how Challenger and Columbia show it."""
CODE = 'flight4_norm_deviance'
BOOK = {
    "title": "Normalisation of Deviance",
    "subtitle": "Small drifts, accepted risks and how to reset the standard",
    "chapters": [
        ("A phrase from Challenger",
         "The sociologist Diane Vaughan studied the Challenger launch decision and described normalisation of deviance. It is the slow process by which a risk that breaks the rules comes to seem ordinary."),
        ("Small drifts",
         "Each time a small problem appears and nothing bad happens, the team accepts it a little more. Over many flights, a standard can drift without anyone choosing to lower it."),
        ("Challenger",
         "Erosion of the O-rings was seen on earlier flights and treated as acceptable, even though it was never meant to happen. The danger came to seem normal until the day it was not."),
        ("Columbia",
         "Foam strikes had hit the Shuttle before Columbia's last flight. Each one was accepted as routine, and the risk grew quieter with every flight."),
        ("Spotting drift",
         "To spot drift, compare what happens with what should happen. Ask whether a problem is growing, whether a rule is being bent, and whether anyone is still surprised."),
        ("Resetting standards",
         "Reset the standard when drift is found. Write it down, go back to the original rule, and test any exception in the open. A team that resets early stays safe."),
    ],
    "test": [
        ("Who studied the Challenger decision and described normalisation of deviance?",
         [("a", "Diane Vaughan"), ("b", "Edwin Link"), ("c", "Gene Kranz"), ("d", "Fred Whipple")], "a"),
        ("What is normalisation of deviance?",
         [("a", "A quick launch"), ("b", "A new planet"), ("c", "A flight plan"), ("d", "A risk that breaks the rules slowly becomes ordinary")], "d"),
        ("Which two losses are linked to this idea in the book?",
         [("a", "Apollo and Gemini"), ("b", "Skylab and Salyut"), ("c", "Voyager and Galileo"), ("d", "Challenger and Columbia")], "d"),
        ("How do small drifts add up?",
         [("a", "Quickly"), ("b", "Never"), ("c", "Each accepted problem makes the next one easier to accept"), ("d", "They stop")], "c"),
        ("What should a team do when it finds drift?",
         [("a", "Ignore it"), ("b", "Reset the standard and go back to the original rule"), ("c", "Hide it"), ("d", "Cheer")], "b"),
    ],
}
