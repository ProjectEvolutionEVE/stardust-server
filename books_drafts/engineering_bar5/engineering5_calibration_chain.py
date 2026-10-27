"""Calibration Hierarchy and Traceability Chains: how every measuring instrument links back to a national standard."""
CODE = "engineering5_calibration_chain"
BOOK = {
    "title": "Calibration Hierarchy and Traceability Chains",
    "subtitle": "From national standards down to the shop-floor gauge",
    "chapters": [
        ("Why calibrate", "A measurement is only useful if it can be compared with a known reference. Calibration compares an instrument with a standard, so its readings can be trusted."),
        ("The hierarchy", "National standards sit at the top. Reference instruments are calibrated against them, and working instruments are calibrated against the reference instruments. Each level is one step down."),
        ("Traceability", "A traceability chain is the unbroken link from a working instrument back to the national standard. Each link is recorded, so anyone can follow the chain."),
        ("Calibration intervals", "Instruments drift with use, so they are checked again at set intervals. Heavy use or harsh conditions usually mean shorter intervals."),
        ("Certificates", "A calibration certificate records the result, the uncertainty and the standard used. Customers and auditors use it to check that the instrument was fit for use."),
        ("The money side", "Calibration costs time and money. A bad measurement can cost much more in scrap, disputes and failed inspections, so calibration is usually cheap insurance."),
    ],
    "test": [
        ("What is traceability?", [("a", "An unbroken link from an instrument back to a national standard"), ("b", "A type of electrical cable"), ("c", "A kind of paint for gauges"), ("d", "A fast drill bit")], "a"),
        ("What sits at the top of the calibration hierarchy?", [("a", "The shop floor"), ("b", "The staff room"), ("c", "National standards"), ("d", "The packing area")], "c"),
        ("Why are instruments calibrated again at intervals?", [("a", "They drift with use"), ("b", "They get lighter with age"), ("c", "They need fresh paint"), ("d", "They become cheaper over time")], "a"),
        ("What does a calibration certificate record?", [("a", "The name of the canteen"), ("b", "The result, the uncertainty and the standard used"), ("c", "The weather on the day"), ("d", "The parts list")], "b"),
        ("Why can a poor measurement cost more than calibration?", [("a", "It can lead to scrap, disputes and failed inspections"), ("b", "Calibration is always free"), ("c", "It makes the room bigger"), ("d", "It changes the colour of the parts")], "a"),
    ],
}
