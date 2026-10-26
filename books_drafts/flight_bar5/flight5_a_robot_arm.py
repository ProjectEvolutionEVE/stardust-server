"""Robot Arms: the long mechanical arms that move loads, capture craft and help crews in space."""
CODE = 'flight5_a_robot_arm'
BOOK = {
    "title": 'Robot Arms',
    "subtitle": 'Long mechanical arms for loads, capture and crew support',
    "chapters": [
        ('Canadarm',
         'The Canadarm was a long robotic arm flown on the Space Shuttle. It lifted satellites out of the cargo bay, and it helped capture and move large parts. Its success led to many later arms.'),
        ('Canadarm2 and Dextre',
         'Canadarm2 is a larger arm on the space station, and it can walk along the station by moving from one attachment point to another. Dextre is a smaller two-armed robot that does fine tasks at the end of Canadarm2.'),
        ('Control',
         'Robot arms are controlled by people on the ground or inside the station, and some steps are automated. Operators check each move against the limits of the joints and the loads. Smooth motion keeps the arm and the load safe.'),
        ('Loads',
         'A robot arm must handle the loads it lifts, and it must not strain its joints. The mass and the position of the load change how the arm moves. Engineers test each lift on the ground first.'),
        ('Capture',
         'A robot arm can capture a free-flying craft, grabbing a fitting so the craft can be moved or berthed. Capture is one of the hardest moves, because the target is moving. Careful timing and sensing make it possible.'),
        ('Support for crews',
         'Robot arms also help crews during spacewalks, by holding parts and positioning the astronaut. They reduce the strain of work outside the craft. The arm is a partner in the job.'),
    ],
    "test": [
        ('What was the Canadarm?',
         [('a', 'A long robotic arm flown on the Space Shuttle'), ('b', 'A wind turbine'), ('c', 'A water pump'), ('d', 'A crew bunk')], 'a'),
        ('What is Dextre?',
         [('a', 'A kind of rocket fuel'), ('b', 'A smaller two-armed robot that does fine tasks at the end of Canadarm2'), ('c', 'A type of radio'), ('d', 'A crew member')], 'b'),
        ('Why is capturing a free-flying craft hard?',
         [('a', 'Because the arm is painted'), ('b', 'Because the Sun is too bright'), ('c', 'Because the target is moving'), ('d', 'Because the craft has no fuel')], 'c'),
        ('What must engineers check before a lift?',
         [('a', 'The colour of the load'), ('b', 'The date on a calendar'), ('c', 'The name of the pilot'), ('d', 'The arm and the load stay within their limits')], 'd'),
        ('How do robot arms help during spacewalks?',
         [('a', 'By holding parts and positioning the astronaut'), ('b', 'By making the crew sleep'), ('c', 'By turning off the air'), ('d', 'By stopping the radio')], 'a'),
    ],
}
