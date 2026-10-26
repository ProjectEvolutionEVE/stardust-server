"""Time Scales and the Julian Date: the clocks that astronomers and navigators must agree on."""
CODE = 'navigation3a_time_scales'
BOOK = {
    "title": 'Time Scales and the Julian Date',
    "subtitle": 'Atomic time, Earth time, and one day count for every calculation',
    "chapters": [
        ('More than one clock',
         'Astronomers do not use one clock. The Earth turns unevenly, so a time based on the day alone drifts. Atomic clocks keep steady time, and each time scale is built for a different job.'),
        ('Atomic time and UTC',
         'International Atomic Time, called TAI, counts seconds from the steady ticks of many atomic clocks. Coordinated Universal Time, UTC, is TAI with leap seconds added from time to time, so that it stays close to the turning of the Earth.'),
        ('Terrestrial and barycentric time',
         'Terrestrial Time, TT, is a steady scale for Earth-based calculations and sits a fixed 32.184 seconds ahead of TAI. Barycentric Dynamical Time, TDB, is used for motion around the solar system. The two differ by only a tiny, regular wobble of about two thousandths of a second.'),
        ('The Julian Date',
         'The Julian Date is a count of days since a starting point long ago, at noon on 1 January 4713 BC in the old Julian calendar. Its fractions give the time of day. Because it is one plain number, it makes subtracting two dates simple.'),
        ('Why a navigator cares',
         'A position is only correct for the moment it describes. If the time scale is wrong by a few seconds, a fast body can be many kilometres from where the table says. Navigators state the time scale with every number they quote.'),
        ('A common mistake',
         'Mixing up UTC and TT is an easy error. A log written in UTC and a table written in TT differ by a known amount, so the difference must be applied before the two are compared. Always check the scale before you trust a sum.'),
    ],
    "test": [
        ('Why do astronomers use more than one clock?',
         [('a', 'Because clocks break easily'), ('b', 'Because the Sun needs its own clock'), ('c', 'Because the turning Earth is uneven, and each scale suits a different job'), ('d', 'Because a clock must be wound up')], 'c'),
        ('What does UTC add to TAI so that it stays close to the turning of the Earth?',
         [('a', 'Leap seconds'), ('b', 'Extra days'), ('c', 'Degrees of longitude'), ('d', 'Light years')], 'a'),
        ('What is the Julian Date?',
         [('a', 'The date of a Julian festival'), ('b', 'A season of the year'), ('c', 'A type of star'), ('d', 'A count of days since a starting point long ago, with fractions for the time of day')], 'd'),
        ('Terrestrial Time sits a fixed amount ahead of TAI. What is that amount?',
         [('a', 'About 32 days'), ('b', 'About 32.184 seconds'), ('c', 'About 32 hours'), ('d', 'Exactly zero')], 'b'),
        ('Why does a navigator state the time scale with every number?',
         [('a', 'Because the scale changes the colour of the chart'), ('b', 'Because the Starship requires it for the bar'), ('c', 'Because a position is only correct for the time scale it was given in'), ('d', 'Because it makes the number longer')], 'c'),
    ],
}
