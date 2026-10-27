"""Water Hammer and Surges in Pipes: why a sudden stop in a water line makes a damaging pressure wave, and how to protect against it."""
CODE = "engineering4_water_hammer"
BOOK = {
    "title": "Water Hammer and Surges in Pipes",
    "subtitle": "Pressure waves, valve closing speed and surge protection",
    "chapters": [
        ("A sudden stop",
         "When a valve closes quickly, the moving water behind it must stop. Its momentum turns into a pressure wave that runs back up the pipe. The sharp knock you may hear is the wave hitting a bend or a closed end."),
        ("Pressure waves",
         "The wave travels at the speed of sound in water in that pipe, which is far faster than the flow itself. It reflects off pumps, bends and reservoirs, and reflections can add together."),
        ("Valve closing speed",
         "A slow closure spreads the stop over a longer time and gives a smaller surge. Designers set the closing time with the wave's travel time in mind, because a closure that is too quick gives the highest peak."),
        ("Surge tanks",
         "A surge tank is a tall tank joined to the line. It takes in water when the pressure rises and gives water back when the pressure falls. It smooths out the shock."),
        ("Protective valves",
         "Relief valves, air vessels and check valves protect the pipe. A pressure-relief valve opens and releases water when the pressure passes a set limit."),
        ("The damage",
         "A surge can burst pipes, crack joints, slam valves shut and damage pumps. Engineers check the pressure rise for every line that can close quickly, long before a fault shows up."),
    ],
    "test": [
        ("What causes water hammer?",
         [("a", "Water freezing"), ("b", "Warm water"), ("c", "A sudden change in flow, such as a fast valve closing"), ("d", "A low tank")], "c"),
        ("What is a surge tank for?",
         [("a", "Storing drinking water"), ("b", "Taking in water when pressure rises and giving it back when it falls"), ("c", "Heating the pipe"), ("d", "Measuring the flow")], "b"),
        ("How does a slower valve closing affect the pressure peak?",
         [("a", "It lowers it"), ("b", "It raises it"), ("c", "It makes no change"), ("d", "It doubles it")], "a"),
        ("How fast does the pressure wave travel in a water pipe?",
         [("a", "Slower than walking"), ("b", "Zero"), ("c", "Exactly the speed of the flow"), ("d", "Faster than the flow itself")], "d"),
        ("What can a surge do to a pipe?",
         [("a", "Make it lighter"), ("b", "Burst it or crack its joints"), ("c", "Make it warmer"), ("d", "Improve its paint")], "b"),
    ],
}
