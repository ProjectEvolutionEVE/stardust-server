"""Hazard Analysis: finding what could go wrong, and building barriers before it does."""
CODE = 'flight5_hazard'
BOOK = {
    'title': 'Hazard Analysis',
    'subtitle': 'Finding what could go wrong, and building barriers',
    'chapters': [
        ('What a hazard is', 'A hazard is a condition that could lead to harm. Hazard analysis finds those conditions early, while changes are still cheap. It is a standard step in good engineering.'),
        ('HAZOP', 'HAZOP, short for hazard and operability study, was developed in the chemical industry in the 1960s. A team reads the design and asks what happens if each flow or action goes too high, too low, or wrong. Each answer is written down.'),
        ('Fault trees and event trees', 'A fault tree starts from an unwanted event and works back to its causes. An event tree starts from a starting fault and works forward through the possible outcomes. Both show how small faults can combine.'),
        ('Barriers', 'A barrier stops a hazard from becoming harm. Barriers can be a design feature, a warning, a procedure or a person. Good designs use several barriers, so that one failure does not lead to disaster.'),
        ('Residual hazard', 'Some hazard always remains after the barriers are in place. This is the residual hazard. A leader must decide whether it is acceptable, and must write that decision down with its reasons.'),
        ('Keeping records', 'Keep the analysis up to date as the design changes. Record each hazard, its cause, its barrier, and the person who checks it. Old analyses that no one updates can be dangerous.'),
    ],
    'test': [
        ('What is a hazard?', [('a', 'A type of ship'), ('b', 'A condition that could lead to harm'), ('c', 'A bright light'), ('d', 'A kind of fuel tank')], 'b'),
        ('In which industry was HAZOP first developed?', [('a', 'Fashion industry'), ('b', 'Music industry'), ('c', 'Publishing industry'), ('d', 'Chemical industry')], 'd'),
        ('What does a fault tree start from?', [('a', 'The first morning of a project'), ('b', 'The price of fuel'), ('c', 'An unwanted event, working back to its causes'), ('d', 'The best possible outcome')], 'c'),
        ('What is a barrier?', [('a', 'Something that stops a hazard from becoming harm'), ('b', 'A wall that blocks the view'), ('c', 'A type of fuel'), ('d', 'A line on a map')], 'a'),
        ('What is residual hazard?', [('a', 'The hazard that was removed entirely'), ('b', 'A hazard that never existed'), ('c', 'A fee paid to the bank'), ('d', 'The hazard that remains after the barriers are in place')], 'd'),
    ],
}
