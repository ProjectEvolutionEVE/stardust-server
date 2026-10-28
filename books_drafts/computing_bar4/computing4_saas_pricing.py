"""SaaS Pricing Models: the main ways a software service charges customers, and how to choose among them."""
CODE = 'computing4_saas_pricing'
BOOK = {
    "title": 'SaaS Pricing Models',
    "subtitle": 'The main ways a software service charges, and how to choose among them',
    "chapters": [
        ('Per-seat pricing',
         'Per-seat pricing charges for each user who has an account. It is simple to understand and grows with the customer. Its weakness is that customers may share logins or cut the number of seats to save money.'),
        ('Tiers',
         'Tiers are packages, such as basic, standard and advanced, each with a set list of features and limits. Tiers help customers choose and make upgrades feel natural. Too many tiers confuse people, so most products keep the list short.'),
        ('Usage-based pricing',
         'Usage-based pricing charges for what the customer uses, such as storage, messages or processing time. It matches cost to value well. Customers may find the bill hard to predict, so clear limits and alerts help.'),
        ('Freemium',
         'Freemium offers a free version with limits, and charges for the extra features or capacity. It spreads the product widely at low cost. The free users must be a path to paying ones, not only a cost to the business.'),
        ('Price anchoring',
         'Price anchoring is the effect of an early number on later judgement. A high top tier can make the middle tier look like good value. Use anchors honestly, and make sure the prices reflect real costs and value.'),
        ('Choosing a model',
         'Choose a model that matches how customers get value and how your costs rise. Test changes with a small group before a full change. Be open about price changes, and give existing customers a clear notice.'),
    ],
    "test": [
        ('What does per-seat pricing charge for?',
         [('a', 'The number of windows in the office'), ('b', 'The number of birthdays'), ('c', 'The length of the lunch break'), ('d', 'Each user who has an account')], 'd'),
        ('What is freemium?',
         [('a', 'A paid service with no free version at all'), ('b', 'A free version with limits, and paid extras'), ('c', 'A gift card'), ('d', 'A tax on software')], 'b'),
        ('What is the risk of usage-based pricing?',
         [('a', 'It is always cheaper for the business'), ('b', 'It cannot be measured'), ('c', 'Customers may find the bill hard to predict'), ('d', 'It requires paper bills')], 'c'),
        ('What is price anchoring?',
         [('a', 'An early number that influences later judgement of value'), ('b', 'Tying a boat to a pier'), ('c', 'A rule that prices never change'), ('d', 'A type of discount code')], 'a'),
        ('What should a pricing model match?',
         [('a', 'The colour of the logo'), ('b', 'How customers get value and how your costs rise'), ('c', 'The name of the competitor'), ('d', 'The number of employees on holiday')], 'b'),
    ],
}
