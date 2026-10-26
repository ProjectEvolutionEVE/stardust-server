"""Navigation Errors and Corrections: how small mistakes grow with distance, and how a pilot brings a craft back on course."""
CODE = 'flight3a_navigation_errors'
BOOK = {
    "title": 'Navigation Errors and Corrections',
    "subtitle": 'How small mistakes grow with distance, and how a pilot brings a craft back on course',
    "chapters": [
        ('Small errors grow',
         "Every measurement carries a small error. Over a short run the error is tiny. Over a long run, the same small error builds up and can put the craft far from where the plan says it should be."),
        ('Dead reckoning',
         "Dead reckoning works out where you are from your last known position, your speed, your heading and the time that has passed. It is simple, but each step carries a little error, and those errors add up. The longer you go without a fix, the less you can trust the answer."),
        ('Fixes',
         "A fix is a check against something you know well, such as a star, a beacon or a known landmark. A fix shrinks the error back down. Pilots take a fix whenever they can, because a fix resets the drift."),
        ('Drift',
         "Drift is a slow, steady error, such as a sensor that reads a little too high. Drift hides for a while and then grows large. Pilots watch for a trend that keeps moving in the same direction."),
        ('Small early corrections',
         "When the error is small, a small correction puts it right. A large error found late needs a bigger burn, which uses more fuel. The rule is to correct early and gently."),
        ('Check, then correct',
         "Before any correction, check the new reading against a second source. Then make the smallest change that does the job, and check again afterwards. A confident wrong fix can do more harm than no fix at all."),
    ],
    "test": [
        ('Why do small measurement errors become big over a long trip?',
         [('a', 'Colour hides them'), ('b', 'The engines cancel them out'), ('c', 'They add up as the distance and the time grow'), ('d', 'Space shrinks them')], 'c'),
        ('What is dead reckoning?',
         [('a', 'Working out your position from the last known point, speed, heading and time'), ('b', 'A game of cards'), ('c', 'Reading the colour of the hull'), ('d', 'Waiting in port')], 'a'),
        ('What is a fix?',
         [('a', 'A broken part'), ('b', 'A check against something known, which shrinks the error'), ('c', 'A kind of food'), ('d', 'A type of hatch')], 'b'),
        ('What is drift?',
         [('a', 'A quick jump in position'), ('b', 'A type of thruster'), ('c', 'The sound of the hull'), ('d', 'A slow, steady error that can grow large over time')], 'd'),
        ('Why is a small early correction usually better than a large late one?',
         [('a', 'It makes the hull brighter'), ('b', 'It stops the clock'), ('c', 'It costs less fuel and is easier to get right'), ('d', 'It is never needed')], 'c'),
    ],
}
