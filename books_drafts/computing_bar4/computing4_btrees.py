"""B-Trees and Disk Pages: wide trees that suit slow storage."""
CODE = "computing4_btrees"
BOOK = {
    "title": "B-Trees and Disk Pages",
    "subtitle": "Wide trees that suit slow storage",
    "chapters": [
        ("Why disks favour wide nodes", "Reading from a disk is slow, and disks move data in blocks, called pages. A node that fills a whole page holds many keys and needs few reads. Wide, shallow trees suit this better than tall, narrow ones."),
        ("Page size", "The page size is often a few kilobytes, set by the storage system. A B-tree node is sized to match one page. Choosing a page size is a trade-off between read cost and wasted space."),
        ("Search and insert", "Search checks the keys in a node and follows the right child down to the leaves. Insertion adds a key to a leaf. The tree stays balanced, so every search takes about the same number of reads."),
        ("Splitting and merging", "When a node is full, it splits into two and passes a key up to its parent. When nodes become too empty after deletions, they merge or borrow keys from a neighbour. These steps keep the tree in shape."),
        ("Keeping the tree shallow", "Because each node holds many keys, the tree grows very slowly. A few levels can index millions of entries. Fewer levels mean fewer disk reads for each lookup."),
        ("The trees behind most databases", "Most relational databases index their tables with B-tree variants. The same idea helps file systems find data quickly. Learning B-trees explains many everyday speed-ups."),
    ],
    "test": [
        ("Why do B-trees use wide nodes?",
         [("a", "Wide nodes take no space"), ("b", "Keys must be sorted by colour"), ("c", "Disk reads are slow, so fewer reads are better"), ("d", "Pages cannot hold numbers")], "c"),
        ("What is a page on a disk?",
         [("a", "A printed sheet of paper"), ("b", "A kind of password"), ("c", "A map in the game"), ("d", "A block of data read or written at once")], "d"),
        ("What happens when a B-tree node is full and a key is added?",
         [("a", "The node splits and passes a key to its parent"), ("b", "The key is thrown away"), ("c", "The whole database is deleted"), ("d", "The tree grows sideways forever")], "a"),
        ("Why does a B-tree stay shallow?",
         [("a", "It has only one key"), ("b", "Each node holds many keys"), ("c", "It stores data in the sky"), ("d", "It is never searched")], "b"),
        ("Where are B-tree variants commonly found?",
         [("a", "Most relational databases"), ("b", "Paint programs only"), ("c", "Music players only"), ("d", "Calculators only")], "a"),
    ],
}
