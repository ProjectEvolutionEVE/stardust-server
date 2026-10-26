"""Metal Fatigue: how repeated loads crack metal, even when it looks fine."""
CODE = "flight5_s_fatigue"
BOOK = {
    "title": "Metal Fatigue",
    "subtitle": "How repeated loads crack metal, even when it looks fine",
    "chapters": [
        ("Repeated stress",
         "Metal can crack under a load far smaller than the one it could hold once. The cause is repetition: each cycle of stress adds a little damage."),
        ("How a crack grows",
         "A tiny crack often starts at a sharp corner, a hole or a scratch. With every cycle it grows a little longer, until the part fails suddenly."),
        ("The Comet airliner",
         "In the 1950s, several de Havilland Comet airliners broke apart in the air. Investigators found fatigue cracks that began near the square corners of the windows."),
        ("Aloha Flight 243",
         "In 1988 Aloha Airlines Flight 243 lost a large part of its upper fuselage in flight. Fatigue cracks had linked up along rivet holes, and the aircraft landed safely."),
        ("Inspection",
         "Engineers inspect metal parts on a schedule and look for cracks with special tests. Finding a crack early is the best way to stop it growing."),
        ("Life limits",
         "Some parts are given a fixed life, a set number of flights or hours, and are replaced before fatigue becomes likely. It is a simple rule that saves lives."),
    ],
    "test": [
        ("What is metal fatigue?",
         [("a", "Cracking caused by repeated loads"), ("b", "Metal getting hot"), ("c", "Metal turning into dust"), ("d", "Paint wearing off")], "a"),
        ("Where do fatigue cracks often start?",
         [("a", "On smooth flat sheets"), ("b", "In the middle of a clean wall"), ("c", "In the open sky"), ("d", "At sharp corners, holes or scratches")], "d"),
        ("What did the Comet airliners' problems involve?",
         [("a", "Radio failures"), ("b", "Fatigue cracks near window corners"), ("c", "Fuel leaks alone"), ("d", "Bird strikes")], "b"),
        ("What is a life limit?",
         [("a", "A rule on how long a passenger may stay aboard"), ("b", "The top speed of an engine"), ("c", "A set number of flights or hours after which a part is replaced"), ("d", "The weight of a seat")], "c"),
        ("What is the best way to stop a fatigue crack growing?",
         [("a", "Find it early through inspection"), ("b", "Paint over it"), ("c", "Make the part hotter"), ("d", "Leave it alone")], "a"),
    ],
}
