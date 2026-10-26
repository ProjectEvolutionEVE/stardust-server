"""Reaction Wheels and Momentum: turning a craft without pushing on anything outside it."""
CODE = 'flight3a_reaction_wheels'
BOOK = {
    "title": 'Reaction Wheels and Momentum',
    "subtitle": 'Turning a craft without pushing on anything outside it',
    "chapters": [
        ('Spin one way, turn the other',
         "A reaction wheel is a heavy wheel inside the craft. When its spin speeds up one way, the craft turns the other way. The turn needs no fuel, because the push acts between parts of the same craft."),
        ('Momentum is kept',
         "Spinning momentum stays the same unless something outside acts on the craft. Speed the wheel up one way, and the craft turns the opposite way by the same amount. This is the conservation of angular momentum."),
        ('Three wheels, three axes',
         "Most craft use three wheels set at right angles, so they can turn the craft about any axis. Some add a fourth wheel as a spare. Each wheel adds weight and draws power, so the designers keep the count as low as they safely can."),
        ('Momentum builds up',
         "Small outside forces, such as the push of sunlight or a trace of drag, keep feeding momentum into the wheels. Over time they spin faster and faster, until the wheels are saturated and cannot take any more. The craft then cannot turn them any further."),
        ('Unloading the wheels',
         "To bring the wheels back to a safe speed, the craft fires thrusters, or uses magnetic coils that push against the planet's field. This is called desaturation. It uses some fuel or power, so the pilot plans it in advance."),
        ('Power and wear',
         "Wheels need power to speed up and to slow down, so the power budget must include them. A wheel that wobbles or rubs gives a warning sign in its readings, and pilots watch those readings for signs of wear."),
    ],
    "test": [
        ('How does a reaction wheel turn a craft without fuel?',
         [('a', 'It pushes on the air outside'), ('b', 'It changes its spin, and the craft turns the other way'), ('c', 'It releases a puff of gas'), ('d', 'It drags against the Sun')], 'b'),
        ('Which law of motion does a reaction wheel rely on?',
         [('a', 'Conservation of angular momentum'), ('b', "Ohm's law for circuits"), ('c', 'The law of the market'), ('d', 'The rule that craft always spin')], 'a'),
        ('Why do many craft use three wheels set at right angles?',
         [('a', 'To make the craft heavier'), ('b', 'To hold the food supplies'), ('c', 'To hide the craft from light'), ('d', 'To turn the craft about any axis')], 'd'),
        ('What does it mean when a wheel is saturated?',
         [('a', 'It is painted'), ('b', 'It is glowing'), ('c', 'It has spun up so much that it cannot take more momentum'), ('d', 'It has no power left')], 'c'),
        ('What is desaturation?',
         [('a', 'Using thrusters or magnetic coils to unload a wheel\'s momentum'), ('b', 'Cooling the hold'), ('c', 'Removing crew from the craft'), ('d', 'Drying out the wheels')], 'a'),
    ],
}
