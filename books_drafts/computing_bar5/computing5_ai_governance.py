"""AI Governance and Oversight: risk tiers, model cards, oversight boards, incident reporting, documentation and continuous review."""
CODE = 'computing5_ai_governance'
BOOK = {'title': 'AI Governance and Oversight',
 'subtitle': 'Rules, records and review for systems that make decisions',
 'chapters': [('Risk tiers',
               'Governance of AI often sorts systems into risk tiers. Uses judged unacceptable may be '
               'banned, high-risk systems face strict duties, and low-risk systems face lighter rules. The '
               "European Union's AI Act adopted this kind of approach."),
              ('Model cards',
               'A model card is a short document that describes what a model is for, how it was tested, '
               'where it performs poorly, and what data shaped it. Researchers proposed the idea in 2019, '
               'and it has spread widely since.'),
              ('Oversight boards',
               'Organisations may set up oversight boards with people from different backgrounds to review '
               'high-stakes uses of AI. A board works best with clear authority and access to the facts it '
               'needs.'),
              ('Incident reporting',
               'Recording and reporting harmful AI incidents helps others avoid the same failures. Clear '
               'rules about what to report, and to whom, make reporting more consistent and useful.'),
              ('Documentation',
               'Good documentation records data sources, design choices, testing and known limits. '
               'Documentation makes it possible to audit a system after it has been put into use.'),
              ('Continuous review',
               'AI systems can change in behaviour as data and users change. Continuous review and '
               'monitoring of results keep governance from becoming a one-time event at launch.')],
 'test': [('What does AI governance often do with systems?',
           [('a', 'Ignores them all'),
            ('b', 'Sorts them into risk tiers'),
            ('c', 'Paints them a single colour'),
            ('d', 'Sells them at auction')],
           'b'),
          ('What is a model card?',
           [('a', 'A birthday greeting'),
            ('b', 'A payment card for a bank'),
            ('c', 'A map of a city'),
            ('d', 'A short document describing what a model is for, how it was tested and its limits')],
           'd'),
          ('What do oversight boards need to work well?',
           [('a', 'Clear authority and access to the facts'),
            ('b', 'No information at all'),
            ('c', 'Only members of one family'),
            ('d', 'A ban on questions')],
           'a'),
          ('Why is incident reporting useful?',
           [('a', 'It hides problems from everyone'),
            ('b', 'It makes systems slower on purpose'),
            ('c', 'It helps others avoid the same failures'),
            ('d', 'It removes the need for testing')],
           'c'),
          ('Why is continuous review needed?',
           [('a', 'Because AI systems can change as data and users change'),
            ('b', 'Because AI never changes at all'),
            ('c', 'Because reviews cost nothing'),
            ('d', 'Because review is only needed on Mondays')],
           'a')]}
