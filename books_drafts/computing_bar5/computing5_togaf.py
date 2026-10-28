"""Enterprise Architecture Frameworks: the TOGAF approach to planning how a whole organisation's systems should work together."""
CODE = 'computing5_togaf'
BOOK = {
    "title": 'Enterprise Architecture Frameworks',
    "subtitle": "Planning a whole organisation's systems, with TOGAF as the main example",
    "chapters": [
        ('What enterprise architecture is',
         "Enterprise architecture plans how an organisation's business, information, applications and technology fit together. It looks across departments rather than inside one project. Its aim is to keep the whole estate coherent."),
        ('Architecture domains',
         'TOGAF describes four domains: business, data, application and technology architecture. Each domain has its own questions and its own models. Together they cover the whole enterprise.'),
        ('The architecture development method',
         'The Architecture Development Method, or ADM, is a repeating cycle of phases. It moves from setting the vision, through each domain, to the planning and migration of change. The cycle is revisited as the organisation learns.'),
        ('Capability maps and governance',
         'Capability maps show what the organisation can do, independent of how it is organised. Governance sets who approves architecture decisions and how compliance is checked. Both help leaders see where to invest.'),
        ('Criticism and value',
         'Critics say enterprise frameworks can become heavy, slow and paper-based, and can miss the needs of working teams. Supporters point to better shared language and fewer costly clashes. The value depends on how lightly and sensibly the framework is applied.'),
        ('Adoption',
         "Successful adoption starts with a clear purpose and a small first scope. Tailoring the framework to the organisation's size and culture matters more than following every step. Training and visible early wins build support."),
    ],
    "test": [
        ('Which framework is the main example in this book?',
         [('a', 'TOGAF'), ('b', 'COBOL'), ('c', 'Scrum'), ('d', 'Markdown')], 'a'),
        ('What does enterprise architecture plan?',
         [('a', 'The office menu'), ('b', 'The colours of the staff badges'), ('c', 'How business, information, applications and technology fit together'), ('d', 'The annual sports day')], 'c'),
        ('How many domains does TOGAF describe?',
         [('a', 'One'), ('b', 'Four'), ('c', 'Nine'), ('d', 'Twelve')], 'b'),
        ('What is the Architecture Development Method?',
         [('a', 'A method for cooking eggs'), ('b', 'A test for typing speed'), ('c', 'A paint technique'), ('d', 'A repeating cycle of phases from vision to migration')], 'd'),
        ('What is a common criticism of enterprise frameworks?',
         [('a', 'They can become heavy and miss the needs of working teams'), ('b', 'They make computers too fast'), ('c', 'They remove all risks'), ('d', 'They cannot be written down')], 'a'),
    ],
}
