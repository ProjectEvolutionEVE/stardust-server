"""Writing Requirements: clear, testable statements that say what a system must do, and can be checked."""
CODE = 'flight5_requirements'
BOOK = {
    'title': 'Writing Requirements',
    'subtitle': 'Clear statements that can be checked',
    'chapters': [
        ('What a requirement is', 'A requirement says what a system must do or be. It is the agreed promise that the design is measured against. A vague requirement leads to a disputed result.'),
        ('The word shall', 'Good requirements use the word shall, as in the craft shall hold its position within one metre. Shall marks a requirement that must be met. Words like should or might leave the test open.'),
        ('Testable', 'A requirement must be testable. If you cannot say how it will be checked, it is not yet a requirement. Put numbers, units and conditions into it, so that a pass or fail is clear.'),
        ('Traceable', 'Each requirement should trace back to a need and forward to a test. Traceability shows that nothing was lost and that every test has a purpose. Gaps in the trace show risks.'),
        ('Conflicts and creep', 'Two requirements can conflict, and a team must resolve the conflict before building. Requirements also creep upward as ideas are added. Each addition should go through the change process.'),
        ('Examples', 'A weak requirement says the system should be fast. A strong one says the craft shall reach its set speed within ten seconds on level flight. The strong version can be tested and agreed.'),
    ],
    'test': [
        ('Which word marks a requirement that must be met?', [('a', 'Might'), ('b', 'Could'), ('c', 'Shall'), ('d', 'Perhaps')], 'c'),
        ('Why must a requirement be testable?', [('a', 'So that a pass or fail can be clearly shown'), ('b', 'So that it is longer'), ('c', 'So that it is written in a poem'), ('d', 'So that it can be painted')], 'a'),
        ('What does traceability do?', [('a', 'Removes all tests'), ('b', 'Makes requirements shorter'), ('c', 'Turns requirements into music'), ('d', 'Links each requirement back to a need and forward to a test')], 'd'),
        ('What is requirements creep?', [('a', 'A slow crawl of a robot'), ('b', 'Ideas being added to requirements over time without proper control'), ('c', 'A kind of paint'), ('d', 'A rule against any change')], 'b'),
        ('Which requirement is strong?', [('a', 'The craft shall reach its set speed within ten seconds on level flight'), ('b', 'The system should be fast'), ('c', 'The craft might be nice to fly'), ('d', 'The craft is good')], 'a'),
    ],
}
