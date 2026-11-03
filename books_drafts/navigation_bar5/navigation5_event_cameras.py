"""Event Cameras for Navigation: sensors that report changes in light as they happen, pixel by pixel."""
CODE = 'navigation5_event_cameras'
BOOK = {
    "title": 'Event Cameras for Navigation',
    "subtitle": 'Asynchronous pixels, speed, high dynamic range, processing, data and limits',
    "chapters": [
        ('Asynchronous pixels',
         'An event camera does not take whole frames on a fixed clock. Each pixel reports on its own when its brightness changes. The result is a stream of events rather than pictures.'),
        ('Speed',
         'Because each pixel reports as soon as it changes, the camera responds very quickly. Fast motion is recorded without the blur of a long exposure. This suits fast vehicles and drones.'),
        ('High dynamic range',
         'Event cameras can handle scenes with very bright and very dark areas at the same time. A normal camera may lose detail in one or the other. The event camera keeps both.'),
        ('Processing',
         'Processing events needs methods built for asynchronous data. Standard image tools do not fit the stream well. Researchers are building new methods to turn events into position estimates.'),
        ('Data',
         'The data is sparse, since a still scene produces few events. The output is much smaller than full video. Storing and sending the events is simpler in many cases.'),
        ('Limits',
         'A still scene gives few events, so the camera can struggle to see stationary objects. The processing methods are still young. Event cameras work best combined with other sensors.'),
    ],
    "test": [
        ('What do event cameras report?',
         [('a', 'Full frames only'), ('b', 'Sound'), ('c', 'Temperature'), ('d', 'Changes in brightness at each pixel, as they happen')], 'd'),
        ('Why are event cameras fast?',
         [('a', 'Each pixel reports on its own as soon as it changes'), ('b', 'They wait for a frame'), ('c', 'They use film'), ('d', 'They need extra light')], 'a'),
        ('What is high dynamic range?',
         [('a', 'A loud sound'), ('b', 'Fast driving'), ('c', 'The ability to see both very bright and very dark areas'), ('d', 'A heavy camera')], 'c'),
        ('What is a limit of event cameras?',
         [('a', 'They see still objects well'), ('b', 'A still scene gives few events, and new processing methods are needed'), ('c', 'They are too cheap'), ('d', 'They use no power')], 'b'),
        ('What kind of data do they produce?',
         [('a', 'A stream of events'), ('b', 'A single photograph'), ('c', 'A written report'), ('d', 'A map of towns')], 'a'),
    ],
}
