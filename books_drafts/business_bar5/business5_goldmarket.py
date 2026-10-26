"""The Gold Market: bars and coins, the London fix, central bank holdings, jewellery demand, gold as a haven and the costs of holding it."""
CODE = 'business5_goldmarket'
BOOK = {
    "title": 'The Gold Market',
    "subtitle": 'Bars, coins, the fix and why people hold gold',
    "chapters": [
        ('Bars and coins',
         'Gold is traded as bars of standard weights and purity, and as coins. Bars are sold for their metal content, and coins often carry a premium over the metal price because of their design and rarity. Buyers should know which kind they are getting.'),
        ('The London fix',
         'For more than a century, the London market set a benchmark gold price, known as the fix, at set times each day. Today a benchmark is set electronically by auction twice a day in London. Many contracts and prices around the world are tied to it.'),
        ('Central banks',
         'Central banks hold gold in their reserves, partly as a store of value that does not depend on any one government. Their buying and selling can move the market over months and years. Gold is one of several reserve assets, alongside foreign currency.'),
        ('Jewellery demand',
         "Much of the world's gold goes into jewellery, especially in India and China. Demand there rises with incomes and with festivals and weddings. Jewellery buying often falls when prices are high, which affects the market."),
        ('Gold as a haven',
         'Many people buy gold when they fear inflation, a currency crisis or a market crash. Gold does not pay interest, so its appeal depends on confidence and on how much else pays. Its price can still swing a lot in the short run.'),
        ('Costs of holding',
         'Holding gold has costs. Storage, insurance and dealers spreads all take money from the value, and selling bars can mean accepting a lower price than the headline one. Gold can be a useful part of savings for some people, but it is not free to keep. Compare the costs before you buy.'),
    ],
    "test": [
        ('What does a central bank do with gold?',
         [('a', 'Eats it'), ('b', 'Sells it only to jewellers'), ('c', 'Holds it in reserves as a store of value'), ('d', 'Keeps it in a lake')], 'c'),
        ('What was the London fix?',
         [('a', 'A repair shop for watches'), ('b', 'A tax on jewellery'), ('c', 'A tool for mining'), ('d', 'A benchmark gold price set at set times each day')], 'd'),
        ('Which two regions are known for large jewellery demand?',
         [('a', 'India and China'), ('b', 'Iceland and Canada'), ('c', 'Chile and Peru'), ('d', 'Mexico and Egypt')], 'a'),
        ('Why do some people buy gold?',
         [('a', 'To earn interest every week'), ('b', 'As a haven when they fear inflation or a crash'), ('c', 'Because it is a fish'), ('d', 'Because it must be bought by law')], 'b'),
        ('What is one cost of holding gold?',
         [('a', 'A monthly fee paid to the Sun'), ('b', 'Having to feed it'), ('c', 'Storage, insurance and dealer spreads'), ('d', 'A ban on owning it')], 'c'),
    ],
}
