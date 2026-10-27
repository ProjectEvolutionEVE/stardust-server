"""Password-Authenticated Key Exchange: proving a shared password without sending it, limits on offline guessing, SRP and OPAQUE ideas, and phishing limits."""
CODE = 'computing5_pake'
BOOK = {'title': 'Password-Authenticated Key Exchange',
 'subtitle': 'Proving a shared password without sending it',
 'chapters': [('Proving a password without sending it',
               'A password-authenticated key exchange lets two parties who share a password agree on a strong key. The password itself is never sent across the network. An '
               'eavesdropper learns nothing useful from the exchange.'),
              ('PAKE design',
               'A PAKE protocol mixes the password into a key exchange so that each attempt at a guess needs a live interaction. A careful design prevents an attacker from '
               'checking many guesses offline. Designing one correctly is subtle, and standard protocols are preferred.'),
              ('Limits on offline guessing',
               'Passwords are often weak, so an attacker who captures stored data could guess them offline. Good PAKE designs stop the attacker from testing guesses without '
               'talking to the server. Strong password policies and rate limits add protection.'),
              ('SRP and OPAQUE',
               'The Secure Remote Password protocol, SRP, is an early and widely studied PAKE. OPAQUE is a later design that keeps the password hidden even from the server during '
               'registration and login. Both are used in real products.'),
              ('Deployment',
               'Deploying a PAKE needs careful handling of account setup, password changes and recovery. Libraries that implement the protocol correctly should be used. Mistakes '
               'in these steps can silently remove the protection.'),
              ('Phishing limits',
               'A PAKE does not stop a user from typing their password into a fake site. It protects the wire, not the person. Phishing resistance needs other defences, such as '
               'hardware keys or origin-bound logins.')],
 'test': [('What does a PAKE let two parties do?',
           [('a', 'Share a photo album'),
            ('b', 'Print a password on paper'),
            ('c', 'Agree on a strong key from a shared password, without sending the password'),
            ('d', 'Erase a password')],
           'c'),
          ('What limits an attacker who wants to guess a password?',
           [('a', 'Each guess needs a live interaction in a good design'),
            ('b', 'Guesses are free and unlimited'),
            ('c', 'Passwords cannot be guessed at all'),
            ('d', 'Guesses are printed in colour')],
           'a'),
          ('What is SRP?',
           [('a', 'A type of screen'), ('b', 'A kind of printer'), ('c', 'A cloud storage plan'), ('d', 'The Secure Remote Password protocol, an early PAKE')],
           'd'),
          ('What does OPAQUE add in its design?',
           [('a', 'Sending the password in plain text'),
            ('b', 'Keeping the password hidden even from the server'),
            ('c', 'Removing the need for any password'),
            ('d', 'Printing the password')],
           'b'),
          ('What can a PAKE not stop by itself?',
           [('a', 'A user typing their password into a fake site'),
            ('b', 'Eavesdropping on the network'),
            ('c', 'Offline guessing from captured data'),
            ('d', 'A replayed exchange')],
           'a')]}
