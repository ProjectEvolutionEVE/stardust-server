"""Autonomy: letting a craft make decisions on its own, and why checking it matters more than trusting it."""
CODE = 'flight5_a_autonomy'
BOOK = {
    "title": 'Autonomy',
    "subtitle": 'Onboard decisions, and how they are checked',
    "chapters": [
        ('Why autonomy',
         'Radio signals take time to travel, and some decisions must be made faster than a ground team can respond. Autonomy means the craft makes some decisions on its own. It is needed for distant missions and for fast tasks such as docking.'),
        ('Mars rovers',
         'Mars rovers drive with onboard software that picks safe routes around rocks and slopes. They can travel further each day because they do not wait for each move to be approved from Earth. Their drives are still planned and checked by people.'),
        ('Autonomous docking',
         'Some craft dock to a station with little human control in the final steps. The software reads sensors, measures the distance and speed, and steers the craft into place. Each step is set out in advance and has limits.'),
        ('Verification',
         'Autonomous software must be tested in many situations, including faults. Engineers run simulations and tests on real hardware. The goal is to show that the software does the right thing, every time.'),
        ('Trust',
         'Trust in autonomy is earned slowly, through records of success. Teams often keep a human in the loop for the most important choices. They also give the craft a safe fallback if the software is unsure.'),
        ('Limits',
         'Autonomy cannot do everything. It works within its design, and it can fail in cases nobody foresaw. Good autonomy knows its limits and hands control back to people when it should.'),
    ],
    "test": [
        ('Why do distant craft need autonomy?',
         [('a', 'Because they want to be alone'), ('b', 'Because radio signals take time and some decisions are quick'), ('c', 'Because the Sun turns them off'), ('d', 'Because they cannot hear anything')], 'b'),
        ('What do Mars rovers use onboard software to do?',
         [('a', 'Bake bread'), ('b', 'Send radio songs'), ('c', 'Pick safe routes around rocks and slopes'), ('d', 'Paint the wheels')], 'c'),
        ('What kind of tasks are automated in autonomous docking?',
         [('a', 'Cooking meals'), ('b', 'Writing letters'), ('c', 'Playing music'), ('d', 'Reading sensors and steering the final approach into place')], 'd'),
        ('How is autonomous software checked?',
         [('a', 'By testing in many situations, including faults'), ('b', 'By trusting it without tests'), ('c', 'By asking the Sun'), ('d', 'By not checking it at all')], 'a'),
        ('What is a sensible limit of autonomy?',
         [('a', 'It works within its design and hands control back when it should'), ('b', 'It never fails'), ('c', 'It replaces every person on the team'), ('d', 'It makes the craft invisible')], 'a'),
    ],
}
