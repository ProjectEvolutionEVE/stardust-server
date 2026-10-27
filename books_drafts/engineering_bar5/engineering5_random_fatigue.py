"""Random Vibration Fatigue: estimating fatigue from loads that vary randomly, like a road or a rocket."""
CODE = "engineering5_random_fatigue"
BOOK = {
    "title": "Random Vibration Fatigue",
    "subtitle": "Estimating fatigue from loads that vary randomly, like a road or a rocket",
    "chapters": [
        ("Random loads",
         "Road bumps, wind gusts and rocket noise do not repeat in a regular pattern. Their size changes at random, so fatigue must be estimated in a statistical way."),
        ("Power spectral density",
         "The power spectral density shows how the energy of a random load is spread across frequencies. It is the usual way to describe such loads."),
        ("Miner's rule for random loads",
         "The spectrum gives the expected number of cycles of each size, which feeds into Miner's rule to add up the damage. Predictions for random loads depend on this count."),
        ("The Dirlik method",
         "The Dirlik method estimates the distribution of cycle sizes from the spectrum, without needing a full time record. It is widely used for random vibration fatigue."),
        ("Road and rocket noise",
         "Vehicles see vibration from the road, and rockets see intense acoustic noise at launch. Both can be turned into power spectra and then used for fatigue checks."),
        ("Checking the result",
         "Compare the predicted life with a test on a shaker table, which reproduces the random load. Repeated tests give more confidence in the prediction."),
    ],
    "test": [
        ("What is a power spectral density?",
         [("a", "A price"), ("b", "A colour chart"), ("c", "How the energy of a random load is spread across frequencies"), ("d", "A weight measure")], "c"),
        ("Why are random loads described statistically?",
         [("a", "Because they repeat exactly"), ("b", "Because their size changes at random"), ("c", "Because they are zero"), ("d", "Because they are painted")], "b"),
        ("What does the Dirlik method estimate?",
         [("a", "The distribution of cycle sizes from a spectrum"), ("b", "The price of steel"), ("c", "The weather"), ("d", "A paint code")], "a"),
        ("What is a shaker table used for?",
         [("a", "Testing a random load in the laboratory"), ("b", "Boiling a kettle"), ("c", "Riding a bicycle"), ("d", "Climbing a ladder")], "a"),
        ("What does Miner's rule need from the spectrum for a random load?",
         [("a", "The colour"), ("b", "The buyer's name"), ("c", "The date"), ("d", "The expected number of cycles of each size")], "d"),
    ],
}
