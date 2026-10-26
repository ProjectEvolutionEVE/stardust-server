"""What Drains Each Bar: stamina, energy and focus, what wears each one down, and what gives each one back."""
CODE = 'flight3b_what_drains_bars'
BOOK = {
    "title": 'What Drains Each Bar',
    "subtitle": 'Stamina, energy and focus: what wears each one down, and what gives it back',
    "chapters": [
        ('Three bars, three jobs',
         'Your character has three bars, each from 0 to 100: stamina, energy and focus. Stamina is the strength of the body, energy is the fuel that keeps you going, and focus is the attention of the mind. Each bar wears down over a waking day, and each needs its own kind of rest.'),
        ('Stamina',
         'Stamina is the bar that tells you the body is tired. Long hours at the controls, hard hauling and heavy physical work all use it up. Sleep is the main way to restore it, and a well-timed rest in your own bed does more than a short doze in a chair.'),
        ('Focus',
         'Focus is the bar that tells you the mind is tired. Close reading, scanning the rings, taking a library test, trading and drafting all ask for sustained attention. Focus recovers best with calm, quiet rest, and it does not come back from rushing.'),
        ('Energy',
         'Energy drains steadily all the time you are awake. It is the slowest bar to notice and the easiest to forget, which is why a long day can wear it down before you feel it. Regular meals, water and rest keep it steady.'),
        ('The rate in the game',
         'In the game as it stands, each bar drains about 2.2 points an hour while the character is awake. A 16-hour day takes a rested character from 100 down to about 65, which is the lowest recommended level. Plan the day to match those hours.'),
        ('Why the three matter together',
         'A pilot can have plenty of energy and still have a tired mind. Look at all three bars, not just the one you feel most. The lowest bar sets how well you can do your duties, and it is the one to act on first.'),
    ],
    "test": [
        ('Which bar stands for the mind?',
         [('a', 'Stamina'), ('b', 'Energy'), ('c', 'Focus'), ('d', 'Warmth')], 'c'),
        ('In the game as it stands, how fast does each bar drain while the character is awake?',
         [('a', 'About 22 points an hour'), ('b', 'About 35 points a day'), ('c', 'About 0.22 points an hour'), ('d', 'About 2.2 points an hour')], 'd'),
        ('Which task asks most of focus?',
         [('a', 'Taking a library test'), ('b', 'Lifting cargo'), ('c', 'Sleeping in bed'), ('d', 'Drinking water')], 'a'),
        ('What does the lowest bar tell you?',
         [('a', 'How much the craft weighs'), ('b', 'How well you can perform your duties, so it is the one to act on first'), ('c', 'The distance to the Sun'), ('d', 'The price of fuel')], 'b'),
        ('Why does a 16-hour day matter for the bars?',
         [('a', 'It doubles the fuel bar'), ('b', 'It restores all three bars to 100 at once'), ('c', 'It takes a rested character from 100 down to about 65'), ('d', 'It stops the drain for the rest of the day')], 'c'),
    ],
}
