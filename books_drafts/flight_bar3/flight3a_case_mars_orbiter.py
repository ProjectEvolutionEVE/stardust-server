"""Case Study: Mars Climate Orbiter, 1999. A spacecraft lost to a mismatch of units."""
CODE = 'flight3a_case_mars_orbiter'
BOOK = {
    "title": 'Case Study: Mars Climate Orbiter, 1999',
    "subtitle": 'A spacecraft lost to a mismatch of units',
    "chapters": [
        ('A craft for Mars',
         "NASA's Mars Climate Orbiter was built to study the weather and climate of Mars. It flew for about nine months to reach the planet. In September 1999 it was due to fire its engine, slow down and settle into orbit."),
        ('Two systems of units',
         "One team's software gave thrust data in pound-force seconds, an imperial unit. The navigation team expected newton-seconds, the metric unit. A pound-force second is about four and a half times a newton-second, so every number from that source was wrong."),
        ('Small errors that grew',
         "Each burn was planned from the wrong numbers, so each one pushed the craft a little off its planned path. The errors built up over the months of flight. By the time of arrival, the craft was far closer to Mars than planned."),
        ('The loss',
         "The craft passed too low into the upper atmosphere of Mars and was lost. The mission cost well over a hundred million dollars, and the loss was a great disappointment to the teams who had built it."),
        ('Clear units',
         "The review that followed called for clear units on every value passed between teams. A label on each number stops a silent mismatch from getting through. Simple checks often catch what complex systems miss."),
        ('What a pilot learns',
         "Read the units on every number, even when you think you know the source. A correct formula with the wrong unit gives the wrong answer. Ask a second person to check any number that will change your course."),
    ],
    "test": [
        ('Where was NASA\'s Mars Climate Orbiter going?',
         [('a', 'The Moon'), ('b', 'Mars'), ('c', 'Jupiter'), ('d', 'The Sun')], 'b'),
        ('Which units caused the trouble?',
         [('a', 'Pound-force seconds and newton-seconds'), ('b', 'Metres and seconds'), ('c', 'Kilograms and litres'), ('d', 'Degrees and minutes')], 'a'),
        ('What was the main result of the unit mismatch?',
         [('a', 'The craft got brighter'), ('b', 'The crew moved to the Moon'), ('c', 'Each burn pushed the craft off its planned path, and the errors grew'), ('d', 'The fuel doubled')], 'c'),
        ('What happened to the craft in September 1999?',
         [('a', 'It landed safely'), ('b', 'It stopped for lunch'), ('c', 'It turned into a moon'), ('d', 'It passed too low into the upper atmosphere and was lost')], 'd'),
        ('What is a sensible habit taught by this case?',
         [('a', 'Trust the numbers because a computer produced them'), ('b', 'Read the units on every number, and have a second person check any number that changes the course'), ('c', 'Never send data between teams'), ('d', 'Keep every number secret from the other teams')], 'b'),
    ],
}
