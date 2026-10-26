"""Naval Customs of Command: ranks, watches, the ship's log, discipline, the captain's table and tradition."""
CODE = 'flight5_naval_customs'
BOOK = {
    "title": 'Naval Customs of Command',
    "subtitle": 'How a ship is run, day by day, through ranks, watches and tradition',
    "chapters": [
        ('Ranks',
         'A ship is run through a clear chain of ranks, from the most junior sailor to the captain. Each rank has its duties and its authority. Everyone knows whom to report to, and whom they answer for.'),
        ('Watches',
         'A ship keeps watch around the clock, and the day is split into watches of about four hours. Shorter dog watches of two hours let the crew rotate their shifts. Watchkeepers are responsible for the ship while they are on duty.'),
        ("The ship's log",
         'The ship keeps a log that records the course, speed, weather and events of each watch. The log is an official record that is kept honestly and checked. Good logs help the crew learn and help investigators after any problem.'),
        ('Discipline',
         'Discipline keeps a crew safe and working together. Rules are clear, and punishments follow a set process. Fairness is seen as a key part of good command, because a crew that trusts its leaders works better.'),
        ("The captain's table",
         "Traditionally the captain dines separately, and his table is a place for formal courtesy and for meeting guests. Such customs mark the captain's responsibility for the whole ship. The custom is also a way to keep the captain in touch with the officers."),
        ('Tradition',
         'Naval traditions carry lessons from many years of sea service. They keep standards steady across generations and make new crew feel part of a long story. For players, the lesson is that good habits, once learned, make a crew safer and more united.'),
    ],
    "test": [
        ('What is a watch at sea?',
         [('a', 'A type of anchor'), ('b', 'A kind of sail'), ('c', 'A period on duty, usually about four hours'), ('d', 'A mooring rope')], 'c'),
        ('What is a dog watch?',
         [('a', 'A watch kept only by dogs'), ('b', 'A watch in the engine room'), ('c', 'A sleeping period'), ('d', 'A shorter watch of about two hours')], 'd'),
        ("What does the ship's log record?",
         [('a', 'The course, speed, weather and events of each watch'), ('b', 'Only the menu'), ('c', "The names of the crew's pets"), ('d', "The ship's paint colours")], 'a'),
        ('Why is fairness in discipline important?',
         [('a', 'Because punishments are fun'), ('b', 'Because a crew that trusts its leaders works better'), ('c', 'Because rules are never needed'), ('d', 'Because officers do not need to report')], 'b'),
        ('What do naval traditions do for a crew?',
         [('a', 'They end all rules'), ('b', "They replace the ship's log"), ('c', 'They keep standards steady across generations'), ('d', 'They remove the chain of command')], 'c'),
    ],
}
