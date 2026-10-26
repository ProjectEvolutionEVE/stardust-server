"""Hard bugs: bisecting the history, chasing bugs that come and go, and keeping a clear record of what was found."""
CODE = 'computing3a_hard_bugs'
BOOK = {
    "title": 'Hard Bugs',
    "subtitle": 'Bisecting history, chasing bugs that come and go, and keeping a clear record',
    "chapters": [
        ('When the easy checks fail',
         'Some bugs are simple, like a typo or a missing check. Others hide for days, come and go, or appear only after a certain sequence of actions. For these, change how you search. Write down what you know, what you have tried and what you saw.'),
        ('Bisecting the history',
         'If a program worked last month and fails now, the change that broke it lies somewhere in between. Bisecting tests the middle change, then halves the search again and again. Version control tools such as git bisect do this for you. A history of about 1,000 changes needs only about 10 tests.'),
        ('Reproduce it first',
         'A bug you cannot make happen is very hard to fix. Find the smallest set of steps that triggers it and write them down. If it comes and goes, repeat the same steps many times, or change one thing at a time to see what really matters.'),
        ('Timing and order',
         'Intermittent bugs often depend on timing: which request arrives first, or how long a slow step takes. Adding a short wait can make the bug show up every time, which helps you see it. Race conditions are a common cause, as the book on race conditions explains.'),
        ('Logs and clues',
         'A log is a written record of what a program did and when. Good log lines have a time, the name of the part that wrote them, and the values that matter. The game\'s background loops print their errors with the error type and the message, so a failure leaves a clue.'),
        ('Fixing and recording',
         'Once you find the cause, fix it, then add a test that would have failed without the fix. Write a short note about what went wrong, so the next person does not have to find it again.'),
    ],
    "test": [
        ('What does bisecting a history do?',
         [('a', 'It checks the middle change, then halves the search, to find the change that broke a program'), ('b', 'It splits a file into two halves for storage'), ('c', 'It doubles the size of each change'), ('d', 'It sorts the names alphabetically')], 'a'),
        ('About how many tests does bisecting need to search 1,000 changes?',
         [('a', 'About 1,000'), ('b', 'Just 1'), ('c', 'About 500'), ('d', 'About 10')], 'd'),
        ('Why is a bug you cannot make happen so hard to fix?',
         [('a', 'You cannot tell whether a fix works'), ('b', 'Bugs that do not happen are always harmless'), ('c', 'Computers hide their errors from people'), ('d', 'Fixes can only be made on Fridays')], 'a'),
        ('What is a good first step for a bug that comes and goes?',
         [('a', 'Restart the computer and forget about it'), ('b', 'Delete the logs'), ('c', 'Find the smallest set of steps that triggers it'), ('d', 'Change the colour of the screen')], 'c'),
        ('What should a good log line include?',
         [('a', 'Only the word "error"'), ('b', 'A time, the name of the part, and the values that matter'), ('c', 'The whole source code of the game'), ('d', 'Nothing that could help')], 'b'),
    ],
}
