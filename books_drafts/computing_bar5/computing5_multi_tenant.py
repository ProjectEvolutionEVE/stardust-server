"""Multi-Tenant SaaS Architecture: sharing one system among many customers while keeping their data, performance and billing separate."""
CODE = 'computing5_multi_tenant'
BOOK = {
    "title": 'Multi-Tenant SaaS Architecture',
    "subtitle": 'Many customers on one system, each kept separate',
    "chapters": [
        ('What multi-tenancy is',
         "A multi-tenant system serves many customers, called tenants, from shared infrastructure. Sharing lowers costs and simplifies updates. The challenge is keeping each tenant's data and experience separate."),
        ('Shared versus isolated tenants',
         "Tenants may share everything, or each may get its own database or environment. Shared designs are cheaper, while isolated ones give stronger separation. Many systems mix the two, depending on the customer's needs."),
        ('Noisy neighbours',
         'A noisy neighbour is a tenant whose heavy use slows down everyone else. Limits per tenant, fair queuing and monitoring help contain the effect. Good design stops one customer from spoiling the service for the rest.'),
        ('Tenant data models',
         "Each record is usually tagged with its tenant, and every query must filter by that tag. A single missing filter can expose one customer's data to another. Automated checks and strict access rules guard against this."),
        ('Per-tenant upgrades and billing hooks',
         'Some customers need to stay on an older version for a while, which complicates shared upgrades. Billing hooks measure usage per tenant so that charges match consumption. Both need clear rules and careful testing.'),
        ('Security',
         "Isolation must hold against attacks as well as mistakes. Teams use strong authentication, encryption and regular security reviews. Tests should try to read one tenant's data as another."),
    ],
    "test": [
        ('What is a tenant in a multi-tenant system?',
         [('a', 'A building for rent'), ('b', 'A type of server cable'), ('c', 'A paper form'), ('d', 'A customer served from shared infrastructure')], 'd'),
        ('What is a noisy neighbour?',
         [('a', 'A neighbour who plays music'), ('b', 'A tenant whose heavy use slows everyone else'), ('c', 'A person who lives next door'), ('d', 'A sound effect in a game')], 'b'),
        ('Why must each query filter by tenant?',
         [('a', 'So queries run in colour'), ('b', 'So the database never needs backups'), ('c', "So one customer cannot see another customer's data"), ('d', 'So the screen stays on')], 'c'),
        ('What do billing hooks do?',
         [('a', "They measure each tenant's usage so charges match consumption"), ('b', 'They hang pictures on the wall'), ('c', 'They fix broken keyboards'), ('d', 'They stop all payments')], 'a'),
        ('What is the trade-off of shared tenant designs?',
         [('a', 'They cost more and are always slower'), ('b', 'They are cheaper but offer weaker separation than isolated ones'), ('c', 'They cannot share any code'), ('d', 'They can only serve one customer')], 'b'),
    ],
}
