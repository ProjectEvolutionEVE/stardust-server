"""Systems Engineering: turning a mission need into a design that works as one whole, and proving it does."""
CODE = 'flight5_systems_eng'
BOOK = {
    'title': 'Systems Engineering',
    'subtitle': 'From a mission need to a proven whole',
    'chapters': [
        ('The whole picture', 'Systems engineering looks at the whole mission, not only its parts. It turns a need into requirements, a design and a proof that the design meets the need.'),
        ('Requirements and trade studies', 'Requirements say what the system must do. Trade studies compare the options for meeting them. Each decision is recorded with the reasons behind it.'),
        ('The V-model', 'The V-model shows design going down one side and testing coming up the other. Each level of design has a matching level of test. This keeps the tests tied to what the design promised.'),
        ('Interfaces', 'Parts meet at interfaces, and most integration problems happen there. Define each interface clearly, with its units, sizes and signals. Check that the parts fit before they are built.'),
        ('Verification', 'Verification asks whether the system was built right. Validation asks whether it is the right system for the need. Both are needed before the mission is trusted.'),
        ('The NASA handbook', 'NASA publishes a Systems Engineering Handbook that describes these practices in detail. It is free to read, and many organisations use it as a guide.'),
    ],
    'test': [
        ('What does systems engineering look at?', [('a', 'Only one part at a time'), ('b', 'The whole mission, from need to proof'), ('c', 'Only the paint of the hull'), ('d', 'Only the timetable of meals')], 'b'),
        ('What does the V-model show?', [('a', 'A letter in a name'), ('b', "A ship's sail"), ('c', 'A map of rivers'), ('d', 'Design going down one side and testing coming up the other')], 'd'),
        ('Where do most integration problems happen?', [('a', 'Only in the paint'), ('b', 'Only in the crew quarters'), ('c', 'At interfaces between parts'), ('d', 'In the weather')], 'c'),
        ('What is verification?', [('a', 'Asking whether the system was built right'), ('b', 'Choosing a colour'), ('c', 'Counting the crew'), ('d', 'Sending a message')], 'a'),
        ('What is validation?', [('a', 'Painting the badge'), ('b', 'Setting the time of lunch'), ('c', 'Hiring a new captain'), ('d', 'Asking whether it is the right system for the need')], 'd'),
    ],
}
