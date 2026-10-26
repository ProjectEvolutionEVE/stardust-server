"""Case Study: Gemini 8, 1966. The first docking, a stuck thruster, a spin, and a calm return."""
CODE = 'flight4_gemini8'
BOOK = {
    "title": "Case Study: Gemini 8, 1966",
    "subtitle": "The first docking, a stuck thruster and a calm return",
    "chapters": [
        ("The first docking",
         "In March 1966 Gemini 8 became the first craft to dock with another spacecraft in orbit. Neil Armstrong and David Scott linked up with an unmanned Agena target vehicle. The docking went well, and the crew was pleased with the result."),
        ("A stuck thruster",
         "Soon after, one of the small thrusters on the Gemini stuck open. The craft began to roll, and then to spin faster and faster. The docked pair had to separate, but the spin grew worse."),
        ("Keeping calm",
         "Armstrong kept his head and worked through the problem. He used the separate reentry control system to stop the spin. Clear thinking mattered more than speed."),
        ("An early return",
         "The mission had to end early. The crew brought the craft down in the Pacific Ocean, where a recovery ship picked them up. Both men were safe."),
        ("What the team learned",
         "Investigators traced the stuck thruster to a fault in its electrical wiring. The lesson was that a control can fail in a way nobody expects. Careful testing and checking of wiring became standard practice."),
        ("Why it still matters",
         "Gemini 8 shows that a crew must know their craft well enough to act when a backup is needed. Reading the problem, choosing the right fix and acting calmly all saved the crew."),
    ],
    "test": [
        ("What was Gemini 8 the first to do?",
         [("a", "Land on the Moon"), ("b", "Dock with another spacecraft in orbit"), ("c", "Fly to Mars"), ("d", "Walk in space")], "b"),
        ("What caused the spin?",
         [("a", "A stuck thruster"), ("b", "A broken window"), ("c", "Too much food"), ("d", "A lost parachute")], "a"),
        ("What did Armstrong use to stop the spin?",
         [("a", "The main engine"), ("b", "The separate reentry control system"), ("c", "A cargo hook"), ("d", "Radio only")], "b"),
        ("Where did the Gemini 8 crew come down?",
         [("a", "In the desert"), ("b", "On a mountain"), ("c", "In the Pacific Ocean"), ("d", "In a lake")], "c"),
        ("What is the main lesson of the flight?",
         [("a", "Speed beats care"), ("b", "A control can fail in a way nobody expects, so crews must know their craft"), ("c", "Spins never matter"), ("d", "Docking is always unsafe")], "b"),
    ],
}
