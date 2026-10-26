"""The Chicago Board of Trade: grain in 1848, standard contracts, the trading pit, the grain elevators, clearing and the move to screens."""
CODE = 'business5_cbot'
BOOK = {
    "title": 'The Chicago Board of Trade',
    "subtitle": 'From grain sheds to the trading screen',
    "chapters": [
        ('Chicago in 1848',
         'Chicago was a growing town on the lake when a group of merchants founded the Chicago Board of Trade in 1848. Farmers brought grain by wagon and then by rail, and the city needed a fair place to buy and sell it. The Board became the place where that trade was organised.'),
        ('Standard contracts',
         'Early traders agreed to deliver grain at a future date, and the Board made these deals standard. Each contract set the quantity, the grade and the delivery month. Because every contract looked the same, people could buy and sell them easily without inspecting each sack.'),
        ('The pit',
         'Traders shouted and signalled to each other on the floor of the exchange, in a sunken area called the pit. Hand signs and calls carried bids and offers in a noisy crowd. The pit became a symbol of open outcry trading for more than a century.'),
        ('The grain elevators',
         'Huge grain elevators stored the crop along the rail lines and the lake. Warehouse receipts from these elevators could be traded, which tied the physical grain to the paper contracts. A trader could buy grain for later delivery without ever touching it.'),
        ('Clearing',
         'A clearing house stands between buyers and sellers, so each trade is guaranteed by the house rather than by a single stranger. Members post money as a safety margin each day. This system lets large positions change hands with much less risk of default.'),
        ('The move to screens',
         'Over the late twentieth century, most trading moved from the pit to electronic screens. The Board merged with the Chicago Mercantile Exchange in 2007, and the combined group now trades almost everything on computers. The pit still stands as a memory of how grain was once priced.'),
    ],
    "test": [
        ('In what year was the Chicago Board of Trade founded?',
         [('a', '1776'), ('b', '1929'), ('c', '1999'), ('d', '1848')], 'd'),
        ('What made the contracts easy to trade?',
         [('a', 'They were standard, with the same quantity, grade and delivery month'), ('b', 'They were written in code'), ('c', 'They had no dates'), ('d', 'They were only for gold')], 'a'),
        ('What was the pit?',
         [('a', 'A place to store grain under the lake'), ('b', 'A sunken floor where traders shouted and signalled bids and offers'), ('c', 'A ship that carried grain'), ('d', 'An office in Paris')], 'b'),
        ('What did warehouse receipts from the elevators do?',
         [('a', 'Prove a trader was born in Chicago'), ('b', 'Pay wages'), ('c', 'Tie physical grain to the paper contracts'), ('d', 'Stop the rail lines')], 'c'),
        ('What does a clearing house do?',
         [('a', 'Keeps the grain fresh'), ('b', 'Trains new farmers'), ('c', 'Sells the pit as scrap'), ('d', 'Guarantees each trade so buyers and sellers do not rely on each other alone')], 'd'),
    ],
}
