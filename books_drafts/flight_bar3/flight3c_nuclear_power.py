"""Nuclear Power in Space: heat and electricity from a nuclear source, and why it is handled with great care."""
CODE = "flight3c_nuclear_power"
BOOK = {
    "title": "Nuclear Power in Space",
    "subtitle": "Heat and electricity from a nuclear source, and why it is handled with great care",
    "chapters": [
        ("Two kinds of nuclear help",
         "Nuclear energy can help a craft in two main ways: as a source of electricity, and as a source of heat to drive an engine. Both use the energy released when atoms change. Neither works by burning a fuel the way a chemical engine does."),
        ("Radioisotope generators",
         "Many deep-space probes carry a radioisotope generator. It turns the steady heat from the slow decay of a radioactive material into electricity, and it has no moving parts to wear out. The Voyager probes, Cassini and the Curiosity rover have all used this kind of power."),
        ("Nuclear heat for thrust",
         "A nuclear thermal engine heats a propellant, often hydrogen, in a reactor and lets the hot gas out through a nozzle. Ground tests in the 1960s suggested it could give more push for each kilogram of propellant than a chemical engine. As far as this book's facts go, no nuclear thermal engine has yet flown as a craft's main engine."),
        ("Safety comes first",
         "Nuclear material is only launched after strict checks, and every step is planned to keep it safe if something goes wrong. The source is shielded and sealed. The rules are strict on purpose, because a fault must never spread."),
        ("Cost and weight",
         "Nuclear systems are heavy, costly to build and costly to test. They are chosen for long missions far from the Sun, where solar panels give too little power. Weigh the extra cost against what the mission gains, the same way you weigh any big purchase."),
        ("A pilot's view",
         "A pilot may never touch a nuclear source, but should know why a craft far from the Sun may depend on one. Sunlight gets weaker with distance, so the further you go, the more the power budget matters. Know where your power comes from before you plan the trip."),
    ],
    "test": [
        ("What does a radioisotope generator make?",
         [("a", "Heat for the crew only"), ("b", "Fuel from ice"), ("c", "Electricity from the steady heat of decay"), ("d", "Light for the hold")], "c"),
        ("Which probes have used this kind of power?",
         [("a", "Sputnik 1"), ("b", "Vostok 1"), ("c", "Mariner 2"), ("d", "Voyager and Cassini")], "d"),
        ("Why does a far-off craft struggle with solar panels?",
         [("a", "Sunlight thins out with distance"), ("b", "The Sun gets colder"), ("c", "Panels break in the cold"), ("d", "Space is too dark to see")], "a"),
        ("What does a nuclear thermal engine do with its heat?",
         [("a", "Cools the craft"), ("b", "Heats a propellant and pushes it out"), ("c", "Makes ice"), ("d", "Lights up the hold")], "b"),
        ("Why is nuclear material handled so carefully?",
         [("a", "It makes the craft lighter"), ("b", "Pilots must wear it"), ("c", "It only works on Tuesdays"), ("d", "It is shielded and checked, because a fault must be kept from spreading")], "d"),
    ],
}
