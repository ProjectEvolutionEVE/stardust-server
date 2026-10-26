"""Science Aboard a Research Vessel: how a research ship keeps its science honest, safe and shared. Science career, bar 2 (Scientist)."""
CODE = 'science2_ship'
BOOK = {
    "title": 'Science Aboard a Research Vessel',
    "subtitle": 'How a research ship keeps its science honest, safe and shared',
    "chapters": [
        ('A ship built for study',
         'A research ship carries instruments, laboratories and crew whose job is to observe and record. The Starship is a large exploratory science and research ship, so its science is part of its daily work, not a side project.'),
        ('Keep a log',
         'On a working research ship, each watch keeps a log of the time, the position, the readings and the events. Logs are kept so that anything can be checked later, by the crew or by someone who was never aboard.'),
        ('Calibrate the instruments',
         'Before a survey, instruments are checked against known standards, and they are checked again afterward. A reading is only as good as the instrument that made it, so a record should always say when the instrument was last calibrated.'),
        ('Keep the data safe',
         'Data are backed up, labelled with the time and place they were taken, and stored so that a second scientist can read and use them. Data that cannot be found or understood later are lost to science, however good they were.'),
        ('Drills and shared rules',
         'Research ships run regular safety drills, so that everyone knows the procedure before an emergency happens. Every person follows the same safety rules, whatever their role or rank.'),
        ('Odd readings',
         'When a reading is strange, write it down exactly as it was seen, flag it to the team and check it before drawing any conclusion. An odd reading is often a fault in the instrument, and a strange finding needs more checks, not a quick answer.'),
    ],
    "test": [
        ('Why does a research ship keep a log?',
         [('a', 'So anything can be checked later'), ('b', 'To count the crew each day'), ('c', 'Because logs are never read'), ('d', 'To replace the instruments')], 'a'),
        ('Why are instruments calibrated against known standards?',
         [('a', 'Because standards make instruments heavier'), ('b', 'Because a reading is only as good as the instrument that made it'), ('c', 'So that instruments never need checking again'), ('d', 'To change the readings')], 'b'),
        ('What should you do with an odd reading?',
         [('a', 'Ignore it, since odd readings are always faults'), ('b', 'Keep it secret until it is proven'), ('c', 'Write it down exactly as seen and check it before concluding'), ('d', 'Change it to match the expected value')], 'c'),
        ('What makes a data set useful to another scientist?',
         [('a', 'It is kept in one copy only'), ('b', 'It is labelled with the time, the place and the method'), ('c', 'It is written in pencil and never dated'), ('d', 'It has no units')], 'b'),
        ('Why do research ships run regular safety drills?',
         [('a', 'So the crew can practise their handwriting'), ('b', 'So everyone knows the procedure before an emergency happens'), ('c', 'Because the drills replace the logs'), ('d', 'To test the instruments')], 'b'),
    ],
}
