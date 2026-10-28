"""Options as Price Insurance: paying a premium to keep the right to sell at a set price."""
CODE = 'mining5_options_insure'
BOOK = {
    "title": 'Options as Price Insurance',
    "subtitle": 'Paying a premium to protect against falling prices',
    "chapters": [
        ('Put options', 'A put option gives its holder the right, but not the duty, to sell at a set price by a set date. If the market price falls below that level, the option gains value. If the price stays high, the holder simply lets it expire.'),
        ('Premiums', 'The buyer of an option pays an upfront premium. The premium is the cost of the protection, and it is paid whether or not the option is used. Think of it like an insurance premium.'),
        ('Strike choice', 'The strike price is the level at which the option can be used. A high strike gives more protection but costs more. A low strike is cheaper but leaves more price risk. The choice is a trade-off between cost and cover.'),
        ('Costs', 'The total cost of protection includes the premium and any extra fees. Cost is weighed against the loss it could prevent. A seller should know exactly how much the protection costs each year.'),
        ('Accounting', "Options can be recorded at fair value, which means their value changes each period. Some companies use hedge accounting to match the option's effect with the sales it protects. The rules are technical, so accountants should be consulted."),
        ('Policy design', 'A company can set a policy that buys protection each year for a set share of expected output. Clear rules remove guesswork and stop emotional decisions in a price fall. The policy should be reviewed by the board.'),
    ],
    "test": [
        ('What right does a put option give its holder?', [('a', 'The right to buy a house'), ('b', 'The right to stop a train'), ('c', 'The right to name a river'), ('d', 'The right, not the duty, to sell at a set price by a set date')], 'd'),
        ('What is an option premium?', [('a', 'The price of a meal'), ('b', 'The upfront cost paid for the protection'), ('c', 'A reward for good weather'), ('d', 'A gift from the seller at the end')], 'b'),
        ('What happens to a higher strike price?', [('a', 'Less protection and no cost'), ('b', 'Protection that is always free'), ('c', 'More protection, but usually a higher cost'), ('d', 'No change at all')], 'c'),
        ('Why might a company set an annual protection policy?', [('a', 'Clear rules remove guesswork during a price fall'), ('b', 'To avoid reading any prices'), ('c', 'To make prices fall on purpose'), ('d', 'To stop all sales forever')], 'a'),
        ('What is an option that is not used called when it expires?', [('a', 'Paid back in full with interest'), ('b', 'Worthless, with the premium as the cost of protection'), ('c', 'Converted into a loan'), ('d', 'Turned into a share')], 'b'),
    ],
}
