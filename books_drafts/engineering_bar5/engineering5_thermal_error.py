"""Thermal Error Compensation in Machine Tools: heat sources in machines, thermal drift, sensor placement, compensation models and accuracy gains."""
CODE = "engineering5_thermal_error"
BOOK = {
    "title": "Thermal Error Compensation in Machine Tools",
    "subtitle": "Correcting for a machine that grows as it warms up",
    "chapters": [
        ("A machine that changes size",
         "A machine tool warms as it runs. Motors, bearings, hydraulics and the cutting itself all add heat. The frame and spindle grow slightly, and the part comes out a little off target."),
        ("Heat sources",
         "The main heat sources are the spindle motor, the bearings, the drive motors and the cutting zone. Each warms a different part of the machine. Knowing the sources helps engineers predict where the drift will come from."),
        ("Thermal drift",
         "Thermal drift is the slow change in position as the machine warms. It can take an hour or more to settle. Early parts can be out of tolerance unless the drift is managed."),
        ("Sensor placement",
         "Temperature sensors are placed on the frame, spindle and other key spots. Good placement shows the real pattern of heat. A few well-chosen sensors often predict the drift better than many poor ones."),
        ("Compensation models",
         "A compensation model turns the sensor readings into a correction for the tool position. The model is built from test runs that record the drift against the temperatures. The machine control then adjusts the axes as it runs."),
        ("Gains in accuracy",
         "Compensation can reduce the thermal error a great deal, which keeps parts within tolerance for longer. Less scrap and fewer warm-up cycles save money. The cost of sensors and the model is weighed against those savings."),
    ],
    "test": [
        ("Why does a machine tool change size as it runs?",
         [("a", "It loses weight each hour"), ("b", "It is painted in the sun"), ("c", "It gets colder"), ("d", "Its motors, bearings and cutting add heat, so it grows slightly")], "d"),
        ("What is thermal drift?",
         [("a", "The slow change in position as the machine warms"), ("b", "A type of wind in the factory"), ("c", "A loose belt"), ("d", "A burnt fuse")], "a"),
        ("Where are temperature sensors placed?",
         [("a", "On the ceiling only"), ("b", "On the frame, spindle and other key spots"), ("c", "Inside the coolant tank only"), ("d", "Nowhere on the machine")], "b"),
        ("What does a compensation model do?",
         [("a", "It paints the machine"), ("b", "It orders new tools"), ("c", "It turns sensor readings into a correction for the tool position"), ("d", "It counts the workers")], "c"),
        ("What is a benefit of thermal compensation?",
         [("a", "The machine never needs power"), ("b", "The parts get heavier"), ("c", "Warm-up is no longer needed in any case"), ("d", "Parts stay within tolerance for longer, with less scrap")], "d"),
    ],
}
