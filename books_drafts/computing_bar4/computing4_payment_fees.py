"""Payment Fees and Chargebacks: what card processing costs, how disputes work, and how to reduce losses."""
CODE = 'computing4_payment_fees'
BOOK = {
    "title": 'Payment Fees and Chargebacks',
    "subtitle": 'What card processing costs, how disputes work, and how to reduce losses',
    "chapters": [
        ('Processing fees',
         'Card payments usually carry a fee taken by the processor, often a percentage of the sale plus a small fixed amount. The total fee can be large for small sales. Compare fees using the full cost per sale, not just the headline rate.'),
        ('The chargeback process',
         'A chargeback is when a card holder asks their bank to reverse a payment. The bank takes the money back from the merchant while the claim is looked at. The merchant can then respond with evidence.'),
        ('Disputes',
         'A dispute is the merchant’s chance to show the sale was valid, such as a receipt, a delivery record or a login history. Respond on time, because late replies usually lose. Keep clear records of every transaction.'),
        ('Reserves',
         'A processor may hold back part of your takings as a reserve, to cover future chargebacks. Reserves tie up cash, which can strain a young business. Ask how reserves are set and when they are released.'),
        ('Pricing around fees',
         'Fees are a cost of sale, and they can be built into prices or shown as a separate charge where the law allows. Make sure the price covers the real cost. A business that ignores fees may sell at a loss without noticing.'),
        ('Reducing losses',
         'Clear product descriptions, fair refund rules and simple contact details reduce disputes. Watch chargeback rates, because high rates can lead to higher fees or loss of the account. Prevention is cheaper than fighting each claim.'),
    ],
    "test": [
        ('What is a chargeback?',
         [('a', 'A fee for a new account'), ('b', 'A request by a card holder to reverse a payment through their bank'), ('c', 'A discount for regular customers'), ('d', 'A type of bank loan')], 'b'),
        ('What is a reserve held by a processor?',
         [('a', 'A spare credit card'), ('b', 'A bonus for the staff'), ('c', 'A sale of old stock'), ('d', 'Part of the takings held back to cover future chargebacks')], 'd'),
        ('Why must a merchant respond to a dispute on time?',
         [('a', 'Late replies usually lose the dispute'), ('b', 'Late replies are always accepted'), ('c', 'Replies are not needed'), ('d', 'Only the bank can respond')], 'a'),
        ('Why compare fees by the full cost per sale?',
         [('a', 'Fees are always the same for everyone'), ('b', 'Fees are never shown'), ('c', 'Small sales can carry a large fee when fixed amounts apply'), ('d', 'Fees are paid by the customer only in every country')], 'c'),
        ('Which step helps reduce disputes?',
         [('a', 'Hiding the contact details'), ('b', 'Making the refund rules unclear'), ('c', 'Ignoring all customer messages'), ('d', 'Clear product descriptions and fair refund rules')], 'd'),
    ],
}
