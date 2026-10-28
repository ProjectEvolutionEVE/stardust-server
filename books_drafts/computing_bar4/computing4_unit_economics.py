"""Unit Economics of a Software Product: whether each customer brings in more money than it costs to win and serve them."""
CODE = 'computing4_unit_economics'
BOOK = {
    "title": 'Unit Economics of a Software Product',
    "subtitle": 'Whether each customer brings in more money than it costs to win and serve',
    "chapters": [
        ('Revenue and cost per customer',
         'Unit economics looks at one customer, or one typical customer, and asks what they bring in and what they cost. Revenue is what they pay over their time with you. Cost includes the servers, support and other services they use.'),
        ('Contribution margin',
         'Contribution margin is revenue minus the costs that rise with each new customer. It shows how much each customer adds towards paying for the rest of the business. A product with a thin margin needs very large numbers to succeed.'),
        ('Acquisition cost',
         'Acquisition cost is what you spend to win one customer, such as advertising, sales time and free trials. Compare it honestly with the margin each customer earns. Hidden sales costs are easy to forget.'),
        ('Payback',
         'Payback is how many months of margin it takes to repay the acquisition cost. A short payback lowers the risk of growing. A long payback means the business must have cash to wait for each customer to pay back.'),
        ('Retention effects',
         'A customer who stays longer earns more margin, and the value of retention grows over time. Small changes in cancellation rates can change the whole picture. Track retention as carefully as you track new sales.'),
        ('Cohort views',
         'A cohort view groups customers by the month they joined, and follows each group over time. It shows whether newer customers behave like older ones. Cohorts reveal trends that a single total number can hide.'),
    ],
    "test": [
        ('What does unit economics examine?',
         [('a', 'The colour of the office carpet'), ('b', 'What one customer brings in and what they cost'), ('c', 'The number of coffee machines'), ('d', 'The weather in the city')], 'b'),
        ('What is contribution margin?',
         [('a', 'The total size of the office'), ('b', 'The number of staff on holiday'), ('c', 'The price of paper'), ('d', 'Revenue minus the costs that rise with each new customer')], 'd'),
        ('What is acquisition cost?',
         [('a', 'What it costs to win one customer'), ('b', 'The cost of the building lease'), ('c', 'The cost of a server rack'), ('d', 'The cost of the annual party')], 'a'),
        ('What does a long payback period mean?',
         [('a', 'Customers pay at once'), ('b', 'The business has no costs'), ('c', 'It takes many months of margin to repay the cost of winning a customer'), ('d', 'The customers never leave')], 'c'),
        ('What does a cohort view show?',
         [('a', 'A list of the office plants'), ('b', 'The menu of the canteen'), ('c', 'The weather forecast'), ('d', 'How groups of customers who joined together behave over time')], 'd'),
    ],
}
