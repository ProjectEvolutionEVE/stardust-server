"""Database reliability engineering: restore tests, failover drills, capacity, connection storms, zero-downtime upgrades and runbooks."""
CODE = 'computing5_db_reliability'
BOOK = {
    "title": 'Database Reliability Engineering',
    "subtitle": 'Keeping databases running, recoverable and ready for the next failure',
    "chapters": [
        ('A backup is not proven',
         'A backup that has never been restored is only a hope. Teams schedule restore tests to prove that data really comes back.'),
        ('Failover drills',
         'Failover moves work to a standby system when the main one fails. Drills rehearse the move so it works smoothly under pressure.'),
        ('Capacity limits',
         'Every database has limits on connections, memory and disk. Teams watch these trends so they can add capacity before a limit is reached.'),
        ('Connection storms',
         'When many applications reconnect at once, the database can be overwhelmed. Connection pooling and gradual retries help prevent this.'),
        ('Upgrades without downtime',
         'Upgrades can be tried first on a standby, with careful checks before switching over. A rollback plan should be ready.'),
        ('Runbooks',
         'A runbook is a written guide for responding to a known problem. On-call staff use runbooks so they act clearly at night under stress.'),
    ],
    "test": [
        ('Why test restores regularly?',
         [('a', 'To prove that backups really come back'), ('b', 'To make backups bigger'), ('c', 'To delete old data'), ('d', 'To sell the server')], 'a'),
        ('What is a failover drill?',
         [('a', 'A fire drill for the kitchen'), ('b', 'A game of cards'), ('c', 'Turning the database off forever'), ('d', 'Rehearsing a move to a standby system')], 'd'),
        ('What can a connection storm do?',
         [('a', 'Print the schema'), ('b', 'Fix all bugs'), ('c', 'Overwhelm the database'), ('d', 'Lower the bill')], 'c'),
        ('Why are runbooks useful on call?',
         [('a', 'They replace the database'), ('b', 'They give clear steps for a known problem'), ('c', 'They are decorative'), ('d', 'They stop all alerts forever')], 'b'),
        ('What helps upgrades avoid downtime?',
         [('a', 'Trying on a standby first, with a ready rollback'), ('b', 'Turning everything off at once'), ('c', 'Skipping all checks'), ('d', 'Upgrading at random')], 'a'),
    ],
}
