"""The test pyramid: many small tests at the base, fewer connected tests in the middle, and a few whole-journey tests at the top."""
CODE = 'computing3a_test_pyramid'
BOOK = {
    "title": 'The Test Pyramid',
    "subtitle": 'Many small tests, fewer bigger ones, and a few that try the whole game',
    "chapters": [
        ('Why plan your tests',
         'A test plan answers two questions: what to check, and how much to check it each way. Testing everything in the same way is slow and wasteful. Different kinds of tests find different kinds of mistakes.'),
        ('The base: small tests',
         'The widest and cheapest part of the pyramid is the unit test: many small checks of one function or one rule. Unit tests run in a fraction of a second, and when one fails it points straight at the broken line.'),
        ('The middle: connected tests',
         'Integration tests check that parts work together, such as a function that writes to a database and then reads the value back. They are slower and need more setup, so there are fewer of them.'),
        ('The top: whole-journey tests',
         'End-to-end tests run the whole program the way a person would, from the first screen to the last. They are the slowest and the most fragile, so keep a small number of them, for the paths that matter most.'),
        ('Guard the money first',
         'Put the most tests around the parts that handle money, goods and sign-in. A mistake there costs the most. The game\'s test file checks its books with the same audit the server uses, so a broken total is caught before it reaches players.'),
        ('A safe place to test',
         'Tests should run on their own copy of the data, never on the live game. The game\'s test file refuses to run on any database whose name does not end in "test". A check like that stops a test from wiping real players\' data.'),
    ],
    "test": [
        ('What is a unit test?',
         [('a', 'A check of one small function or rule'), ('b', 'A test of the whole program on a phone'), ('c', 'A measure of the screen size'), ('d', 'A test that only players run')], 'a'),
        ('Why are there fewer end-to-end tests than unit tests?',
         [('a', 'They are slower and more fragile, so a small number covers the key paths'), ('b', 'They are not needed at all'), ('c', 'They can only test colours'), ('d', 'They are only allowed on Fridays')], 'a'),
        ('Which part of a game deserves the most tests?',
         [('a', 'The decorative effects'), ('b', 'The parts that handle money, goods and sign-in'), ('c', 'The volume of the music'), ('d', 'The welcome text')], 'b'),
        ('Why does the game\'s test file refuse to run on a database whose name does not end in "test"?',
         [('a', 'Because test names must be short'), ('b', 'To save disk space'), ('c', 'So a test cannot wipe the live game\'s data'), ('d', 'To make the tests run faster')], 'c'),
        ('What does an integration test check?',
         [('a', 'Several parts working together, such as writing to a database and reading it back'), ('b', 'One line of code only'), ('c', 'How the program looks'), ('d', 'How fast the mouse moves')], 'a'),
    ],
}
