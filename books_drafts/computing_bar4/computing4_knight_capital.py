"""Knight Capital: A Deployment Gone Wrong: how an old piece of code was switched back on by a faulty release, and the lessons for changes."""
CODE = 'computing4_knight_capital'
BOOK = {
    "title": 'Knight Capital: A Deployment Gone Wrong',
    "subtitle": 'How old code was switched back on by a faulty release, and the lessons for changes',
    "chapters": [
        ('Old code reactivated',
         'In August 2012, the trading firm Knight Capital released new software. A flag that had once turned off an old trading routine was reused for a new purpose. On one of its servers, the old code was still present, and the flag switched it back on.'),
        ('A faulty deployment',
         'The new software was not put on all of the company’s servers. The one server still running the old code behaved differently from the rest. The mismatch between servers was not spotted before trading began.'),
        ('Trading losses',
         'The old routine began sending a large volume of unwanted orders into the market. The firm lost about 440 million dollars in roughly 45 minutes. The losses were far larger than the firm’s normal daily results.'),
        ('The response',
         'Staff tried to find the cause while the losses grew, and the firm had to stop trading. The firm later raised money to survive, and it was bought by another company. The event became a widely studied case in software operations.'),
        ('Control failures',
         'The episode exposed weak controls, such as no automatic check that all servers matched, and no clear kill switch for the trading system. Old code had been left in place rather than removed. Missing checks let a small mistake grow into a huge one.'),
        ('Lessons for releases',
         'Keep every server on the same version, and check that they match before and after a release. Remove dead code rather than leaving it switched off. Make sure there is a fast way to stop a system, and rehearse using it.'),
    ],
    "test": [
        ('What happened in the Knight Capital episode in August 2012?',
         [('a', 'A faulty release switched on old trading code'), ('b', 'A new office was opened'), ('c', 'A bank holiday was cancelled'), ('d', 'A new phone was launched')], 'a'),
        ('Why was one server behaving differently from the rest?',
         [('a', 'All servers were turned off'), ('b', 'The servers had new paint'), ('c', 'The new software had not been put on all of the servers'), ('d', 'The servers were in different countries on purpose')], 'c'),
        ('What was the approximate loss in roughly 45 minutes?',
         [('a', 'About 44 dollars'), ('b', 'About 440 million dollars'), ('c', 'Nothing at all'), ('d', 'About 4 billion pounds of cake')], 'b'),
        ('What should be done with dead code rather than leaving it switched off?',
         [('a', 'Hide it in a drawer'), ('b', 'Copy it to every server'), ('c', 'Name it after a holiday'), ('d', 'Remove it')], 'd'),
        ('Which lesson does this case give for releases?',
         [('a', 'Check that every server matches before and after a release'), ('b', 'Release on every server at random'), ('c', 'Never check anything'), ('d', 'Keep old code forever')], 'a'),
    ],
}
