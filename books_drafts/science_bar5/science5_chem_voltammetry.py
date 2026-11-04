"""Voltammetry and Electroanalytical Methods: sweeping a voltage to read chemical signals."""
CODE = "science5_chem_voltammetry"
BOOK = {
    "title": "Voltammetry and Electroanalytical Methods",
    "subtitle": "Cyclic voltammetry, peak currents, electrodes and detection limits",
    "chapters": [
        ("Reading chemistry with voltage", "Voltammetry measures the current that flows through an electrode as the voltage is changed. The shape of the current curve tells us about the chemistry at the electrode. It is a sensitive way to study redox reactions."),
        ("Cyclic voltammetry", "In cyclic voltammetry, the voltage is swept up and then back down in a triangle shape. The current peaks show when species are oxidised or reduced. The shape and spacing of the peaks reveal how reversible a reaction is."),
        ("Peak currents", "The size of a peak current depends on the concentration of the species and on how fast the voltage is swept. In many simple cases the peak current rises with the square root of the scan rate. Concentration can be measured from peak height."),
        ("Electrode materials", "Electrodes are made from materials such as glassy carbon, gold or platinum. Each one has its own range of voltages and its own surface behaviour. Choosing the right material matters for a clean signal."),
        ("Detection limits", "The detection limit is the lowest concentration that can be reliably measured. It depends on background current, noise and the sensitivity of the method. Better electrodes and techniques lower the limit."),
        ("Sensor design", "Electrochemical sensors use voltammetry to detect substances such as glucose or pollutants. A good sensor is selective, stable and cheap to make. Field tests show whether a sensor works outside the lab."),
    ],
    "test": [
        ("What does voltammetry measure?",
         [("a", "The weight of a sample"), ("b", "The colour of a solution"), ("c", "The current through an electrode as the voltage changes"), ("d", "The age of a rock")], "c"),
        ("What shape is the voltage sweep in cyclic voltammetry?",
         [("a", "A straight line that never returns"), ("b", "A circle with no end"), ("c", "A spiral into the sky"), ("d", "A triangle, up and back down")], "d"),
        ("What does a peak current depend on?",
         [("a", "The colour of the wire only"), ("b", "The concentration of the species and the scan rate"), ("c", "The day of the week"), ("d", "The length of the lab bench")], "b"),
        ("What is the detection limit?",
         [("a", "The highest voltage a device can take"), ("b", "The lowest concentration that can be reliably measured"), ("c", "The time it takes to boil water"), ("d", "The number of electrons in a jar")], "b"),
        ("What are electrochemical sensors used for?",
         [("a", "Detecting substances such as glucose or pollutants"), ("b", "Making a gold coin from sand"), ("c", "Carrying people through the air"), ("d", "Melting ice in the sun")], "a"),
    ],
}
