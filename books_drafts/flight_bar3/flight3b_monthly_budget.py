"""The Pilot's Monthly Budget: how to set flight hours against the weekly lease over a 28-day month, and keep a buffer for the unexpected."""
CODE = 'flight3b_monthly_budget'
BOOK = {
    "title": "The Pilot's Monthly Budget",
    "subtitle": 'Flight hours against the weekly lease, month by month, with a buffer for the unexpected',
    "chapters": [
        ('Think in months',
         'A week is too short to judge a pilot\'s money. Plan by the month instead, which here means the 28-day contract. Look at all the costs that fall within that month, not just the next payment.'),
        ('Two ways to pay',
         'You can pay 50 credits for each hour in the air, with fuel included. Or you can take the weekly lease: 500 credits a week, paid up front, on a 28-day contract that renews automatically. Over a 28-day month, the lease is 2,000 credits in total.'),
        ('The monthly break-even',
         'Divide the lease for the month by the hourly rate: 2,000 divided by 50 is 40 hours. Fly more than 40 hours in the month and the lease costs less. Fly fewer and the hourly rate costs less. This is the same break-even as 10 hours a week, seen across the whole month.'),
        ('Count the hours you plan',
         'Write down the flying you expect to do in the month, the missions and the rest days. Compare the total with 40 hours. A plan that stays well below 40 hours points to the hourly rate, and a plan that clearly goes above 40 points to the lease.'),
        ('Keep a buffer',
         'Surprises happen: a tow, a repair, a long mission that runs over. Keep a buffer of credits that is not already promised to the lease or the hours. A buffer is what lets you fly on without borrowing in a hurry.'),
        ('Review each month',
         'At the end of each month, compare what you planned with what you flew, and check the buffer. Change the plan only when the pattern has held for a while, not after one unusual month. Good money habits are built month by month.'),
    ],
    "test": [
        ('How many days is the lease contract in this game?',
         [('a', '7 days'), ('b', '14 days'), ('c', '28 days'), ('d', '365 days')], 'c'),
        ('What is the total cost of the lease over one 28-day month?',
         [('a', '500 credits'), ('b', '1,000 credits'), ('c', '5,000 credits'), ('d', '2,000 credits')], 'd'),
        ('How many hours in a 28-day month makes the hourly rate and the lease cost the same?',
         [('a', '40 hours'), ('b', '20 hours'), ('c', '10 hours'), ('d', '100 hours')], 'a'),
        ('Why keep a buffer of credits?',
         [('a', 'So the craft flies faster'), ('b', 'To cover surprises such as a tow or a repair without borrowing in a hurry'), ('c', 'To raise the hourly rate'), ('d', 'To stop the fuel bar draining')], 'b'),
        ('When should you change your plan after reviewing the month?',
         [('a', 'After every single unusual month'), ('b', 'Every hour of the day'), ('c', 'Only when the pattern has held for a while'), ('d', 'Never')], 'c'),
    ],
}
