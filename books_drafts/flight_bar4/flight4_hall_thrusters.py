"""Hall Thrusters and Plasma Drives: electric propulsion that is gentle but lasts a long time."""
CODE = 'flight4_hall_thrusters'
BOOK = {
    "title": "Hall Thrusters and Plasma Drives",
    "subtitle": "Plasma in a field, efficiency, and the satellites that use them",
    "chapters": [
        ("What a Hall thruster is",
         "A Hall thruster uses electricity to turn a gas into plasma, a hot mix of charged particles. A magnetic field traps electrons in a ring, and an electric field pushes the ions out the back. The result is a steady, gentle thrust."),
        ("A Soviet idea",
         "The design grew out of Soviet work in the 1960s and 1970s. It is named after the physicist Edwin Hall, whose effect it uses. Engineers in the Soviet Union built working engines first, and the design later spread around the world."),
        ("Efficiency",
         "A Hall thruster gives much more push for each kilogram of fuel than a chemical rocket does. It is not strong, though. It pushes gently over long periods, so it suits long trips rather than quick launches."),
        ("Satellites that use them",
         "Many modern satellites use Hall thrusters to hold their orbits and to move. Large internet constellations such as Starlink use them. The engines draw their power from solar panels."),
        ("Power needs",
         "A thruster is only as strong as the power it gets. Solar panels give a limited amount, so the size of the thruster must match the size of the power supply. Designers balance power, mass and the job the craft has to do."),
        ("Aiming the push",
         "Thrust always points one way, so a craft turns to aim it. Long, steady burns let small changes in direction add up over time. Patience and careful planning are needed to move a craft exactly where it must go."),
    ],
    "test": [
        ("What does a Hall thruster use to make its thrust?",
         [("a", "Plasma"), ("b", "Coal"), ("c", "Water pumps"), ("d", "Paper")], "a"),
        ("Where did the Hall thruster idea grow?",
         [("a", "Germany in 1945"), ("b", "The Soviet Union in the 1960s and 1970s"), ("c", "Brazil in 2010"), ("d", "On the Moon in 1969")], "b"),
        ("Compared with chemical rockets, a Hall thruster is...",
         [("a", "Only for the Moon"), ("b", "More efficient per kilogram of fuel, but gentle"), ("c", "Always faster to start"), ("d", "Heavier for its push")], "b"),
        ("What powers a Hall thruster on most craft?",
         [("a", "Pedal power"), ("b", "Wind"), ("c", "Sugar"), ("d", "Solar panels")], "d"),
        ("Why are Hall thrusters best for long trips?",
         [("a", "They give strong short bursts"), ("b", "They push gently over long periods"), ("c", "They run on sound"), ("d", "They fly through air")], "b"),
    ],
}
