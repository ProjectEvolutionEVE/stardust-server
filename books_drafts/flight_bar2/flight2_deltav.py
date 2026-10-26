"""Delta-v and Burns: the budget of speed a craft has, and why the timing of every push changes where you go."""
CODE = "flight2_deltav"
BOOK = {
    "title": "Delta-v and Burns",
    "subtitle": "The budget of speed a craft has, and how timed pushes change the path",
    "chapters": [
        ("What delta-v means",
         "Delta-v is the change in speed a craft can make. Engineers use it to plan a journey, because it tells them the total amount of pushing a trip needs. It counts changes in speed, not distance, so a big delta-v means the craft can change its speed a lot."),
        ("The rocket equation",
         "A real craft must carry propellant for every change in speed it makes. The rocket equation shows that the propellant needed rises steeply as the change in speed grows. A small rise in the budget can mean a much larger load to carry."),
        ("Some real numbers",
         "A craft in low Earth orbit travels at about 7.8 kilometres a second. To escape the pull of the Earth altogether, a craft needs about 11.2 kilometres a second. Getting from the ground into low orbit takes roughly 9 kilometres a second of delta-v once losses are counted."),
        ("What a burn is",
         "A burn is a timed push of the engines. The change in speed depends on how hard and how long you push, but where the path goes depends on when in the orbit you push. Good planners choose the moment of each burn for the place it will take the craft."),
        ("Forward and backward",
         "In orbit, a burn in the direction of travel raises the far side of the orbit, and a burn against the direction of travel lowers it. The effect shows up on the opposite side of the orbit, half a lap later. Planners use this to change the shape of a path."),
        ("Plan the path, then the push",
         "Look at where the path will end up before you push. Every burn bends the path, so each one should be picked for where it leaves you. Writing the plan down helps you see the whole path at once."),
    ],
    "test": [
        ("What does delta-v measure?",
         [("a", "The distance to a planet"), ("b", "The change in speed a craft can make"), ("c", "How bright the engine is"), ("d", "How heavy the hold is")], "b"),
        ("About what speed does a craft need to escape the pull of the Earth altogether?",
         [("a", "About 7.8 kilometres a second"), ("b", "About 11.2 kilometres a second"), ("c", "About 25 kilometres a second"), ("d", "About 500 metres a second")], "b"),
        ("What does a burn in the direction of travel do in orbit?",
         [("a", "Lowers the far side of the orbit"), ("b", "Stops the craft at once"), ("c", "Raises the far side of the orbit"), ("d", "Turns the craft towards the Sun")], "c"),
        ("Why does the rocket equation matter for planning?",
         [("a", "The propellant needed rises steeply as the change in speed grows"), ("b", "It shows the colour of the engine"), ("c", "It sets the size of the hold"), ("d", "It tells you the time of day")], "a"),
        ("What decides where a burn sends a craft in orbit?",
         [("a", "The colour of the craft"), ("b", "The number of bars you have"), ("c", "The name of the planet"), ("d", "When in the orbit the burn is made")], "d"),
    ],
}
