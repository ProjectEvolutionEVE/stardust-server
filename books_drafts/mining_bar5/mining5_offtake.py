"""Offtake Agreements and Price Terms: how buyers commit to future output and how prices are set in contracts."""
CODE = 'mining5_offtake'
BOOK = {
    "title": 'Offtake Agreements and Price Terms',
    "subtitle": 'How buyers commit to future output and how prices are set',
    "chapters": [
        ('Offtake contracts', "An offtake agreement is a contract in which a buyer agrees to take a set share of a mine's future output. It gives the mine a secure market and helps it raise money. The buyer gets a steady supply."),
        ('Price floors and caps', 'A price floor sets the lowest price the seller will receive, and a cap sets the highest price the buyer will pay. Floors protect the seller in a slump, and caps protect the buyer in a boom. Both are often built into the contract together.'),
        ('Provisional pricing', 'Provisional pricing means the seller is paid a first estimate of the price on delivery, with a final adjustment later. The final price is set by a market average over a stated period. This is common for metals.'),
        ('Credit risk', "Credit risk is the chance the buyer cannot pay. A seller checks the buyer's finances and may ask for a letter of credit or a deposit. Good credit checks protect the mine's cash flow."),
        ('Delivery terms', 'Delivery terms say where the risk and cost pass from seller to buyer. Standard trade terms, such as the Incoterms published by the International Chamber of Commerce, are widely used. Clear terms prevent disputes.'),
        ('Contract design', 'A good offtake contract balances price, volume, quality, timing and risk. Each clause should be easy to understand and easy to check. The best contracts are fair enough to last through a full price cycle.'),
    ],
    "test": [
        ('What is an offtake agreement?', [('a', 'A contract where a buyer agrees to take a share of future output'), ('b', 'A plan to leave a mine empty'), ('c', 'A fee for a lunch break'), ('d', 'A prize for the first worker')], 'a'),
        ('What does a price floor do?', [('a', 'Sets the highest price for paint'), ('b', 'Stops a mine from digging'), ('c', 'Sets the lowest price the seller will receive'), ('d', 'Makes the buyer pay twice')], 'c'),
        ('What is provisional pricing?', [('a', 'Paying nothing at all'), ('b', 'Setting the price after the mine closes'), ('c', 'Paying in gold coins only'), ('d', 'Paying an estimated price first, then adjusting to the final price later')], 'd'),
        ('What is credit risk?', [('a', 'The chance a bank changes its colour'), ('b', 'The chance the buyer cannot pay'), ('c', 'The chance a truck has a flat tyre'), ('d', 'The chance the sun rises late')], 'b'),
        ('What do delivery terms say?', [('a', 'Who owns the ore before it is dug'), ('b', 'How many pictures go in a report'), ('c', 'Where the cost and risk pass from seller to buyer'), ('d', 'What time lunch is served')], 'c'),
    ],
}
