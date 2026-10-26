"""Chemical Engines: fast, strong and thirsty, and why they need so much propellant."""
CODE = "flight3c_chemical_engines"
BOOK = {
    "title": "Chemical Engines",
    "subtitle": "Hot gas from burning fuel, and why it takes so much propellant",
    "chapters": [
        ("Burning for push",
         "A chemical engine makes its push by burning a fuel with an oxidiser, such as liquid hydrogen with liquid oxygen. The burn makes very hot gas, which rushes out of the nozzle, and the craft is pushed the other way. It is the strongest kind of engine most craft carry."),
        ("Specific impulse",
         "Engineers measure how well an engine uses its propellant with a number called specific impulse, given in seconds. The higher the number, the more push each kilogram of propellant gives. Chemical engines usually fall in the range of a few hundred seconds."),
        ("Two liquids or one",
         "Some engines carry two liquids that burn together. Others use one liquid that breaks down into hot gas when it touches a catalyst. The single-liquid engine is simpler, but it gives less push for each kilogram of propellant."),
        ("Thrust and restarts",
         "A chemical engine can give a big push quickly, which is why it lifts a craft off a planet. Many can restart, so one engine can make several burns on one flight. Each burn uses propellant, so count the burns before you plan them."),
        ("The weight of the tank",
         "Propellant is heavy, and a full tank makes the whole craft heavier. As a burn goes on, the craft grows lighter, so the same push changes its speed a little more each second. The fuel you carry is a cost before you even light the engine."),
        ("A pilot's view",
         "The chemical engine is the workhorse of most flights. When you plan a burn, count the propellant as a real cost, set the push with the throttle, and leave a margin for the unexpected. Simple engines are often weaker, and weaker can still be right for the job."),
    ],
    "test": [
        ("What does a chemical engine burn to make its push?",
         [("a", "Sunlight"), ("b", "Fuel with an oxidiser"), ("c", "Air from outside"), ("d", "Electricity from a battery")], "b"),
        ("What does specific impulse measure?",
         [("a", "How bright the engine glows"), ("b", "How hot the nozzle gets"), ("c", "How much push each kilogram of propellant gives"), ("d", "How many crew fit in the cockpit")], "c"),
        ("Why is a full propellant tank a cost in itself?",
         [("a", "It makes the craft heavier, so the same push changes its speed less"), ("b", "It shrinks the craft"), ("c", "It stops the engine from restarting"), ("d", "It cools the hold")], "a"),
        ("Compared with a two-liquid engine, a single-liquid engine usually gives:",
         [("a", "Always more push"), ("b", "The same push, always"), ("c", "No push at all"), ("d", "Less push for each kilogram of propellant")], "d"),
        ("Why is a chemical engine used to lift a craft off a planet?",
         [("a", "It uses no propellant at all"), ("b", "It gives a big push quickly"), ("c", "It makes no heat"), ("d", "It needs no tank")], "b"),
    ],
}
