"""Power Systems: real-world ways of making, storing and moving electrical power. Background knowledge only."""
CODE = "power"
BOOK = {
    "title": "Power Systems",
    "subtitle": "Making, storing and sharing electrical power",
    "chapters": [
        ("Power and energy",
         "Power is how fast energy is used, measured in watts. Watts = volts × amps. Energy is power over time: a "
         "1,000-watt heater running for one hour uses one kilowatt-hour. Every machine needs both enough power and "
         "enough energy to keep going."),
        ("Sunlight",
         "Solar panels turn sunlight straight into electricity. Near Earth's old orbit, sunlight brings about 1,361 "
         "watts onto every square metre. It weakens fast with distance: out at Jupiter, about five times farther "
         "from the Sun, it is roughly 27 times weaker. Most panels are made from silicon."),
        ("Generators",
         "Spin a coil of copper wire past a magnet and electricity flows. That is a generator, and it is how most of "
         "the world's power has been made. Strong magnets made with neodymium help small generators and motors do a "
         "lot of work."),
        ("Batteries and fuel cells",
         "A battery stores energy as chemistry and gives it back as electricity; lithium makes light, powerful "
         "batteries. A fuel cell joins hydrogen and oxygen to make electricity, and its only waste is water."),
        ("Nuclear power",
         "Splitting heavy atoms such as uranium (fission) releases huge amounts of heat from a little fuel, and "
         "thorium can be used as a fuel too. Joining light atoms (fusion) powers the Sun. Helium-3 is a fusion fuel "
         "scientists have studied for a long time, but on Earth it has stayed research, not a working power plant."),
        ("Sharing power safely",
         "Power travels along cables, and thick copper cables waste less of it as heat. Breakers cut the power when "
         "something goes wrong. Spare capacity and backups keep the important systems running if one source fails."),
        ("Power aboard",
         "The raw materials behind these power sources are in the Raw Materials Catalogue: silicon, copper, "
         "neodymium, lithium, hydrogen, oxygen, uranium, thorium and helium-3. A blueprint that makes, stores or "
         "carries power lists them like any other material."),
    ],
    "test": [
        ("What is power measured in?",
         [("a", "Kilograms"), ("b", "Watts"), ("c", "Metres"), ("d", "Litres")], "b"),
        ("What happens to sunlight as you move farther from the Sun?",
         [("a", "It gets weaker"), ("b", "It gets stronger"), ("c", "It stays the same"), ("d", "It turns blue")], "a"),
        ("What does a generator spin past a coil of wire?",
         [("a", "A magnet"), ("b", "A rock"), ("c", "Water"), ("d", "A battery")], "a"),
        ("What is the only waste from a hydrogen fuel cell?",
         [("a", "Smoke"), ("b", "Slag"), ("c", "Water"), ("d", "Ash")], "c"),
        ("What is splitting heavy atoms like uranium called?",
         [("a", "Fusion"), ("b", "Smelting"), ("c", "Fission"), ("d", "Casting")], "c"),
    ],
}
