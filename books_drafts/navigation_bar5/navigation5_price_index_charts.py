"""Price Indexes for Chart Products: index design, weights, updates, inflation, comparisons and use."""
CODE = 'navigation5_price_index_charts'
BOOK = {
    "title": 'Price Indexes for Chart Products',
    "subtitle": 'Measuring how the price of maps and charts changes over time',
    "chapters": [
        ('Why an index helps',
         'A price index turns many prices into one number that moves over time. It answers a simple question: are the charts we sell costing more or less than they did before? One index hides many small changes, so it must be read with care.'),
        ('Designing the index',
         'First choose which products belong in the basket. Then choose a base period, the year that is set to 100. Every later value is compared with that base, so the index shows change, not the price itself.'),
        ('Weights',
         'Products are not all equally important. A product that sells in large amounts should count for more than a rare one. Weights tell the index how much each price matters, and they are usually based on sales.'),
        ('Updates',
         'Products change. New charts appear and old ones are retired. The basket must be updated from time to time, so that it still reflects what customers buy. Note every change so that the series stays honest.'),
        ('Inflation and real prices',
         'Inflation is a general rise in prices across the economy. A price index helps separate a real change in chart prices from the general rise. Comparing a price with the index shows whether it has gained or lost value in real terms.'),
        ('Comparisons and use',
         'Indexes let a mapping agency compare prices across years, between regions and with other products. Use them to plan budgets and to test whether a price change is fair. Always state the base year and the basket so others can check your work.'),
    ],
    "test": [
        ('What does a price index do?',
         [('a', 'It sets the price of each chart'), ('b', 'It counts the number of charts printed'), ('c', 'It turns many prices into one number that tracks change over time'), ('d', 'It lists the cost of paper')], 'c'),
        ('What are weights in a price index?',
         [('a', 'How much each product counts, often based on its sales'), ('b', 'The mass of each printed map'), ('c', 'The fee paid to the printer'), ('d', 'The number of pages in each chart')], 'a'),
        ('Why must the basket of products be updated?',
         [('a', 'Because prices never change'), ('b', 'Because the base year changes every day'), ('c', 'Because the index must always rise'), ('d', 'Because products appear and disappear, and the basket should reflect what is bought')], 'd'),
        ('What does a real price mean?',
         [('a', 'The price printed on the chart'), ('b', 'The price with general inflation taken into account'), ('c', 'The price set by the government'), ('d', 'The price of the first chart ever made')], 'b'),
        ('Why state the base year when using an index?',
         [('a', 'So others can see what the index is compared against'), ('b', 'Because the base year sets the price of paper'), ('c', 'Because the base year is the cheapest year'), ('d', 'It is not needed at all')], 'a'),
    ],
}
