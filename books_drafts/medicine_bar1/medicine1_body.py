"""Medicine, bar 1: How the Body Works. The main body systems in plain words, for the Medic track."""
CODE = 'medicine1_body'
BOOK = {
    "title": 'How the Body Works',
    "subtitle": 'The heart, lungs, muscles, brain and digestion, and how they work together',
    "chapters": [
        ('Many systems, one body',
         'Your body is a set of systems that work together. Each one has its own job, and none of them can do its work alone. Knowing what each system does is the first step to knowing how to keep yourself well.'),
        ('Heart and blood',
         'The heart is a muscle that pumps blood around the body through a network of tubes called blood vessels. The blood carries oxygen and food to every cell and takes away waste. The heart keeps beating all your life, and it never has to be told to start.'),
        ('Lungs and breathing',
         'The lungs take in air through the nose and mouth. Tiny air sacs in the lungs pass oxygen into the blood, while carbon dioxide passes out to be breathed away. Breathing is mostly automatic, but you can slow it down or speed it up when you choose.'),
        ('Muscles and bones',
         'Bones form a frame that holds the body up and protects delicate parts such as the heart and brain. Muscles are fixed to bones, and when they shorten they pull the bones and make you move. Bones also make new blood cells inside their marrow.'),
        ('Brain and nerves',
         'The brain is the control centre. It takes in messages from your senses, decides what to do, and sends signals along the nerves to your muscles. Nerves are long fibres that carry those signals quickly around the body.'),
        ('Digestion',
         'Digestion breaks food down into small pieces the body can use. The stomach and intestines absorb the useful parts into the blood, and the liver helps to process them. Whatever the body cannot use leaves as waste.'),
    ],
    "test": [
        ('What does the heart do?',
         [('a', 'It stores air for the lungs'), ('b', 'It pumps blood around the body'), ('c', 'It breaks food into pieces'), ('d', 'It sends messages to the eyes')], 'b'),
        ('What do the lungs pass into the blood?',
         [('a', 'Carbon dioxide'), ('b', 'Water'), ('c', 'Oxygen'), ('d', 'Iron')], 'c'),
        ('What do bones make inside their marrow?',
         [('a', 'Blood cells'), ('b', 'Nerves'), ('c', 'Muscle fibres'), ('d', 'Air sacs')], 'a'),
        ('What do nerves carry around the body?',
         [('a', 'Food'), ('b', 'Signals'), ('c', 'Blood'), ('d', 'Heat')], 'b'),
        ('Where are the useful parts of food absorbed into the blood?',
         [('a', 'In the brain'), ('b', 'In the lungs'), ('c', 'In the stomach and intestines'), ('d', 'In the bones')], 'c'),
    ],
}
