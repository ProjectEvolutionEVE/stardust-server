"""Calibration and Traceable Standards: reference materials, calibration curves, traceability, drift and certificates."""
CODE = "science4_method_calibration"
BOOK = {
    "title": "Calibration and Traceable Standards",
    "subtitle": "Making sure a measurement can be trusted anywhere",
    "chapters": [
        ("Reference materials", "A reference material is a substance with a known, certified property, such as its purity or concentration. Labs use them to check their measurements. They act as an anchor for many results."),
        ("Calibration curves", "A calibration curve plots the instrument's response against known standards. An unknown sample's response is then read off the curve. The curve must cover the range of the samples measured."),
        ("Traceability chains", "Traceability links a measurement to a national or international standard through an unbroken chain of comparisons. Each link states its uncertainty. A traceable result can be compared with results from other labs."),
        ("Calibration intervals", "Instruments are recalibrated at set intervals to catch drift. The interval depends on how stable the instrument is and how it is used. Records show when each item is next due."),
        ("Drift", "Drift is a slow change in an instrument's readings over time. It can come from wear, from temperature changes or from electronic components changing their behaviour. Regular checks against standards reveal drift early."),
        ("Certificates", "A calibration certificate records the standard used, the results, the uncertainty and the date. It is evidence that a measurement is traceable. Keep certificates on file for audits."),
    ],
    "test": [
        ("What is a reference material?",
         [("a", "A type of paper"), ("b", "A substance with a known, certified property used to check measurements"), ("c", "A chemical that smells"), ("d", "A form for leave")], "b"),
        ("What is a calibration curve?",
         [("a", "A bent glass tube"), ("b", "A map of a lab"), ("c", "A list of staff"), ("d", "A plot of instrument response against known standards")], "d"),
        ("What does traceability link a measurement to?",
         [("a", "A national or international standard through an unbroken chain of comparisons"), ("b", "The colour of the instrument"), ("c", "The lab's car park"), ("d", "The number of pages in a manual")], "a"),
        ("What is drift?",
         [("a", "A fast crash of a machine"), ("b", "A method of sampling"), ("c", "A slow change in an instrument's readings over time"), ("d", "A rule about lab coats")], "c"),
        ("What does a calibration certificate record?",
         [("a", "The lunch order"), ("b", "The name of the cleaner"), ("c", "The standard used, the results, the uncertainty and the date"), ("d", "The price of the building")], "c"),
    ],
}
