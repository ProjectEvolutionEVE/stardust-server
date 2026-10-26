"""Thrusters and the Short Pulse: small firings, the shortest push a thruster can make, and why pulse length matters."""
CODE = 'flight3a_thruster_pulses'
BOOK = {
    "title": 'Thrusters and the Short Pulse',
    "subtitle": 'Small firings, the shortest possible push, and why pulse length matters',
    "chapters": [
        ('Small thrusters, small pushes',
         "Thrusters are small engines around the hull that push the craft in a chosen direction. Each firing gives a small change in motion. Used together, they can turn or move a craft with real precision."),
        ('The shortest push',
         "Every thruster has a shortest firing it can make reliably. This is called its minimum impulse bit. A firing shorter than that is not dependable, so a plan must allow for it."),
        ('Pulse length',
         "A longer pulse gives a bigger change in motion. The pilot sets the length of each pulse to match the change needed, not just the number of firings. A long firing wastes fuel when a shorter one would do."),
        ('The deadband',
         "Attitude control often uses a deadband: a small range of pointing error the craft allows before it fires. A wide deadband saves fuel but is less precise. A narrow deadband is precise but fires more often, and so uses more fuel."),
        ('Fuel by the pulse',
         "Every firing uses fuel, and the amount depends on how long the thruster fires. Count the firings and their lengths together, then check the tank. A plan that looks cheap on paper can still run the tank dry."),
        ('Wheels and thrusters together',
         "Reaction wheels and thrusters work as a team. Wheels handle small, steady turns with no fuel, and thrusters handle the bigger jobs and unload the wheels when they are full. A good plan uses each for what it does best."),
    ],
    "test": [
        ('What is a thruster?',
         [('a', 'A small engine that pushes the craft in a chosen direction'), ('b', 'A cooling fan for the hull'), ('c', 'A kind of window in the Tower'), ('d', 'A ration pack for the crew')], 'a'),
        ('What is a minimum impulse bit?',
         [('a', 'The price of the fuel'), ('b', 'The number of crew on board'), ('c', 'The shortest firing a thruster can make reliably'), ('d', 'The biggest burn the craft can make')], 'c'),
        ('Why must a pilot set the length of each pulse with care?',
         [('a', 'Pulses change colour'), ('b', 'A longer pulse gives a bigger change and can waste fuel'), ('c', 'Every pulse is always the same'), ('d', 'Pulses cannot be timed')], 'b'),
        ('What is a deadband?',
         [('a', 'A band of cloth'), ('b', 'A tank of water'), ('c', 'A type of window'), ('d', 'A range of pointing error allowed before the thruster fires')], 'd'),
        ('What job do the wheels and the thrusters share?',
         [('a', 'Wheels make small steady turns with no fuel, and thrusters do the big jobs and unload the wheels'), ('b', 'Thrusters paint the hull'), ('c', 'Wheels fire rockets'), ('d', 'Nothing, one of them is enough')], 'a'),
    ],
}
