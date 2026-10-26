"""Queues and Waiting Lines: Erlang and telephones, arrival and service, why waits explode near capacity, Little's law, pooling servers, and designing a line."""
CODE = 'business4_queue'
BOOK = {
    "title": 'Queues and Waiting Lines',
    "subtitle": 'Why waits grow fast as a service gets busy, and how to design around it',
    "chapters": [
        ('Erlang and telephones',
         'In the early 1900s the Danish engineer Agner Krarup Erlang studied telephone calls for the Copenhagen Telephone Company. He developed the mathematics of waiting lines to work out how many lines and operators were needed. His work is still the basis of much queue planning.'),
        ('Arrival and service',
         'A queue has two basic parts: customers arrive at some rate, and servers finish them at some rate. When arrivals are steady and service is steady, the line behaves in one way. When either varies, which is common, the line can build up quickly.'),
        ('Why waits explode near capacity',
         'When a service runs at low use, waits are short. As use approaches full capacity, waits rise sharply, and a small extra load can cause a large increase in waiting time. A system that is always nearly full has little room to absorb a bad day.'),
        ("Little's law",
         "Little's law says that the average number of items in a system equals the average arrival rate times the average time each item spends in it. The law holds for many systems and gives a quick way to link stock, flow and time."),
        ('Pooling servers',
         'Putting several servers into one shared queue usually gives shorter average waits than splitting the same servers into separate lines. A single pool can use idle capacity more evenly, so customers wait less on average for the same number of staff.'),
        ('Designing a line',
         'A good design keeps utilisation below full capacity, pools servers where it can, and sets clear expectations for waits. Fast service for short tasks, a separate line for them, and honest waiting-time signs all help. The aim is to make the wait feel fair as well as short.'),
    ],
    "test": [
        ('Which Danish engineer developed the mathematics of waiting lines for telephone calls?',
         [('a', 'Niels Bohr'), ('b', 'Hans Christian Andersen'), ('c', 'Agner Krarup Erlang'), ('d', 'Carl Jacobsen')], 'c'),
        ('What happens to waiting times as a service nears full capacity?',
         [('a', 'They fall to zero'), ('b', 'They stay exactly the same'), ('c', 'They become fixed by law'), ('d', 'They rise sharply')], 'd'),
        ("What does Little's law link?",
         [('a', 'Items in a system, arrival rate and time spent in the system'), ('b', 'Price, tax and interest'), ('c', 'Rent and wages'), ('d', 'Shoe size and height')], 'a'),
        ('What usually happens when several servers share one queue?',
         [('a', 'Waits always double'), ('b', 'Average waits tend to be shorter than with separate lines'), ('c', 'Customers must leave'), ('d', 'Servers stop working')], 'b'),
        ('Which design choice helps a line feel fair?',
         [('a', 'Hiding how long the wait will be'), ('b', 'Letting the busiest customers cut in'), ('c', 'Setting clear expectations for waits and a separate line for short tasks'), ('d', 'Closing the line at noon')], 'c'),
    ],
}
