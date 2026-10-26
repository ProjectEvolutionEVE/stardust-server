"""Walking Round Before You Fly: a physical inspection of the craft, how to log a defect, and why an open defect can stop a flight."""
CODE = 'flight3b_walk_round'
BOOK = {
    "title": 'Walking Round Before You Fly',
    "subtitle": 'A physical inspection of the craft, how to log a defect, and when a fault stops the flight',
    "chapters": [
        ('Look before you lift',
         'Real pilots walk round the aircraft before every flight. They look for damage, leaks, loose panels and anything out of place. No screen shows everything, so the eyes and hands are part of the check.'),
        ('What to look for',
         'Check the outside of the craft for dents, cracks and scorch marks. Look at the panels, the fittings and the thruster nozzles. Note anything that looks new, loose or wet, and do not assume that someone else has checked it.'),
        ('Log every defect',
         'Write down each defect when you find it, with its place and what you saw. A small note can prevent a large problem later. Record the defect even if you think it is harmless, because only a record can show a pattern.'),
        ('When a defect stops a flight',
         'Some defects are safe to fly with, and some are not. If a defect affects control, power or the seal of a hull, the flight must wait. Do not fly with an open defect that you cannot judge. Ask for a second opinion and keep the craft on the ground.'),
        ('Check the tow and the fuel',
         'Walk round with the fuel bar in mind. A craft that is low on fuel or has a history of trouble needs a closer look. Note the fuel level in your log before each flight.'),
        ('A good habit',
         'The walk-round takes a few minutes, and it protects both the crew and the budget. A defect found on the ground is cheap. The same defect found in space can be very costly.'),
    ],
    "test": [
        ('Why do real pilots walk round the aircraft before a flight?',
         [('a', 'To choose the music'), ('b', 'To look for damage, leaks and loose parts before flying'), ('c', 'To count the passengers'), ('d', 'To check the weather in another country')], 'b'),
        ('Why should you log each defect, even a small one?',
         [('a', 'Because logs replace fuel'), ('b', 'Because logs make the craft lighter'), ('c', 'Because only a record can show a pattern'), ('d', 'Because the Tower forbids notes')], 'c'),
        ('Which kind of defect stops a flight?',
         [('a', 'A small scratch on the paint'), ('b', 'A label that is hard to read'), ('c', 'A slightly dusty window'), ('d', 'A defect that affects control, power or the hull seal')], 'd'),
        ('What should you do if you cannot judge whether a defect is safe?',
         [('a', 'Ask for a second opinion and keep the craft on the ground'), ('b', 'Fly anyway and see what happens'), ('c', 'Hide the defect from the log'), ('d', 'Remove the defect with a hammer')], 'a'),
        ('Why is a defect found on the ground cheaper than one found in space?',
         [('a', 'Because the ground is free'), ('b', 'Because it can be fixed before it becomes a costly problem in flight'), ('c', 'Because the Tower pays for it'), ('d', 'Because the paint is cheaper on the ground')], 'b'),
    ],
}
