"""Margaret Hamilton: the lead of the Apollo guidance software, the priority scheduling that saved the Apollo 11 landing, and her lasting influence."""
CODE = "flight5_margaret_hamilton"
BOOK = {
    "title": "Margaret Hamilton",
    "subtitle": "The Apollo software lead and the alarms that mattered",
    "chapters": [
        ("Apollo software lead",
         "Margaret Hamilton led the team that wrote the flight software for the Apollo guidance computer. The software guided the spacecraft and the lunar module. Her team worked to make the code reliable enough to trust with human lives."),
        ("Priority scheduling",
         "The guidance computer could only do so much at once, so the software was built to put the most important tasks first. This is known as priority scheduling. The design let the computer drop less important work when it was overloaded."),
        ("The 1202 alarms",
         "During the Apollo 11 descent, the computer showed alarms with the codes 1202 and 1201. The priority design let the computer keep the landing on track. The landing went on, and the crew landed safely."),
        ("Testing",
         "Hamilton's team tested the software with great care and checked it against many scenarios. They looked for errors in both the code and in the way it handled faults. Her focus on testing set a standard for later work."),
        ("Software engineering",
         "Hamilton is often credited with popularising the term software engineering. She argued that software deserved the same care as other engineering. Her work helped the field grow into a serious discipline."),
        ("Honours",
         "Hamilton received honours for her work on Apollo and her later contributions to computing. Her career shows what careful design and rigorous testing can achieve. Her name is linked to one of the great technical achievements of the Moon landings."),
    ],
    "test": [
        ("What did Margaret Hamilton lead?",
         [("a", "The cooking team"), ("b", "The rocket engine factory"), ("c", "The flight software for the Apollo guidance computer"), ("d", "The spacesuit design shop")], "c"),
        ("What is priority scheduling?",
         [("a", "Putting the most important tasks first"), ("b", "Doing tasks at random"), ("c", "Skipping all tests"), ("d", "Waiting for a holiday")], "a"),
        ("Which mission had alarms that the priority design handled?",
         [("a", "Vostok 6"), ("b", "Apollo 11"), ("c", "Gemini 4"), ("d", "Skylab 2")], "b"),
        ("What term is Hamilton often credited with popularising?",
         [("a", "Space tourism"), ("b", "Lunar cooking"), ("c", "Radio silence"), ("d", "Software engineering")], "d"),
        ("What does her work show about careful design?",
         [("a", "Testing is a waste of time"), ("b", "Software never matters"), ("c", "Careful design and rigorous testing can achieve great things"), ("d", "Alarms should always be ignored")], "c"),
    ],
}
