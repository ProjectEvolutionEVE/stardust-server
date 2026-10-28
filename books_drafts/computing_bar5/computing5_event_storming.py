"""Event Storming: a workshop in which a team maps a business through the events that happen in it, then turns the map into software."""
CODE = 'computing5_event_storming'
BOOK = {
    "title": 'Event Storming',
    "subtitle": 'Mapping a business through its events, on a wall of sticky notes',
    "chapters": [
        ('What the workshop is',
         'Event Storming is a collaborative workshop, popularised by Alberto Brandolini. People put domain events on a long wall using sticky notes. Events are written in the past tense, such as order placed or payment failed.'),
        ('Domain events on sticky notes',
         'Each orange note is a domain event, something that happened and matters to the business. Notes are arranged roughly in time order from left to right. Seeing the sequence makes gaps and repeats obvious.'),
        ('Hot spots',
         'Hot spots are questions, disagreements or risks that people mark with a pink or red note. They show where the team needs to learn more. Naming them early prevents surprises later.'),
        ('Aggregates',
         'Aggregates are the groups of data and rules that handle a set of related events together. Identifying them shows the natural boundaries inside the system. Each aggregate tends to become one piece of the software.'),
        ('Process modelling',
         'The team adds commands, actors and policies around the events. A command is a request, an actor is the person or system that makes it, and a policy is a rule that reacts to an event. The result is a picture of how the business really runs.'),
        ('Turning output into code',
         'The workshop output guides the design of services, modules and their messages. Event names often become the names in the code. The map is revisited as the system and the business change.'),
    ],
    "test": [
        ('Who popularised Event Storming?',
         [('a', 'Ada Lovelace'), ('b', 'Claude Shannon'), ('c', 'Linus Torvalds'), ('d', 'Alberto Brandolini')], 'd'),
        ('How are domain events usually written on the notes?',
         [('a', 'In capital letters only, with no verbs'), ('b', 'In the past tense, such as order placed'), ('c', 'As numbers only'), ('d', 'As drawings of animals')], 'b'),
        ('What are hot spots in Event Storming?',
         [('a', 'The warmest seats in the room'), ('b', 'Printers that overheat'), ('c', 'Questions, disagreements or risks the team needs to learn more about'), ('d', 'Special offers for customers')], 'c'),
        ('What is an aggregate?',
         [('a', 'A group of data and rules that handle related events together'), ('b', 'A type of rock used in roads'), ('c', 'A total of the office budget'), ('d', 'A tool for cutting paper')], 'a'),
        ('What is a policy in process modelling?',
         [('a', 'A paper insurance form'), ('b', 'A rule that reacts to an event'), ('c', 'A seating plan'), ('d', 'A recipe for lunch')], 'b'),
    ],
}
