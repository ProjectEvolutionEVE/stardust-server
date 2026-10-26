"""Case Study: Piper Alpha. A North Sea platform, the permit-to-work system, a shift handover, the fire, the Cullen report and its lessons."""
CODE = 'flight5_piper_alpha'
BOOK = {
    "title": 'Case Study: Piper Alpha',
    "subtitle": 'An offshore platform fire in the North Sea, and the safety changes it forced',
    "chapters": [
        ('A North Sea platform',
         'Piper Alpha was an oil and gas platform in the North Sea, far from shore. Hundreds of people lived and worked on it in shifts. Its safety depended on many systems working together, and on the people who ran them.'),
        ('Permit to work',
         'A permit to work is a written record that says a job is safe to start, and which parts of the plant must be kept isolated. A permit must be checked and handed over with care. On Piper Alpha the system had gaps that were not clearly understood by everyone.'),
        ('Shift handover',
         'When one shift handed over to the next, important information about work in progress was not passed on fully. A pump that had been worked on was not fully understood by the incoming crew. A missed handover can leave a hidden hazard in place.'),
        ('The fire',
         'In July 1988 a condensate pump was started while a safety valve had been removed for maintenance. Gas leaked and ignited, and fire spread quickly through the platform. Escape was made very difficult, and the rescue was hampered by the spread of the fire. The disaster killed 167 people.'),
        ('The Cullen report',
         "A public inquiry, led by Lord Cullen, examined the disaster in detail. Its report made clear that the company's management of safety had failed. It recommended a new system in which operators must show that their platforms are safe."),
        ('Lessons',
         'Piper Alpha changed how offshore industries plan safety, with clear written safety cases and better communication between shifts. The lesson for players is that a permit or a handover is only as strong as the people who check it.'),
    ],
    "test": [
        ('What is a permit to work?',
         [('a', 'A ticket for a boat'), ('b', 'A visa for a platform'), ('c', 'A written record that says a job is safe to start'), ('d', 'A fuel receipt')], 'c'),
        ('What was the main weakness at the shift handover?',
         [('a', 'The shift was too short for coffee'), ('b', 'The lights were turned off'), ('c', 'The crews were not allowed to talk'), ('d', 'Information about work in progress was not fully passed on')], 'd'),
        ('Where was Piper Alpha located?',
         [('a', 'The North Sea'), ('b', 'The Sahara Desert'), ('c', 'The Pacific Ocean'), ('d', 'The Arctic Circle')], 'a'),
        ("What did the Cullen report say about the platform's safety?",
         [('a', 'No one was responsible'), ('b', "The company's management of safety had failed"), ('c', 'The fire was caused by a bird'), ('d', 'The platform was perfectly safe')], 'b'),
        ('What did the inquiry recommend?',
         [('a', 'Closing all platforms forever'), ('b', 'Removing all shifts'), ('c', 'A system where operators must show their platforms are safe'), ('d', 'Banning written records')], 'c'),
    ],
}
