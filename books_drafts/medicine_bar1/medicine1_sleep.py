"""Medicine, bar 1: Sleep and Recovery. The real science of sleep, and the three bars exactly as ruled (body.py, CLAUDE.md)."""
CODE = 'medicine1_sleep'
BOOK = {
    "title": 'Sleep and Recovery',
    "subtitle": 'What sleep does for the body and the brain, and how your three bars refill',
    "chapters": [
        ('What sleep is for',
         'Sleep is when the body repairs muscle and tissue, and when the brain sorts and stores what you learned during the day. Most adults need about 7 hours or more a night. Feeling fine on less is rare, and sleep debt builds up quietly.'),
        ('Sleep cycles',
         'A night of sleep moves through cycles of about 90 minutes. Each cycle has light sleep, deep sleep and dream sleep. Deep sleep does most of the physical repair, and dream sleep helps with memory and mood.'),
        ('Your three bars',
         'Aboard the Starship your body has three bars: stamina, energy and mental focus. While you are awake, each one drains by 2.2 points an hour. That means a 16-hour day takes you from 100% down to 65%.'),
        ('When the bars fall',
         '65% is the lowest recommended level. Near the top of the scale your abilities slip only slightly. Below 65% they decline severely, and below 50% they decline extremely, so studying and guiding the ship become much harder. On-screen warnings remind you when you are pushing past healthy rest.'),
        ('Resting in bed',
         'In bed, sleep refills each bar by 35 points every 6 hours, about 5.8 points an hour. From 65%, 6 hours takes you back to 100%. From 50%, 6 hours reaches only 85%, and a full rest takes about 8½ hours. Sleeping in the cockpit out in space refills at half that rate, so the bed is always the best rest.'),
        ('Real rest, real time',
         'The game runs in real time, just as the real world does. A nap does not speed up a job that takes weeks. A steady sleep time helps the body clock stay in step, so try to rest at the same hours each day.'),
    ],
    "test": [
        ('How many hours of sleep do most adults need?',
         [('a', 'About 2 hours'), ('b', 'About 4 hours'), ('c', 'About 7 hours or more'), ('d', 'About 12 hours')], 'c'),
        ('About how long is a typical sleep cycle?',
         [('a', 'About 90 minutes'), ('b', 'About 10 minutes'), ('c', 'About 6 hours'), ('d', 'About 2 days')], 'a'),
        ('How fast does each bar drain while you are awake?',
         [('a', '35 points an hour'), ('b', 'It never drains'), ('c', '10 points an hour'), ('d', '2.2 points an hour')], 'd'),
        ('From 50%, how long does a full rest take in bed?',
         [('a', '6 hours'), ('b', 'About 8½ hours'), ('c', '24 hours'), ('d', 'It cannot be done')], 'b'),
        ('At what level do abilities start to decline severely?',
         [('a', '90%'), ('b', 'Below 65%'), ('c', 'Below 35%'), ('d', 'Below 10%')], 'b'),
    ],
}
