"""Distributed File Systems: keeping files across many machines, with metadata, chunks and copies."""
CODE = 'computing5_distributed_fs'
BOOK = {
    "title": 'Distributed File Systems',
    "subtitle": 'Keeping files across many machines, with metadata, chunks and copies',
    "chapters": [
        ('Files across many machines', 'A distributed file system spreads files over many machines but lets users see one set of folders. Programs open and read files as if they were local. The system hides where each piece really lives.'),
        ('Metadata servers', 'A metadata server keeps the directory tree and records where each file pieces are stored. The data itself flows between clients and storage servers. Keeping metadata apart from data is a common and effective design.'),
        ('GFS and HDFS ideas', 'The Google File System, described in 2003, and the Hadoop Distributed File System, which took many of its ideas, store large files as chunks spread across many servers. These designs were built for large batch work on ordinary machines.'),
        ('Chunking', 'Large files are split into fixed-size chunks, and each chunk is stored on several servers. Reads can come from any copy, and parallel reads speed up big jobs. Chunking spreads both load and risk.'),
        ('Replication', 'Each chunk is kept in several copies, so a single server failure does not lose data. When a copy is lost, the system copies it again from the survivors. Replication costs disk space but gives strong protection.'),
        ('Consistency', 'Consistency in these systems often means a relaxed rule for concurrent writes, such as record appends. Clients may see a copy that is a little behind. Designers decide which guarantees matter most for each workload.'),
    ],
    "test": [
        ('What does a distributed file system let users see?',
         [('a', 'Only fish'), ('b', 'Only colours'), ('c', 'Many suns'), ('d', 'One set of folders')], 'd'),
        ('What does a metadata server keep?',
         [('a', 'The directory tree and where each file pieces are stored'), ('b', 'Only songs'), ('c', 'The weather'), ('d', 'Only pictures')], 'a'),
        ('When was the Google File System described?',
         [('a', '1066'), ('b', '1492'), ('c', '2003'), ('d', '1800')], 'c'),
        ('Why are large files split into chunks?',
         [('a', 'To store them in colour'), ('b', 'To spread load and risk, and allow parallel reads'), ('c', 'To hide them from the user'), ('d', 'To make them smaller for paper')], 'b'),
        ('Why keep several copies of each chunk?',
         [('a', 'So one server failure does not lose data'), ('b', 'So the file is painted'), ('c', 'So the power is saved'), ('d', 'So the folder is blue')], 'a'),
    ],
}
