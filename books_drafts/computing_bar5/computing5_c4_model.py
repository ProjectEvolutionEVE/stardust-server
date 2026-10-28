"""The C4 Model for Architecture Diagrams: four levels of picture, from the wider context down to the code, each for a different audience."""
CODE = 'computing5_c4_model'
BOOK = {
    "title": 'The C4 Model for Architecture Diagrams',
    "subtitle": 'Four levels of picture, each for a different reader',
    "chapters": [
        ('Why diagrams fail',
         'Many architecture diagrams mix too many details in one picture, so nobody can read them. The C4 model, created by Simon Brown, gives a set of zoomable views. Each view answers a different question for a different reader.'),
        ('Context',
         'The context diagram shows the system as one box, with its users and the other systems it talks to. It suits anyone who needs the big picture, including non-technical staff. It should fit on a single page.'),
        ('Containers',
         'A container is something that runs or stores data, such as a web app, a mobile app or a database. The container diagram shows how these pieces communicate. Developers and operations staff use it most.'),
        ('Components and code',
         'Components are the groups of code inside one container, such as a service module. The component diagram shows their responsibilities and links. The code level is optional, and is usually better left to the code itself.'),
        ('Naming and keeping diagrams current',
         'Clear, consistent names matter more than fancy shapes. Each element should say what it is and what it does. Diagrams go stale quickly, so they should be updated with the code or generated from it.'),
        ('Review sessions and anti-patterns',
         'Diagrams work best when reviewed in a group with the right people in the room. Common anti-patterns include unlabelled arrows, one huge diagram for every purpose, and diagrams that never change. Keeping each level small avoids most of them.'),
    ],
    "test": [
        ('Who created the C4 model?',
         [('a', 'Alan Turing'), ('b', 'Simon Brown'), ('c', 'Grace Hopper'), ('d', 'Dennis Ritchie')], 'b'),
        ('What does the context diagram show?',
         [('a', 'Every line of code'), ('b', 'The colour palette of the office'), ('c', 'The staff rota'), ('d', 'The system as one box, with its users and nearby systems')], 'd'),
        ('What is a container in the C4 model?',
         [('a', 'Something that runs or stores data, such as a web app or database'), ('b', 'A box for shipping goods'), ('c', 'A folder for holiday photos'), ('d', 'A type of coffee cup')], 'a'),
        ('Which level is usually left to the code itself?',
         [('a', 'The context level'), ('b', 'The container level'), ('c', 'The code level'), ('d', 'The title page')], 'c'),
        ('Which is a common anti-pattern in architecture diagrams?',
         [('a', 'Clear and consistent names'), ('b', 'Diagrams kept near the code'), ('c', 'Small, focused levels'), ('d', 'Unlabelled arrows and one huge diagram for every purpose')], 'd'),
    ],
}
