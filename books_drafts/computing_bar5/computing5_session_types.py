"""Session Types: protocols written as types, so programs follow the agreed conversation."""
CODE = 'computing5_session_types'
BOOK = {
    "title": 'Session Types',
    "subtitle": 'Protocols written as types, so programs follow the agreed conversation',
    "chapters": [
        ('A conversation with rules', 'Many programs talk to other programs in a fixed order. A login asks for a name, then a password, then answers yes or no. A session type writes that order down as a type, a kind of label that the checker reads before the program runs.'),
        ('Checking the order', 'A checker compares each message against the agreed script. If a program tries to send the password before the name, or to reply twice when only one reply is due, the checker reports the mistake. The check happens before the program is run.'),
        ('Duality', 'Every sending step has a matching receiving step on the other side. Duality is the idea that if one side of a conversation has a given type, the other side has the mirror image of it. Both sides can then be checked against one written script.'),
        ('Several parties', 'Some conversations have more than two parties, such as a buyer, a seller and a bank. Multiparty session types describe the whole conversation at once, and then check that each party part fits into it.'),
        ('Libraries that do it', 'Session types are often used through libraries and language features. Some languages build them in, and many others have libraries that copy the idea using the type system the language already has.'),
        ('Bugs prevented', 'Many errors in network code are not wrong data but wrong timing: a message arrives when nobody expects it, or a side waits forever. Session types catch many of these before the program ships, which saves time chasing them later.'),
    ],
    "test": [
        ('What is a session type mainly used to describe?',
         [('a', 'The colour of a screen'), ('b', 'The agreed order of messages between parties'), ('c', 'The price of memory'), ('d', 'The size of a file')], 'b'),
        ('When is a message-order mistake usually caught with session types?',
         [('a', 'At the moment of a crash, by luck'), ('b', 'Only after customers complain'), ('c', 'Before the program runs, by the checker'), ('d', 'Never; they cannot be caught')], 'c'),
        ('What does duality mean?',
         [('a', 'Each send has a matching receive on the other side'), ('b', 'Two programs must use two languages'), ('c', 'A program must run twice'), ('d', 'Each party keeps two copies of data')], 'a'),
        ('What do multiparty session types add?',
         [('a', 'Faster hard disks'), ('b', 'Free cloud storage'), ('c', 'A new colour scheme'), ('d', 'A way to describe conversations with more than two parties')], 'd'),
        ('Which kind of error do session types help prevent most directly?',
         [('a', 'Messages sent or received in the wrong order'), ('b', 'Typing mistakes in comments'), ('c', 'Slow screen drawing'), ('d', 'Running out of disk space')], 'a'),
    ],
}
