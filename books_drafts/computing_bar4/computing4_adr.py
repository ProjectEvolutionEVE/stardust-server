"""Architecture Decision Records: writing down why a design choice was made, so the reasons outlive the people."""
CODE = 'computing4_adr'
BOOK = {
    "title": 'Architecture Decision Records',
    "subtitle": 'Writing down why a design choice was made, so the reasons last',
    "chapters": [
        ('What a decision record is',
         'An architecture decision record is a short document that captures one important design choice. It explains the situation, the choice made and the results expected. Each record is kept with the code so anyone can find it later.'),
        ('Context, decision and consequences',
         'A good record has three parts. The context describes the forces at play. The decision states what was chosen. The consequences list both the benefits and the costs, including the ones nobody likes. Honest consequences make the record useful.'),
        ('When to write one',
         'Write a record when a choice is hard to reverse, affects many parts of the system, or was debated at length. Small choices that are easy to change do not need one. Writing too many records makes the important ones harder to find.'),
        ('Status changes',
         'Each record has a status, such as proposed, accepted, superseded or deprecated. When a decision changes, the new record should link to the old one and the old record should not be deleted. The history of thinking is valuable in itself.'),
        ('Linking records to code',
         'A record is most useful when the code that follows it points back to it. A short comment or a link in the code tells a reader where the reasoning lives. This stops a future engineer from undoing a choice without knowing why it was made.'),
        ('Avoiding bloat',
         'Records should be short, plain and easy to scan. If a record grows into a long essay, few people will read it. Review the set of records on a regular rhythm, and archive those that no longer matter.'),
    ],
    "test": [
        ('What does an architecture decision record capture?',
         [('a', 'A photograph of the team'), ('b', 'The salary of each engineer'), ('c', 'One important design choice and the reasons for it'), ('d', 'The weather on release day')], 'c'),
        ('What are the three main parts of a good record?',
         [('a', 'Context, decision and consequences'), ('b', 'Title, font and colour'), ('c', 'Price, time and place'), ('d', 'Start, middle and end of a film')], 'a'),
        ('When is a record most worth writing?',
         [('a', 'For every single variable name'), ('b', 'For lunch orders'), ('c', 'Only after the system is deleted'), ('d', 'For a hard-to-reverse choice that affects many parts of the system')], 'd'),
        ('What should happen when a decision changes?',
         [('a', 'The old record is deleted'), ('b', 'The new record links to the old, which is kept'), ('c', 'Nothing is written down'), ('d', 'The team changes its name')], 'b'),
        ('Why should records be kept short?',
         [('a', 'So they cost less paper'), ('b', 'So they can hide the costs'), ('c', 'So people will actually read and find them'), ('d', 'So the code never changes')], 'c'),
    ],
}
