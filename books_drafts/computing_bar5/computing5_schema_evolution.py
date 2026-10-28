"""Schema evolution: forward and backward compatibility, safe changes, rolling deploys, expand-and-contract migrations and contract tests."""
CODE = 'computing5_schema_evolution'
BOOK = {
    "title": 'Schema Evolution and Compatibility',
    "subtitle": 'Changing the shape of data without breaking the systems that read it',
    "chapters": [
        ('Shapes change',
         'Products grow, so records gain new fields and some old fields fade away. The trouble starts when old and new programs must read the same data.'),
        ('Forward and backward',
         'Backward compatibility means new readers can read old data. Forward compatibility means old readers can handle new data, at least by ignoring what they do not know.'),
        ('Safe changes',
         'Adding an optional field with a default value is usually safe. Removing a field, or reusing its number, can break readers that still expect it.'),
        ('Rolling deploys',
         'Large systems update one part at a time, so old and new versions run together for a while. Changes must work across that mix.'),
        ('Expand and contract',
         'A common pattern first adds the new field, then moves the code over, and only later removes the old one. Each step keeps the system working.'),
        ('Testing',
         "Teams test old and new readers against samples of old and new data. Contract tests catch changes that would break another team's program."),
    ],
    "test": [
        ('What is backward compatibility?',
         [('a', 'New readers can read old data'), ('b', 'Old readers can read paper'), ('c', 'Data is printed'), ('d', 'No data is saved')], 'a'),
        ('Which change is usually safe?',
         [('a', 'Reusing an old field number'), ('b', 'Deleting a field that readers expect'), ('c', 'Adding an optional field with a default value'), ('d', 'Turning off all readers')], 'c'),
        ('Why do rolling deploys matter?',
         [('a', 'They print the new code'), ('b', 'They stop all updates'), ('c', 'They delete old data'), ('d', 'Old and new versions run together for a time')], 'd'),
        ('What does the expand-and-contract pattern do?',
         [('a', 'Removes everything at once'), ('b', 'Adds the new first and removes the old later'), ('c', 'Copies the database to paper'), ('d', 'Stops the team')], 'b'),
        ('What do contract tests catch?',
         [('a', 'Spelling in the manual'), ('b', 'Lunch orders'), ('c', "Changes that would break another team's program"), ('d', 'Colour in the logo')], 'c'),
    ],
}
