"""Systems-theoretic Accident Analysis: looking at accidents as failures of control, not only chains of broken parts."""
CODE = 'flight5_stamp'
BOOK = {
    'title': 'Systems-theoretic Accident Analysis',
    'subtitle': 'Accidents as failures of control',
    'chapters': [
        ('Beyond the broken part', 'The usual way to study an accident is to find the broken part and the person who touched it last. This can miss the wider reasons. Nancy Leveson proposed a different way of looking.'),
        ("Leveson's idea", "Nancy Leveson suggested that many accidents happen when a system's controls fail to enforce its safety rules. The parts may all work, and still the system can move into danger."),
        ('Control structure', 'Map the controllers, the controlled parts, the feedback and the rules. Ask where a controller had the wrong picture of the system, or where an order was not carried out. This shows the gaps between the parts.'),
        ('Unsafe control actions', 'An unsafe control action is one that leads to a hazard, such as an order given too early or too late, or one that is never given. Listing these actions shows where the system is most exposed.'),
        ('The Challenger case', 'The Challenger accident shows why this view matters. The launch decision was shaped by pressure, unclear responsibility and weak feedback, as well as by a failed seal. A parts-only view misses most of this.'),
        ('Comparing with chains', 'A chain-of-events view and a control view often tell the story differently. Use both. The control view is most useful when designing what to change in how decisions are made.'),
    ],
    'test': [
        ('What did Nancy Leveson suggest about many accidents?', [('a', "They happen when a system's controls fail to enforce its safety rules"), ('b', 'They are always caused by one broken part'), ('c', 'They never have a cause'), ('d', 'They only happen at sea')], 'a'),
        ('What is a control structure?', [('a', 'A type of hull'), ('b', 'A bridge over a river'), ('c', 'The controllers, the controlled parts, the feedback and the rules'), ('d', 'A kind of fuel')], 'c'),
        ('What is an unsafe control action?', [('a', 'A control action that is always safe'), ('b', 'A control action that leads to a hazard'), ('c', 'A paint colour'), ('d', 'A rule that was never written')], 'b'),
        ('What did the Challenger case show in this method?', [('a', 'Only the failed seal mattered'), ('b', 'The launch was never decided'), ('c', 'Nobody was on board'), ('d', 'Pressure, unclear responsibility and weak feedback also shaped the decision')], 'd'),
        ('How do a chain view and a control view differ?', [('a', 'They always tell the same story'), ('b', 'The chain view is never useful'), ('c', 'They can tell the story differently, so using both is useful'), ('d', 'The control view is only for music')], 'c'),
    ],
}
