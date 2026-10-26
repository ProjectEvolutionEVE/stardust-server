"""Mapping Mars and the Moon: how the maps of other worlds are made, from orbit and from the ground."""
CODE = 'navigation3b_other_worlds'
BOOK = {
    "title": "Mapping Mars and the Moon",
    "subtitle": "How the maps of other worlds are made, from orbit and from the ground",
    "chapters": [
        ("No sea to start from",
         "Mars and the Moon have no sea to use as a level surface. Mapmakers agree on a reference shape for each world, and heights are measured from that agreed surface. The first step is always to decide the reference."),
        ("Laser heights from orbit",
         "On Mars, the Mars Orbiter Laser Altimeter on the Mars Global Surveyor timed laser pulses down to the surface and built a height map over several years. It showed that Olympus Mons, the largest known volcano on Mars, is about 22 kilometres high, roughly two and a half times the height of Mount Everest above sea level."),
        ("The Moon's height map",
         "The Lunar Reconnaissance Orbiter, launched in 2009, carries a laser altimeter called LOLA. It maps the height of the Moon in fine detail, showing craters, ridges and the deep floors of craters near the poles."),
        ("Pictures from many angles",
         "Orbiting cameras photograph the same ground from slightly different angles. Those pairs of pictures allow photogrammetry, so the height of the ground can be worked out without anyone standing on it."),
        ("Names and agreed positions",
         "The International Astronomical Union approves the names of features on the Moon and the planets. It also agrees the coordinate systems in use. A feature name in one catalogue is then the same name in every map."),
        ("No satellite navigation on Mars",
         "Earth's satellite navigation does not reach Mars. Landers and rovers fix their positions by comparing what their cameras see with orbital images and maps made earlier. That is a strong reason to build good maps before the arrival, not after it."),
    ],
    "test": [
        ("What did MOLA, the laser altimeter on Mars Global Surveyor, do?",
         [("a", "Measured the height of the Martian surface with laser pulses"), ("b", "Filmed the Martian sky"), ("c", "Carried rock samples back to Earth"), ("d", "Sent radio messages to the Sun")], "a"),
        ("About how high is Olympus Mons, the largest known volcano on Mars?",
         [("a", "About 2 kilometres"), ("b", "About 22 kilometres"), ("c", "About 220 kilometres"), ("d", "About 2,200 kilometres")], "b"),
        ("How does Olympus Mons compare with Mount Everest's height above sea level?",
         [("a", "About the same"), ("b", "About one-tenth"), ("c", "About two and a half times"), ("d", "About twenty times")], "c"),
        ("Why can Earth's satellite navigation not be used to fix positions on Mars?",
         [("a", "Because Mars is a gas giant"), ("b", "Because Earth's navigation satellites do not serve Mars"), ("c", "Because Mars has too much air"), ("d", "Because the Moon blocks the signal")], "b"),
        ("What does the International Astronomical Union do for the maps of other worlds?",
         [("a", "Approves the names of features and agrees the coordinate systems"), ("b", "Sells the maps"), ("c", "Builds the rovers"), ("d", "Sets the price of land")], "a"),
    ],
}
