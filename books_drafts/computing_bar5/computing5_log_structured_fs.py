"""Log-Structured File Systems: writing everything in order at the end of a log, and tidying up behind it."""
CODE = 'computing5_log_structured_fs'
BOOK = {
    "title": 'Log-Structured File Systems',
    "subtitle": 'Writing everything in order at the end of a log, and tidying up behind it',
    "chapters": [
        ('Append-only writes', 'A log-structured file system writes new data at the end of a log rather than in place. Changes are added in order, which turns many small random writes into one long sequential write. Sequential writes are much faster on disks.'),
        ('Segment cleaning', 'Old data in the log becomes dead when files change, leaving gaps. A cleaner gathers live data from partly empty segments and rewrites it together, freeing whole segments. This is called segment cleaning.'),
        ('The LFS history', 'Mendel Rosenblum and John Ousterhout described the Sprite log-structured file system in the early 1990s. Their work showed that writing in a log could make disks much faster for small writes. Many later designs took ideas from it.'),
        ('Flash friendliness', 'Flash memory dislikes overwriting in place, and repeated rewrites wear it out. Log-style writing suits flash, because data goes to fresh pages and the cleaner handles old ones. That is one reason the idea is common in flash storage.'),
        ('Checkpoints', 'The file system writes checkpoints that record where the latest structures are. After a crash, it reads the most recent checkpoint and replays the log from there. This keeps recovery quick.'),
        ('Garbage in logs', 'Logs fill with old versions of data, which must be cleaned. Cleaning costs time and can slow the system when the disk is nearly full. Good designs balance the cleaning rate against everyday speed.'),
    ],
    "test": [
        ('Where does a log-structured file system write new data?',
         [('a', 'On paper'), ('b', 'At the end of a log'), ('c', 'Only in memory'), ('d', 'In random places only')], 'b'),
        ('What is segment cleaning?',
         [('a', 'Washing windows'), ('b', 'Painting disks'), ('c', 'Deleting the power'), ('d', 'Gathering live data from partly empty segments and rewriting it together')], 'd'),
        ('Who described the Sprite log-structured file system?',
         [('a', 'Rosenblum and Ousterhout'), ('b', 'Turing and Church'), ('c', 'Lovelace and Babbage'), ('d', 'Hopper and Knuth')], 'a'),
        ('Why does log-style writing suit flash?',
         [('a', 'Flash likes paint'), ('b', 'Flash needs no pages'), ('c', 'Data goes to fresh pages instead of rewriting in place'), ('d', 'Flash is always wet')], 'c'),
        ('What do checkpoints record?',
         [('a', 'Where the latest structures are'), ('b', 'The weather'), ('c', 'The owner pet'), ('d', 'The price of disks')], 'a'),
    ],
}
