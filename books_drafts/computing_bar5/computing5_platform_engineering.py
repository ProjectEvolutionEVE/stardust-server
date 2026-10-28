"""Platform Engineering: building an internal platform as a product, so product teams can deliver software without rebuilding the basics."""
CODE = 'computing5_platform_engineering'
BOOK = {
    "title": 'Platform Engineering',
    "subtitle": 'An internal platform, run as a product for product teams',
    "chapters": [
        ('What a platform is',
         'An internal developer platform gives product teams the tools, services and rules they need to build and run software. It takes the repeated work of setting up infrastructure off their plates. The platform team builds it for the teams that use it.'),
        ('Paved roads',
         'A paved road is a supported, well-trodden way of doing a common task, such as deploying a service. Teams may leave the road, but the road is the easiest choice. Making the right path the easy path is the central idea.'),
        ('Self-service',
         'Self-service lets a team create a database, a test environment or a pipeline without waiting for a ticket. Clear guardrails keep self-service safe. The platform team focuses on making good defaults rather than doing each task by hand.'),
        ('The platform as a product',
         'The platform has users, a roadmap and feedback, just like any product. Its team listens to the product teams and measures whether the platform helps. Treating it as a product keeps it useful and not merely imposed.'),
        ('Adoption metrics',
         'Useful measures include how many teams use the platform, how long common tasks take, and how often the platform causes incidents. Surveys and interviews show whether the platform feels helpful. Numbers and opinions are both needed.'),
        ('Team boundaries',
         'The platform team must agree clearly with product teams on who owns what. Unclear boundaries lead to duplicated work or to problems nobody owns. Written agreements and regular reviews keep the boundary healthy.'),
    ],
    "test": [
        ('What does an internal developer platform provide?',
         [('a', 'A new brand of office chairs'), ('b', 'Tools, services and rules that product teams use to build and run software'), ('c', 'A cinema for staff'), ('d', 'A library of paper books only')], 'b'),
        ('What is a paved road?',
         [('a', 'A road made of concrete for cars'), ('b', 'A path in a garden'), ('c', 'A map of the city'), ('d', 'A supported, well-trodden way of doing a common task')], 'd'),
        ('What does self-service let a team do?',
         [('a', 'Create resources without waiting for a ticket, within guardrails'), ('b', 'Skip every rule'), ('c', 'Ignore the platform forever'), ('d', 'Print the software')], 'a'),
        ('Why treat the platform as a product?',
         [('a', 'So it never changes'), ('b', 'So it can be sold to the public'), ('c', 'So it has users, feedback and a roadmap, and stays useful'), ('d', 'So no one needs to use it')], 'c'),
        ('What do adoption metrics help a platform team see?',
         [('a', 'The number of biscuits in the kitchen'), ('b', 'The colour of the screens'), ('c', 'How many people wear hats'), ('d', 'Whether teams use the platform and whether it actually helps')], 'd'),
    ],
}
