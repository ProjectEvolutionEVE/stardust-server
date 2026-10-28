"""Data lineage at scale: table and column lineage, capture methods, impact analysis, audit use and tooling limits."""
CODE = 'computing5_data_lineage'
BOOK = {
    "title": 'Data Lineage at Scale',
    "subtitle": 'Tracing where each number came from, and what breaks if it changes',
    "chapters": [
        ('Following the path',
         'Data lineage shows the path a value takes from its source, through each step of processing, to the report where people see it.'),
        ('Table and column lineage',
         'Table-level lineage shows which tables feed which. Column-level lineage goes further and shows which source field feeds each reported field.'),
        ('How lineage is captured',
         "Lineage can come from reading query logs, parsing the code that transforms data, or reading the scheduling tool's records. Most large teams combine methods."),
        ('Impact analysis',
         'Before changing a field, a team can ask what depends on it. Lineage gives a list of the reports and tables that would be affected.'),
        ('Audit and trust',
         "Auditors and regulators often ask where a figure came from. Lineage gives a clear trail, so the answer does not depend on one person's memory."),
        ('Tooling and limits',
         'Lineage tools can miss links, such as logic hidden in spreadsheets or in scripts outside the system. Teams check their lineage against reality from time to time.'),
    ],
    "test": [
        ('What does data lineage show?',
         [('a', 'The path a value takes from source to report'), ('b', 'The price of servers'), ('c', 'The staff holiday plan'), ('d', 'The colour of charts')], 'a'),
        ('What does column-level lineage show?',
         [('a', 'The room temperature'), ('b', 'The number of desks'), ('c', 'The name of the printer'), ('d', 'Which source field feeds each reported field')], 'd'),
        ('Which is a way to capture lineage?',
         [('a', 'Baking bread'), ('b', 'Reading query logs'), ('c', 'Painting walls'), ('d', 'Ringing a bell')], 'b'),
        ('What is impact analysis used for?',
         [('a', 'Choosing a song'), ('b', 'Counting birds'), ('c', 'Finding what would be affected by a change'), ('d', 'Buying lunch')], 'c'),
        ('Why do auditors value lineage?',
         [('a', 'It makes data larger'), ('b', 'It gives a clear trail for where figures came from'), ('c', 'It stops all audits'), ('d', 'It replaces the accounts')], 'b'),
    ],
}
