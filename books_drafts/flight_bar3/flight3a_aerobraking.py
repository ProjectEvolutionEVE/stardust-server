"""Aerobraking: using a planet's thin upper air to shed speed without burning fuel."""
CODE = 'flight3a_aerobraking'
BOOK = {
    "title": 'Aerobraking: Slowing Down with Air',
    "subtitle": "Using a planet's thin upper air to shed speed without burning fuel",
    "chapters": [
        ('Braking costs fuel',
         "Slowing a craft usually means burning fuel, and fuel is heavy and costly to carry. Every kilogram that must be lifted to orbit adds to the bill at launch. Engineers look for other ways to shed speed."),
        ('Skimming the top of the air',
         "Aerobraking uses a planet's thin upper atmosphere as a brake. The craft dips into the air at the lowest point of its orbit, and the drag slows it a little on each pass. Its path shrinks from a long oval into a rounder, lower orbit."),
        ('Many small passes',
         "Each pass takes away only a small amount of speed, so the work can take months. Mars Global Surveyor used aerobraking to settle into its final orbit around Mars in the late 1990s. Patience takes the place of fuel."),
        ('Heat is the risk',
         "Air heats a craft as it rubs through, so the craft must carry shields and be watched closely. Dip too deep and the craft can overheat. Dip too shallow and the drag is too weak to help at all."),
        ('The trade',
         "Aerobraking swaps fuel for time and careful flying. The craft is cheaper to run, because less fuel is carried, but the mission takes longer and needs more checks. A pilot counts both costs before choosing it."),
        ('Where it fits',
         "Aerobraking works only where there is air up high. Out in open space, with no air at all, a craft cannot use this brake, so the pilot must use a burn instead. Choose the brake that the place allows."),
    ],
    "test": [
        ("What is the main idea of aerobraking?",
         [('a', "Using a planet's upper air to slow down"), ('b', 'Freezing the craft to stop it'), ('c', 'Filling the tanks in space'), ('d', "Speeding up with the Sun's light")], 'a'),
        ('Why do engineers like aerobraking?',
         [('a', 'It makes the craft heavier'), ('b', 'It removes the need for any shield'), ('c', 'It makes the trip faster'), ('d', 'It saves fuel that would otherwise have to be carried')], 'd'),
        ('Why must aerobraking happen over many passes?',
         [('a', 'The air changes each day'), ('b', 'The craft must rest between passes'), ('c', 'Each pass removes only a small amount of speed'), ('d', 'The planet moves away')], 'c'),
        ('What is the main danger of dipping too deep?',
         [('a', 'The craft may overheat'), ('b', 'The craft becomes too slow'), ('c', 'The fuel freezes'), ('d', 'The hold runs out of air')], 'a'),
        ('Where can aerobraking not be used?',
         [('a', 'Where there is air up high'), ('b', 'Around Mars'), ('c', 'In open space, where there is no air'), ('d', 'Near the ground')], 'c'),
    ],
}
