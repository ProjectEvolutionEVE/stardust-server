"""Exchange Rates: what a rate is, floating and fixed systems, purchasing power parity, trade effects, and currency risk for a firm."""
CODE = 'business4_fx'
BOOK = {
    "title": 'Exchange Rates',
    "subtitle": 'What a currency is worth against another, and why it moves',
    "chapters": [
        ('What a rate is',
         'An exchange rate is the price of one currency in terms of another. If one dollar buys 0.9 euros, that is the rate. Every trip abroad, every import and every foreign investment depends on it.'),
        ('Floating and fixed',
         'In a floating system, supply and demand in the currency markets set the rate, and it moves every day. In a fixed system, the government or central bank holds the rate near a set value, buying and selling its own currency to keep it there. Many countries use a mix of the two.'),
        ('Purchasing power parity',
         "Purchasing power parity is the idea that, over time, exchange rates should move so that the same basket of goods costs about the same in each country. The Economist's Big Mac index is a light-hearted way to check it. In practice, rates can stay far from parity for years."),
        ('Interest rates and currencies',
         'Money tends to flow toward places where it earns more after allowing for the exchange rate. Interest-rate parity is the idea that differences in interest rates should be offset by expected moves in the rate. Changes in interest rates are one of the main forces that move currencies day to day.'),
        ('Trade effects',
         'A stronger currency makes imports cheaper and exports dearer for foreign buyers. A weaker one does the opposite. A firm that sells abroad may win orders when its currency falls, and lose them when it rises, even though its product has not changed at all.'),
        ('Currency risk for a firm',
         'A firm that buys or sells in another currency carries risk. Prices agreed in advance can become costly if the rate moves. Firms often use forward contracts to fix a rate for a future date, or hold cash in more than one currency, so that a sudden swing does not sink the year.'),
    ],
    "test": [
        ('What is an exchange rate?',
         [('a', 'The price of one currency in terms of another'), ('b', 'The interest paid on a savings account'), ('c', 'A tax on imported goods'), ('d', 'The number of banks in a country')], 'a'),
        ('In a floating system, what mainly sets the exchange rate?',
         [('a', 'A fixed decree every year'), ('b', 'Supply and demand in the currency markets'), ('c', 'The price of gold alone'), ('d', 'The number of tourists')], 'b'),
        ('What is purchasing power parity?',
         [('a', 'A rule that every currency must stay fixed'), ('b', 'A bank deposit that cannot be withdrawn'), ('c', 'The idea that a basket of goods should cost about the same in each country over time'), ('d', "The share of a country's people who vote")], 'c'),
        ('When a currency gets stronger, what usually happens to exports for foreign buyers?',
         [('a', 'They become cheaper'), ('b', 'They are banned'), ('c', 'Their price is not affected at all'), ('d', 'They become dearer')], 'd'),
        ('What is a forward contract used for?',
         [('a', 'To fix a rate for a future date'), ('b', 'To store gold in a vault'), ('c', 'To pay wages in cash'), ('d', 'To set the national budget')], 'a'),
    ],
}
