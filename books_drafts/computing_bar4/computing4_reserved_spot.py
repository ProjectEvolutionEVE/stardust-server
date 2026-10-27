"""Reserved and Spot Capacity: choosing between paying on demand and committing ahead for lower prices."""
CODE = 'computing4_reserved_spot'
BOOK = {
    "title": 'Reserved and Spot Capacity',
    "subtitle": 'Choosing between paying on demand and committing ahead for lower prices',
    "chapters": [
        ('On-demand versus committed use',
         'On-demand capacity is paid for by the hour or second, with no promise. Committed capacity is a promise to use a set amount for one or three years, in return for a lower price. The choice depends on how steady your demand is.'),
        ('Spot interruptions',
         'Spot capacity is spare cloud capacity sold at a steep discount. The provider can reclaim it with little warning. Spot suits work that can stop and restart safely, such as batch jobs that save their progress.'),
        ('Savings plans',
         'A savings plan commits to a certain spend per hour, and the discount applies across matching usage. It gives flexibility in which machine types you use. Read the terms, because unused commitment is still paid for.'),
        ('Coverage targets',
         'Coverage is the share of your usage that a commitment covers. A common approach is to commit to the steady base load and leave the peaks on demand or spot. Setting a target for coverage keeps the decision honest and easy to review.'),
        ('Utilisation risk',
         'Utilisation is how much of a commitment you actually use. A reservation you do not use is wasted money. Watch utilisation monthly, and adjust before a commitment becomes a burden.'),
        ('Buying decisions',
         'Before buying, forecast the steady demand over the commitment period. Consider how likely the product is to change or close. Start with modest commitments, then increase them as the forecast proves right.'),
    ],
    "test": [
        ('What is on-demand capacity?',
         [('a', 'Capacity given away for free'), ('b', 'Capacity paid for by use, with no long promise'), ('c', 'Capacity that is always locked for three years'), ('d', 'Capacity kept on paper')], 'b'),
        ('What is the catch of spot capacity?',
         [('a', 'It is always slower'), ('b', 'It comes with no computer'), ('c', 'It is only sold to governments'), ('d', 'The provider can reclaim it with little warning')], 'd'),
        ('What does coverage measure?',
         [('a', 'The share of usage that a commitment covers'), ('b', 'The size of the data centre floor'), ('c', 'The number of staff trained'), ('d', 'The colour of the invoice')], 'a'),
        ('What is utilisation risk?',
         [('a', 'The chance of a fire in the office'), ('b', 'The risk of a password leak'), ('c', 'Paying for a commitment that you do not fully use'), ('d', 'The risk of too many meetings')], 'c'),
        ('What is a sensible way to start a commitment?',
         [('a', 'Commit to everything on day one'), ('b', 'Never commit to anything'), ('c', 'Choose the largest machine available'), ('d', 'Start with modest commitments and grow them as the forecast proves right')], 'd'),
    ],
}
