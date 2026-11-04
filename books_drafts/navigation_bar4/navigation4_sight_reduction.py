"""Sight Reduction by Hand: turning one observed altitude into a line on the chart."""
CODE = "navigation4_sight_reduction"
BOOK = {
    "title": "Sight Reduction by Hand",
    "subtitle": "Working out where a sight places you, step by step",
    "chapters": [
        ("Why reduce a sight", "A sight gives you an observed altitude of a star, planet or the Sun. Sight reduction turns that single number into a line on the chart. Before calculators, navigators did the work by hand with printed tables."),
        ("The assumed position", "You begin with an assumed position near your dead reckoning position. Choose a point in whole degrees of latitude and longitude, which keeps the tables simple. The gap between the assumed and true positions is small enough to work with."),
        ("The calculated altitude", "From the assumed position, you work out the altitude the body should have at that moment. This comes from the navigational triangle, using latitude, declination and local hour angle. Tables do most of the arithmetic for you."),
        ("The azimuth", "The azimuth is the compass direction from the assumed position toward the body. It tells you which way the line of position runs. Together with the intercept, it fixes the line on the chart."),
        ("The altitude intercept", "The intercept is the difference between the observed altitude and the calculated altitude. If the observed altitude is larger, you measure the intercept toward the body. If it is smaller, you measure it away from the body."),
        ("Plotting and checking", "Plot the intercept along the azimuth line, then draw the line of position at right angles to the azimuth through that point. Check the reduction by working it a second way, or by comparing with another sight. A careful check catches most slips in arithmetic."),
    ],
    "test": [
        ("Why do navigators choose an assumed position in whole degrees?",
         [("a", "Whole degrees are required by law"), ("b", "The Earth can only be measured in whole degrees"), ("c", "It keeps the tables simple to use"), ("d", "Stars only appear at whole degrees")], "c"),
        ("What is the altitude intercept?",
         [("a", "The observed altitude minus the calculated altitude"), ("b", "The calculated altitude plus the azimuth"), ("c", "The latitude minus the declination"), ("d", "The local hour angle divided by two")], "a"),
        ("How does the line of position run, compared with the azimuth?",
         [("a", "Parallel to the azimuth"), ("b", "Along the meridian"), ("c", "Through the assumed position at 45 degrees"), ("d", "At right angles to the azimuth")], "d"),
        ("If the observed altitude is greater than the calculated altitude, which way is the intercept measured?",
         [("a", "Away from the body"), ("b", "Toward the body"), ("c", "Along the horizon"), ("d", "Always to the north")], "b"),
        ("What is a good way to check a sight reduction?",
         [("a", "Round the answer up"), ("b", "Skip the azimuth"), ("c", "Work it a second way or compare with another sight"), ("d", "Read the almanac backwards")], "c"),
    ],
}
