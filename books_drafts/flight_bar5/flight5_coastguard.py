"""Search and Rescue: search plans and patterns, coordination, the Coast Guard, real cases and training."""
CODE = 'flight5_coastguard'
BOOK = {
    "title": 'Search and Rescue',
    "subtitle": 'How people are found at sea and on land, and brought home',
    "chapters": [
        ('Plans',
         'A search starts with a plan. Searchers estimate where a missing vessel or person may be, using the last known position, drift, wind and time. A good plan puts the most effort where the chance of finding someone is highest.'),
        ('Patterns',
         'Searchers fly or sail in set patterns, such as parallel lines or expanding squares, to cover an area evenly. Each pattern is chosen for the size of the area and the type of search. Careful patterns mean fewer gaps.'),
        ('Coordination',
         'Many agencies and vessels may take part in one search. A coordinator keeps track of every unit, its area and its progress. Clear communication keeps the searchers from covering the same ground twice.'),
        ('The Coast Guard',
         'Coast Guards run search and rescue along many coasts, and they keep ships and aircraft ready at short notice. They work with navies, fishing boats and local teams. Their work saves many lives each year.'),
        ('Cases',
         'Real rescues show how planning, speed and teamwork save lives. Searchers often find people by careful reading of the sea and the weather. Each case is studied afterward to improve the next search.'),
        ('Training',
         'Search and rescue crews train often, practising searches, first aid and the handling of boats in rough seas. Training keeps skills fresh and teams working as one. For players, the lesson is that a good search is a plan, a pattern and a team, all working together.'),
    ],
    "test": [
        ('What does a search plan begin with?',
         [('a', 'A party'), ('b', 'A new boat'), ('c', 'A map of the moon'), ('d', 'An estimate of where the missing person or vessel may be')], 'd'),
        ('What is an expanding square?',
         [('a', 'A type of search pattern'), ('b', 'A kind of sail'), ('c', 'A ship name'), ('d', 'A brand of radio')], 'a'),
        ('What does a search coordinator do?',
         [('a', 'Sails the boat alone'), ('b', 'Keeps track of every unit, its area and its progress'), ('c', 'Cooks food for the crew'), ('d', 'Stops all searching')], 'b'),
        ('What does the Coast Guard do?',
         [('a', 'Builds ocean liners'), ('b', 'Sells maps'), ('c', 'Runs search and rescue along many coasts'), ('d', 'Runs a film studio')], 'c'),
        ('Why is each rescue studied afterward?',
         [('a', 'To choose a new ship name'), ('b', 'To set the price of fuel'), ('c', 'To find a new hobby'), ('d', 'To improve the next search')], 'd'),
    ],
}
