"""Vulnerability Scoring: CVE names and CVSS scores, and how defenders decide which weakness to fix first."""
CODE = 'computing5_cvss_cve'
BOOK = {'title': 'Vulnerability Scoring: CVE and CVSS',
 'subtitle': 'Naming vulnerabilities, base and temporal scores, and setting priorities',
 'chapters': [('One name for each weakness',
               'A CVE identifier gives a publicly known security weakness a unique name, such as '
               'CVE followed by a year and a number. The name lets teams talk about the same flaw '
               'without confusion. It does not say how serious the flaw is.'),
              ('Base scores',
               'The Common Vulnerability Scoring System, CVSS, gives a base score from 0 to 10. It '
               'considers how the flaw can be reached and what it damages. The base score '
               'describes the flaw itself.'),
              ('Temporal scores',
               'Temporal factors change over time, such as whether a fix exists or an exploit is '
               'public. They adjust the score as the situation develops. Teams should check them, '
               'not only the base score.'),
              ('Exploitability',
               'Exploitability asks how easily an attacker could use the flaw. A flaw that needs '
               'no login and little skill is more urgent. Scores help teams rank this, though they '
               'cannot measure it perfectly.'),
              ('Prioritising with context',
               'The same score means different things on different systems. A flaw on an '
               'internet-facing server matters more than one on an isolated machine. Good teams '
               'combine the score with their own context.'),
              ('Scoring errors',
               'Scores can be wrong, and experts sometimes disagree. Teams should treat scores as '
               'a guide, not a verdict. Checking the reasoning behind a score is part of good '
               'practice.')],
 'test': [('What does a CVE identifier do?',
           [('a', 'Rates the price of a car'),
            ('b', 'Gives a known security weakness a unique name'),
            ('c', 'Counts the users online'),
            ('d', 'Sets the screen brightness')],
           'b'),
          ('What range does a CVSS base score use?',
           [('a', 'From 100 to 200'),
            ('b', 'From A to Z'),
            ('c', 'From 0 to 10'),
            ('d', 'From minus 50 to minus 40')],
           'c'),
          ('What do temporal factors describe?',
           [('a', 'The age of the programmer'),
            ('b', 'The time of a lunch break'),
            ('c', 'The shape of the server'),
            ('d', 'How the situation changes over time, such as a fix or public exploit')],
           'd'),
          ('What does exploitability ask?',
           [('a', 'How easily an attacker could use the flaw'),
            ('b', 'How expensive the computer was'),
            ('c', 'How many pages the report has'),
            ('d', 'How loud the fan is')],
           'a'),
          ('Why does context matter when prioritising?',
           [('a', 'Context changes nothing'),
            ('b', 'Scores never apply to servers'),
            ('c', 'The same score matters more on an internet-facing system'),
            ('d', 'Context only matters on paper')],
           'c')]}
