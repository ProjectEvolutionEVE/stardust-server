"""Batteries in Space: how spacecraft store power, how cycles and depth wear batteries down, and the heat lessons from a 2013 airliner fault."""
CODE = "flight4_batteries"
BOOK = {
    "title": "Batteries in Space",
    "subtitle": "Storing power through sunlight and shadow",
    "chapters": [
        ("Why batteries", "A craft in orbit may spend part of each orbit in shadow, where its solar panels make no power. Batteries carry the craft through the dark part."),
        ("Chemistry types", "Several battery types have flown in space. Nickel-hydrogen and nickel-cadmium cells were common for many years. Lithium-ion cells now hold more energy for their weight and are widely used."),
        ("Cycles and depth", "Each charge and discharge is a cycle. A battery that is drained deeply each time wears out faster than one that is only drained a little. Engineers limit how deep each cycle goes to make the battery last longer."),
        ("Heat limits", "Batteries work best within a narrow range of temperatures. Too much heat can damage them, and in the worst cases it can start a dangerous runaway reaction, called thermal runaway."),
        ("Charge control", "A charge controller decides how fast and how far the battery charges. It protects the cells from overcharge, and it keeps each cell in the pack balanced with the others."),
        ("Lessons and end of life", "A 2013 battery fault on a Boeing 787 airliner taught engineers to guard against thermal runaway with better cell designs and containment. Over the years, every battery loses capacity, so the mission plan must allow for the end of its life."),
    ],
    "test": [
        ("Why do craft in orbit need batteries?", [("a", "To make the paint shine"), ("b", "To heat the crew's food only"), ("c", "To make the craft heavier for fun"), ("d", "To carry them through the part of each orbit in shadow")], "d"),
        ("What does a deep discharge do to a battery's life?", [("a", "It wears the battery out faster"), ("b", "It makes the battery last forever"), ("c", "It has no effect"), ("d", "It makes the battery invisible")], "a"),
        ("What is thermal runaway?", [("a", "A fast run around the deck"), ("b", "A dangerous, self-feeding heating reaction in a battery"), ("c", "A cold snap"), ("d", "A type of radio")], "b"),
        ("What does a charge controller do?", [("a", "Paints the battery"), ("b", "Plays music"), ("c", "Protects the cells from overcharge and keeps the pack balanced"), ("d", "Grows plants")], "c"),
        ("What kind of battery holds more energy for its weight and is widely used now?", [("a", "Lithium-ion"), ("b", "Wood"), ("c", "Paper"), ("d", "Ice")], "a"),
    ],
}
