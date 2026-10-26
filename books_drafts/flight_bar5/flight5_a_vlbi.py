"""Very Long Baseline Methods: using two distant stations and far-off quasars to pin down a craft's direction."""
CODE = 'flight5_a_vlbi'
BOOK = {
    "title": 'Very Long Baseline Methods',
    "subtitle": 'Two distant stations and far-off quasars',
    "chapters": [
        ('Two stations, one signal',
         'Very long baseline methods use two radio stations on different continents, both receiving the same signal from a craft. The distance between the stations is the baseline. Because the baseline is so large, the method can measure direction very precisely.'),
        ('Quasars as reference points',
         'Quasars are very distant, bright objects whose positions are known with great precision. Teams observe a quasar near the craft in the sky. The difference in timing between the stations then tells the team the direction to the craft, relative to the quasar.'),
        ('Delta-DOR',
         'A method called delta-DOR uses this idea. It compares the arrival times of the signal at two stations, with a quasar as a fixed point. It is especially useful for finding where a craft is across the sky.'),
        ('Angular accuracy',
         'The method can measure angles to a very small fraction of a degree. This is far better than most tracking methods. For a craft far away, that precision translates into a useful position.'),
        ('Mars landers',
         'Delta-DOR has been used to help navigate spacecraft on the way to Mars, including landers that needed to arrive at a precise place. The method helps reduce the uncertainty before a critical arrival.'),
        ('Use today',
         'Very long baseline methods are used together with Doppler and ranging. Each method adds a different kind of information. Together they give a strong fix on where a craft is and where it is going.'),
    ],
    "test": [
        ('What are the two stations in a very long baseline method used for?',
         [('a', 'To paint the craft'), ('b', 'To receive the same signal and measure small timing differences'), ('c', 'To cook the crew meals'), ('d', 'To count the planets')], 'b'),
        ('What are quasars used for in these methods?',
         [('a', 'As fuel for the craft'), ('b', 'As landing pads'), ('c', 'As fixed reference points in the sky'), ('d', 'As crew cabins')], 'c'),
        ('What is delta-DOR?',
         [('a', 'A cooking method'), ('b', 'A type of solar panel'), ('c', 'A new kind of engine'), ('d', 'A method that compares signal arrival at two stations with a quasar as a fixed point')], 'd'),
        ('What does a very long baseline let the method do?',
         [('a', 'Measure direction very precisely'), ('b', 'Stop the rocket'), ('c', 'Turn night into day'), ('d', 'Make the craft lighter')], 'a'),
        ('What kind of mission has used delta-DOR?',
         [('a', 'Missions to Mars'), ('b', 'Ocean fishing trips'), ('c', 'Bus routes'), ('d', 'Ski races')], 'a'),
    ],
}
