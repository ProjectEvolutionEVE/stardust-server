"""Master data management: duplicate records, matching, merging, golden records, stewardship and failure modes."""
CODE = 'computing5_master_data'
BOOK = {
    "title": 'Master Data Management',
    "subtitle": 'One trusted record for each customer, product or supplier',
    "chapters": [
        ('The same customer, many times',
         'A large firm often has the same customer in several systems, with slightly different names and addresses. Reports then count the same person twice.'),
        ('Matching',
         'Master data management compares records to find those that refer to the same thing. Matching uses exact fields such as tax numbers, along with fuzzy comparisons of names.'),
        ('Merging',
         'Once matched, records are merged into one. Rules decide which value wins when two records disagree, such as which address is newer.'),
        ('Golden records',
         'The merged record is the golden record, the single version other systems can trust. It is kept in a central hub or shared with other systems.'),
        ('Stewardship',
         'Data stewards are people who review hard cases and set the rules. Machines do the bulk of the work, but people settle the doubtful matches.'),
        ('Failure modes',
         'Matching can go wrong, and merging two different customers is a serious mistake. Hubs can also go out of date if no one owns them.'),
    ],
    "test": [
        ('What problem does master data management solve first?',
         [('a', 'Duplicate records for the same customer'), ('b', 'Too many chairs'), ('c', 'Slow printers'), ('d', 'Missing sunshine')], 'a'),
        ('What is a golden record?',
         [('a', 'A gold-coloured file'), ('b', 'A reward for staff'), ('c', 'A backup disk'), ('d', 'The single trusted version of a record')], 'd'),
        ('What do matching rules do?',
         [('a', 'Print labels'), ('b', 'Turn off the network'), ('c', 'Find records that refer to the same thing'), ('d', 'Delete old staff')], 'c'),
        ('Who settles the doubtful matches?',
         [('a', 'A data steward'), ('b', 'The printer'), ('c', 'A cloud robot alone'), ('d', 'Nobody')], 'a'),
        ('What is a serious mistake in matching?',
         [('a', 'Matching a customer to a tax number'), ('b', 'Keeping a record of one address'), ('c', 'Reviewing a report'), ('d', 'Merging two different customers into one')], 'd'),
    ],
}
