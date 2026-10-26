"""Troubleshooting a Machine: a calm method for finding why a machine has stopped or misbehaves."""
CODE = 'engineering2_troubleshooting'
BOOK = {
    "title": 'Troubleshooting a Machine',
    "subtitle": 'A calm method for finding why a machine has stopped or misbehaves',
    "chapters": [
        ('Start with the symptom',
         "Write down exactly what happens: what the machine does, what it should do, when it started, and what changed just before. "
         "A clear symptom is half the diagnosis. 'It grinds when the pump starts' is far more useful than 'it's broken'."),
        ('Check the simple things first',
         "Most faults are simple: no power, a blown fuse, a closed valve, a loose connection, low fluid, a blocked filter. Check these "
         "before taking anything apart. A simple check can save hours of work."),
        ('Change one thing at a time',
         "Change or test one thing, then check the result, so you know what fixed it. Changing three things at once hides the answer, "
         "and it can leave a new fault in place without anyone noticing."),
        ('Split the problem in half',
         "When the cause lies somewhere along a long chain, test the middle point. If it works there, the fault is further along; if "
         "not, it is earlier in the chain. Keep halving until you reach the faulty section. This is quicker than checking every step in turn."),
        ('Find the root cause',
         "A fault often has a root cause. A worn bearing can make a motor draw too much current, which then trips a breaker. Resetting "
         "the breaker treats only the symptom. Ask why the part failed, then fix that."),
        ('Prove the fix',
         "After a repair, run the machine under the same conditions the fault appeared under, and keep it running long enough to be "
         "sure. Then record the fault, its cause and the fix, so the next person does not start from zero."),
    ],
    "test": [
        ("When a machine stops, what should you check first?",
         [('a', 'Its paint colour'), ('b', 'Simple things, such as power, fuses, closed valves and loose connections'), ('c', 'The price of its parts'), ('d', 'Its serial number')], 'b'),
        ("Why change only one thing at a time?",
         [('a', 'It saves tools'), ('b', 'It is always faster'), ('c', 'Changing one thing is always safer'), ('d', 'So you know which change fixed the fault')], 'd'),
        ("What does 'split the problem in half' mean?",
         [('a', 'Cut the machine in two'), ('b', 'Share the repair between two people'), ('c', 'Test a middle point, to see which half holds the fault'), ('d', 'Halve the power supply')], 'c'),
        ("What is a symptom?",
         [('a', 'What the machine does wrong'), ('b', 'The cause of the fault'), ('c', 'The part that breaks'), ('d', 'The repair you make')], 'a'),
        ("After a repair, what should you do?",
         [('a', 'Put the tools away at once'), ('b', 'Paint the machine'), ('c', 'Forget about the fault'), ('d', 'Run it under the same conditions the fault appeared under, then record the fault, cause and fix')], 'd'),
    ],
}
