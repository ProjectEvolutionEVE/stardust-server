"""Low-Code Platforms: visual builders for software, their extension points, and the governance they need once they grow."""
CODE = 'computing5_low_code'
BOOK = {
    "title": 'Low-Code Platforms',
    "subtitle": 'Visual building for software, with room to grow',
    "chapters": [
        ('What low-code means',
         'Low-code platforms let people build applications with visual editors and ready-made parts, writing little or no traditional code. They speed up simple and medium-sized applications. They suit many internal tools and workflows.'),
        ('Visual builders',
         "A visual builder lets users drag screens, forms and rules into place. The platform handles much of the plumbing, such as storage and login. The result is quicker to make but is shaped by the platform's choices."),
        ('Extension points',
         'Extension points allow custom code where the built-in parts are not enough. Good platforms document these points clearly. Using them well keeps the application maintainable.'),
        ('Governance',
         'Governance sets who may build, what is approved for live use and how changes are tracked. Without it, many small apps appear with no owner. Clear rules keep the estate safe as it grows.'),
        ('Lock-in',
         'Applications built in a platform often depend on its format and services. Moving away later can be expensive and slow. Teams weigh this against the speed gained at the start.'),
        ('Scaling, performance and citizen developers',
         "Apps that succeed can outgrow their platform's limits for speed or volume. Citizen developers, who are not professional engineers, need support, training and review. Scaling well means planning for both growth and skill."),
    ],
    "test": [
        ('What do low-code platforms let people do?',
         [('a', 'Build only paper forms'), ('b', 'Replace electricity'), ('c', 'Write poems without a computer'), ('d', 'Build applications with visual editors and ready-made parts')], 'd'),
        ('What are extension points?',
         [('a', 'Points on a sports pitch'), ('b', 'Places where custom code can be added when built-in parts are not enough'), ('c', 'Tips for a school exam'), ('d', 'Electric plugs')], 'b'),
        ('What is lock-in?',
         [('a', 'A type of door lock'), ('b', 'A record of lost keys'), ('c', "Depending on a platform's format and services, so moving away is hard"), ('d', 'A password for a computer')], 'c'),
        ('What does governance set for low-code apps?',
         [('a', 'Who may build, what is approved for live use and how changes are tracked'), ('b', 'The colour of the buttons'), ('c', 'The weather forecast'), ('d', "The name of each user's pet")], 'a'),
        ('What do citizen developers usually need?',
         [('a', 'No rules at all'), ('b', 'Support, training and review'), ('c', 'A promise that nothing will ever break'), ('d', 'A permanent office on a ship')], 'b'),
    ],
}
