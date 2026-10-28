"""API Governance: shared standards, review and linting that keep many APIs consistent, usable and safe to change."""
CODE = 'computing5_api_governance'
BOOK = {
    "title": 'API Governance',
    "subtitle": 'Shared standards that keep many APIs consistent',
    "chapters": [
        ('Why APIs need governance',
         'An organisation with many APIs quickly ends up with many styles. Developers then spend time learning each one, and mistakes multiply. Governance sets shared rules so every API feels familiar.'),
        ('API standards',
         'A standard covers naming, error formats, authentication, pagination and versioning. Writing these rules down gives teams a clear target. The standard should be short enough that people actually read it.'),
        ('Review boards',
         'A review board checks new and changed APIs against the standard before they are released. Its members should include experienced builders and users of the API. Feedback should explain the reasons, not just say no.'),
        ('Linting',
         "Linters check an API's description file automatically for rule breaks, such as a missing error code. Automated checks catch most simple problems quickly. Humans still judge the design choices that a tool cannot."),
        ('Deprecation policy',
         'Deprecation means announcing that a feature will be removed later. A good policy gives notice, a migration path and a clear end date. Users should never be surprised by a break.'),
        ('Developer portals and enforcement',
         'A developer portal gathers documentation, examples and standards in one place. Governance works best when the standard is easy to follow and the paved path is the easiest choice. Enforcement is strongest when the tools make the right thing automatic.'),
    ],
    "test": [
        ('Why does governance matter for many APIs?',
         [('a', 'Without shared rules, every API becomes a different style to learn'), ('b', 'APIs never need documentation'), ('c', 'Governance makes keyboards faster'), ('d', 'It removes the need for testing')], 'a'),
        ('What does an API standard usually cover?',
         [('a', 'The office seating plan'), ('b', 'The colour of the logo'), ('c', 'Naming, error formats, authentication, pagination and versioning'), ('d', 'The lunch menu')], 'c'),
        ('What does a linter do?',
         [('a', 'It spins the server fan'), ('b', 'It checks an API description automatically for rule breaks'), ('c', "It writes the company's accounts"), ('d', 'It paints the documentation')], 'b'),
        ('What should a deprecation policy give users?',
         [('a', 'A sudden removal with no warning'), ('b', 'A new password every day'), ('c', 'A list of other companies'), ('d', 'Notice, a migration path and a clear end date')], 'd'),
        ('What is a developer portal?',
         [('a', 'A place that gathers documentation, examples and standards'), ('b', 'A type of server cabinet'), ('c', 'A cinema ticket'), ('d', 'A new kind of keyboard')], 'a'),
    ],
}
