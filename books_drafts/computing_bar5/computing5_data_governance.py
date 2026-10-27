"""Data governance programmes: policies, owners and stewards, catalogues, access rules, shared standards and measurement."""
CODE = 'computing5_data_governance'
BOOK = {
    "title": 'Data Governance Programmes',
    "subtitle": 'Who may use what data, who is responsible for it, and how it stays under control',
    "chapters": [
        ('What governance is',
         'Data governance is the set of policies, roles and habits that decide how an organisation handles its data. It answers who owns data, who may see it, and what it is for.'),
        ('Owners and stewards',
         'Each important dataset has an owner who is accountable for it. Stewards handle daily care, such as definitions and fixing errors.'),
        ('Catalogues',
         'A data catalogue lists what data exists, what each field means, and who to ask. People cannot use data well if they cannot find it or understand it.'),
        ('Access rules',
         'Access should follow the job. People get the data they need, and sensitive fields are restricted or masked.'),
        ('Standards and councils',
         'Shared definitions, such as what counts as an active customer, stop teams from reporting different answers. A governance council settles disputes between teams.'),
        ('Measuring it',
         'Governance can be measured by how much data is catalogued, how many issues are closed, and how often access requests are handled on time. Too many rules can slow people down, so balance matters.'),
    ],
    "test": [
        ('What does data governance decide?',
         [('a', 'What colour the office is'), ('b', 'Who owns data and who may use it'), ('c', 'How many desks to buy'), ('d', 'Which tea to serve')], 'b'),
        ("What is a steward's job?",
         [('a', 'Daily care of data, such as definitions and fixes'), ('b', 'Designing the building'), ('c', 'Selling the data'), ('d', 'Cooking lunch')], 'a'),
        ('What does a data catalogue do?',
         [('a', 'Plays music'), ('b', 'Prints invoices'), ('c', 'Lists data and explains what it means'), ('d', 'Heats the office')], 'c'),
        ('Why have shared definitions?',
         [('a', 'So nobody reads reports'), ('b', 'So data is deleted'), ('c', 'So the building is quieter'), ('d', 'So teams do not report different answers for the same thing')], 'd'),
        ('What can too many governance rules do?',
         [('a', 'Slow people down'), ('b', 'Make data fly'), ('c', 'Remove all risk'), ('d', 'Make the server bigger')], 'a'),
    ],
}
