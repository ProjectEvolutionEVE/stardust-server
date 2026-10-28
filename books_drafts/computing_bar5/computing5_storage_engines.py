"""Storage engines: B-tree versus LSM trees, write, read and space amplification, and how workloads map to engines."""
CODE = 'computing5_storage_engines'
BOOK = {
    "title": 'Storage Engines Compared',
    "subtitle": 'B-trees and log-structured trees, and the costs each one pushes onto the system',
    "chapters": [
        ('Two common designs',
         'A B-tree updates data in place, keeping a sorted tree on disk. A log-structured merge tree writes changes quickly to new files, then merges them in the background.'),
        ('Write amplification',
         'Write amplification is how many bytes are written to disk for each byte the user changed. Background merges add writes, so log-structured designs often write more in total.'),
        ('Read amplification',
         'Read amplification is how many places must be checked to find one value. A log-structured design may check several files, while a B-tree usually checks a few pages.'),
        ('Space amplification',
         'Space amplification is how much storage is used compared with the data itself. Old copies waiting to be merged take up room.'),
        ('The trade-off',
         'Researchers describe a trade-off between read, write and space costs. Improving one often makes another worse.'),
        ('Choosing and tuning',
         'Teams map their workload to an engine. A write-heavy system may suit a log-structured design, and a read-heavy one a B-tree, and both can be tuned.'),
    ],
    "test": [
        ('How does a B-tree write data?',
         [('a', 'It updates data in place'), ('b', 'It prints every change'), ('c', 'It sends data by email'), ('d', 'It deletes the table each time')], 'a'),
        ('What is write amplification?',
         [('a', 'Louder disks'), ('b', 'Faster typing'), ('c', 'Bytes written to disk for each byte changed'), ('d', 'More screens')], 'c'),
        ('What does read amplification measure?',
         [('a', 'The brightness of the screen'), ('b', 'How many users are online'), ('c', 'The price of paper'), ('d', 'How many places must be checked to find a value')], 'd'),
        ('What does space amplification measure?',
         [('a', 'The number of tables'), ('b', 'Storage used compared with the data itself'), ('c', 'The age of the server'), ('d', 'The length of queries')], 'b'),
        ('What is the trade-off between these costs?',
         [('a', 'Every cost always falls'), ('b', 'No cost matters'), ('c', 'Costs are set by the weather'), ('d', 'Improving one often makes another worse')], 'd'),
    ],
}
