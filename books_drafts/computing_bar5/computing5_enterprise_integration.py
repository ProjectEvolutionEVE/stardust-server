"""Enterprise Integration Patterns: the recurring ways systems pass messages to each other, and when heavy middleware is not needed."""
CODE = 'computing5_enterprise_integration'
BOOK = {
    "title": 'Enterprise Integration Patterns',
    "subtitle": 'Routing messages between systems, and knowing when to keep it simple',
    "chapters": [
        ('Why integration is hard',
         'Organisations run many systems that must share data, and each uses its own formats and timing. Integration connects them with messages. The patterns describe proven ways to do this without tangling everything together.'),
        ('Message routers',
         'A message router decides where each message should go next. Routers let one producer feed several consumers without knowing the details of each. They keep the connections between systems simpler.'),
        ('Content-based routing',
         'Content-based routing looks inside a message and chooses its route from what it contains. An order for a foreign customer might go to a different team than a domestic one. The routing rule should be easy to read and test.'),
        ('Canonical data models',
         'A canonical data model is one shared format that every system translates to and from. It reduces the number of translations, but it can become a large, slow compromise. Teams weigh its cost against the savings.'),
        ('The enterprise service bus',
         'The enterprise service bus was a popular central layer for routing and transforming messages. Many organisations found that it became a bottleneck and a complicated dependency. Its history is a warning about putting too much logic in one place.'),
        ('When to avoid heavy middleware',
         'For a small number of systems, a direct call or a simple queue is often enough. Heavy middleware adds cost, skills needs and a single point of failure. Simpler designs are preferred until the need for more is clear.'),
    ],
    "test": [
        ('What does a message router decide?',
         [('a', 'What colour the server is'), ('b', 'Who gets a birthday card'), ('c', 'How many chairs are in the room'), ('d', 'Where each message should go next')], 'd'),
        ('What does content-based routing use to choose a route?',
         [('a', 'The day of the week only'), ('b', 'What the message itself contains'), ('c', 'The brand of the laptop'), ('d', 'The number of coffee cups')], 'b'),
        ('What is a canonical data model?',
         [('a', 'A model of a car engine'), ('b', 'A paper sewing pattern'), ('c', 'One shared format that systems translate to and from'), ('d', 'A fashion show')], 'c'),
        ('What did many organisations find about the enterprise service bus?',
         [('a', 'It could become a bottleneck and a complicated dependency'), ('b', 'It always made everything free'), ('c', 'It removed all messages'), ('d', 'It only worked on paper')], 'a'),
        ('When might heavy middleware be unnecessary?',
         [('a', 'Whenever there are more than a thousand systems'), ('b', 'For a small number of systems, where a direct call or simple queue is enough'), ('c', 'Only in the kitchen'), ('d', 'Never, under any circumstances')], 'b'),
    ],
}
