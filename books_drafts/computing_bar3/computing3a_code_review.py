"""Code review: reading another person's change carefully, and giving feedback that helps."""
CODE = 'computing3a_code_review'
BOOK = {
    "title": 'Code Review',
    "subtitle": 'Reading another person\'s change carefully, and giving feedback that helps',
    "chapters": [
        ('A second pair of eyes',
         'Code review means another person reads a change before it becomes part of the program. The author knows what the change is meant to do, so they often miss their own mistakes. A reviewer reads it fresh, and that is where many problems are caught.'),
        ('Keep changes small',
         'A small change is easier to read and easier to understand. A reviewer who faces a huge change tends to skim it. Splitting one big job into several small changes makes each review more careful.'),
        ('What to look for',
         'Check that the change does what it says, that it handles the edge cases, and that it does not break other parts. Look for unclear names, code that is hard to follow, and missing tests. Ask whether a rule now lives in one place or has been copied into many.'),
        ('Money and safety first',
         'Give extra care to any change that touches money, sign-in or private data. The game\'s review team checks each blueprint design before it can be approved, using steps such as listing, showing, asking for changes, approving or rejecting. Code that changes what players own deserves the same care.'),
        ('Giving good feedback',
         'Write comments about the code, not about the person. Say what you saw, why it matters, and what might work better. A question often helps: "What happens if this list is empty?" can teach more than a flat order.'),
        ('Being reviewed',
         'Receiving a review well is a skill too. Read every comment, answer each one, and thank the reviewer for finding what you missed. If you disagree, explain why, and let the reviewer weigh in before you decide.'),
    ],
    "test": [
        ('What is the main purpose of a code review?',
         [('a', 'To time how fast a developer types'), ('b', 'To replace all testing'), ('c', 'To have a second person read a change before it becomes part of the program'), ('d', 'To hide changes from the team')], 'c'),
        ('Why are small changes easier to review?',
         [('a', 'They never contain bugs'), ('b', 'They are easier to read and understand carefully'), ('c', 'They skip the review step'), ('d', 'They use less storage')], 'b'),
        ('When a reviewer checks a change, which question is most useful?',
         [('a', 'Does the change do what it says, and what happens at the edges?'), ('b', 'Is the author the fastest typist on the team?'), ('c', 'Is the file the largest one in the project?'), ('d', 'Can the change be left without a description?')], 'a'),
        ('Which kind of change deserves the most care in review?',
         [('a', 'A change to a colour in the menu'), ('b', 'A change to a comment'), ('c', 'A change to the window title'), ('d', 'A change to money, sign-in or private data')], 'd'),
        ('What makes a review comment most helpful?',
         [('a', 'It is short and says only "bad"'), ('b', 'It is about the code, says what was seen and why it matters, and suggests a way forward'), ('c', 'It attacks the author'), ('d', 'It gives no reason at all')], 'b'),
    ],
}
