"""Pricing Autonomous Navigation Services: per-mile pricing, subscriptions, costs of operation, liability, demand and fairness."""
CODE = 'navigation5_autonomy_pricing'
BOOK = {
    "title": 'Pricing Autonomous Navigation Services',
    "subtitle": 'How to charge for self-guiding vehicles in a way that is clear and fair',
    "chapters": [
        ('Per-mile pricing',
         'Per-mile pricing charges for each mile travelled. It matches the price to the use, so people who travel more pay more. It is simple to explain, but users may find the total hard to predict.'),
        ('Subscriptions',
         'A subscription is a regular payment for continued access. It gives users a steady price and gives the provider steady income. Subscriptions suit people who use a service often.'),
        ('Costs of operation',
         'A service must cover its costs. These include the vehicles, maintenance, power, insurance, mapping and software updates. A price that does not cover these costs cannot last.'),
        ('Liability',
         'Liability is legal responsibility for harm caused. Providers must decide who pays when something goes wrong, and that choice shapes the price. Clear terms protect both users and providers.'),
        ('Demand',
         'Demand changes with the time of day, the weather, and the season. Prices that reflect demand can spread use more evenly. Users need to understand how prices change.'),
        ('Fairness',
         'Fair pricing means clear prices, and no users unfairly shut out of a service they need. Discounts for those who need them can help. Fairness builds trust, and trust keeps customers.'),
    ],
    "test": [
        ('What is per-mile pricing?',
         [('a', 'A price paid once a year'), ('b', 'A price set by the colour of the vehicle'), ('c', 'A price charged for each mile travelled'), ('d', 'A free service for everyone')], 'c'),
        ('What is a subscription?',
         [('a', 'A single payment for one trip'), ('b', 'A regular payment for continued access'), ('c', 'A type of ship'), ('d', 'A fine for late payment')], 'b'),
        ('What costs must a self-guiding service cover?',
         [('a', 'None at all'), ('b', 'Only the paint'), ('c', 'Only the staff'), ('d', 'Operation, maintenance, insurance and updates')], 'd'),
        ('What is liability?',
         [('a', 'Legal responsibility for harm caused'), ('b', 'A type of signal'), ('c', 'A map colour'), ('d', 'A fuel tank')], 'a'),
        ('What does fairness require in pricing?',
         [('a', 'Charging some users far more for no reason'), ('b', 'Hiding the prices'), ('c', 'Clear prices that do not unfairly exclude people who need the service'), ('d', 'Charging nothing ever')], 'c'),
    ],
}
