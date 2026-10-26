"""Activity-Based Costing: overhead and its allocation, cost drivers, tracing costs, surprising results, limits, and when it is worth the effort."""
CODE = 'business4_abc'
BOOK = {
    "title": 'Activity-Based Costing',
    "subtitle": 'Tracing overhead to the work that really causes it',
    "chapters": [
        ('Overhead and its allocation',
         'Overhead is the cost of running a business that cannot be tied to one product, such as rent, power and admin. Firms must spread these costs across products to price them. Traditional methods often spread overhead by a simple measure, such as direct labour hours.'),
        ('Cost drivers',
         'A cost driver is the factor that causes a cost to rise, such as the number of set-ups on a machine, the number of orders processed, or the number of inspections. Activity-based costing links overhead to the drivers that really cause it.'),
        ('Tracing costs',
         'The method first identifies the activities a firm performs, such as receiving goods or packing orders. It then works out the cost of each activity and traces it to the products that use it, by the number of times each product needs that activity.'),
        ('Surprising results',
         'When costs are traced this way, products that looked profitable can turn out to lose money, and the reverse can also happen. A simple, high-volume product may use few activities, while a small, complex one may use many. Managers are often surprised by what they find.'),
        ('Limits',
         'Activity-based costing takes time and effort to set up and maintain. It can give false precision when the drivers are guesses. Its results also depend on the choice of activities and drivers, which is a judgement, not a fact of nature.'),
        ('When it is worth the effort',
         'The method is worth the effort when overhead is large, when products differ a lot in their use of activities, and when pricing or product choices depend on accurate costs. A firm with small overhead and similar products may do fine with a simpler method.'),
    ],
    "test": [
        ('What is overhead?',
         [('a', 'The cost of running a business that cannot be tied to one product'), ('b', 'The cost of raw materials for one product'), ('c', 'The profit a firm keeps'), ('d', 'The interest on savings')], 'a'),
        ('What is a cost driver?',
         [('a', 'A person who drives a delivery van'), ('b', 'The factor that causes a cost to rise'), ('c', 'A type of tax'), ('d', 'A bank account')], 'b'),
        ('What is the first step in activity-based costing?',
         [('a', 'Sell all the stock'), ('b', 'Cut the rent in half'), ('c', 'Identify the activities the firm performs'), ('d', 'Stop all production')], 'c'),
        ('Why can activity-based costing reveal surprises?',
         [('a', 'Because all products always cost the same'), ('b', 'Because overhead never changes'), ('c', 'Because it ignores the work done'), ('d', 'Because products that looked profitable may lose money once costs are traced')], 'd'),
        ('When is the method most worth the effort?',
         [('a', 'When overhead is large and products use activities very differently'), ('b', 'When overhead is zero'), ('c', 'When all products are identical and tiny'), ('d', 'When no pricing decisions are made')], 'a'),
    ],
}
