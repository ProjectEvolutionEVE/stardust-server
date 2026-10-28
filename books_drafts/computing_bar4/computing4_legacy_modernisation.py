"""Modernising Legacy Systems: understanding old code before changing it, and deciding what to keep."""
CODE = 'computing4_legacy_modernisation'
BOOK = {
    "title": 'Modernising Legacy Systems',
    "subtitle": 'Understanding old code before changing it, and deciding what to keep',
    "chapters": [
        ('What counts as legacy',
         'Legacy code is not simply old code. It is code that people still depend on but no longer fully understand. A system can be ten years old and well understood, or three years old and already a tangle of guesses.'),
        ('Assessing what you have',
         'Before changing anything, list the parts of the system, who uses them, and how often they run. Note which parts break most often and which parts nobody dares to touch. This map shows where the real risk sits.'),
        ('Characterisation tests',
         'A characterisation test records what the code does today, even if that behaviour looks wrong. It gives you a safety net. When you later change the code, the tests show every place where behaviour has shifted, and you can decide whether that shift is intended.'),
        ('Seams and safe change',
         'A seam is a place where you can alter behaviour without editing the code around it, such as an interface you can swap or a configuration value. Finding seams lets you put tests around old code and change it in small, safe steps.'),
        ('Incremental rewrites',
         'Rewriting a legacy part in small pieces is usually safer than a single big rewrite. Each piece has its own tests and can be released on its own. When a piece is done, the team can compare the old and new results before the old code is removed.'),
        ('Deciding what to keep',
         'Not everything old should be replaced. Some code is reliable, cheap to run and well tested, and keeping it is the wise choice. Ask whether a part is a source of risk, a source of cost, or simply unfamiliar, because each answer leads to a different decision.'),
    ],
    "test": [
        ('What is legacy code, in this book?',
         [('a', 'Any code written in a language that is no longer popular'), ('b', 'Code people still depend on but no longer fully understand'), ('c', 'Code that has never been tested'), ('d', 'Code written by a previous company')], 'b'),
        ('What is a characterisation test?',
         [('a', 'A test that only checks the colour of a screen'), ('b', 'A test written by the user'), ('c', 'A test that never runs'), ('d', 'A test that records what the code does today')], 'd'),
        ('What is a seam in old code?',
         [('a', 'A place where behaviour can be changed without editing the code around it'), ('b', 'A bug that is hidden in the code'), ('c', 'A copy of the database'), ('d', 'A printed manual for the system')], 'a'),
        ('Why are incremental rewrites often safer than one large rewrite?',
         [('a', 'They never need any tests at all'), ('b', 'They avoid the need to talk to anyone'), ('c', 'Each piece can be tested and released on its own'), ('d', 'They make the old code run faster by default')], 'c'),
        ('Why should a team sometimes keep old code?',
         [('a', 'Because old code is always more secure'), ('b', 'Because the law requires it'), ('c', 'Because new code cannot be written'), ('d', 'Because reliable, cheap and well tested code may be worth keeping')], 'd'),
    ],
}
