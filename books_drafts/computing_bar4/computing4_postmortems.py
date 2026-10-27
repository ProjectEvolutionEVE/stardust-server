"""Blameless Postmortems: learning from an incident by asking how the system allowed it, not who to blame."""
CODE = 'computing4_postmortems'
BOOK = {
    "title": 'Blameless Postmortems',
    "subtitle": 'Learning from an incident by asking how the system allowed it',
    "chapters": [
        ('Why look back',
         'After an incident, a team writes a postmortem to understand what happened and why. The goal is learning, not punishment. A good postmortem makes the next incident less likely and less harmful.'),
        ('The incident timeline',
         'Start with a timeline of events, written in order and with times. Record what was seen, what was done and what was believed at each point. A clear timeline stops the story from being rewritten later by memory.'),
        ('Contributing factors',
         'Rarely does one cause explain an incident. Look for several contributing factors, such as a missing alert, a rushed change or an unclear runbook. Each factor is a place where the system could be made safer.'),
        ('Blameless language',
         'Write about actions and systems, not about people as bad actors. Instead of saying an engineer was careless, say the tool allowed a risky change without a warning. People who feel safe report problems honestly, and honest reports make systems better.'),
        ('Action items',
         'Each postmortem should end with a short list of action items, each with an owner and a date. Actions should reduce risk, such as adding a check or simplifying a process. Long wish lists that nobody owns are not useful.'),
        ('Following up',
         'Review the actions a few weeks later to see whether they were finished and whether they worked. Share the lessons with other teams who may face the same risk. A postmortem that is filed and forgotten teaches nothing.'),
    ],
    "test": [
        ('What is the main goal of a blameless postmortem?',
         [('a', 'To find someone to punish'), ('b', 'To hide the incident from customers'), ('c', 'To close the office early'), ('d', 'To learn how the system allowed the incident')], 'd'),
        ('Why is a timeline written with times and events?',
         [('a', 'So the document is longer'), ('b', 'So the story is not rewritten later from memory'), ('c', 'So the printer has something to do'), ('d', 'So nobody needs to read it')], 'b'),
        ('What is a contributing factor?',
         [('a', 'A worker who is paid to fix bugs'), ('b', 'A type of backup tape'), ('c', 'One of several conditions that helped the incident happen'), ('d', 'A new customer')], 'c'),
        ('Why is blameless language important?',
         [('a', 'People report problems honestly when they feel safe'), ('b', 'It makes reports shorter'), ('c', 'It avoids the need for any actions'), ('d', 'It stops managers from reading the report')], 'a'),
        ('What should each action item have?',
         [('a', 'A colour and a font'), ('b', 'An owner and a date'), ('c', 'A picture of a cat'), ('d', 'A vote from the whole company')], 'b'),
    ],
}
