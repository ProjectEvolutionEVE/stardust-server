"""Tail Latency at Scale: why the slowest few requests decide how a large service feels, and how to tame them."""
CODE = 'computing5_tail_latency'
BOOK = {'title': 'Tail Latency at Scale',
 'subtitle': 'Percentiles, fan-out, hedged and tied requests',
 'chapters': [('Percentiles',
               'An average hides the slow requests. A percentile such as the 99th shows the time '
               'that all but one in a hundred requests beat. Engineers watch the tail, the slowest '
               'slice, because users notice it.'),
              ('Fan-out amplification',
               'A request that calls many services at once waits for the slowest of them. As the '
               'number of calls grows, the chance of hitting a slow one grows too. A small rare '
               'delay becomes common at the top.'),
              ('Hedged requests',
               'A hedged request sends a second copy to another server if the first is slow to '
               'reply. The faster answer is used and the other is cancelled. This cuts the tail at '
               'the cost of some extra work.'),
              ('Tied requests',
               'A tied request sends copies to two servers and tells each about the other. When '
               'one starts, it cancels the other copy. This reduces the wasted work of hedging.'),
              ('Causes of slow tails',
               'Slow tails come from queues, garbage collection pauses, shared resources, and busy '
               'machines. Each cause needs its own fix. Finding the cause is part of the job.'),
              ('Mitigation',
               'Teams limit queue lengths, spread load evenly, and keep background tasks small. '
               'They measure the tail after every change. A system that is fast at the middle can '
               'still feel slow at the edges.')],
 'test': [('What does the 99th percentile show?',
           [('a', 'The average time of every request'),
            ('b', 'The time that all but about one in a hundred requests beat'),
            ('c', 'The number of users'),
            ('d', 'The size of the disk')],
           'b'),
          ('What is fan-out amplification?',
           [('a', 'A fan that cools a server'),
            ('b', 'A way to make requests faster by ignoring them'),
            ('c', 'A request waits for the slowest of many calls, so rare delays become common'),
            ('d', 'A type of network cable')],
           'c'),
          ('What does a hedged request do?',
           [('a', 'Stops all requests for an hour'),
            ('b', 'Deletes the slow server'),
            ('c', 'Writes a letter to the user'),
            ('d', 'Sends a second copy when the first is slow, and uses the faster answer')],
           'd'),
          ('What is an improvement of tied requests over plain hedging?',
           [('a', 'They cancel the other copy, which wastes less work'),
            ('b', 'They send no copies at all'),
            ('c', 'They make every request slower'),
            ('d', 'They only work on paper')],
           'a'),
          ('Which is a common cause of slow tails?',
           [('a', 'Using a blue keyboard'),
            ('b', 'Having too few windows'),
            ('c', 'Long queues on busy machines'),
            ('d', 'Reading the news')],
           'c')]}
