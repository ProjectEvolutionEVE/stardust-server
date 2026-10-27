"""The Morris Worm: the 1988 internet worm, the flaws it used, spread and slowdown, the response, the legal outcome and defence lessons."""
CODE = 'computing5_morris_worm'
BOOK = {
    "title": 'The Morris Worm',
    "subtitle": 'The 1988 program that slowed a young internet',
    "chapters": [
        ('The 1988 internet worm',
         'On 2 November 1988 a self-copying program, later called the Morris worm, spread across the early internet. It was written by Robert Tappan Morris, a graduate student at Cornell University. It spread far more widely than its author had intended.'),
        ('The flaws it used',
         'The worm exploited weaknesses in common network programs, such as the mail system and remote login tools, and tried to guess weak passwords. Many systems had not been patched, even though fixes for these weaknesses existed.'),
        ('Spread and slowdown',
         'Machines were infected again and again, and the load grew until many computers slowed badly or stopped. Thousands of machines were affected. Much of the harm came from the worm\'s own copying rather than from deliberate destruction.'),
        ('The response',
         'System administrators worked through the night to disconnect machines, share information and find fixes. The episode led to the founding of the CERT Coordination Center at Carnegie Mellon University, to help respond to future incidents.'),
        ('The legal outcome',
         'Morris was prosecuted under federal computer crime law and convicted. The sentence was probation, community service and a fine. The case became an early example of how the law treats network intrusion.'),
        ('Defence lessons',
         'Keep systems patched, switch off services that are not needed, use strong passwords, and watch for unusual load. Many of the lessons of 1988 are still the first steps in defence today.'),
    ],
    "test": [
        ('Who wrote the Morris worm?',
         [('a', 'A professional bank clerk'), ('b', 'Robert Tappan Morris, a graduate student'), ('c', 'A famous film director'), ('d', 'A school teacher in London')], 'b'),
        ('What did the worm exploit?',
         [('a', 'Lightning strikes'), ('b', 'Printer paper'), ('c', 'Traffic signals'), ('d', 'Weaknesses in common network programs and weak passwords')], 'd'),
        ('Why did many machines slow down or stop?',
         [('a', 'Repeated reinfection and copying loaded them heavily'), ('b', 'They ran out of paper'), ('c', 'They were turned into museum pieces'), ('d', 'Their keyboards were removed')], 'a'),
        ('What lasting organisation came out of the response?',
         [('a', 'The end of computers'), ('b', 'The closure of every university'), ('c', 'The CERT Coordination Center'), ('d', 'A ban on all email')], 'c'),
        ('Which defence lesson comes from 1988?',
         [('a', 'Leave systems unpatched'), ('b', 'Use weak passwords'), ('c', 'Keep systems patched and switch off needless services'), ('d', 'Share all passwords by letter')], 'c'),
    ],
}
