"""Battery-Electric Haulage and Charging: running mine trucks on batteries, with attention to battery cycles, charging, heat, fleet planning and payback."""
CODE = "mining5_bev"
BOOK = {
    "title": "Battery-Electric Haulage and Charging",
    "subtitle": "Battery cycles, charging stations, energy use, heat and payback",
    "chapters": [
        ("Trucks on batteries",
         "Battery-electric haul trucks run on large battery packs instead of diesel. They produce no exhaust underground, which helps ventilation and worker health. They also need a different plan for charging and power."),
        ("Battery cycles",
         "A battery loses capacity slowly with each charge and discharge cycle, and with age. How hard a battery is worked, and how hot it is kept, affects how fast it ages. Fleet plans must allow for this loss."),
        ("Charging stations",
         "Trucks charge at fixed stations or through swap systems. Charging takes time, and the stations need a steady power supply. The number and place of stations decide how many trucks can keep running."),
        ("Energy use and heat",
         "Heavy trucks use a lot of energy on steep grades, and heat builds up in the battery. Cooling is needed to keep the battery safe and long lived. Routes that let trucks regenerate energy on descent help the total."),
        ("Fleet planning",
         "A fleet plan matches the number of trucks to the haul cycle and charging time. It must allow for spare trucks and for battery replacement. Testing a small fleet first shows what the real numbers are."),
        ("Payback",
         "Battery trucks cost more to buy, but they save on fuel and maintenance. The payback period depends on fuel prices, power costs and how many hours the trucks run. A fair payback estimate uses real numbers for the site."),
    ],
    "test": [
        ("What is a battery-electric haul truck powered by?",
         [("a", "Large battery packs instead of diesel"), ("b", "Steam from a kettle"), ("c", "Wind alone"), ("d", "Hand cranks")], "a"),
        ("What happens to a battery as it goes through many cycles?",
         [("a", "It gets larger every time"), ("b", "It never changes"), ("c", "It slowly loses capacity"), ("d", "It turns into wood")], "c"),
        ("Why must cooling be planned for batteries?",
         [("a", "Cold makes all batteries explode"), ("b", "Heat makes the truck heavier"), ("c", "Cooling is only for the cab"), ("d", "Heat shortens battery life and must be kept under control")], "d"),
        ("What does a fleet plan match?",
         [("a", "The number of birds to the trees"), ("b", "The number of trucks to the haul cycle and charging time"), ("c", "The colour of the cabs to the weather"), ("d", "The price of coffee to the miners")], "b"),
        ("What does a fair payback estimate use?",
         [("a", "Real numbers for the site, such as fuel and power costs"), ("b", "Guesses from a film"), ("c", "Only the price of the paint"), ("d", "The number of stars in the sky")], "a"),
    ],
}
