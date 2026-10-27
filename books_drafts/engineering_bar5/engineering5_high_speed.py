"""High-Speed Machining and Spindle Dynamics: spindle speeds, high-speed cutting data, thermal growth, spindle bearings and balancing in the spindle."""
CODE = "engineering5_high_speed"
BOOK = {
    "title": "High-Speed Machining and Spindle Dynamics",
    "subtitle": "Cutting fast without losing accuracy or control",
    "chapters": [
        ("Faster is not always simple",
         "High-speed machining cuts at speeds far above normal practice. It can remove metal quickly and leave a good surface. But at high speed, the spindle, the tool and the bearings all behave differently."),
        ("Spindle speed",
         "Spindle speed is the rate the spindle turns, often measured in revolutions per minute. The right speed depends on the tool, the material and the cut. Too fast wears the tool quickly; too slow wastes time."),
        ("Thermal growth",
         "A spindle warms as it runs, and it grows slightly as it warms. This thermal growth can move the tool tip off its target. Warm-up cycles and temperature sensors help hold accuracy."),
        ("Spindle bearings",
         "At high speed, bearings must run cool and steady. Their type, preload and lubrication are chosen for the speed. A worn bearing can cause chatter and poor surfaces."),
        ("Balancing in the spindle",
         "An unbalanced tool holder or tool shakes at high speed. The shaking loads the bearings and spoils the cut. Balancing the tool and holder together keeps the spindle smooth."),
        ("Cutting data and cost",
         "High-speed cutting data gives the speeds and feeds that work for a material and a tool. Using good data cuts time per part and tool cost. Machines that run fast also use more power, so the cost per part must be checked."),
    ],
    "test": [
        ("What does high-speed machining do?",
         [("a", "It cuts paper slowly"), ("b", "It cuts metal at speeds far above normal practice"), ("c", "It melts the tool"), ("d", "It stops the spindle")], "b"),
        ("What is spindle speed usually measured in?",
         [("a", "Litres per hour"), ("b", "Kilograms per metre"), ("c", "Revolutions per minute"), ("d", "Degrees Celsius")], "c"),
        ("What is thermal growth in a spindle?",
         [("a", "The spindle turns into metal"), ("b", "The spindle gets smaller in winter"), ("c", "The spindle changes colour"), ("d", "The spindle grows slightly as it warms, moving the tool tip")], "d"),
        ("What can a worn bearing cause at high speed?",
         [("a", "Chatter and poor surfaces"), ("b", "A brighter light"), ("c", "A cooler room"), ("d", "A heavier tool")], "a"),
        ("Why must the tool holder and tool be balanced?",
         [("a", "Balance changes the tool colour"), ("b", "An unbalanced tool shakes and loads the bearings"), ("c", "Balance makes the tool heavier only"), ("d", "Balance is never needed")], "b"),
    ],
}
