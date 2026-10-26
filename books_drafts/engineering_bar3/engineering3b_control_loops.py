"""Control loops and PID: how a machine measures its own results, corrects itself, and settles on the target."""
CODE = 'engineering3b_control_loops'
BOOK = {
    "title": 'Control Loops and PID',
    "subtitle": 'How a machine watches its own results, corrects itself, and settles on the target',
    "chapters": [
        ('Sense, decide, act',
         'A control loop measures something, compares it with a target, and acts to close the gap. The target is the setpoint, the measurement comes from a sensor, the decision is made by a controller, and the action is carried out by an actuator such as a valve or a motor. The loop repeats many times a second.'),
        ('Feedback',
         'Feedback means the result of an action is measured and used to decide the next action. A thermostat is the simplest example: it switches a heater on below the setpoint and off above it. Feedback keeps a process near its target even when the outside world changes.'),
        ('On and off control',
         'Simple on-off control works, but it swings. The temperature overshoots the target, then undershoots it, and the heater keeps switching on and off. A dead band, a small gap between the switch-on and switch-off points, cuts down how often it switches.'),
        ('Proportional control',
         'A proportional controller acts in proportion to the error, which is the gap between the setpoint and the measurement. The bigger the gap, the harder it pushes. It is gentle near the target, but on its own it can stop short and leave a steady offset, because it needs some error in order to act.'),
        ('Integral and derivative',
         'The integral term adds up the error over time, so a steady offset is slowly pushed away. The derivative term reacts to how fast the error is changing, and it eases the action as the target nears, which damps overshoot. Together with proportional action, they make the classic PID controller.'),
        ('Tuning and stability',
         'Each of the three terms has a gain that must be set. Too much gain makes the system oscillate or even run out of control, and too little makes it slow and sluggish. Tune one term at a time, test with a small change of setpoint, and write down the settings that work.'),
    ],
    "test": [
        ('What is the setpoint in a control loop?',
         [('a', 'The sensor that does the measuring'), ('b', 'The target value the loop works toward'), ('c', 'The valve itself'), ('d', 'The fault log')], 'b'),
        ('What does a thermostat do?',
         [('a', 'Stores heat in a battery'), ('b', 'Paints the room'), ('c', 'Measures wind speed'), ('d', 'Switches a heater on below the target and off above it')], 'd'),
        ('What is the main problem with simple on-off control?',
         [('a', 'The value swings above and below the target'), ('b', 'It never switches at all'), ('c', 'It uses too little power'), ('d', 'It cannot be measured')], 'a'),
        ('What does proportional control leave behind if it acts alone?',
         [('a', 'A bigger error than before'), ('b', 'A broken sensor'), ('c', 'A steady offset from the target'), ('d', 'No error at all')], 'c'),
        ('What does the derivative term do in a PID controller?',
         [('a', 'Adds up the error over time'), ('b', 'Sets the target'), ('c', 'Measures the temperature'), ('d', 'Reacts to how fast the error is changing, and eases the action near the target')], 'd'),
    ],
}
