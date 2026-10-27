"""Response Spectrum Method in Seismic Analysis: how engineers estimate the peak response of a building to earthquake shaking using modes and a spectrum."""
CODE = "engineering5_srs"
BOOK = {
    "title": "Response Spectrum Method in Seismic Analysis",
    "subtitle": "Estimating peak earthquake response from modes and a design spectrum",
    "chapters": [
        ("What a spectrum is", "A response spectrum plots the largest response of a simple oscillator against its natural period, for one earthquake or one design rule. Short-period oscillators respond to some shaking and long-period ones to other shaking. The curve summarises that behaviour for all periods."),
        ("Spectral acceleration", "Spectral acceleration is the peak acceleration a simple oscillator would feel at a given period. Engineers read it from the design spectrum for the site. It is the main input to the method."),
        ("Modes of the structure", "A building has several natural modes, each with its own shape and period. For each mode, the spectrum gives a peak response. The method treats each mode separately, which is why it is cheaper than a full time-history analysis."),
        ("Combining the modes", "The peak responses of the modes do not all happen at the same instant. Engineers combine them with rules such as the square root of the sum of squares, called SRSS, or the complete quadratic combination, called CQC. The rule is chosen to suit how close the modes are in period."),
        ("Base shear", "The base shear is the total horizontal force at the bottom of the structure. It is the main number that tells the designer how strong the foundation and the lower storeys must be. Mode combination gives it."),
        ("Design ground motion", "The design spectrum comes from the seismic code for the area, based on the local hazard, the soil and the importance of the building. The method is only as good as that input, so the choice of ground motion matters a great deal."),
    ],
    "test": [
        ("What does a response spectrum plot?", [("a", "The price of construction materials"), ("b", "The sound of a building"), ("c", "The number of windows"), ("d", "The peak response of simple oscillators against their natural period")], "d"),
        ("What is spectral acceleration?", [("a", "The speed of a lift"), ("b", "The rate of rainfall"), ("c", "The peak acceleration a simple oscillator would feel at a given period"), ("d", "The power of a pump")], "c"),
        ("What is the total horizontal force at the bottom of a structure called?", [("a", "Base shear"), ("b", "Rooftop load"), ("c", "Paint pressure"), ("d", "Wind chill")], "a"),
        ("Which rules are used to combine modal responses?", [("a", "Colour and weight"), ("b", "Price and time"), ("c", "North and south"), ("d", "SRSS and CQC")], "d"),
        ("What sets the design spectrum?", [("a", "The colour of the building"), ("b", "The seismic code, based on local hazard, soil and building importance"), ("c", "The shop that sells the glass"), ("d", "The age of the architect")], "b"),
    ],
}
