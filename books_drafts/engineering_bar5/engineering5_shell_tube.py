"""Shell-and-Tube Exchanger Mechanical Design: the tubes, tube sheets, baffles and expansion allowances that make a heat exchanger work and last."""
CODE = "engineering5_shell_tube"
BOOK = {
    "title": "Shell-and-Tube Exchanger Mechanical Design",
    "subtitle": "Tube layouts, tube sheets, baffles and thermal growth",
    "chapters": [
        ("Two fluids, one shell", "A shell-and-tube exchanger has a bundle of tubes inside a larger shell. One fluid flows through the tubes and the other flows around them inside the shell."),
        ("Tube layouts", "Tubes are arranged in patterns such as triangular or square. The pattern affects both heat transfer and how easily the outside of the tubes can be cleaned."),
        ("Tube sheets", "The tubes are held at each end by tube sheets. The tube sheets must be designed for the pressure and the loads they carry."),
        ("Baffles", "Baffles guide the shell-side fluid across the tubes, which improves heat transfer. They also support the tubes against sagging and vibration."),
        ("Thermal expansion and vibration", "Expansion joints and careful support allow for growth with temperature, and they limit tube vibration. Without them the tubes can be damaged."),
        ("Pressure design", "The shell and tubes are designed to hold their working pressures safely. The design follows the pressure vessel codes that apply to the job."),
    ],
    "test": [
        ("What does a shell-and-tube exchanger have?", [("a", "A bowl of soup"), ("b", "A bundle of tubes inside a shell"), ("c", "A single flat plate"), ("d", "A bicycle frame")], "b"),
        ("What do tube sheets do?", [("a", "Hold the tubes at each end"), ("b", "Paint the tubes"), ("c", "Sell the tubes to customers"), ("d", "Light up the tubes")], "a"),
        ("What do baffles do?", [("a", "Block the sun from the plant"), ("b", "Store the tubes when not in use"), ("c", "Guide the shell-side fluid across the tubes"), ("d", "Make the shell heavier")], "c"),
        ("Why are expansion joints used?", [("a", "To paint the tubes"), ("b", "To stop the flow entirely"), ("c", "To make the exchanger smaller"), ("d", "To allow for growth with temperature")], "d"),
        ("What must the shell and tubes be designed for?", [("a", "The speed of passing cars"), ("b", "Their working pressures, following code rules"), ("c", "The colour of the room"), ("d", "The number of shoes in the store")], "b"),
    ],
}
