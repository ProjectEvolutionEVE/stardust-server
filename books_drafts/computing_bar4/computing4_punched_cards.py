"""Punched Cards and Early Data Processing: how records were stored, sorted and counted before electronic storage."""
CODE = 'computing4_punched_cards'
BOOK = {
    "title": 'Punched Cards and Early Data Processing',
    "subtitle": 'How records were stored, sorted and counted before electronic storage',
    "chapters": [
        ('Hollerith tabulation',
         'Herman Hollerith developed a method of counting census records with punched cards and electrical tabulating machines. His system was used for the United States census of 1890. It made counting far faster than hand tallies.'),
        ('Census work',
         'Census offices faced huge volumes of records, and the tabulating machines helped them finish counts within a practical time. Each card held information about one person, and the machines could count and sort them by category.'),
        ('Card formats',
         'A card had a fixed layout, with columns and rows, and each column held a particular piece of data. Later card formats, such as the eighty-column card, were widely used. The fixed layout made data reliable but also rigid.'),
        ('Sorting machines',
         'Sorting machines dropped cards into pockets according to the holes in one column. Operators ran cards through several passes to sort by many fields. This was slow compared with modern methods but reliable.'),
        ('Data as records',
         'Punched cards taught early computing that data should be stored as records, each with the same set of fields. This idea remains at the heart of databases and spreadsheets. The shape of a record still matters.'),
        ('Legacy practices',
         'Some habits of card processing, such as checking totals and keeping batches in order, lasted long after cards were gone. They influenced the way organisations test and audit data. Early practices shaped later careful work.'),
    ],
    "test": [
        ('Who developed the early punched card tabulating method?',
         [('a', 'Isaac Newton'), ('b', 'Marie Curie'), ('c', 'Herman Hollerith'), ('d', 'Galileo Galilei')], 'c'),
        ('For which official count was Hollerith’s method used in 1890?',
         [('a', 'The United States census'), ('b', 'A school sports day'), ('c', 'A music festival'), ('d', 'A train timetable')], 'a'),
        ('What did each card in a census count usually hold?',
         [('a', 'A whole city'), ('b', 'A recipe'), ('c', 'A map of the moon'), ('d', 'Information about one person')], 'd'),
        ('What did sorting machines do with cards?',
         [('a', 'Painted them'), ('b', 'Dropped them into pockets according to holes in one column'), ('c', 'Folded them into boats'), ('d', 'Sent them by post')], 'b'),
        ('What idea did punched cards teach early computing?',
         [('a', 'Data should never be counted'), ('b', 'Data is always stored on paper boats'), ('c', 'Data should be stored as records with the same set of fields'), ('d', 'Data is illegal to sort')], 'c'),
    ],
}
