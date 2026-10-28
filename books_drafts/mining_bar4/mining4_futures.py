"""Futures and Price Discovery: standard contracts traded on exchanges, and what their prices tell us."""
CODE = 'mining4_futures'
BOOK = {
    "title": 'Futures and Price Discovery',
    "subtitle": 'Standard contracts on an exchange, and what their prices reveal',
    "chapters": [
        ('Exchange futures',
         'A futures contract is a standard agreement to buy or sell a set amount of a commodity at a set price on a set future date. Standard size and terms let many buyers and sellers trade the same contract.'),
        ('Settlement',
         'Futures are settled each day as prices move, so gains and losses are paid in cash as they arise. At the end, a contract settles by delivery of the metal or by a cash payment.'),
        ('Basis',
         'Basis is the spot price minus the futures price. It shows the gap between buying metal now and agreeing a price for later. The basis changes as the delivery date gets closer.'),
        ('Contango and backwardation',
         'In contango, futures prices are higher than the spot price, usually because of storage and carrying costs. In backwardation, futures prices are lower than the spot price, often when supply is tight now.'),
        ('Reading a price curve',
         'A price curve lines up futures prices by delivery date. Its slope shows what traders expect and how tight the market is today. Analysts read the shape as well as the level.'),
        ('Prices as information',
         'Futures prices pool the views of many buyers and sellers. They are not a promise of the future, but they are a useful signal of where the market thinks prices are heading.'),
    ],
    "test": [
        ('What is a futures contract?',
         [('a', 'A promise to visit a friend'), ('b', 'A kind of furnace'), ('c', 'A standard agreement to buy or sell a set amount at a set price on a future date'), ('d', 'A map of the sea')], 'c'),
        ('How are futures gains and losses handled?',
         [('a', 'They are settled in cash as prices move each day'), ('b', 'They are kept secret for ever'), ('c', 'They are paid only in paint'), ('d', 'They are never paid')], 'a'),
        ('What is basis?',
         [('a', 'The floor of the mine'), ('b', 'The weight of one ingot'), ('c', 'The number of staff'), ('d', 'The spot price minus the futures price')], 'd'),
        ('What is contango?',
         [('a', 'A type of rock'), ('b', 'Futures priced above the spot price'), ('c', 'A kind of drill'), ('d', 'A tax on boats')], 'b'),
        ('What do futures prices offer?',
         [('a', 'A guarantee of the future'), ('b', 'A price for lunch'), ('c', 'A useful signal of where the market thinks prices are heading'), ('d', 'A list of colours')], 'c'),
    ],
}
