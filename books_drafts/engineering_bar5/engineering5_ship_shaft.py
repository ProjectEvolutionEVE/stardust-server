"""Ship Propulsion Shafts and Thrust Bearings: alignment, thrust loads, bearing design, vibration and maintenance access."""
CODE = "engineering5_ship_shaft"
BOOK = {
    "title": "Ship Propulsion Shafts and Thrust Bearings",
    "subtitle": "Alignment, thrust, bearings and vibration at sea",
    "chapters": [
        ("The shaft's job",
         "The propeller shaft carries turning power from the engine to the propeller. It usually runs through the hull in a sealed tube at the stern. Its strength and its straightness both matter a great deal."),
        ("Thrust",
         "The propeller pushes the ship forward, and that push travels back along the shaft. A thrust bearing takes this force along the length of the shaft and passes it on to the hull, so the shaft itself does not slide."),
        ("Alignment",
         "The engine, gearbox and shaft must line up closely. If they do not, loads concentrate on bearings and couplings, and those parts wear fast. Alignment is checked when the ship is built and again over its working life."),
        ("Vibration",
         "Every shaft has speeds at which it vibrates strongly, called critical speeds. Designers keep normal running speeds well away from them. An uneven flow of water behind the hull can also push the shaft into vibration."),
        ("Bearing design",
         "Bearings need a thin film of oil or water to keep metal surfaces apart. The lubricant must stay clean, cool and at the right pressure. A bearing that runs hot is a warning sign that needs attention."),
        ("Maintenance access",
         "Shafts and bearings must be reachable for inspection and repair. Good designs leave room to draw parts out without cutting into the hull. Planned checks cost far less than failures at sea."),
    ],
    "test": [
        ("What does the propeller shaft carry?",
         [("a", "Fresh water"), ("b", "Electricity to the lights"), ("c", "Air to the crew"), ("d", "Turning power from the engine to the propeller")], "d"),
        ("What does a thrust bearing take?",
         [("a", "The ship's weight only"), ("b", "Heat from the galley"), ("c", "The push along the shaft from the propeller"), ("d", "Waves hitting the bow")], "c"),
        ("What happens when shaft alignment is poor?",
         [("a", "The ship floats higher"), ("b", "The paint lasts longer"), ("c", "Fuel burns more slowly"), ("d", "Loads concentrate and bearings wear fast")], "d"),
        ("What is a critical speed?",
         [("a", "The top speed of a ship"), ("b", "The speed of sound in water"), ("c", "A legal speed limit"), ("d", "A shaft speed where it vibrates strongly")], "d"),
        ("What keeps metal parts apart inside a bearing?",
         [("a", "A clean oil or water film"), ("b", "Dry air"), ("c", "Sand"), ("d", "Rust")], "a"),
    ],
}
