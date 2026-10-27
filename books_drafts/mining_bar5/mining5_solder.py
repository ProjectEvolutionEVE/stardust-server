"""Lead-Free Solders: tin-based alloys that replaced lead solder in electronics, and the reliability questions they raise."""
CODE = "mining5_solder"
BOOK = {
    "title": "Lead-Free Solders",
    "subtitle": "Tin alloys for electronics, and why they need more care",
    "chapters": [
        ("Why lead went", "Lead solder was the standard for decades. Many countries restricted lead in electronics from the mid 2000s, because lead is toxic. Makers switched to tin-based alloys, which are now the norm."),
        ("The common alloy", "A common lead-free solder is tin with about 3% silver and 0.5% copper, often called SAC305. It melts at a higher temperature than old tin-lead solder, so circuit boards must be heated more."),
        ("Intermetallics", "When solder joins a copper pad, tiny compounds form at the boundary. These are intermetallics, such as copper and tin compounds. A thin, even layer helps the joint, but a thick one can make it brittle."),
        ("Thermal fatigue", "Electronics heat up and cool down many times in their life. Solder joints expand and shrink at slightly different rates than the board. Over time this can crack a joint. Lead-free joints can be more prone to this, so designs allow for it."),
        ("Rules and costs", "Lead-free rules are set by law in many regions. Silver adds cost, so makers balance alloy price against joint strength and the process they use."),
        ("Testing the joint", "Engineers test solder joints by heating and cooling boards many times, and by looking at them under a microscope. A joint that passes these tests is trusted in a phone, a car or a satellite."),
    ],
    "test": [
        ("Why were lead solders replaced?",
         [("a", "Lead is toxic"), ("b", "Lead was too strong"), ("c", "Lead was too cheap"), ("d", "Lead was too bright")], "a"),
        ("What is the main metal in lead-free solder?",
         [("a", "Iron"), ("b", "Gold"), ("c", "Tin"), ("d", "Mercury")], "c"),
        ("What is an intermetallic?",
         [("a", "A plastic board"), ("b", "A compound that forms where solder meets a metal pad"), ("c", "A type of paint"), ("d", "A metal that never melts")], "b"),
        ("What is thermal fatigue?",
         [("a", "A fever in the worker"), ("b", "Melting in a freezer"), ("c", "Shine loss from polish"), ("d", "Cracking from repeated heating and cooling")], "d"),
        ("What does the common alloy SAC305 contain besides tin?",
         [("a", "Lead and iron"), ("b", "Silver and copper"), ("c", "Gold and nickel"), ("d", "Only carbon")], "b"),
    ],
}
