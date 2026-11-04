"""The Economic Cost of a GNSS Outage: sectors affected, hours lost, costs per day, scenarios, resilience and policy."""
CODE = 'navigation5_gnss_outage_economy'
BOOK = {
    "title": 'The Economic Cost of a GNSS Outage',
    "subtitle": 'What happens to work and trade when satellite positioning stops',
    "chapters": [
        ('Sectors affected',
         'Many sectors rely on satellite positioning and timing. Shipping, aviation, farming, surveying, emergency services and finance all depend on them in some way. A single outage can reach many parts of the economy at once.'),
        ('Hours lost',
         'An outage stops work that depends on positioning, and the lost hours add up across every sector. Some hours are a small inconvenience. Others mean cargo delayed, crops missed and services stalled.'),
        ('Costs per day',
         'The cost of one day without positioning can be large, and it varies widely between sectors. Estimate the cost for each sector, then add them up with care.'),
        ('Scenarios',
         'Test what happens in a short outage, a long one, and a wide one. Each scenario gives a different cost, and the comparison shows where the risk is greatest.'),
        ('Resilience',
         'Backup systems, such as land-based positioning and independent time sources, reduce the damage an outage can cause. Resilience is the ability to keep working, or to recover quickly, when the main system fails.'),
        ('Policy',
         'Governments weigh the cost of backups against the cost of outages. Good policy looks at both sides and asks who bears the risk, so that the choice is clear and fair.'),
    ],
    "test": [
        ('Which of these depends on satellite positioning and timing?',
         [('a', 'Only paper maps'), ('b', 'Only handwriting'), ('c', 'Many sectors, such as shipping, farming and aviation'), ('d', 'Only cooking')], 'c'),
        ('What does an outage do to economic activity?',
         [('a', 'It stops work and adds up lost hours'), ('b', 'It doubles output'), ('c', 'It has no effect at all'), ('d', 'It makes every trip faster')], 'a'),
        ('What is resilience in this context?',
         [('a', 'Being unable to recover'), ('b', 'Backup systems that reduce the damage from an outage'), ('c', 'The colour of the receiver'), ('d', 'The price of a battery')], 'b'),
        ('Why test several scenarios?',
         [('a', 'To find one single answer'), ('b', 'To ignore the risk'), ('c', 'To hide the result'), ('d', 'To see how the cost changes with short, long and wide outages')], 'd'),
        ('What do governments weigh in policy on outages?',
         [('a', 'The cost of backups against the cost of outages'), ('b', 'The colour of the satellites'), ('c', 'The size of the logo'), ('d', 'Nothing at all')], 'a'),
    ],
}
