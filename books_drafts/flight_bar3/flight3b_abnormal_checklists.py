"""When Something Goes Wrong: how a pilot uses an abnormal checklist, calm steps and the rule to fly the craft first."""
CODE = 'flight3b_abnormal_checklists'
BOOK = {
    "title": 'When Something Goes Wrong',
    "subtitle": 'How to use an abnormal checklist, with calm steps and the craft flown first',
    "chapters": [
        ('Two kinds of checklist',
         'Normal checklists run before and after each flight, in order. Abnormal checklists are for when something has gone wrong, such as a warning light or a reading that will not settle. They are short, written in plain steps, and meant to be read in a calm voice.'),
        ('Fly the craft first',
         'Before anything else, keep the craft safe. Hold your heading and speed, and keep it under control. A checklist is no help if the craft is drifting into something while you read it. Fly first, then deal with the problem.'),
        ('Memory items',
         'A few steps are so urgent that pilots learn them by heart. These memory items come first, because there may be no time to read. Everything else waits for the checklist.'),
        ('Identify, confirm, act',
         'Name the problem, check it against a second reading, then take the step the checklist gives. Confirming first stops you from fixing a fault that is not really there. Say each step aloud so the whole crew hears it.'),
        ('Do not skip ahead',
         'Work through the checklist in order and tick each step as you go. Skipping ahead to the step you think is right is how a second problem gets made. If a step does not work, read the next one, and say so.'),
        ('After the problem',
         'Once the craft is safe, run the clean-up steps and write down what happened. Tell the Tower, record the event in your flight log, and note anything you would change next time. A checklist is a tool, and a good crew improves it.'),
    ],
    "test": [
        ('What is an abnormal checklist for?',
         [('a', 'Working through steps when something has gone wrong'), ('b', 'Choosing a new colour for the craft'), ('c', 'Planning a holiday'), ('d', 'Counting the stars')], 'a'),
        ('What should come first when a problem appears?',
         [('a', 'Open the hold'), ('b', 'Keep the craft safe and under control'), ('c', 'Read the market prices'), ('d', 'Start a new card game')], 'b'),
        ('Why do pilots learn memory items by heart?',
         [('a', 'They are the longest steps in the checklist'), ('b', 'They are written in a foreign language'), ('c', 'They are the most urgent, and there may be no time to read them'), ('d', 'They replace the flight log')], 'c'),
        ('Why confirm a fault before acting on it?',
         [('a', 'So the craft gets heavier'), ('b', 'So the battery lasts longer'), ('c', 'So the Tower can see the hold'), ('d', 'So you do not fix a fault that is not really there')], 'd'),
        ('What is the right way to use an abnormal checklist?',
         [('a', 'Read it aloud, work through the steps in order and tick each one'), ('b', 'Skip to the step you think is right'), ('c', 'Read it only after the craft has landed'), ('d', 'Memorise the whole thing and never look at it')], 'a'),
    ],
}
