"""Case Study: Costa Concordia. A close pass by an island, grounding, delayed evacuation, the captain's conduct and the lessons."""
CODE = 'flight5_costa_concordia'
BOOK = {
    "title": 'Case Study: Costa Concordia',
    "subtitle": 'A cruise ship grounded off an Italian island in 2012',
    "chapters": [
        ('A close pass',
         'In January 2012 the cruise ship Costa Concordia sailed very close to the island of Giglio, off the coast of Italy. The pass was not part of the planned route, and it put the ship in shallow water near the rocks.'),
        ('Grounding',
         'The ship struck rocks near the island, tearing a long gash in its hull. Water flooded into the lower decks, and the ship tilted onto its side. The grounding was the start of a chain of errors.'),
        ('Delay',
         'The evacuation was slow to begin, and the crew gave passengers unclear and sometimes wrong information. Some lifeboats could not be launched because the ship was tilted so far. Many people were still aboard when the order to leave came.'),
        ('Evacuation',
         'Passengers and crew were brought off by lifeboats and by boats from the island. The evacuation took several hours, and many people were rescued from the water and the decks. Some people died in the chaos.'),
        ("The captain's conduct",
         "The captain left the ship early, and was later found to have acted against his duty to stay aboard until all were off. He was convicted in court for his conduct. The case showed how much a captain's choices can shape a disaster."),
        ('Lessons',
         "The disaster led to closer attention to passenger safety drills. It showed that a crew must be trained to lead an evacuation with clear information. For players, the lesson is that a captain's first duty is to the people in his care."),
    ],
    "test": [
        ('What was the name of the cruise ship?',
         [('a', 'Costa Concordia'), ('b', 'Titanic'), ('c', 'Endurance'), ('d', 'Victoria')], 'a'),
        ('Near which island did the ship sail too close?',
         [('a', 'Hawaii'), ('b', 'Giglio'), ('c', 'Madagascar'), ('d', 'Tahiti')], 'b'),
        ('What was the main problem with the lifeboats during the evacuation?',
         [('a', 'They were painted gold'), ('b', 'They were too many to count'), ('c', 'Some could not be launched because the ship was tilted so far'), ('d', 'They were sold before the trip')], 'c'),
        ('What did the court find about the captain?',
         [('a', 'He was given a medal'), ('b', 'He was never asked about it'), ('c', 'He was found to be asleep at the bow'), ('d', 'He was convicted for his conduct')], 'd'),
        ('What is a key lesson of Costa Concordia?',
         [('a', "A captain's first duty is to the people in his care"), ('b', 'Captains should leave first'), ('c', 'Passengers never need information'), ('d', 'Close passes are always safe')], 'a'),
    ],
}
