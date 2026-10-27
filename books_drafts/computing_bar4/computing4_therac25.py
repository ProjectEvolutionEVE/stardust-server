"""Therac-25: Software and Safety: how software faults in a radiation therapy machine led to serious injuries, and what it taught engineers."""
CODE = 'computing4_therac25'
BOOK = {
    "title": 'Therac-25: Software and Safety',
    "subtitle": 'How software faults in a radiation therapy machine caused serious harm, and what it taught engineers',
    "chapters": [
        ('A radiation therapy machine',
         'The Therac-25 was a medical machine that delivered radiation to treat cancer, in the 1980s. It could deliver different kinds of beam, and operators set the treatment through a computer. Accurate control was essential to patient safety.'),
        ('Software faults',
         'Several accidents happened in which patients received far too much radiation. Investigations found that software faults were a major cause. Earlier models had hardware safety locks, and the newer design relied more on software to do the same job.'),
        ('Race and interlock failures',
         'Investigators found a race condition, where fast keyboard input could leave the machine in a state the software did not check properly. The safety interlock that should have stopped the beam did not always work as intended. The failures involved timing and checking, not just a single line.'),
        ('The investigation',
         'Engineers and researchers examined the machine, its records and the way it was built. The investigation found weak testing, unclear error messages and poor documentation. Much of the blame fell on the manufacturer\'s design and software practices.'),
        ('Design lessons',
         'The case taught engineers that software can cause physical harm, and that safety must be designed in from the start. Independent safety reviews, simple and checkable designs, and keeping proven hardware safeguards all matter. Reusing software without re-checking it is risky.'),
        ('Safety culture',
         'A safety culture listens to reports of near misses, and treats them seriously. Warnings that are ignored or dismissed can become tragedies. Teams that are open about problems prevent harm far more reliably than teams that hide them.'),
    ],
    "test": [
        ('What was the Therac-25?',
         [('a', 'A kitchen oven'), ('b', 'A car engine'), ('c', 'A ship radio'), ('d', 'A radiation therapy machine')], 'd'),
        ('What did older models have that helped protect patients?',
         [('a', 'A paper manual only'), ('b', 'Hardware safety locks'), ('c', 'A bigger screen'), ('d', 'Painted walls')], 'b'),
        ('What is a race condition?',
         [('a', 'A contest between two computers'), ('b', 'A type of printer error'), ('c', 'A problem where timing leaves the software in a state it did not check'), ('d', 'A fast way to save files')], 'c'),
        ('What did the investigation find among the causes?',
         [('a', 'Weak testing, unclear error messages and poor documentation'), ('b', 'That the machine was too cheap'), ('c', 'That no software was involved'), ('d', 'That patients caused every problem')], 'a'),
        ('What is a safety culture?',
         [('a', 'Hiding problems from staff'), ('b', 'Listening to near-miss reports and treating them seriously'), ('c', 'Ignoring all warnings'), ('d', 'Running machines without checks')], 'b'),
    ],
}
