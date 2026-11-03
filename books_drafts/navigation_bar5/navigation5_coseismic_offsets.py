"""Coseismic Offsets in Geodetic Networks: earthquake jumps, estimating offsets, post-seismic creep, updating the network, GNSS detection and public records."""
CODE = 'navigation5_coseismic_offsets'
BOOK = {
    "title": 'Coseismic Offsets in Geodetic Networks',
    "subtitle": 'When an earthquake moves the ground, and the survey network has to be updated',
    "chapters": [
        ('Earthquake jumps',
         'When an earthquake happens, the ground on each side of a fault can move suddenly. Survey stations near the fault can jump by centimetres or more in a single event.'),
        ('Estimating offsets',
         'Scientists estimate the size of these offsets by comparing station positions before and after the event. Good models separate the sudden jump from normal motion.'),
        ('Post-seismic creep',
         'After an earthquake the ground may keep moving slowly for months or years. This slow motion, called post-seismic creep, must be modelled as well.'),
        ('Updating the network',
         'Survey networks must be updated so that their coordinates match the new positions of the ground. Otherwise maps and boundaries fall out of step with reality.'),
        ('GNSS detection',
         'GNSS stations can detect the offsets of an earthquake quickly and automatically. This helps agencies respond to the event.'),
        ('Public records',
         'Changed coordinates are often recorded in public records, such as land records, so that boundaries and maps remain correct after the event.'),
    ],
    "test": [
        ('What is a coseismic offset?',
         [('a', 'A kind of mountain'), ('b', 'A type of rock'), ('c', 'A sudden shift of the ground during an earthquake'), ('d', 'A spelling error in a survey')], 'c'),
        ('How are offsets estimated?',
         [('a', 'By guessing'), ('b', 'By counting birds on the site'), ('c', 'By the colour of the soil'), ('d', 'By comparing station positions before and after the event')], 'd'),
        ('What is post-seismic creep?',
         [('a', 'Slow ground motion that continues after an earthquake'), ('b', 'A quick shake during the quake'), ('c', 'A type of tree'), ('d', 'A heavy rain storm')], 'a'),
        ('Why must survey networks be updated after an earthquake?',
         [('a', 'To change the colour of maps'), ('b', 'So that coordinates match the new positions'), ('c', 'To stop earthquakes from happening'), ('d', 'To lower the sea level')], 'b'),
        ('Why do changed coordinates matter in public records?',
         [('a', 'They are decoration'), ('b', 'They set the time of the Sun'), ('c', 'Boundaries and maps must stay correct'), ('d', 'They stop the rain')], 'c'),
    ],
}
