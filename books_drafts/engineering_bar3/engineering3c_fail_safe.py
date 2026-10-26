"""Fail-Safe Design: choosing what a machine does when it can no longer work properly, or loses power."""
CODE = 'engineering3c_fail_safe'
BOOK = {
    "title": 'Fail-Safe Design: When Power Dies',
    "subtitle": 'Choosing what a machine does when it can no longer work properly',
    "chapters": [
        ('A safe state',
         "A fail-safe design chooses a safe state for the system to fall into when something breaks. For a door, that might be locked. For a moving part, it is usually stopped. The question is always what happens when things go wrong, not only when they go right."),
        ('Springs on the safe side',
         "A spring-applied brake clamps on when power is lost, because the spring pushes it on and the power holds it off. A lift brake often works this way, so a dead motor stops the load. The safe state is built into the design, and no power is needed to reach it."),
        ('Energised to stop or to run',
         "A system can be built so that power keeps it running, or so that losing power stops it. Railway signals are often arranged so that a broken wire or lost power sets the signal to danger. Choose the arrangement that makes the failure harmless."),
        ('Interlocks',
         "An interlock stops one action until another is safe, such as a guard that must be closed before a machine can start. Interlocks are simple and inexpensive, and they save lives. Never wire one out just to make a machine easier to run."),
        ('The failure nobody expected',
         "Designers list the failures they can imagine, but the surprising one is often the one that hurts. A fail-safe design limits the damage from failures no one thought of. Ask what the worst unexpected failure could do."),
        ('The cost of safety',
         "Fail-safe parts cost more and need more care, but they cost far less than an accident. Include the expected cost of failure in the design budget. A safe state is an investment that is paid once and kept for the life of the machine."),
    ],
    "test": [
        ('What is a fail-safe design?',
         [('a', 'One that chooses a safe state for the system to fall into when something breaks'), ('b', 'One that never breaks'), ('c', 'One with no safety features'), ('d', 'One that runs faster when it breaks')], 'a'),
        ('How does a spring-applied brake behave when power is lost?',
         [('a', 'It releases'), ('b', 'It turns to gas'), ('c', 'It is stuck open'), ('d', 'It clamps on, because the spring pushes it on and the power holds it off')], 'd'),
        ('Why are railway signals often arranged to fail to danger?',
         [('a', 'So they cost less'), ('b', 'So a broken wire or lost power sets the signal to danger, the harmless side'), ('c', 'So they can be painted'), ('d', 'So they are louder')], 'b'),
        ('What is an interlock?',
         [('a', 'A type of rope'), ('b', 'A cable connector'), ('c', 'A device or wiring that stops one action until another is safe, such as a guard that must be closed before a machine starts'), ('d', 'A paint finish')], 'c'),
        ('What should a designer ask about the worst unexpected failure?',
         [('a', 'Whether it has been painted'), ('b', 'Whether it is cheaper than the old part'), ('c', 'Whether it is listed in the manual'), ('d', 'What damage it could do, since surprises are often the ones that hurt')], 'd'),
    ],
}
