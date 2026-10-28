"""Coordinated Vulnerability Disclosure: how a security flaw is reported, fixed and made public in a responsible order."""
CODE = 'computing5_vuln_disclosure'
BOOK = {'title': 'Coordinated Vulnerability Disclosure',
 'subtitle': 'The timeline from finding to fix, embargoes, duties and disclosure policies',
 'chapters': [('From finding to fix',
               'A researcher finds a flaw and reports it privately to the maker. The maker '
               'confirms it, builds a fix and ships it. Only then is the flaw described in public. '
               'This order protects users.'),
              ('Embargoes',
               'An embargo is an agreed period of silence while a fix is prepared. Everyone '
               'involved keeps the details private until the date. Embargoes help users get '
               'protected before attackers learn of the flaw.'),
              ('Researcher and vendor duties',
               'Researchers should report carefully and give the maker reasonable time. Vendors '
               'should acknowledge reports, keep researchers informed and fix flaws promptly. Both '
               'sides share the goal of protecting users.'),
              ('Disclosure policies',
               'Many organisations publish a policy that explains how to report flaws and what to '
               'expect. Clear policies build trust. They set common timelines, such as a fixed '
               'number of days.'),
              ('Famous disputes',
               'Some disclosures have caused sharp arguments when researchers went public before a '
               'fix or a maker felt rushed. These disputes showed the need for clear, agreed '
               'rules. They shaped modern practice.'),
              ('Safe harbour',
               'Safe-harbour ideas protect good-faith researchers from legal action when they '
               'follow agreed rules. Such protection encourages reporting. The details differ '
               'widely between places.')],
 'test': [('What is the usual order in coordinated disclosure?',
           [('a', 'Publish first, then report'),
            ('b', 'Report privately, fix, then describe the flaw publicly'),
            ('c', 'Sell the flaw to strangers'),
            ('d', 'Never describe the flaw')],
           'b'),
          ('What is an embargo?',
           [('a', 'A ban on boats'),
            ('b', 'A shop closing day'),
            ('c', 'An agreed period of silence while a fix is prepared'),
            ('d', 'A fee for a sale')],
           'c'),
          ('What is a vendor duty?',
           [('a', 'To ignore every report'),
            ('b', 'To sell the flaw'),
            ('c', 'To post passwords'),
            ('d', 'To acknowledge reports and fix flaws promptly')],
           'd'),
          ('What does a disclosure policy do?',
           [('a', 'Explains how to report flaws and what to expect'),
            ('b', 'Sets the price of computers'),
            ('c', 'Chooses the office colours'),
            ('d', 'Counts the staff')],
           'a'),
          ('What is safe harbour for researchers?',
           [('a', 'A safe place to park a boat'),
            ('b', 'A free holiday'),
            ('c', 'Protection from legal action when following agreed rules'),
            ('d', 'A ban on reporting')],
           'c')]}
