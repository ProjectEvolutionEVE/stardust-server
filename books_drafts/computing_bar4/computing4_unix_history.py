"""The History of Unix: from Bell Labs to today's systems, with its small tools, pipes and licensing splits."""
CODE = 'computing4_unix_history'
BOOK = {
    "title": 'The History of Unix',
    "subtitle": 'From Bell Labs to today’s systems, with small tools, pipes and licence splits',
    "chapters": [
        ('Bell Labs origins',
         'Unix began in 1969 at Bell Labs, where Ken Thompson and Dennis Ritchie worked on a small operating system. It was designed to be simple and useful to programmers. Its early growth came from the people who used it and shared it.'),
        ('Pipes and small tools',
         'Unix encouraged small programs that each do one job well. In 1973, a pipe feature let the output of one program feed straight into another. This simple idea made complex work from simple parts, and it remains central to Unix culture.'),
        ('C and portability',
         'Unix was rewritten in the C language, which made it easier to move to other computers. This portability was one of its great strengths. Many later systems and languages were shaped by this approach.'),
        ('Licensing splits',
         'Unix was licensed by AT&T, and licences restricted how it could be shared. Over time, several branches emerged with different terms. These disputes shaped the later open-source movement.'),
        ('The BSD and Linux lineage',
         'The Berkeley Software Distribution, or BSD, grew from university work on Unix and is still developed in several forms. Linux, begun in 1991, was written from scratch but followed Unix ideas. Many systems today trace their habits to these roots.'),
        ('Lessons',
         'Unix shows the value of simple tools, clear interfaces and portable code. It also shows how licences and ownership can split a community. Its history is a useful reminder that design choices and legal choices both shape a system’s future.'),
    ],
    "test": [
        ('When did Unix begin at Bell Labs?',
         [('a', '1901'), ('b', '1995'), ('c', '1850'), ('d', '1969')], 'd'),
        ('What did the pipe feature in 1973 allow?',
         [('a', 'Water to flow through the computer'), ('b', 'The output of one program to feed into another'), ('c', 'Printing in colour'), ('d', 'Music to play during work')], 'b'),
        ('Why was Unix rewritten in C?',
         [('a', 'To make it impossible to read'), ('b', 'To remove all tools'), ('c', 'To make it easier to move to other computers'), ('d', 'To stop programmers using it')], 'c'),
        ('What is the BSD?',
         [('a', 'A Unix lineage that grew from university work'), ('b', 'A type of bicycle'), ('c', 'A brand of keyboard'), ('d', 'A bank in Europe')], 'a'),
        ('What do Unix licence splits show?',
         [('a', 'That licences are never needed'), ('b', 'How ownership and licences can divide a community'), ('c', 'That Unix has no users'), ('d', 'That Unix only runs on paper')], 'b'),
    ],
}
