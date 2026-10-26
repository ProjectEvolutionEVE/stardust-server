"""Ion Drives: a gentle push for a long time, from electric engines that use propellant very efficiently."""
CODE = "flight3c_ion_drives"
BOOK = {
    "title": "Ion Drives",
    "subtitle": "Electric engines that push very gently and use propellant very efficiently",
    "chapters": [
        ("A very gentle push",
         "An ion drive uses electricity to speed up charged atoms of gas, usually xenon, and throws them out of the back. The push is far weaker than a chemical engine's. It keeps going for a long time, and a long time adds up."),
        ("Efficient with propellant",
         "The ions leave the engine very fast, so each kilogram of propellant gives much more total push over a long burn. Ion drives can reach a specific impulse in the thousands of seconds, many times that of a chemical engine. They carry less propellant for the same job."),
        ("Power is the limit",
         "An ion drive needs a great deal of electricity, which comes from solar panels or a nuclear source on board. The more power available, the stronger the engine can run. The power budget decides how many ion engines a craft can run at once."),
        ("Slow to build speed",
         "Because the push is so gentle, an ion-powered craft may take weeks or months to reach its top speed. It suits long trips, where patience and little fuel can beat a quick, heavy burn. It is a poor choice for a quick escape."),
        ("Real missions",
         "Deep Space 1 tested an ion drive in space in 1998. Later, the Dawn spacecraft used ion engines to visit two large objects in the asteroid belt, Vesta and Ceres, and to enter orbit around each in turn. Dawn is one of the clearest examples of ion power doing a job that chemical fuel could not."),
        ("A pilot's view",
         "Think of an ion drive as a steady wage rather than a single payment. It pays out slowly, but it adds up over the trip. Plan the power first, then the time, and remember that a gentle engine still needs care when you stop or turn."),
    ],
    "test": [
        ("What does an ion drive push out?",
         [("a", "Hot smoke"), ("b", "Water"), ("c", "Light"), ("d", "Charged gas atoms such as xenon")], "d"),
        ("Compared with a chemical engine, what does an ion drive give?",
         [("a", "More push in a single second"), ("b", "No push at all"), ("c", "A gentle push, with much better use of propellant"), ("d", "The same push, using more fuel")], "c"),
        ("What does an ion drive need a lot of?",
         [("a", "Electricity"), ("b", "Air"), ("c", "Ice"), ("d", "Sunlight only")], "a"),
        ("Why would a craft with an ion drive take a long time to reach its top speed?",
         [("a", "The engine is broken"), ("b", "The push is gentle, so speed builds up slowly"), ("c", "Ions travel slowly through space"), ("d", "It must wait for a full moon")], "b"),
        ("Which spacecraft used ion engines to visit Vesta and Ceres?",
         [("a", "Apollo 11"), ("b", "Voyager 1"), ("c", "Dawn"), ("d", "Sputnik 1")], "c"),
    ],
}
