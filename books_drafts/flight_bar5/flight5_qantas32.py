"""Case Study: Qantas 32. An uncontained engine failure on an Airbus A380, the damage and checks, the landing and the lessons."""
CODE = 'flight5_qantas32'
BOOK = {
    "title": 'Case Study: Qantas 32',
    "subtitle": 'An engine failure on the largest airliner, and a safe landing',
    "chapters": [
        ('Engine failure',
         'In November 2010 an Airbus A380, the largest passenger airliner in service, lost one of its four engines soon after take-off from Singapore. The engine broke apart, and pieces of it flew out and damaged the wing.'),
        ('Damage',
         'The damage cut fuel lines and harmed several systems, and warning messages came in large numbers. The crew had to sort out which systems still worked and which had failed. The wing and its controls had been hit in several places.'),
        ('Checks',
         'The crew worked through the checklists one step at a time. Many warnings were false or linked to the same cause, so the crew had to find the true problem. Careful checks kept the aircraft under control while they decided where to land.'),
        ('Landing',
         'The crew returned to Singapore and landed the aircraft safely. Everyone on board survived, although some people were injured. The landing shows how much a well-trained crew can do with a badly damaged plane.'),
        ('Teamwork',
         'The crew shared tasks and kept each other informed. Several pilots on the flight deck helped manage the load of checks and decisions. Good communication kept small problems from becoming big ones.'),
        ('Lessons',
         'The investigation led to changes in engine design and inspection, and to better guidance for crews facing many warnings at once. The lesson for players is that a long list of warnings should be sorted by cause before action, and that a calm, shared checklist is the best tool in a crisis.'),
    ],
    "test": [
        ('What type of aircraft was Qantas 32?',
         [('a', 'An Airbus A380'), ('b', 'A Boeing 747'), ('c', 'A Cessna light aircraft'), ('d', 'A DC-3')], 'a'),
        ('What failed on the Qantas 32 flight?',
         [('a', 'The cabin lights'), ('b', 'One of the four engines'), ('c', 'The toilets'), ('d', 'The seat belts')], 'b'),
        ('Where did the aircraft return to land?',
         [('a', 'Sydney'), ('b', 'Tokyo'), ('c', 'Singapore'), ('d', 'Auckland')], 'c'),
        ('Why was it hard to find the true problem?',
         [('a', 'There were no warnings at all'), ('b', 'The cockpit was dark'), ('c', 'The crew had no checklists'), ('d', 'Many warnings were false or linked to the same cause')], 'd'),
        ('What is a key lesson of this incident?',
         [('a', 'A long list of warnings should be sorted by cause before action'), ('b', 'Warnings should always be ignored'), ('c', 'Checklists slow down any crisis'), ('d', 'Crews should land at once without checks')], 'a'),
    ],
}
