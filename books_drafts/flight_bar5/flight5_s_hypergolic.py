"""Hypergolic Propellants: fuels that ignite the moment they meet, and why they are both useful and dangerous."""
CODE = "flight5_s_hypergolic"
BOOK = {
    "title": "Hypergolic Propellants",
    "subtitle": "Fuels that ignite on contact, and the trade they bring",
    "chapters": [
        ("Ignition on contact",
         "Hypergolic propellants catch fire the moment a fuel and an oxidiser meet. No spark or igniter is needed. That makes the engine simple to start and reliable when it counts."),
        ("Storable fuels",
         "Common hypergolic pairs stay liquid at ordinary temperatures, so they can sit in tanks for long periods. This suits craft that wait a long time before they fire."),
        ("Apollo and the service module",
         "The Apollo service module carried a hypergolic engine. It moved the spacecraft into and out of orbit around the Moon and sent it home. A reliable start was a key part of that design."),
        ("Titan rockets",
         "The Titan II rocket used hypergolic fuel. It carried the Gemini spacecraft into orbit, and the same family of fuels has long been used in other rockets."),
        ("The cost of toxicity",
         "These fuels are highly toxic and corrosive. They need special suits, careful handling and strict procedures, and each step adds time and money."),
        ("Choosing a trade",
         "Engineers weigh the easy start and long storage against the danger of handling. Today some teams look for safer fuels that still start reliably."),
    ],
    "test": [
        ("What happens when a hypergolic fuel and its oxidiser meet?",
         [("a", "They freeze solid"), ("b", "They ignite without a spark"), ("c", "They turn into water"), ("d", "They need a heater first")], "b"),
        ("What is a main benefit of storable hypergolic fuels?",
         [("a", "They must be used within minutes"), ("b", "They glow in the dark"), ("c", "They can stay in tanks for long periods"), ("d", "They float to the top of the tank")], "c"),
        ("Which Apollo system used a hypergolic engine for its orbit and return burns?",
         [("a", "The service module propulsion system"), ("b", "The lunar rover"), ("c", "The launch tower"), ("d", "The space suits")], "a"),
        ("What is the main drawback of hypergolic fuels?",
         [("a", "They are too cold to use"), ("b", "They hold no energy"), ("c", "They cannot be stored"), ("d", "They are highly toxic and corrosive")], "d"),
        ("Which rocket used hypergolic fuel and carried Gemini into orbit?",
         [("a", "Saturn V"), ("b", "Titan II"), ("c", "The Space Shuttle"), ("d", "A passenger jet")], "b"),
    ],
}
