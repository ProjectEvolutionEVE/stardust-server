"""Light Takes Time: the position you see is where a body was, and how Romer first measured light's speed."""
CODE = 'navigation3a_light_time'
BOOK = {
    "title": 'Light Takes Time',
    "subtitle": 'Why the planets you see are old news, and how light was first measured',
    "chapters": [
        ('Seeing the past',
         'Light takes time to cross space, so every view of the sky is a little out of date. The Sun is about 8 minutes and 20 seconds away, so the light you see left it that long ago. A planet is seen where it was when its light left.'),
        ('Light time across the solar system',
         'Light from the Moon takes about a second and a quarter. Light from Mars takes a few minutes at its closest, and light from Jupiter takes about 43 minutes on average. Far beyond the planets, the delays grow to hours and then days.'),
        ('Correcting for the delay',
         "A navigator must place a body where it is now, not where its light left. The method is to work out the light time, step back that long in the body's orbit, and use the position from that earlier moment. This is called the light-time correction."),
        ("Ole Rømer and Jupiter's moon",
         "In 1676, the Danish astronomer Ole Rømer timed the eclipses of Io, one of Jupiter's moons. The eclipses came later when Earth was farther from Jupiter. He traced this to light taking time to cross Earth's orbit, and his estimate was about 22 minutes."),
        ('The speed, measured properly',
         "Modern measurement gives the speed of light as 299,792 kilometres a second, exactly, because the metre is now defined from it. The distance across Earth's orbit is about 2 AU, which light crosses in about 16.6 minutes."),
        ('Why it matters for a fix',
         'A fix that ignores light time can be off by a noticeable amount for a fast-moving or distant body. A planner who reads the position at the wrong moment aims at the wrong place. Always ask when the light you are using left its source.'),
    ],
    "test": [
        ("What does a planet's position in the sky show you?",
         [('a', 'Exactly where it is at this moment'), ('b', 'Where it was when its light left'), ('c', 'Where it will be next year'), ('d', 'Where its shadow falls')], 'b'),
        ('About how long does sunlight take to reach Earth?',
         [('a', 'About one second'), ('b', 'About one hour'), ('c', 'About one day'), ('d', 'About 8 minutes and 20 seconds')], 'd'),
        ('Which of these did Ole Rømer use in 1676 to show light takes time?',
         [('a', 'The colour of Mars'), ('b', 'Ships on the sea'), ('c', "Eclipses of Io, one of Jupiter's moons"), ('d', 'A sextant sighting on the Moon')], 'c'),
        ('What is the light-time correction?',
         [('a', "Stepping back the light time in the body's orbit to place it correctly now"), ('b', 'Turning the telescope to face the Sun'), ('c', 'Painting the planet a new colour'), ('d', 'Adding a second to the clock')], 'a'),
        ('Why is the speed of light a fixed number today?',
         [('a', 'Because Earth stopped moving'), ('b', 'Because the metre is now defined from it'), ('c', 'Because the Sun sets it'), ('d', 'Because it is the same as the speed of a ship')], 'b'),
    ],
}
