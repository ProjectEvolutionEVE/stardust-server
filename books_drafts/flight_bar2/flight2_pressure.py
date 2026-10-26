"""Thinking Under Pressure: an order of priorities for emergencies, and calm habits that keep a bad moment from getting worse."""
CODE = "flight2_pressure"
BOOK = {
    "title": "Thinking Under Pressure",
    "subtitle": "An order of priorities for bad moments, and calm habits that help",
    "chapters": [
        ("Fly the craft first",
         "When something goes wrong, the first job is always to keep control of the craft. Aviators use the order: aviate, navigate, communicate. Keep the craft flying, then work out where you are, then tell others. Keeping to this order stops one problem from becoming two."),
        ("Slow the clock down",
         "Under pressure, time seems to speed up. Take one breath, and name the problem in a short sentence. A clear sentence makes it much easier to choose the next step."),
        ("Look for the simplest safe step",
         "Ask which step makes things safer right now. Lower your speed, hold to take the controls, or turn back toward the debris. Save the complicated fixes for later, once the craft is steady."),
        ("Use the checklist",
         "If the problem matches an item on your checklist, follow the list in order. Skipping steps is easy when you are rushed, so tick each step off as you go. The list was written for the moment you are in now."),
        ("After the moment",
         "Once the craft is safe, look at what happened and why. Write down the cause and the change you will make, so the next flight is safer. A short note is enough."),
        ("A real example",
         "On Apollo 13 in 1970, an oxygen tank failed on the way to the Moon, and the mission had to be changed. The crew and mission control worked through the problems one step at a time, and the crew returned safely to Earth."),
    ],
    "test": [
        ("What is the first priority in an emergency?",
         [("a", "Keep control of the craft"), ("b", "Post a message"), ("c", "Fill the hold"), ("d", "Open the scanner")], "a"),
        ("What is the order of priorities that aviators use?",
         [("a", "Communicate, navigate, aviate"), ("b", "Aviate, navigate, communicate"), ("c", "Navigate, communicate, aviate"), ("d", "Scan, sleep, collect")], "b"),
        ("Why take one breath and name the problem in a short sentence?",
         [("a", "It stops the autopilot"), ("b", "It starts the radar"), ("c", "It adds to your bars"), ("d", "A clear sentence helps you choose the next step")], "d"),
        ("Which is usually the simplest safe first step?",
         [("a", "Start a complicated repair at once"), ("b", "Warp to Jupiter"), ("c", "Lower your speed and take back the controls"), ("d", "Open the hold")], "c"),
        ("What was the main emergency on Apollo 13 in 1970?",
         [("a", "An oxygen tank failure"), ("b", "A lost Moon rock"), ("c", "A market crash"), ("d", "A broken radio in Earth orbit")], "a"),
    ],
}
