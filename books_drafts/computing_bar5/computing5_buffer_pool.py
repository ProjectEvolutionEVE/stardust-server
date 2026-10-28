"""Buffer pools: caching disk pages, pinning, dirty pages, replacement policies and interaction with the operating system."""
CODE = 'computing5_buffer_pool'
BOOK = {
    "title": 'Buffer Pools and Page Management',
    "subtitle": 'Keeping the most useful pages of data in memory',
    "chapters": [
        ('Disk is slow',
         'Reading from a disk is far slower than reading from memory. A database keeps a working set of data pages in memory to avoid most disk reads.'),
        ('The buffer pool',
         'The buffer pool is a region of memory holding copies of disk pages. When a query needs a page, the database checks the pool first.'),
        ('Pinning',
         'A page in use is pinned so it cannot be pushed out of memory while someone is reading or writing it. Unpinned pages can be replaced.'),
        ('Replacement policies',
         'When the pool is full, a policy picks a page to remove. Least recently used and the clock algorithm are common choices.'),
        ('Dirty pages',
         'A page changed in memory is dirty until it is written back to disk. The database must write it safely, often using a log, before reusing its space.'),
        ('The operating system',
         'The operating system also caches files, so the same data can sit in memory twice. Some databases use direct I/O to bypass that cache and manage memory themselves.'),
    ],
    "test": [
        ('Why keep pages in memory?',
         [('a', 'Memory is much faster than disk'), ('b', 'Disks are faster than memory'), ('c', 'Pages have no value'), ('d', 'To print them')], 'a'),
        ('What does pinning do?',
         [('a', 'Paints the page'), ('b', 'Deletes the page'), ('c', 'Stops a page being removed while in use'), ('d', 'Sends the page to a printer')], 'c'),
        ('What is a dirty page?',
         [('a', 'A page changed in memory but not yet written to disk'), ('b', 'A page with spelling errors'), ('c', 'A page with no data'), ('d', 'A page of a book')], 'a'),
        ('Which is a common replacement policy?',
         [('a', 'Most colourful first'), ('b', 'Random dancing'), ('c', 'Alphabetical by weather'), ('d', 'Least recently used')], 'd'),
        ('Why might the same data sit in memory twice?',
         [('a', 'The disk has two heads'), ('b', 'The database and operating system both cache files'), ('c', 'The printer copies it'), ('d', 'The screen shows it twice')], 'b'),
    ],
}
