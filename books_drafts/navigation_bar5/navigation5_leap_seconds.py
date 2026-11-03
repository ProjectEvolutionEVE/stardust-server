"""Leap Seconds and Their History: the slowing of the Earth, announcing a leap, software failures, the proposal to stop them, the effects and the future."""
CODE = 'navigation5_leap_seconds'
BOOK = {
    "title": 'Leap Seconds and Their History',
    "subtitle": 'Why a clock sometimes has to wait one extra second',
    "chapters": [
        ('The Earth slows down',
         'The rotation of the Earth is not perfectly steady. The pull of the Moon slows it over time, and winds, ocean currents and the core make the length of the day change a little. Time based on atoms does not change this way, so the two drift apart.'),
        ('Announcing a leap',
         'When the rotation of the Earth falls too far behind atomic time, a leap second is added. Leap seconds are usually added at the end of June or December. The International Earth Rotation and Reference Systems Service announces them months in advance.'),
        ('Software failures',
         'Computers count time as a steady run of seconds. A minute that has 61 seconds can confuse software that expects 60. Some systems have crashed or stalled when a leap second arrived.'),
        ('The proposal to stop them',
         'Many engineers want to stop adding leap seconds, because they cause errors in computer systems. Others want to keep civil time tied to the position of the Sun. The debate has run for many years.'),
        ('The effects',
         'A leap second is small, but power grids, telephone networks, banks and satellites all depend on exact time. Well-designed systems handle a leap second smoothly, by stretching a second slightly rather than inserting a jump.'),
        ('The future',
         'In 2022 the international conference on weights and measures agreed to stop adding leap seconds by about 2035. It also asked for a decision later on how civil time should be kept after that.'),
    ],
    "test": [
        ('Why are leap seconds added?',
         [('a', 'Because the rotation of the Earth is not perfectly steady and drifts away from atomic time'), ('b', 'Because clocks run out of power'), ('c', 'To make the year longer'), ('d', 'To pay the engineers who build clocks')], 'a'),
        ('Who announces a leap second?',
         [('a', 'A telephone company'), ('b', 'A single computer'), ('c', 'The International Earth Rotation and Reference Systems Service'), ('d', 'The Moon itself')], 'c'),
        ('What problem can leap seconds cause in computers?',
         [('a', 'They make computers run faster'), ('b', 'They make computers colder'), ('c', 'Software that assumes every minute has 60 seconds can fail'), ('d', 'They erase files from disks')], 'c'),
        ('What did the 2022 conference agree?',
         [('a', 'To add two leap seconds every year'), ('b', 'To stop adding leap seconds by about 2035'), ('c', 'To move civil time to Mars'), ('d', 'To remove all clocks from the world')], 'b'),
        ('Why do power grids and banks care about leap seconds?',
         [('a', 'They sell leap seconds'), ('b', 'They run on sunlight'), ('c', 'They have no clocks at all'), ('d', 'They depend on exact time, so a leap second must be handled smoothly')], 'd'),
    ],
}
