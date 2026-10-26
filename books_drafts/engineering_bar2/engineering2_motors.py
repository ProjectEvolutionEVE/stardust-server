"""Electric Motors: turning electricity into motion, and choosing a motor for the job."""
CODE = 'engineering2_motors'
BOOK = {
    "title": 'Electric Motors',
    "subtitle": 'Turning electricity into motion, and choosing a motor for the job',
    "chapters": [
        ('The push on a wire',
         "A wire carrying current inside a magnetic field feels a push at right angles to both the wire and the field. A motor "
         "arranges many coils on a rotor so that these pushes keep turning it round. Most electric motors in use are built this way."),
        ('Stator and rotor',
         "The stator is the fixed part, and it sets up the magnetic field, using magnets or coils. The rotor is the part that turns. "
         "In a brushed DC motor, a commutator feeds current to the coils and switches it as they turn, so the push always turns the "
         "same way. Brushless motors use electronics to do that switching instead."),
        ('Torque and speed',
         "Torque is the turning force. A motor's speed and torque trade off against each other: a motor that spins fast gives less "
         "turning force, and one that gives great force turns slowly. A gearbox matches the two to the job, as the Simple Machines "
         "book describes, slowing the turn and multiplying the torque."),
        ('Power and heat',
         "Power is torque multiplied by speed, in matching units. A motor loses some of its input power as heat in its wire and its "
         "bearings, so no motor is one hundred per cent efficient. That heat has to be carried away, or the insulation on the wire "
         "softens and the motor fails."),
        ('Choosing a motor',
         "Start with the load: how much torque it needs, at what speed, and for how long. Add a margin for starting, which often "
         "takes more torque than running. Check the supply voltage, and the duty cycle, meaning how long the motor may run before it "
         "must rest."),
        ('Motors in ordinary machines',
         "Electric motors drive pumps, fans, winches and the wheels of electric vehicles. The same ideas, the same care over torque "
         "and heat, apply to every one of them. Know the load before you pick the motor."),
    ],
    "test": [
        ("What pushes a wire that carries current inside a magnetic field?",
         [('a', 'Gravity'), ('b', 'The colour of the wire'), ('c', 'Heat in the wire'), ('d', 'A force at right angles to both the wire and the field')], 'd'),
        ("What is the fixed part of a motor called?",
         [('a', 'The rotor'), ('b', 'The stator'), ('c', 'The shaft'), ('d', 'The gearbox')], 'b'),
        ("What is torque?",
         [('a', 'The turning force a motor produces'), ('b', 'The speed of the motor'), ('c', 'The voltage of the supply'), ('d', 'The heat lost in its wire')], 'a'),
        ("Why does a gearbox help a fast motor drive a heavy load?",
         [('a', 'It makes the motor hotter'), ('b', 'It makes the load lighter'), ('c', 'It slows the turn and multiplies the turning force'), ('d', 'It stores electricity')], 'c'),
        ("Why can no motor be one hundred per cent efficient?",
         [('a', 'Its magnets wear out at once'), ('b', 'Some input power is lost as heat in its wire and bearings'), ('c', 'Motors cannot spin'), ('d', 'Electricity carries no energy')], 'b'),
    ],
}
