"""Configuration Control: keeping one agreed version of the design, and a true record of what was built."""
CODE = 'flight5_configuration'
BOOK = {
    'title': 'Configuration Control',
    'subtitle': 'One agreed design, and a true record of what was built',
    'chapters': [
        ('Why it matters', 'A project can fail when people build from different versions of the design. Configuration control keeps one agreed version and a clear record of every change to it.'),
        ('Baselines', 'A baseline is an agreed set of requirements or designs at a given point. Changes after a baseline pass through a formal process. This keeps the team working from the same picture.'),
        ('Change boards', 'A change board reviews each proposed change. It asks what the change affects, what it costs and what risks it brings. Only approved changes go into the design.'),
        ('As-built records', 'The as-built record shows what was really made, not only what was planned. Parts often differ slightly from the drawing. Record every difference, or the next repair may be wrong.'),
        ('Revision letters and numbers', 'Each approved change gets a new revision mark. Old revisions are kept, so that anyone can see what changed and when. A drawing with no revision mark should not be used.'),
        ('A cost worth paying', 'Configuration control adds paperwork and time. The cost is small beside the cost of building the wrong thing. Keep the process light enough that people follow it.'),
    ],
    'test': [
        ('What is a baseline?', [('a', 'A type of paint'), ('b', 'A rope used in docking'), ('c', 'A kind of fuel'), ('d', 'An agreed set of requirements or designs at a given point')], 'd'),
        ('What does a change board do?', [('a', 'Paints the hull'), ('b', 'Reviews each proposed change and its effects before it is approved'), ('c', 'Hires new crew'), ('d', 'Sets the time of launch by vote')], 'b'),
        ('What is an as-built record?', [('a', 'A record of what was really made'), ('b', 'A list of wishes for the future'), ('c', 'A map of the stars'), ('d', 'A list of flights booked')], 'a'),
        ('Why keep old revisions?', [('a', 'To take up space'), ('b', 'Because old drawings are always correct'), ('c', 'So anyone can see what changed and when'), ('d', 'Because nobody reads them')], 'c'),
        ('Why must a drawing with no revision mark not be used?', [('a', 'Because drawings with no mark are too big'), ('b', 'Because its status and version cannot be trusted'), ('c', 'Because revision marks are paid for'), ('d', 'Because it is always the newest')], 'b'),
    ],
}
