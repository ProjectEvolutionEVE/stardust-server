"""Automation and the Pilot: autopilot history, its benefits, skill loss, mode confusion, handover and balance."""
CODE = 'flight5_automation'
BOOK = {
    "title": 'Automation and the Pilot',
    "subtitle": 'How autopilots help, where they fall short, and how crews stay sharp',
    "chapters": [
        ('Autopilot history',
         'The first autopilots were built in the 1910s to hold a plane steady and level. Over the decades they grew into systems that fly a whole route, from take-off to landing. Each step made long flights less tiring and more precise.'),
        ('The benefits',
         'Automation keeps a plane on course and at a steady speed, and it reacts faster than a person in many cases. It lowers the workload on long flights and frees the crew to watch the wider picture. Many accidents have been avoided because the system held steady.'),
        ('Skill loss',
         'If a pilot flies by hand only rarely, hand-flying skills can fade. When the automatic system fails, the crew must fly by hand with less practice. For this reason, training includes regular manual flying.'),
        ('Mode confusion',
         'Automatic systems work in modes, and it is easy to misread which mode is active. A crew may think the system is doing one thing while it is doing another. Clear displays and clear training help reduce this risk.'),
        ('Handover',
         'When automation hands control back to the crew, the handover must be clear and quick. The crew needs to know the state of the plane and what the automation was doing. A clear, calm handover is part of safe flying.'),
        ('Balance',
         'The aim is a balance: use automation to reduce routine work, and keep the skills to fly by hand when needed. Good crews know when to switch systems on and when to take control. For players, the lesson is that a helpful tool still needs a skilled hand behind it.'),
    ],
    "test": [
        ('When were the first autopilots built?',
         [('a', 'In the 1950s'), ('b', 'In the 1910s'), ('c', 'In the 1990s'), ('d', 'In the 2020s')], 'b'),
        ('What is "skill loss" in automation?',
         [('a', 'Pilots forgetting their own name'), ('b', 'Losing the aircraft fuel'), ('c', 'Hand-flying skills fading from lack of practice'), ('d', 'Losing the passenger list')], 'c'),
        ('What is mode confusion?',
         [('a', 'Mixing up the colours of seats'), ('b', 'Forgetting the destination city'), ('c', 'Confusing two passengers'), ('d', 'Misreading which automatic mode is active')], 'd'),
        ('Why must a handover of control be clear?',
         [('a', 'So the crew knows the state of the plane and what automation was doing'), ('b', 'So the passengers can read the screen'), ('c', 'So the engines can be turned off'), ('d', 'So the landing gear is raised')], 'a'),
        ('What is the aim of good automation practice?',
         [('a', 'To replace all human skill'), ('b', 'To reduce routine work while keeping hand-flying skills'), ('c', 'To ban autopilots'), ('d', 'To fly without any checks')], 'b'),
    ],
}
