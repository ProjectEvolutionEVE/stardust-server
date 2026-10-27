"""Cyber Insurance and Risk Transfer: what cyber policies cover, what they leave out, and why prevention still matters."""
CODE = 'computing4_cyber_insurance'
BOOK = {
    "title": 'Cyber Insurance and Risk Transfer',
    "subtitle": 'What cyber policies cover, what they leave out, and why prevention still matters',
    "chapters": [
        ('What policies cover',
         'Cyber insurance can pay some costs of a security incident, such as investigation, legal advice, notifying customers and some business losses. Each policy lists the covered events in its own words. Read the list before you rely on it.'),
        ('Limits and deductibles',
         'A limit is the most the insurer will pay in total, or for one event. A deductible is the part you pay first. A large incident can easily exceed the limit, so the gap falls on the business.'),
        ('Underwriting questions',
         'Before issuing a policy, insurers ask questions about your security, such as whether you use multi-factor sign-in and how you back up data. Weak answers can raise the price or lead to refusal. Honest answers protect you if you later need a claim.'),
        ('Exclusions',
         'Exclusions are events the policy does not cover, such as some acts of war, or losses caused by failing to keep basic protections in place. Exclusions can make a policy far less useful than it appears. Check them early, not after an incident.'),
        ('Risk versus transfer',
         'Transferring risk means paying someone else to carry part of the loss. Reducing risk means changing your systems so the event is less likely or less severe. Insurance does not remove the risk, and it does not restore lost trust.'),
        ('The place of prevention',
         'The cheapest incident is the one that never happens. Prevention, such as patching, training and backups, lowers both the chance and the cost of an event. Insurance works best as a backstop behind good prevention.'),
    ],
    "test": [
        ('What does a policy limit mean?',
         [('a', 'The length of the office lunch'), ('b', 'The number of staff allowed in the building'), ('c', 'The most the insurer will pay'), ('d', 'The colour of the policy')], 'c'),
        ('What is a deductible?',
         [('a', 'The part of a loss you pay first'), ('b', 'A tax on the premium'), ('c', 'A gift from the insurer'), ('d', 'A type of server')], 'a'),
        ('What is an exclusion?',
         [('a', 'A member of staff who leaves'), ('b', 'A special discount'), ('c', 'A list of approved suppliers'), ('d', 'An event the policy does not cover')], 'd'),
        ('Why do insurers ask underwriting questions?',
         [('a', 'To choose the office decor'), ('b', 'To understand your security before setting the price and terms'), ('c', 'To count the number of computers at home'), ('d', 'To sell you a holiday')], 'b'),
        ('What does insurance not do?',
         [('a', 'Pay some costs of an incident'), ('b', 'Cover investigation costs in many policies'), ('c', 'Remove the underlying risk'), ('d', 'Set out the claim process')], 'c'),
    ],
}
