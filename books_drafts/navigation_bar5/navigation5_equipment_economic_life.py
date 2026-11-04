"""The Economic Life of Navigation Equipment: technical versus economic life, upgrades, maintenance costs, replacement timing and records."""
CODE = 'navigation5_equipment_economic_life'
BOOK = {
    "title": 'The Economic Life of Navigation Equipment',
    "subtitle": 'Knowing when old equipment still pays its way, and when to replace it',
    "chapters": [
        ('Technical versus economic life',
         'Equipment can keep working long after it stops paying its way. Its technical life is how long it can run. Its economic life is how long it is worth keeping. The two are often very different.'),
        ('Upgrades',
         'A newer model may cost more to buy but less to run. It may be more accurate, more reliable or easier to service. Compare the total cost of both options, not just the price on the day.'),
        ('Maintenance costs',
         'Repairs tend to rise as equipment ages. At some point the cost of keeping it running can outgrow its value. Watch that trend closely, because it often signals the right time to act.'),
        ('Replacement timing',
         'Consider replacing equipment when the rising cost of keeping it passes the cost of a new unit. Adjust for the time value of money, so that costs in different years are compared fairly.'),
        ('Records',
         'Keep a clear log of repairs, downtime and costs for each item. A good record turns a hunch into a decision that rests on facts, and it helps defend that decision later.'),
        ('Summary',
         'Base the decision on the record, not on a feeling. Review it each year. The best time to replace equipment is usually the time that the numbers, not nostalgia, point to.'),
    ],
    "test": [
        ('What is the difference between technical and economic life?',
         [('a', 'They are exactly the same thing'), ('b', 'Technical life is the price of the item'), ('c', 'Economic life is the colour of the case'), ('d', 'Equipment can work after it stops paying its way')], 'd'),
        ('Why might a newer model be worth buying?',
         [('a', 'Because it is always cheaper to buy'), ('b', 'Because the old one must be kept'), ('c', 'Because it may cost less to run, even if dearer to buy'), ('d', 'Because the old one is free')], 'c'),
        ('What tends to happen to maintenance costs as equipment ages?',
         [('a', 'They tend to rise'), ('b', 'They always fall'), ('c', 'They stop altogether'), ('d', 'They vanish after a year')], 'a'),
        ('When is replacement often worth considering?',
         [('a', 'Only on a sunny day'), ('b', 'When the rising cost of keeping it passes the cost of a new unit'), ('c', 'Never'), ('d', 'When the paint starts to fade')], 'b'),
        ('Why keep a clear log of repairs?',
         [('a', 'To fill a shelf'), ('b', 'To hide mistakes'), ('c', 'So that the decision rests on facts'), ('d', 'To avoid making any decision')], 'c'),
    ],
}
