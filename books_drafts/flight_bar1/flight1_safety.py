"""Pilot Safety and Your Body: the three bars, rest in bed or in the cockpit, and staying safe in space."""
CODE = 'flight1_safety'
BOOK = {
    "title": 'Pilot Safety and Your Body',
    "subtitle": 'Your three bars, rest in bed or in the cockpit, and staying safe in space',
    "chapters": [
        ('Your three bars',
         'Your character has three bars, each from 0 to 100: stamina, energy and mental focus. Together they drain while you are awake, about 2.2 points an hour on average. A full 16-hour day takes a bar from 100% down to about 65%.'),
        ('What the bars mean',
         'At 65% you are at the lowest recommended level. Below that, your abilities begin to decline, and below 50% you can no longer carry out your duties properly. Studying and flying get harder as the bars fall, and the game warns you when you are pushing past healthy limits.'),
        ('Rest in your bed',
         'Your bed in the Private Quarters gives the best rest. Each bar refills 35 points every 6 hours, so 6 hours takes you from 65% back to 100%. Starting from 50%, it takes about 8 and a half hours to be fully rested.'),
        ('Rest in the cockpit',
         "You can also sleep in your craft's cockpit, out in space. It refills at half the rate of your bed, so 35 points takes about 12 hours. Use it when you must, but your bed is always the better rest."),
        ('Why tired pilots fly worse',
         'Tiredness slows reactions and dulls attention, for real pilots and for real astronauts alike. A tired pilot misreads a reading or takes a bearing badly. Rest is part of flying, not a break from it.'),
        ('Staying safe in space',
         "Sunlight gets much stronger as you get closer to the Sun. The inverse-square rule says that at Mercury's distance it is about 6.7 times stronger than at Earth's. Space also carries radiation from the Sun and from deep space, which is why real spacecraft are shielded. Astronauts follow strict sleep schedules too, because tired crews make mistakes."),
    ],
    "test": [
        ('Which three bars does your character have?',
         [('a', 'Health, water and air'), ('b', 'Speed, fuel and heat'), ('c', 'Stamina, energy and mental focus'), ('d', 'Hunger, thirst and sleep')], 'c'),
        ('What is the lowest recommended level for your bars?',
         [('a', '100%'), ('b', '50%'), ('c', '20%'), ('d', '65%')], 'd'),
        ('How long does it take a bar to refill from 65% to 100% in your bed?',
         [('a', 'About 1 hour'), ('b', '6 hours'), ('c', '12 hours'), ('d', '24 hours')], 'b'),
        ('How does resting in the cockpit compare with resting in your bed?',
         [('a', 'It is twice as fast'), ('b', 'It is the same'), ('c', 'It does not refill at all'), ('d', 'It is half the rate')], 'd'),
        ("About how much stronger is sunlight at Mercury's distance than at Earth's?",
         [('a', 'About 6.7 times'), ('b', 'Half as strong'), ('c', 'About the same'), ('d', 'About 100 times')], 'a'),
    ],
}
