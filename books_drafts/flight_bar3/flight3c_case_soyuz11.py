"""Case Study: Soyuz 11, 1971. A valve that opened too early, and why crews now wear suits for launch and return."""
CODE = "flight3c_case_soyuz11"
BOOK = {
    "title": "Case Study: Soyuz 11, 1971",
    "subtitle": "A valve that opened too early, and why crews now wear suits for launch and return",
    "chapters": [
        ("Home from a station",
         "In June 1971, three cosmonauts, Georgi Dobrovolsky, Vladislav Volkov and Viktor Patsayev, came home from the Salyut 1 space station in a Soyuz capsule. They had spent more than three weeks aboard the station. The landing itself was made by the capsule's automatic systems."),
        ("The valve",
         "Before the return, the descent module separated from the rest of the craft. A valve in the capsule was meant to balance the pressure inside. In this flight it opened at the moment of separation, and the cabin air began to escape."),
        ("No suits",
         "The crew had no pressure suits. The cabin lost its air within moments, and the three men died inside the capsule. The capsule landed safely under its automatic systems, but the crew had already been lost."),
        ("Changes that followed",
         "After this loss, Soyuz crews began to wear pressure suits for launch and return. The valve and the separation sequence were redesigned so that the cabin could not be opened to space at that moment. These changes remain part of how Soyuz crews fly today."),
        ("Layers of safety",
         "A safe system has more than one layer of protection. Here a single valve, opened at the wrong moment, removed the whole margin of safety. Designers ask what happens if a part opens or fails at the wrong time, not only what happens when it works."),
        ("A pilot's lesson",
         "Know where your safety comes from. Whether it is a suit, a seal or a checklist, treat it as the thing that keeps you alive. Check it before every return, and never assume it is working because it was working last time."),
    ],
    "test": [
        ("Where had the Soyuz 11 crew been before they came home?",
         [("a", "On the Moon"), ("b", "On the surface of Mars"), ("c", "Aboard the Salyut 1 space station"), ("d", "In a training pool on Earth")], "c"),
        ("What went wrong during the return?",
         [("a", "The parachute was red"), ("b", "A valve opened early and the cabin air leaked out"), ("c", "The engine was too quiet"), ("d", "The crew sang too loudly")], "b"),
        ("Why did the crew not survive?",
         [("a", "Their suits were too bright"), ("b", "The cabin lost its air, and they had no pressure suits"), ("c", "They landed in water"), ("d", "Their food ran out")], "b"),
        ("What do Soyuz crews wear for launch and return now?",
         [("a", "Swimwear"), ("b", "Ordinary tracksuits"), ("c", "Nothing special"), ("d", "Pressure suits")], "d"),
        ("What does a safe system need?",
         [("a", "A single very strong part"), ("b", "More than one layer of protection"), ("c", "No checks at all"), ("d", "Luck")], "b"),
    ],
}
