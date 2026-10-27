"""Measuring Stress by Overcoring: drilling around a small block of rock to let it relax, and reading the strain to work out the stress it held."""
CODE = "mining5_overcore"
BOOK = {
    "title": "Measuring Stress by Overcoring",
    "subtitle": "Stress relief, strain gauges, biaxial cells and stress maps",
    "chapters": [
        ("Relieving the stress",
         "Rock under the ground is always under stress. Overcoring makes a small hole, then drills a larger hole around a sample of rock. Once the sample is freed, it relaxes, and that relaxation tells us the stress it held."),
        ("Strain gauges",
         "Strain gauges are glued to the rock before the overcore is cut. As the core relaxes, the gauges record how much it changes shape. The change is turned into the stress that was there before."),
        ("Biaxial cells",
         "A biaxial cell is a hollow inclusion that is cemented into a pilot hole. It measures the strain in two directions as the rock relaxes. The data give the stress in the plane of the cell."),
        ("Hydraulic fracturing tests",
         "In a hydraulic fracturing test, water is pumped into a sealed section of a borehole until the rock cracks. The pressure needed to open and reopen the crack shows the stress in the rock. The method reaches deeper than most overcoring."),
        ("Stress maps",
         "Measurements from many holes are combined into a stress map of the mine. The map shows where stress is high and where it is low. Engineers use it to place excavations and supports."),
        ("Errors",
         "Drilling can disturb the rock and add microcracks, which change the readings. Gauges can be glued badly or be out of place. Careful work and checks on each measurement keep the errors small."),
    ],
    "test": [
        ("What does overcoring allow us to measure?",
         [("a", "The number of workers in the mine"), ("b", "The price of the drill"), ("c", "The temperature of the office"), ("d", "The stress the rock held before it relaxed")], "d"),
        ("What are strain gauges glued to the rock to record?",
         [("a", "The name of the mine"), ("b", "How much the rock changes shape as it relaxes"), ("c", "The colour of the drill"), ("d", "The number of meals")], "b"),
        ("What does a biaxial cell measure?",
         [("a", "Strain in two directions as the rock relaxes"), ("b", "Sound from the mine"), ("c", "Water quality"), ("d", "Cloud cover")], "a"),
        ("What happens in a hydraulic fracturing test?",
         [("a", "Water is pumped into a sealed section until the rock cracks"), ("b", "Hot oil is poured on the rock"), ("c", "Rock is painted"), ("d", "Rock is dropped from a crane")], "a"),
        ("What can disturb overcoring results?",
         [("a", "Clean and careful work"), ("b", "Checking each measurement"), ("c", "Drilling that adds microcracks, or badly placed gauges"), ("d", "Keeping good records")], "c"),
    ],
}
