"""Echolocation for Spatial Orientation: how bats build a picture of their surroundings from the echoes of their own calls."""
CODE = 'navigation5_bat_echolocation'
BOOK = {
    "title": 'Echolocation for Spatial Orientation',
    "subtitle": 'The call, echo delay, the brain map, aerial hunting, acoustic principles and robotics',
    "chapters": [
        ('The call',
         'Many bats make high-pitched sounds, often too high for people to hear. They send out a call and listen for the echo bouncing back from objects around them.'),
        ('Echo delay',
         'The time between the call and the echo tells the bat how far away an object is. Sound travels at a known speed in air, so a short delay means a near object and a long delay means a far one.'),
        ('A map in the brain',
         'The bat brain turns the timing and direction of echoes into a map of the space around it. This map helps the bat move in dark places and avoid obstacles while flying fast.'),
        ('Aerial hunting',
         'Some bats catch insects in mid-air using echolocation. They adjust their calls as they close in, so the echo gives a fast update on position. The method works even in total darkness.'),
        ('Acoustic principles',
         'Sound bounces differently off different surfaces and shapes. Bats use these differences to tell objects apart, and some can detect very fine structures. The principles of sound reflection make this possible.'),
        ('Robotics',
         'Engineers have used echo principles in sonar and in some robot sensors. Studying bats has helped designers build small, low-power systems that can sense their surroundings in the dark.'),
    ],
    "test": [
        ('What does a bat do with the echo of its call?',
         [('a', 'Throws it away'), ('b', 'Sings it back to the moon'), ('c', 'Writes it on a map'), ('d', 'Uses it to build a picture of the space around it')], 'd'),
        ('What does a longer delay between call and echo mean?',
         [('a', 'The object is farther away'), ('b', 'The object is closer'), ('c', 'The bat is asleep'), ('d', 'The air is cold')], 'a'),
        ('Why do bats often make calls that people cannot hear?',
         [('a', 'Because the calls are too quiet to matter'), ('b', 'Because calls are written in ink'), ('c', 'Because the calls are high pitched, above the range of human hearing'), ('d', 'Because bats have no ears')], 'c'),
        ('What does the bat brain do with echo timing and direction?',
         [('a', 'Throws them away'), ('b', 'Turns them into a map of the space around it'), ('c', 'Paints them on the wall'), ('d', 'Stores them as songs only')], 'b'),
        ('What have engineers learned from bat echolocation?',
         [('a', 'Ideas for sonar and small sensing systems'), ('b', 'A recipe for bread'), ('c', 'A new type of paint'), ('d', 'A way to grow trees')], 'a'),
    ],
}
