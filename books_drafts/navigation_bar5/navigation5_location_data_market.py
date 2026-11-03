"""Markets in Location Data: data brokers, pricing, consent, quality, competition and regulation."""
CODE = 'navigation5_location_data_market'
BOOK = {
    "title": 'Markets in Location Data',
    "subtitle": 'How location data is bought and sold, and the rules that protect people',
    "chapters": [
        ('Data brokers',
         'Brokers collect, package and sell location data from many sources. Their role links buyers and sellers who would otherwise never meet. Brokers must be open about where their data comes from.'),
        ('Pricing',
         'Prices depend on the quality, the amount and the freshness of the data. Pricing should reflect what buyers can actually use, not only what the data cost to gather.'),
        ('Consent',
         'People must know, and agree, when their location is collected and sold. Consent should be clear, specific and easy to withdraw. Hidden terms do not count as real consent.'),
        ('Quality',
         'Poor data misleads buyers and can cause real harm. Quality checks, a record of sources and accuracy tests help a buyer decide what to trust.'),
        ('Competition',
         'A market with few sellers can keep prices high and terms weak. Open competition and clear rules help buyers get fair prices and better service.'),
        ('Regulation',
         'Laws set limits on how location data may be collected, sold and used. Good regulation protects people while still letting useful data flow to those who need it.'),
    ],
    "test": [
        ('What do data brokers do?',
         [('a', 'Collect, package and sell location data'), ('b', 'Build ships'), ('c', 'Print paper maps'), ('d', 'Grow food')], 'a'),
        ('What affects the price of location data?',
         [('a', 'The colour of the file'), ('b', 'The name of the seller'), ('c', 'The quality, amount and freshness of the data'), ('d', 'The day of the week')], 'c'),
        ('What must consent be?',
         [('a', 'Hidden in long text'), ('b', 'Assumed without asking'), ('c', 'Given once and never checked'), ('d', 'Clear, specific and easy to withdraw')], 'd'),
        ('Why do quality checks matter for location data?',
         [('a', 'They do not matter'), ('b', 'Poor data misleads buyers'), ('c', 'They make the data slower'), ('d', 'They remove the need for sources')], 'b'),
        ('What helps buyers in a market with few sellers?',
         [('a', 'Higher prices with no rules'), ('b', 'Hidden terms'), ('c', 'Open competition and clear rules'), ('d', 'Only one seller')], 'c'),
    ],
}
