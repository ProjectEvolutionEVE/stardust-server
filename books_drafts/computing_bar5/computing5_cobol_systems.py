"""Running COBOL Systems: why decades-old business software still runs, what it takes to keep it going, and how it can be replaced safely."""
CODE = 'computing5_cobol_systems'
BOOK = {
    "title": 'Running COBOL Systems',
    "subtitle": 'Keeping old, important business software alive, and replacing it with care',
    "chapters": [
        ('A long-lived language',
         'COBOL dates from the late 1950s and was designed for business data processing. Huge amounts of banking, insurance and government work still run on it. Its longevity reflects how well it did a demanding job.'),
        ('Batch and transaction systems',
         'Many COBOL systems run batch jobs overnight and handle transactions during the day. Their reliability is built on decades of careful operation. Changing them means understanding how each job fits into the whole.'),
        ('Copybooks',
         'Copybooks are shared files of data definitions that many programs include. They keep record layouts consistent across a system. A change to one copybook can affect many programs at once.'),
        ('Skills gaps',
         'Fewer developers learn COBOL today, and experienced staff are retiring. Organisations must train people, pair them with veterans and document what the systems do. The skills gap is a real operational risk.'),
        ('Mainframe economics',
         'Mainframes can be very reliable and efficient at high volume, but they carry licence and hardware costs. Teams compare these with the costs of rebuilding. The right answer depends on the workload, the risks and the time available.'),
        ('Wrapping, replacing and knowledge loss',
         'Wrapping puts modern interfaces around an old system without rewriting its core. Replacing moves the work to a new system in stages, with checks against the old results. Knowledge loss is the quiet danger, so records and tests must capture what the old code really does.'),
    ],
    "test": [
        ('When did COBOL first appear?',
         [('a', 'The year 2020'), ('b', 'The 1800s'), ('c', 'The late 1950s'), ('d', 'The year 1990 only')], 'c'),
        ('What is a copybook?',
         [('a', 'A shared file of data definitions that programs include'), ('b', 'A notebook for a school class'), ('c', 'A type of printer ink'), ('d', 'A map of a shop')], 'a'),
        ('Why are COBOL skills a risk?',
         [('a', 'COBOL files are always blank'), ('b', 'COBOL cannot run on any computer'), ('c', 'COBOL is spoken in one village'), ('d', 'Fewer developers learn it and experienced staff are retiring')], 'd'),
        ('What does wrapping an old system do?',
         [('a', 'It wraps the server in paper'), ('b', 'It puts a modern interface around it without rewriting its core'), ('c', 'It deletes the data'), ('d', 'It moves the system into a cupboard')], 'b'),
        ('What is the quiet danger when replacing old systems?',
         [('a', 'Too many colours on the screen'), ('b', 'The old system being too fast'), ('c', 'Knowledge loss, if what the old code really does is not captured'), ('d', 'Old systems making too little noise')], 'c'),
    ],
}
