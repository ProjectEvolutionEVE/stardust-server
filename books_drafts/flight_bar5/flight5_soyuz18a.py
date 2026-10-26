"""Case Study: Soyuz 18a, 1975. A stage that did not separate, a steep ballistic descent, and a rescue in the snow."""
CODE = "flight5_soyuz18a"
BOOK = {
    "title": "Case Study: Soyuz 18a",
    "subtitle": "A stage failure, an abort, and a steep landing in the snow",
    "chapters": [
        ("The launch",
         "Soyuz 18a was launched in April 1975 to carry two cosmonauts toward the Salyut 4 space station. The rocket worked well at first. Then a fault in the upper stages meant the craft did not reach the orbit that was planned."),
        ("The abort",
         "The third stage did not separate as it should, so the craft could not be put into the right path. The crew were carried on a short flight that went up and came back down again. The descent was an emergency, not a planned landing."),
        ("A steep landing",
         "Because the path was wrong, the craft came back down at a much steeper angle than normal. The forces on the crew were high, and the capsule came down among rough, snowy hills. The angle of the descent is part of why the ride was so hard."),
        ("The rescue",
         "The crew were on the ground in the snow, and the search teams had to reach them. The two cosmonauts were found and brought to safety. Both survived, with some injuries and a long wait in the cold."),
        ("Why it mattered",
         "The flight showed how much depends on a few separation events working in the right order. It also showed the value of a crew trained to stay calm after a failed launch, and of search teams who knew what to do."),
        ("A lesson for any captain",
         "A plan that goes wrong does not end the job. The crew must work the emergency step by step, keep their heads, and trust the teams who are coming to find them. A good captain makes sure every person knows their part before the trouble starts."),
    ],
    "test": [
        ("Where did the Soyuz 18a crew come down?",
         [("a", "In the open sea"), ("b", "In a desert with sand dunes"), ("c", "Among snowy hills"), ("d", "On a city street")], "c"),
        ("What stopped the craft from reaching its planned orbit?",
         [("a", "A stage did not separate as it should"), ("b", "The crew fell asleep"), ("c", "The radio was too loud"), ("d", "The fuel was too cold to use")], "a"),
        ("Why was the landing steeper than normal?",
         [("a", "The crew chose a steep landing for fun"), ("b", "The craft followed a wrong path"), ("c", "The parachutes were red"), ("d", "The ground was made of ice")], "b"),
        ("What happened to the crew in the end?",
         [("a", "They were not found"), ("b", "They flew on to another station"), ("c", "They stayed in orbit for a year"), ("d", "They were rescued and both survived")], "d"),
        ("What does the flight show about a failed launch?",
         [("a", "The crew should panic and wait"), ("b", "Nothing can be done once the craft leaves the pad"), ("c", "A calm crew and trained search teams matter a great deal"), ("d", "Rescue is never needed")], "c"),
    ],
}
