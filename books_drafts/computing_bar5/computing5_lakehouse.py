"""Data lakehouse architecture: files plus tables, open table formats, transactions on object storage, governance and cost."""
CODE = 'computing5_lakehouse'
BOOK = {
    "title": 'Data Lakehouse Architecture',
    "subtitle": 'Cheap file storage with the reliable features of a data warehouse',
    "chapters": [
        ('Two worlds',
         'A data lake keeps files cheaply on storage, but has been hard to trust. A data warehouse is reliable and structured, but can be costly for large volumes.'),
        ('Files plus tables',
         'A lakehouse keeps data as files on cheap object storage, and adds a table layer on top. The table layer tracks which files make up each table.'),
        ('Table formats',
         'Open table formats such as Apache Iceberg, Delta Lake and Apache Hudi add a log of changes. This lets many writers and readers use the same data safely.'),
        ('Transactions',
         'Because the table format records each change, a write either completes or does not appear at all. Readers see a consistent version of the table.'),
        ('Governance and cost',
         'Access rules, schemas and audit logs keep the data controlled. Storage is cheap, but many small files and heavy queries can make compute costs rise.'),
        ('Choosing',
         'A lakehouse suits mixed workloads, but it adds moving parts. Teams weigh its flexibility against the work of running it well.'),
    ],
    "test": [
        ('What is a data lake strong at?',
         [('a', 'Cheap storage of files'), ('b', 'Printing reports'), ('c', 'Playing video'), ('d', 'Sending post')], 'a'),
        ('What does the table layer track?',
         [('a', 'The weather'), ('b', 'Staff birthdays'), ('c', 'Which files make up each table'), ('d', 'The colour of the logo')], 'c'),
        ('Which is an open table format?',
         [('a', 'Microsoft Word'), ('b', 'A paper ledger'), ('c', 'A USB stick'), ('d', 'Apache Iceberg')], 'd'),
        ('Why does the table format keep a log of changes?',
         [('a', 'So storage is free'), ('b', 'So writes are safe and readers see a consistent version'), ('c', 'So the files can be printed'), ('d', 'So the data is deleted monthly')], 'b'),
        ('What can make compute costs rise in a lakehouse?',
         [('a', 'A single large file'), ('b', 'Using one reader'), ('c', 'Many small files and heavy queries'), ('d', 'Turning off logs')], 'c'),
    ],
}
