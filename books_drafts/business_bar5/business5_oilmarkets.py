"""How Oil Is Priced: grades, Brent and WTI, spot and futures, refinery margins, OPEC decisions and the 2020 negative price."""
CODE = 'business5_oilmarkets'
BOOK = {
    "title": 'How Oil Is Priced',
    "subtitle": 'Grades, benchmarks, futures and the 2020 surprise',
    "chapters": [
        ('Not all oil is the same',
         'Crude oil comes in many grades. Light oil flows easily and gives more petrol; heavy oil is thicker and needs more work. Sulphur content matters too, because low-sulphur crude is cleaner to refine. The grade sets how much a barrel is worth.'),
        ('Benchmarks: Brent and WTI',
         'Two main benchmarks set many world prices. Brent comes from the North Sea, and West Texas Intermediate, WTI, is the main US benchmark. Most crude sold worldwide is priced by reference to one of them, with an adjustment for grade and location.'),
        ('Spot and futures',
         'The spot price is the price for oil delivered now. A futures contract agrees a price for delivery in a later month. Futures let producers and airlines plan ahead, and they also let traders bet on where prices will go.'),
        ('Refinery margins',
         'Crude is only raw material. A refinery makes money from the gap between what it pays for crude and what it earns from petrol, diesel and other products, called the crack spread. When that gap is wide, refiners buy more crude and the price is pulled up.'),
        ('OPEC decisions',
         'The Organization of the Petroleum Exporting Countries and its partners meet to decide how much oil their members pump. Cutting output tends to lift prices, and adding output tends to lower them. Their decisions move the market, but demand, weather and politics count too.'),
        ('The negative price of 2020',
         'In April 2020, demand collapsed in the pandemic, storage tanks filled up, and the May WTI futures contract settled below zero. Sellers were paying buyers to take the oil. The episode showed that a futures price is a promise about a delivery, and storage can run out.'),
    ],
    "test": [
        ('What does WTI stand for?',
         [('a', 'World Trade Index'), ('b', 'West Texas Intermediate'), ('c', 'Western Tanker Institute'), ('d', 'Wide Tank Interest')], 'b'),
        ('What is a futures contract?',
         [('a', 'A bar of gold'), ('b', 'A tax on petrol'), ('c', 'An agreement on a price for delivery in a later month'), ('d', 'A ship insurance policy')], 'c'),
        ('What is the crack spread?',
         [('a', 'A split in a pipeline'), ('b', 'The depth of the sea'), ('c', 'A type of crude grade'), ('d', 'The gap between refined product prices and the cost of crude')], 'd'),
        ('What do OPEC decisions on output usually do to prices?',
         [('a', 'Cutting output tends to lift prices'), ('b', 'Cutting output always cancels all demand'), ('c', 'They never affect prices'), ('d', 'They only change the colour of oil')], 'a'),
        ('What happened to the May 2020 WTI futures contract?',
         [('a', 'It rose to a million dollars'), ('b', 'It settled below zero because storage was full'), ('c', 'It was printed on paper'), ('d', 'It was made illegal in every country')], 'b'),
    ],
}
