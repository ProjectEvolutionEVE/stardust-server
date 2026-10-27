"""Brittle fracture and the transition temperature: steel at low temperature, Charpy tests, notches, the Liberty ships and cold service."""
CODE = "engineering4_brittle"
BOOK = {
    "title": "Brittle Fracture and the Transition Temperature",
    "subtitle": "Steel at low temperature, notches and the Liberty ships",
    "chapters": [
        ("Steel that cracks in the cold",
         "Some steels that are tough when warm become brittle when cold. Below a certain temperature the steel can break with little bending. This change is called the ductile-to-brittle transition."),
        ("The transition temperature",
         "The transition temperature is the range where a steel changes from tough to brittle. It depends on the steel's chemistry and how it was made. Choosing a steel with a transition temperature below the lowest service temperature is essential."),
        ("Charpy impact tests",
         "A Charpy test strikes a notched bar with a swinging hammer and measures the energy absorbed. Tests are run over a range of temperatures to find the transition. The result shows how the steel behaves in the cold."),
        ("Notches and stress",
         "A notch or a sharp corner raises the stress locally and makes brittle fracture more likely. Designers avoid sharp corners and welds with defects. Smooth shapes lower the risk of a sudden crack."),
        ("The Liberty ship story",
         "During the Second World War, many Liberty ships built with welded steel hulls cracked in cold seas. Some broke in two without warning. The disasters led to better steel choices and tougher welding practice."),
        ("Choosing steel for cold service",
         "Engineers pick steel by its toughness at the lowest temperature the part will see. They also check the design for notches, welds and thick sections. A steel that is safe warm may still be unsafe in a winter sea."),
    ],
    "test": [
        ("What is the ductile-to-brittle transition?", [("a", "A steel getting heavier when warm"), ("b", "A steel turning into glass"), ("c", "A steel changing from tough to brittle as it gets cold"), ("d", "A steel being painted")], "c"),
        ("What does a Charpy test do?", [("a", "Tests the colour of paint"), ("b", "Measures the length of a ship"), ("c", "Strikes a notched bar with a swinging hammer and measures the energy absorbed"), ("d", "Checks the speed of a boat")], "c"),
        ("Why are notches dangerous in brittle steel?", [("a", "They raise the stress locally and make brittle fracture more likely"), ("b", "They make the steel softer"), ("c", "They add weight"), ("d", "They stop cracks")], "a"),
        ("What problem did many Liberty ships have in cold seas?", [("a", "Their engines froze and never ran again on any voyage"), ("b", "They could not float"), ("c", "They ran out of paint"), ("d", "Some cracked and broke in two without warning")], "d"),
        ("How should steel be chosen for a cold job?", [("a", "By its colour alone"), ("b", "By its toughness at the lowest temperature the part will see"), ("c", "By its shine"), ("d", "By choosing the cheapest name")], "b"),
    ],
}
