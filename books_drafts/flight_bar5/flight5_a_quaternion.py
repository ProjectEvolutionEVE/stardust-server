"""Rotations and Quaternions: how a craft's turn is described without the trap of gimbal lock."""
CODE = 'flight5_a_quaternion'
BOOK = {
    "title": 'Rotations and Quaternions',
    "subtitle": 'Describing a turn without the trap of gimbal lock',
    "chapters": [
        ('Turning in three ways',
         'A craft can turn about three axes, like an aircraft that pitches, rolls and yaws. A simple way to describe this is with three angles, called Euler angles. They are easy to picture and widely taught.'),
        ('Gimbal lock',
         'With Euler angles, there are positions where two of the axes line up. At these positions one degree of freedom is lost, and the description can jump or fail. This is called gimbal lock.'),
        ('Quaternions in words',
         'A quaternion is a set of four numbers that describes a turn. It does not suffer from gimbal lock, and it combines turns smoothly. Many modern spacecraft and games use quaternions for this reason.'),
        ('Why they are used',
         "Quaternions are compact and quick to combine. A computer can update a craft's attitude with them many times a second. They make the software simpler and more reliable."),
        ('Software and care',
         'Quaternions must be kept at unit length, and the software must check this. A small drift can build up if it is not corrected. Good code keeps the numbers tidy.'),
        ('Use today',
         'Attitude control on most modern craft uses quaternions or a close relative. They are a working tool, not a curiosity. Engineers learn them early because they are everywhere.'),
    ],
    "test": [
        ('How many axes can a craft turn about?',
         [('a', 'One'), ('b', 'Two'), ('c', 'Three'), ('d', 'Ten')], 'c'),
        ('What is gimbal lock?',
         [('a', 'A lock on a fuel tank'), ('b', 'A crew door lock'), ('c', 'A way to stop the Moon'), ('d', 'A loss of one degree of freedom when two axes line up')], 'd'),
        ('How many numbers does a quaternion use to describe a turn?',
         [('a', 'Four'), ('b', 'Two'), ('c', 'Seven'), ('d', 'Twelve')], 'a'),
        ('Why do many spacecraft use quaternions?',
         [('a', 'They avoid gimbal lock and combine turns smoothly'), ('b', 'They make the craft louder'), ('c', 'They change the colour of the paint'), ('d', 'They replace fuel')], 'a'),
        ('What must software check about a quaternion?',
         [('a', 'That it is painted'), ('b', 'That it stays at unit length'), ('c', 'That it is printed on paper'), ('d', 'That it is read aloud')], 'b'),
    ],
}
