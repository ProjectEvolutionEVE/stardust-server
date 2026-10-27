"""Strain Gauge Bridges and Calibration: measuring tiny strains with a resistive gauge and a Wheatstone bridge."""
CODE = "engineering5_strain_gauge"
BOOK = {
    "title": "Strain Gauge Bridges and Calibration",
    "subtitle": "Measuring tiny strains with a resistive gauge and a Wheatstone bridge",
    "chapters": [
        ("Strain as a change in resistance",
         "A strain gauge is a thin wire or foil whose electrical resistance changes slightly when it is stretched or squeezed. The change is tiny, so it needs careful measurement."),
        ("Gauge factor",
         "The gauge factor is the ratio of the fractional change in resistance to the strain. The maker supplies it, and it is used to convert the reading into strain."),
        ("Wheatstone bridges",
         "Four resistors arranged in a diamond, with a voltage across it, give a small output that is easy to measure. Gauges placed in the arms turn small strains into a readable voltage."),
        ("Temperature compensation",
         "Temperature also changes resistance, so the gauge needs a compensation method. A dummy gauge in the bridge, or a matched gauge, cancels most of the temperature effect."),
        ("Rosettes",
         "A rosette holds several gauges at set angles at one spot. Their readings give the strain in each direction and the principal strains."),
        ("Calibrating load cells",
         "A load cell with strain gauges is calibrated by applying known loads and recording the output. The calibration curve turns the readings into forces."),
    ],
    "test": [
        ("What changes in a strain gauge when it is strained?",
         [("a", "Its colour"), ("b", "Its price"), ("c", "Its electrical resistance"), ("d", "Its size only")], "c"),
        ("What is the gauge factor?",
         [("a", "The ratio of fractional resistance change to strain"), ("b", "A discount"), ("c", "The paint"), ("d", "A fuse rating")], "a"),
        ("What does a Wheatstone bridge do?",
         [("a", "Heats the part"), ("b", "Paints it"), ("c", "Stores fuel"), ("d", "Turns small resistance changes into a readable voltage")], "d"),
        ("Why is temperature compensation needed?",
         [("a", "Temperature also changes resistance"), ("b", "Temperature paints the gauge"), ("c", "Temperature has no effect"), ("d", "Temperature changes the price")], "a"),
        ("What does a rosette give?",
         [("a", "Strain in several directions at one spot"), ("b", "Only a colour"), ("c", "One number only"), ("d", "A price list")], "a"),
    ],
}
