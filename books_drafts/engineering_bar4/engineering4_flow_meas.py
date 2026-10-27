"""Flow Measurement: orifice plates, ultrasonic meters and turbine meters, and how to choose and calibrate one."""
CODE = "engineering4_flow_meas"
BOOK = {
    "title": "Flow Measurement: Orifices, Meters and Turbines",
    "subtitle": "Measuring how much fluid moves, and choosing the right meter",
    "chapters": [
        ("Why measure flow",
         "Plants sell, control and bill by flow. A flow meter tells you how much fluid passes in a given time. Accuracy matters because a small error repeated over a large volume adds up to a large sum."),
        ("Orifice plates",
         "An orifice plate is a thin plate with a hole, fitted in a pipe. The flow speeds up through the hole, and the pressure falls across it. The pressure drop tells you the flow rate. It is simple and cheap, but it causes a permanent loss of pressure."),
        ("Ultrasonic meters",
         "An ultrasonic meter sends sound pulses across the pipe, both with the flow and against it. The difference in travel time gives the flow speed. It has no parts in the stream, so it causes little pressure loss."),
        ("Turbine meters",
         "A turbine meter has a rotor in the stream that spins at a speed linked to the flow. It is accurate when the flow is steady and clean. Dirt and wear can slow the rotor and cause errors."),
        ("Calibration",
         "A meter is calibrated by comparing its reading with a known reference. Calibration records show drift over time. Schedule checks by how the meter is used and how important its readings are."),
        ("Choosing a meter",
         "Choose by fluid type, the pressure loss allowed, cost, accuracy and whether the pipe must stay clear. Follow the installation rules too, such as the length of straight pipe needed before and after the meter."),
    ],
    "test": [
        ("How does an orifice plate measure flow?",
         [("a", "By its weight"), ("b", "By the pressure drop across the hole"), ("c", "By the colour of the fluid"), ("d", "By heat from the pipe")], "b"),
        ("How does an ultrasonic meter find the flow speed?",
         [("a", "By weighing the fluid"), ("b", "By counting bubbles"), ("c", "By the difference in sound travel time with and against the flow"), ("d", "By heating the fluid")], "c"),
        ("Why is a meter calibrated?",
         [("a", "To make it lighter"), ("b", "To compare its reading with a known reference"), ("c", "To paint it"), ("d", "To remove its rotor")], "b"),
        ("What is a main drawback of an orifice plate?",
         [("a", "It has no parts"), ("b", "A permanent loss of pressure"), ("c", "It cannot measure liquids"), ("d", "It needs no installation")], "b"),
        ("What can slow a turbine meter's rotor and cause errors?",
         [("a", "Dirt and wear"), ("b", "A clean, steady flow"), ("c", "Straight pipe runs"), ("d", "A new bearing")], "a"),
    ],
}
