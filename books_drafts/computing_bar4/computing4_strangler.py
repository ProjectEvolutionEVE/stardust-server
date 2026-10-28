"""Strangler Fig Migration: replacing an old system one piece at a time while it keeps running."""
CODE = 'computing4_strangler'
BOOK = {
    "title": 'Strangler Fig Migration',
    "subtitle": 'Replacing an old system piece by piece while it keeps running',
    "chapters": [
        ('Why not start again',
         'A full rewrite often takes years, and the old system keeps changing while you build the new one. The strangler fig pattern takes a gentler route. You grow the new system around the old one, and slowly take over its work until the old one can be switched off.'),
        ('Routing traffic',
         'The first step is to place a routing layer in front of the old system. Requests arrive at the router, which sends each one to the old code or to the new code. At the start, everything goes to the old system, so nothing changes for users.'),
        ('Replacing one piece at a time',
         'Pick a small, well-bounded feature and build it again in the new system. Once it works, send its requests to the new code and check the results. Then move on to the next piece, and repeat the process many times.'),
        ('Facades and seams',
         'A facade is a simple front door that hides which system does the work. A seam is a place in the old code where you can change behaviour without editing everything around it. Both make it possible to swap parts without breaking callers.'),
        ('Moving the data',
         'Data is the hardest part, because two systems must not disagree about the truth. Teams often move data in steps, copying it, checking both copies match, and then switching writes over. Keep a way to roll back a step if something goes wrong.'),
        ('Retiring the old code',
         'Track how much traffic still reaches the old system, and how many features it still owns. When the count reaches zero, remove the old code and its routes. Celebrate the removal, because an old system that is never switched off costs money and attention every year.'),
    ],
    "test": [
        ('What does the routing layer do in a strangler fig migration?',
         [('a', 'It deletes the old code on the first day'), ('b', 'It stores all the data in a single file'), ('c', 'It sends each request to the old or the new system'), ('d', 'It makes users learn the new system')], 'c'),
        ('Why do teams replace a system one piece at a time?',
         [('a', 'So each step can be checked and rolled back if needed'), ('b', 'So the old system never has to run again'), ('c', 'So users see a change all at once'), ('d', 'Because a full rewrite is always cheaper')], 'a'),
        ('What is a facade in this pattern?',
         [('a', 'A paint colour for the user screen'), ('b', 'A backup copy of the database'), ('c', 'A test that runs only once'), ('d', 'A simple front door that hides which system does the work')], 'd'),
        ('What is the hardest part of the migration?',
         [('a', 'Choosing a colour scheme'), ('b', 'Keeping the two systems from disagreeing about the data'), ('c', 'Writing a single line of code'), ('d', 'Finding a name for the project')], 'b'),
        ('When is it safe to remove the old code?',
         [('a', 'As soon as the new code is written'), ('b', 'When the team gets bored'), ('c', 'When the old system receives no more traffic and owns no more features'), ('d', 'Only after the company changes its name')], 'c'),
    ],
}
