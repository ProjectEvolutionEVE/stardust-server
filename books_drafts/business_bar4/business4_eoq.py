"""Inventory and Economic Order Quantity: ordering cost, holding cost, the EOQ formula, reorder points, safety stock, and ABC classes."""
CODE = 'business4_eoq'
BOOK = {
    "title": 'Inventory and Economic Order Quantity',
    "subtitle": 'How much to order at a time, and when to reorder',
    "chapters": [
        ('Ordering cost',
         'Every order placed with a supplier has a fixed cost: the paperwork, the phone call, the delivery check. Ordering cost is the total of these fixed costs over a year. Placing fewer, larger orders lowers it, while placing many small ones raises it.'),
        ('Holding cost',
         'Stock sitting on a shelf costs money. It ties up cash, takes up space, can spoil or go out of date, and needs insurance and handling. Holding cost is the yearly cost of keeping one unit in stock. Larger orders raise it, since more stock stays on hand for longer.'),
        ('The EOQ formula',
         'The economic order quantity balances the two costs. The usual formula is the square root of two times annual demand times the ordering cost, divided by the holding cost per unit. It gives the order size that makes the total of the two costs as small as possible.'),
        ('Reorder points',
         'A reorder point is the stock level at which a new order should be placed. It is set so that the new order arrives just as the old stock runs out. The point depends on how much is used each day and how long the supplier takes to deliver.'),
        ('Safety stock',
         'Demand and delivery times vary, so a firm keeps some safety stock as a cushion. Holding more safety stock lowers the risk of running out, but raises holding cost. Choosing the level is a trade-off between the cost of shortages and the cost of stock.'),
        ('ABC classes',
         'ABC analysis sorts stock into three groups. Class A items are few but make up most of the value, and deserve close control. Class C items are many but low in value, and can be managed simply. Class B lies between the two.'),
    ],
    "test": [
        ('What does ordering cost cover?',
         [('a', 'The price of the goods themselves only'), ('b', 'The fixed costs of each order placed with a supplier'), ('c', 'The rent of the head office'), ('d', 'The tax on profits')], 'b'),
        ('Which of these is part of holding cost?',
         [('a', 'The fee for placing an order'), ('b', 'The cost of a sales meeting'), ('c', 'The cash tied up in stock on the shelf'), ('d', 'The shipping cost paid by a customer')], 'c'),
        ('What does the economic order quantity balance?',
         [('a', 'Sales against advertising'), ('b', 'Rent against wages'), ('c', 'Tax against interest'), ('d', 'Ordering cost against holding cost')], 'd'),
        ('What is a reorder point?',
         [('a', 'The stock level at which a new order should be placed'), ('b', 'The highest price a shop can charge'), ('c', 'The date a supplier closes'), ('d', 'The number of staff in a warehouse')], 'a'),
        ('In ABC analysis, what do Class A items have?',
         [('a', 'Many items with very low value'), ('b', 'Few items that make up most of the value'), ('c', 'No value at all'), ('d', 'Only the same price as every other item')], 'b'),
    ],
}
