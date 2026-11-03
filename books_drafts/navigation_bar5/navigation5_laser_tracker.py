"""Laser Trackers in Metrology: spherical targets, angle and distance measurement, tracking, accuracy, setup and industrial uses."""
CODE = 'navigation5_laser_tracker'
BOOK = {
    "title": 'Laser Trackers in Metrology',
    "subtitle": 'How a laser follows a target to measure large objects with care',
    "chapters": [
        ('Spherical targets',
         'The tracker follows a reflector mounted in a metal sphere. The laser bounces back from the reflector, so the tracker always knows where the target is. The sphere can be moved from point to point.'),
        ('Angle and distance',
         'A laser tracker measures two things to locate a point: the distance to the target and the angles to it. Together these give the target position in three dimensions.'),
        ('Tracking',
         'Tracking means following a moving target and updating its position continuously. The instrument turns to keep the beam on the reflector, and the position updates as the target moves.'),
        ('Accuracy',
         'Accuracy depends on the quality of the instrument, its calibration, and the conditions around it. Good work records the accuracy and checks it against known standards.'),
        ('Setup',
         'A careful setup matters. The tracker must be stable, placed with a clear line of sight, and allowed to settle to the temperature of the room. Poor setup spoils even a good instrument.'),
        ('Industrial uses',
         'Laser trackers are used to check large parts, such as aircraft components, ship sections and machine tools. They help make sure each part fits its design before it is used.'),
    ],
    "test": [
        ('What is a spherical target on a laser tracker?',
         [('a', 'A reflector mounted in a ball that sends the laser beam back to the tracker'), ('b', 'A ball to play with'), ('c', 'A type of antenna'), ('d', 'A rubber seal')], 'a'),
        ('What two things does a laser tracker measure to locate a point?',
         [('a', 'Colour and weight'), ('b', 'Distance and angles'), ('c', 'Speed and time'), ('d', 'Heat and sound')], 'b'),
        ('What does tracking mean for a laser tracker?',
         [('a', 'Printing tracks on paper'), ('b', 'Laying cable on the ground'), ('c', 'Digging for minerals'), ('d', 'Following a moving target and updating its position continuously')], 'd'),
        ('What is a common industrial use of a laser tracker?',
         [('a', 'Making bread'), ('b', 'Growing crops'), ('c', 'Checking the position of large parts such as aircraft components'), ('d', 'Cutting hair')], 'c'),
        ('What affects the accuracy of a laser tracker?',
         [('a', 'Only the colour of the target'), ('b', 'Only the shoes of the operator'), ('c', 'Setup, temperature and the quality of the calibration'), ('d', 'The name of the factory')], 'c'),
    ],
}
