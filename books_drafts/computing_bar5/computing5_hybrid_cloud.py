"""Hybrid and Multi-Cloud Architecture: workloads across providers, portability, network links, identity, data gravity and governance."""
CODE = 'computing5_hybrid_cloud'
BOOK = {
    "title": 'Hybrid and Multi-Cloud Architecture',
    "subtitle": 'Running work across more than one place, and the price of doing so',
    "chapters": [
        ('Why spread the work',
         'Some organisations keep part of their systems in their own data centres and part with a cloud provider. Others use two or more cloud providers at once. The reasons include legal rules, cost, reliability and avoiding dependence on a single supplier.'),
        ('Portability',
         'Moving a workload between providers is harder than it looks. Each provider has its own services, networking and tools. Teams that use standard formats and containers keep more freedom, but never gain complete freedom.'),
        ('Network links',
         'The places must be connected, and that link is a common point of failure and delay. Teams plan how much traffic will cross between sites, what it costs, and what happens when the link goes down.'),
        ('Identity across places',
         'People and services need one trusted way to sign in everywhere. Identity federation lets a single directory or sign-in system vouch for users in several environments. Without it, access rules drift apart over time.'),
        ('Data gravity',
         'Large amounts of data are slow and costly to move, so work tends to gather around where the data sits. This is called data gravity. A design should place data first, then choose where the processing runs.'),
        ('Governance',
         'Each place has its own settings, costs and security risks. Governance means one set of rules, one way of tagging resources, and one view of spending across all of them. It is the part most often neglected.'),
    ],
    "test": [
        ('Why might an organisation spread its work across several places?',
         [('a', 'Only to make the logo look better'), ('b', 'Because legal rules, cost, reliability or supplier risk may call for it'), ('c', 'Because computers need to be moved every day'), ('d', 'So that no one needs to log in')], 'b'),
        ('Why is moving a workload between providers harder than it looks?',
         [('a', 'Every provider uses exactly the same services'), ('b', 'Moving data is always free and instant'), ('c', 'Each provider has its own services, networking and tools'), ('d', 'Providers forbid all movement')], 'c'),
        ('What is data gravity?',
         [('a', 'Heavy servers falling over'), ('b', 'Work tending to gather where large amounts of data already sit'), ('c', 'A rule that data must be printed'), ('d', 'The weight of a hard drive')], 'b'),
        ('What does identity federation allow?',
         [('a', 'Users to share one password with the whole world'), ('b', 'One trusted sign-in system to vouch for users in several environments'), ('c', 'Turning off all sign-in checks'), ('d', 'Removing user accounts after one day')], 'b'),
        ('What is the part of multi-place design most often neglected?',
         [('a', 'Governance, meaning one set of rules and one view of spending'), ('b', 'The colour of the logo'), ('c', 'Keeping a paper copy of every log'), ('d', 'Buying the largest machine available')], 'a'),
    ],
}
