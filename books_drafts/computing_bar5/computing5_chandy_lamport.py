"""Consistent Global Snapshots: photographing a running distributed system without stopping it."""
CODE = 'computing5_chandy_lamport'
BOOK = {
    "title": 'Consistent Global Snapshots',
    "subtitle": 'Photographing a running distributed system without stopping it',
    "chapters": [
        ('A picture of a moving system', 'A distributed system has no single clock or room where all its state sits. A snapshot records each machine state and the messages in transit, so that the picture makes sense as a whole, even though the machines were not all recorded at the same instant.'),
        ('Marker messages', 'The Chandy and Lamport method, published in 1985, sends special marker messages along every channel. When a process first sees a marker, it saves its own state and sends markers on its outgoing channels. Messages arriving on each channel before its marker are recorded as part of the snapshot.'),
        ('Consistent cuts', 'The recorded picture is a consistent cut: no message is recorded as received without having been sent. A cut like this could have happened during a real run, so the state it shows is possible.'),
        ('Checkpointing', 'Snapshots are a kind of checkpoint, a saved point to restart from. Systems use them to recover after failures, so work does not have to start from scratch. Saving only the needed parts keeps the cost low.'),
        ('Use in recovery', 'After a crash, a system can roll back to the last consistent snapshot and continue. The snapshot guarantees that the restart does not mix states that never existed together. This makes recovery both fast and correct.'),
        ('Reading a running system', 'Operators and debuggers use snapshots to see what a live system is doing, such as which work is waiting on which. Because the picture is consistent, its conclusions are trustworthy, even though the system never paused.'),
    ],
    "test": [
        ('What do marker messages do?',
         [('a', 'Paint the messages'), ('b', 'Mark the boundaries of a consistent snapshot on each channel'), ('c', 'Delete messages'), ('d', 'Speed up the network')], 'b'),
        ('What is a consistent cut?',
         [('a', 'A haircut'), ('b', 'A money-saving plan'), ('c', 'A broken cable'), ('d', 'A snapshot where no message is recorded as received without being sent')], 'd'),
        ('Why is a checkpoint useful?',
         [('a', 'It removes the clock'), ('b', 'It makes users sleep'), ('c', 'It is a saved point to restart from'), ('d', 'It stops the network')], 'c'),
        ('What must a restart after a crash avoid?',
         [('a', 'Using snapshots'), ('b', 'Starting at all'), ('c', 'Logging events'), ('d', 'Mixing states that never existed together')], 'd'),
        ('Why are the conclusions from a snapshot trustworthy?',
         [('a', 'Because the system stopped'), ('b', 'Because nobody looked'), ('c', 'Because the picture is consistent, even though the system did not pause'), ('d', 'Because it is random')], 'c'),
    ],
}
