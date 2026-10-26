"""Charting Moving Bodies: plotting where a planet will be, and why it seems to loop back on itself in the sky."""
CODE = 'navigation3a_charting_movers'
BOOK = {
    "title": 'Charting Moving Bodies',
    "subtitle": 'Plotting planets over time, and reading the loops they make',
    "chapters": [
        ('A chart that moves',
         'A planet on a chart is a point that moves. To chart it, you take its position at several moments and join them up. The line that results is its track. A good chart shows the track with the dates marked along it.'),
        ('Plotting from an ephemeris',
         'Take the positions from an ephemeris, one for each chosen date, and mark them in the same frame. Use a steady time step, such as a week, so that the spacing on the chart shows the speed. Close spacing means slow, wide spacing means fast.'),
        ('Why planets loop',
         "Seen from Earth, an outer planet sometimes seems to slow, turn back for a while, and then continue. This is retrograde motion. Earth, moving faster on its shorter inner orbit, overtakes the outer planet, and the planet's apparent path bends back."),
        ('Charting relative motion',
         "Sometimes the useful chart is not the planet's track in space but its track as seen from your craft. Subtract your own position from the planet's, and the result shows how the planet appears to move from where you are."),
        ('Keep the scale and the frame',
         'A moving chart is only useful if its scale and frame are stated. Note the scale, the frame, the time step and the epoch on every sheet. A reader who finds the sheet years later can then use it safely.'),
        ('Update with new data',
         'A track drawn from old data can drift from the real orbit. Compare each new sighting or tracking fix with the chart, and redraw the track when they disagree. A chart is a working tool, not a finished picture.'),
    ],
    "test": [
        ('What is a track on a chart?',
         [('a', 'The engine trail of a ship'), ('b', 'A list of stars'), ('c', "A line joining a body's positions at several moments"), ('d', 'A ring of debris')], 'c'),
        ('What does wide spacing between marked positions on a moving chart show?',
         [('a', 'The body is fast'), ('b', 'The body is slow'), ('c', 'The chart is damaged'), ('d', 'The body is not moving')], 'a'),
        ('What is retrograde motion?',
         [('a', 'A planet sinking into the Sun'), ('b', 'A ship flying in reverse'), ('c', 'A planet turning to face the Moon'), ('d', "A planet's apparent backward loop in the sky, seen from Earth")], 'd'),
        ('Why does an outer planet appear to loop back?',
         [('a', 'Because it has no gravity'), ('b', 'Because Earth on its faster, inner orbit overtakes it'), ('c', 'Because it is made of gas'), ('d', 'Because the Sun pushes it back')], 'b'),
        ('What must every moving chart state?',
         [('a', 'The name of the artist'), ('b', 'The price of the paper'), ('c', 'The scale, the frame, the time step and the epoch'), ('d', 'The number of crew aboard')], 'c'),
    ],
}
