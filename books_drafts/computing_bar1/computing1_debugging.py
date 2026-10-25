"""Debugging and Testing: finding and fixing mistakes, testing small pieces, and why checks matter."""
CODE = 'computing1_debugging'
BOOK = {
    "title": 'Debugging and Testing',
    "subtitle": 'Finding and fixing mistakes, and checking that they are really fixed',
    "chapters": [
        ('Bugs are normal',
         'A bug is a mistake in a program that makes it do something other than what was meant. Every programmer makes them, and finding them is a normal part of the work. The word is old: one famous early case, in 1947, was a real moth stuck in a computer.'),
        ('Find it step by step',
         'Start by writing down what should happen and what actually happens. Then check the values at a few points in the program, and find the first point where they go wrong. The bug is usually at that point or just before it.'),
        ('Test small pieces',
         'Test one small part at a time, using inputs where you already know the right answer. This is called unit testing. A small piece that passes every test you give it can be trusted before you build more on top of it.'),
        ('Try the edges',
         'Many bugs hide at the edges: an empty list, the number zero, the largest possible value, or a value just over a limit. A good test tries these as well as the easy, typical case.'),
        ('Why checks matter',
         'A check proves that something is what it claims to be. In the game, a receipt code can be looked up on the receipt check, which shows what was recorded without showing who owns it. A blueprint serial works the same way, and it is genuine only if the server issued it.'),
        ('Fixing without breaking',
         'After a fix, run the tests again. A change in one place can break something far away, and rerunning the tests catches that. Write down what you changed and why, so anyone reading later can understand the fix.'),
    ],
    "test": [
        ('What is a bug in a program?',
         [('a', 'A mistake that makes it do something other than what was meant'), ('b', 'A kind of memory chip'), ('c', 'A part of the screen'), ('d', 'A fast type of storage')], 'a'),
        ('What is a good first step when hunting a bug?',
         [('a', 'Rewrite the whole program at once'), ('b', 'Delete all the saved files'), ('c', 'Turn the power off and on again'), ('d', 'Compare what should happen with what actually happens')], 'd'),
        ('What is unit testing?',
         [('a', 'Counting the bytes in a file'), ('b', 'Measuring the speed of the processor'), ('c', 'Testing one small piece on inputs where the right answer is already known'), ('d', 'Running the whole game in one go with no notes')], 'c'),
        ('Which kind of test is most likely to reveal a hidden bug?',
         [('a', 'Only the easy, typical case'), ('b', 'An edge case, such as an empty list, zero or the largest possible value'), ('c', 'A test that always passes'), ('d', 'A test run on a different computer')], 'b'),
        ('Why is a receipt code that anyone can look up useful?',
         [('a', 'It hides who owns the receipt'), ('b', 'It stops the game from running'), ('c', 'It makes the code shorter'), ('d', 'It lets anyone check that a transfer was really recorded, without seeing who owns it')], 'd'),
    ],
}
