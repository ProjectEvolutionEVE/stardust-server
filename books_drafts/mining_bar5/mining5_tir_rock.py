"""Thermal Infrared Spectroscopy of Rocks: reading the heat a rock gives off to tell its minerals apart from a distance."""
CODE = "mining5_tir_rock"
BOOK = {
    "title": "Thermal Infrared Spectroscopy of Rocks",
    "subtitle": "Emissivity, silicate signals, field instruments and their limits",
    "chapters": [
        ("Heat that carries a fingerprint",
         "Every warm object gives off infrared heat. The amount given off at each wavelength depends on the material. Rocks have strong and clear patterns in the thermal infrared, usually between about 8 and 14 micrometres."),
        ("Emissivity features of silicates",
         "Emissivity is how well a surface gives off heat compared with a perfect radiator. Silicate minerals, the main building blocks of most rock, have sharp dips in emissivity at particular wavelengths. These dips work like fingerprints."),
        ("Quartz and carbonate signals",
         "Quartz-rich rock and carbonate rock, such as limestone, each show their own signal. A carbonate signal is different from a silicate one, so the two can be told apart. Clear calibration makes the signal easier to match."),
        ("Field instruments",
         "Handheld and mounted instruments measure rock surfaces up close. Airborne and satellite sensors cover much wider areas at lower detail. Each kind of instrument suits a different scale of question."),
        ("Calibration",
         "Measurements are checked against reference samples of known composition. Temperature, sun angle and the surface itself change the readings, so calibration must be repeated under the same conditions. Careless calibration leads to wrong rock names."),
        ("Mapping and limits",
         "Maps of rock types can be built from the signals across an area. Vegetation, soil and water cover the rock and hide its signal, so the method works best on bare rock. It sees only the surface, not the rock hidden below."),
    ],
    "test": [
        ("In what part of the spectrum do rock fingerprints mainly appear here?",
         [("a", "The thermal infrared, about 8 to 14 micrometres"), ("b", "Visible light only"), ("c", "Radio waves"), ("d", "X-rays only")], "a"),
        ("What is emissivity?",
         [("a", "How well a surface gives off heat compared with a perfect radiator"), ("b", "The weight of a rock sample"), ("c", "The number of cracks in a rock"), ("d", "The price of a mineral")], "a"),
        ("What do silicate minerals show?",
         [("a", "No signal at all"), ("b", "Only a loud sound"), ("c", "Sharp dips in emissivity at particular wavelengths"), ("d", "A bright blue colour")], "c"),
        ("Why must calibration be repeated under the same conditions?",
         [("a", "Because rocks change colour each day"), ("b", "Because the instrument must be painted"), ("c", "Because the samples must be cooked"), ("d", "Because temperature and sun angle change the readings")], "d"),
        ("When does thermal infrared mapping work best?",
         [("a", "Under thick vegetation"), ("b", "On bare rock, since vegetation and soil hide the signal"), ("c", "Under deep water"), ("d", "Inside a closed box")], "b"),
    ],
}
