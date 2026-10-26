"""Hash tables in depth: buckets, collisions, load and resizing, and how lookups stay quick."""
CODE = 'computing3a_hash_tables'
BOOK = {
    "title": 'Hash Tables in Depth',
    "subtitle": 'Buckets, collisions, load and resizing: how lookups stay quick',
    "chapters": [
        ('Buckets',
         'A hash table keeps its items in a row of buckets, numbered from zero. A hash function turns each key into a bucket number, and the table goes straight to that bucket. On average, a lookup takes about the same time, however many items the table holds.'),
        ('Collisions happen',
         'Two different keys can give the same bucket number. This is called a collision. With a fixed number of buckets, collisions cannot be avoided completely, so a good table is built to cope with them.'),
        ('Chaining',
         'One way to cope is chaining. Each bucket holds a short list of all the items that landed there. A lookup scans only that short list. If the hash spreads the keys evenly, each list stays short.'),
        ('Open addressing',
         'Another way is open addressing. When a bucket is already taken, the table tries another bucket in a set order, called probing, until it finds an empty one. Lookups follow the same order to find the item again.'),
        ('Load and resizing',
         'The load factor is the number of items divided by the number of buckets. As it rises, collisions become more common and lookups slow down. Most tables grow to more buckets when the load passes a set level, and then spread the items out again.'),
        ('Choosing a good key',
         'A poor hash, one that gives the same number for many different keys, makes a table slow however good the rest of it is. A table of user names needs a hash that spreads the names across the buckets evenly. Test a table with many keys to see how it really behaves.'),
    ],
    "test": [
        ('What is a bucket in a hash table?',
         [('a', 'A slot that holds the items whose keys hash to its number'), ('b', 'A file on disk'), ('c', 'The root of a tree'), ('d', 'A copy of the whole table')], 'a'),
        ('What is a collision?',
         [('a', 'A table that has been deleted'), ('b', 'A key that is too long'), ('c', 'Two different keys that land in the same bucket'), ('d', 'A lookup that finds nothing')], 'c'),
        ('What does the load factor measure?',
         [('a', 'The number of buckets divided by the number of items'), ('b', 'The time it takes to read a file'), ('c', 'The size of each key'), ('d', 'The number of items divided by the number of buckets')], 'd'),
        ('What does chaining do?',
         [('a', 'Each bucket holds a short list of the items that landed there'), ('b', 'It joins two tables into one'), ('c', 'It stores every item in a single line on disk'), ('d', 'It removes all collisions')], 'a'),
        ('Why does a table grow when its load gets high?',
         [('a', 'To use more memory on purpose'), ('b', 'So that its lists and probes stay short and lookups stay quick'), ('c', 'To make every key unique'), ('d', 'Because keys wear out over time')], 'b'),
    ],
}
