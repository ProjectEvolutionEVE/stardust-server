"""Provisional Pricing and Quotational Periods: how metal prices are settled after delivery."""
CODE = 'mining5_provisional'
BOOK = {
    "title": 'Provisional Pricing and Quotational Periods',
    "subtitle": 'How metal prices are settled after delivery',
    "chapters": [
        ('Pricing on delivery', 'A seller often delivers metal before its final price is known. The invoice is issued at a provisional price, based on the market at delivery. The final amount is settled once the price is fixed.'),
        ('Mark-to-market', 'Mark-to-market means valuing a position at the current market price. Provisional invoices are adjusted to market as prices move. The adjustment can be paid or received after the fact.'),
        ('Price exposure', "Between delivery and final pricing, the seller is exposed to price moves. If the price rises, the seller gains; if it falls, the seller loses. Understanding this exposure is part of managing a mine's risk."),
        ('Settlement', 'Settlement is the final payment that closes the invoice. It uses the average price over the quotational period, which is a stated window of days or weeks. Both parties should agree the source of the price in writing.'),
        ('Disputes', 'Disputes arise when the buyer and seller disagree about the quality, weight or price used. Clear contract terms and independent assay reports help settle them. Early talks usually cost less than court.'),
        ('Hedging the exposure', 'A seller can hedge the price exposure by taking an offsetting position in the futures market. The hedge locks in part of the price. It removes the gain as well as the loss from price moves.'),
    ],
    "test": [
        ('What is a quotational period?', [('a', 'A stated window over which the final metal price is averaged'), ('b', 'A school lesson on quotes'), ('c', 'A short holiday for workers'), ('d', 'A type of machine part')], 'a'),
        ('What does mark-to-market mean?', [('a', 'Painting a market stall'), ('b', 'Setting a price by guessing'), ('c', 'Valuing a position at the current market price'), ('d', 'Ignoring the market completely')], 'c'),
        ('When is a seller exposed to price moves?', [('a', 'Only after the final payment'), ('b', 'Never, if the mine is large'), ('c', 'Only on public holidays'), ('d', 'Between delivery and the final price fixing')], 'd'),
        ('What is the purpose of an independent assay report in a dispute?', [('a', 'To choose the colour of the ore'), ('b', 'To help confirm quality and content'), ('c', 'To hire new staff'), ('d', 'To cancel the contract by default')], 'b'),
        ('What does hedging a price exposure do?', [('a', 'Doubles the price for free'), ('b', 'Stops all sales'), ('c', 'Locks in part of the price, removing gains as well as losses'), ('d', 'Makes the mine invisible to buyers')], 'c'),
    ],
}
