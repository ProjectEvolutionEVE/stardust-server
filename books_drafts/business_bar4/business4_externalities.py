"""Externalities and the Coase Theorem: costs outside the deal, pollution, taxes and permits, Coase's bargain, transaction costs, and cap and trade."""
CODE = 'business4_externalities'
BOOK = {
    "title": 'Externalities and the Coase Theorem',
    "subtitle": 'When a deal leaves others paying the cost, and how they can be made to pay',
    "chapters": [
        ('Costs outside the deal',
         'An externality is a cost or benefit that falls on people who are not part of a deal. A factory that sells its goods but pollutes the river next door has an externality. The buyer and seller never see that cost, so the market does not count it.'),
        ('Pollution',
         'Pollution is the classic case. When a firm does not pay for the damage its smoke or waste causes, it makes too much of the polluting good at too low a price. Clean air and clean water are shared, so no single person has a strong reason to protect them.'),
        ('Taxes and permits',
         'One fix is a tax on the harm, set at the level of the damage. Another is to issue a limited number of permits to pollute and let firms trade them. Both make the polluter face the cost, so each firm chooses how to cut its own emissions.'),
        ("Coase's bargain",
         'In 1960 Ronald Coase argued that when property rights are clear and bargaining is cheap, people affected by an externality can strike a deal to solve it, whoever starts with the legal right. The outcome then depends less on who is liable and more on the total value at stake.'),
        ('Transaction costs',
         'The Coase bargain works only when the costs of bargaining are low. If thousands of people are affected, or the damage is hard to measure, the talks themselves become too costly. That is when governments tend to step in with rules or taxes.'),
        ('Cap and trade',
         'Cap and trade sets a total limit on a pollutant and gives out or sells permits within it. Firms that cut cheaply can sell their spare permits to firms that find cutting costly. The limit is fixed, so the total falls, and the trading finds the lowest-cost way to reach it.'),
    ],
    "test": [
        ('What is an externality?',
         [('a', 'A loan from a foreign bank'), ('b', 'A product sold at a discount'), ('c', 'A cost or benefit that falls on people outside a deal'), ('d', 'A limit on working hours')], 'c'),
        ('In 1960, which economist argued that affected parties can often bargain their way to a solution?',
         [('a', 'Adam Smith'), ('b', 'John Maynard Keynes'), ('c', 'Karl Marx'), ('d', 'Ronald Coase')], 'd'),
        ("What is the main problem that Coase's bargain runs into?",
         [('a', 'Transaction costs of bargaining can be too high'), ('b', 'Bargaining is always free'), ('c', 'Property rights never exist'), ('d', 'Pollution cannot be measured by anyone')], 'a'),
        ('How does cap and trade work?',
         [('a', 'It bans all trade between countries'), ('b', 'It sets a total limit and lets firms trade permits within it'), ('c', 'It pays firms to pollute more'), ('d', 'It fixes the price of gold')], 'b'),
        ('What does a tax set at the level of the damage aim to do?',
         [('a', 'Raise the price of bread'), ('b', 'Shrink the national debt at once'), ('c', 'Make the polluter face the cost of the harm it causes'), ('d', 'Stop all sales of goods')], 'c'),
    ],
}
