"""Crack growth and the Paris law: cyclic loading, growth per cycle, life prediction, inspection intervals and repair planning."""
CODE = "engineering4_paris_law"
BOOK = {
    "title": "Crack Growth and the Paris Law",
    "subtitle": "Cyclic loading, growth per cycle and planning repairs",
    "chapters": [
        ("Cracks grow under repeated loads",
         "A part that is loaded and unloaded many times can have a crack grow a little each cycle. The crack may stay tiny for a long time and then grow fast. This is fatigue crack growth, and it is common in aircraft, bridges and machines."),
        ("Growth per cycle",
         "The Paris law describes how much a crack grows in each load cycle. Growth per cycle rises with the stress intensity range, a measure of the load swing at the crack tip. The rule is a power law, so growth speeds up as the crack gets larger."),
        ("Predicting life",
         "Engineers add up the growth per cycle over the expected number of cycles to predict how long a part lasts. They start from a known or assumed crack size and stop at a critical size. The result is an estimate that depends on the inputs used."),
        ("Inspection intervals",
         "A life prediction sets how often a part must be inspected. Inspections must be frequent enough to find a crack before it reaches the critical size. Engineers set the interval with a margin for uncertainty."),
        ("Planning repairs",
         "When a crack is found, engineers decide whether to repair, replace or monitor the part. A repair may remove the crack or stop it from growing, for example by drilling a hole at its tip. The choice depends on the crack size, the load and the cost."),
        ("Keeping records",
         "Records of loads, inspections and repairs help predict how a part will behave. Over time the data can refine the predicted growth rates. Good records make maintenance planning more reliable."),
    ],
    "test": [
        ("What is fatigue crack growth?", [("a", "A paint crack"), ("b", "A crack that closes on its own"), ("c", "A crack that grows a little each time a part is loaded and unloaded"), ("d", "A crack that never grows")], "c"),
        ("What does the Paris law describe?", [("a", "How much a crack grows in each load cycle"), ("b", "The price of steel"), ("c", "The colour of a weld"), ("d", "The number of bolts in a joint")], "a"),
        ("Why does a crack grow faster as it gets larger?", [("a", "Because cracks never change"), ("b", "Because cracks gain weight"), ("c", "Because cracks get cooler"), ("d", "Because the growth rule is a power law and the crack tip sees more stress")], "d"),
        ("What sets the inspection interval?", [("a", "The weather on the day"), ("b", "The life prediction, with a margin for uncertainty"), ("c", "The colour of the part"), ("d", "The number of staff in the office")], "b"),
        ("What is one way a repair can stop a crack growing?", [("a", "Adding more load"), ("b", "Painting over the crack"), ("c", "Drilling a hole at the crack tip"), ("d", "Ignoring it")], "c"),
    ],
}
