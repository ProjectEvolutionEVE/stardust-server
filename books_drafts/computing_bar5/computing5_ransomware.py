"""Ransomware anatomy: initial access, lateral movement, encryption and extortion, backups and response decisions."""
CODE = 'computing5_ransomware'
BOOK = {
    "title": 'Ransomware Anatomy',
    "subtitle": 'How a ransomware attack unfolds, step by step, and why backups decide recovery',
    "chapters": [
        ('How it gets in',
         "Most ransomware starts with a stolen password, a phishing email, or an unpatched service left open to the internet. The attacker's first goal is a single foothold inside the network."),
        ('Moving around',
         'Once inside, attackers look for higher access rights and move from one computer to another. They often spend days or weeks mapping the network before they act.'),
        ('Encryption and extortion',
         'The attacker then locks files with encryption and demands payment for the key. Many attackers also copy data first and threaten to publish it, which is called double extortion.'),
        ('Backups that work',
         'Backups are the strongest defence. Backups kept offline or set so they cannot be changed, and tested by real restores, let an organisation recover without paying.'),
        ('Decisions under pressure',
         'Leaders must decide quickly how to respond, who to tell, and whether to report the attack to the police and regulators. Plans made before an attack make those decisions calmer.'),
        ('No promises',
         'Paying does not guarantee that files come back, and it encourages more attacks. Many experts advise against relying on payment, and advise planning, backing up and rehearsing instead.'),
    ],
    "test": [
        ('What is a common way ransomware first gets in?',
         [('a', 'Through the printer tray'), ('b', 'A long lunch break'), ('c', 'A phishing email or a stolen password'), ('d', 'Through a wall socket')], 'c'),
        ('What does an attacker often do after getting inside?',
         [('a', 'Looks for higher access and moves between computers'), ('b', 'Turns the screens off'), ('c', 'Sends flowers'), ('d', "Deletes the company's website")], 'a'),
        ('What is double extortion?',
         [('a', 'Paying twice for the same key'), ('b', 'Stealing data and threatening to publish it as well as locking files'), ('c', 'Using two encryption keys'), ('d', 'A discount on backups')], 'b'),
        ('What makes a backup useful against ransomware?',
         [('a', 'It is kept where attackers can easily change it'), ('b', 'It is kept offline or protected from change, and tested by real restores'), ('c', 'It is printed on a sticker'), ('d', 'It is only saved on the same computer')], 'b'),
        ('Why should a team plan before an attack?',
         [('a', 'So the response decisions are made calmly'), ('b', 'So the attack can be ordered'), ('c', 'So the files can be deleted'), ('d', 'So the attacker is paid')], 'a'),
    ],
}
