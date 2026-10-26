"""Case Study: Challenger, 1986. A cold morning, a warning about seals, and the decision to launch."""
CODE = 'flight4_challenger'
BOOK = {
    "title": "Case Study: Challenger, 1986",
    "subtitle": "A cold morning, the O-rings and the decision to launch",
    "chapters": [
        ("A cold morning",
         "On 28 January 1986 the Space Shuttle Challenger was due to launch from Florida. The morning was unusually cold, and ice had formed on the launch pad. Some engineers were worried about the weather."),
        ("The O-rings",
         "The solid rocket boosters are built in sections, and the sections are joined by rubber O-ring seals. In cold weather those rings can stiffen and lose their ability to seal a gap quickly. Engineers knew this, and they had raised concerns before."),
        ("The warning",
         "The night before, engineers at the company that built the boosters warned that the seals might fail in the cold. They advised waiting. Their concerns were not fully accepted when the decision was made."),
        ("The decision",
         "Managers weighed the advice and chose to launch. Seventy-three seconds after liftoff, hot gas burned through a joint, and the shuttle broke apart. All seven crew members were lost."),
        ("The commission",
         "A presidential commission, the Rogers Commission, studied the disaster. It found a faulty seal and a decision process that had not listened to warnings. Its report led to large changes in how the shuttle programme made safety decisions."),
        ("A risk that looked normal",
         "Challenger shows how an accepted risk can slowly seem normal. Each flight with a small problem made the problem look safe. Good teams watch for that drift and speak up early."),
    ],
    "test": [
        ("When was Challenger lost?",
         [("a", "1969"), ("b", "1986"), ("c", "2003"), ("d", "1966")], "b"),
        ("What were the O-rings?",
         [("a", "Engine fuel tanks"), ("b", "Seals between rocket sections"), ("c", "Crew seats"), ("d", "Radio dishes")], "b"),
        ("What did the cold do to the seals?",
         [("a", "Salt water built up on them"), ("b", "Heat made them melt"), ("c", "They stiffened and lost their ability to seal quickly"), ("d", "Lack of oxygen made them shrink")], "c"),
        ("What happened seventy-three seconds after liftoff?",
         [("a", "The engines shut down"), ("b", "The crew landed safely"), ("c", "The shuttle reached orbit"), ("d", "Hot gas burned through a joint and the shuttle broke apart")], "d"),
        ("What did the presidential commission do?",
         [("a", "Cancelled the Moon programme"), ("b", "Studied the disaster and its causes"), ("c", "Built a new shuttle the same day"), ("d", "Ended all spaceflight")], "b"),
    ],
}
