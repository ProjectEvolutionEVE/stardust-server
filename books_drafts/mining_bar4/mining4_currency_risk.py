"""Currency Risk for Miners: what happens when costs and revenues are paid in different currencies."""
CODE = 'mining4_currency_risk'
BOOK = {
    "title": 'Currency Risk for Miners',
    "subtitle": 'Costs in one currency, revenue in another',
    "chapters": [
        ('Costs in one currency',
         'A mine often pays its wages, fuel and equipment in its local currency. Its costs are fixed in that money, and they are counted every month.'),
        ('Revenue in another',
         'Metal is usually sold in a widely traded currency, such as the US dollar. When revenue and costs are in different currencies, the exchange rate between them changes the profit.'),
        ('Natural hedges',
         'A natural hedge matches costs and revenue in the same currency, so the exchange rate moves both sides together. Where possible, a miner buys in the currency it sells in.'),
        ('Forward contracts',
         "A forward contract fixes an exchange rate for a future date. It removes the uncertainty for that amount, but it also gives up any gain if the rate moves in the miner's favour."),
        ('Exposure ratios',
         'An exposure ratio compares the share of costs and revenue in each currency. A large gap between the two shows how much the exchange rate can hurt or help.'),
        ('Budgeting in foreign money',
         'A budget set in foreign money needs a planning exchange rate. Good budgets test how profit changes if the rate moves, so surprises are smaller.'),
    ],
    "test": [
        ("Why can exchange rates change a mine's profit?",
         [('a', 'When the mine paints its gates'), ('b', 'When staff take lunch'), ('c', 'When costs and revenue are in different currencies'), ('d', 'When the sun rises')], 'c'),
        ('What is a natural hedge?',
         [('a', 'Matching costs and revenue in the same currency'), ('b', 'A hedge grown in a garden'), ('c', 'A fence made of wood'), ('d', 'A bank loan with no interest')], 'a'),
        ('What does a forward contract do for an exchange rate?',
         [('a', 'Makes the rate change every hour'), ('b', 'Ends all trade'), ('c', 'Gives free money'), ('d', 'Fixes a rate for a future date, removing uncertainty for that amount')], 'd'),
        ('What does an exposure ratio compare?',
         [('a', 'The height of two chimneys'), ('b', 'The share of costs and revenue in each currency'), ('c', 'The number of trucks and drivers'), ('d', 'The colour of two signs')], 'b'),
        ('Why use a planning exchange rate in a budget?',
         [('a', 'So the rate can be ignored'), ('b', 'So the budget is written in pencil'), ('c', 'So the budget has a fixed rate and profit can be tested if the rate moves'), ('d', 'So no one reads it')], 'c'),
    ],
}
