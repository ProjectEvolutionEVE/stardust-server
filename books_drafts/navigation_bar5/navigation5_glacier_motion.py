"""Glacier Motion Measurement: how ice speed and direction are measured, and why they matter."""
CODE = 'navigation5_glacier_motion'
BOOK = {
    "title": 'Glacier Motion Measurement',
    "subtitle": 'Ice speed, flow, GNSS, radar tracking and mass loss',
    "chapters": [
        ('What a glacier is',
         'A glacier is a large body of ice that builds up over many years from snow that does not fully melt. It flows downhill under its own weight. Glaciers hold a large share of the fresh water on Earth.'),
        ('How ice moves',
         'Ice deforms slowly under its own weight. Many glaciers also slide over the bedrock beneath them, especially where meltwater reaches the base. Speeds vary widely, from a few centimetres a year to several kilometres a year on the fastest outlet glaciers.'),
        ('Measuring position with GNSS',
         'GNSS receivers set on the ice record their position many times a day. Comparing positions over months shows how fast the ice moves and in which direction. The receiver sits on the moving ice, so its own motion must be separated from the signal.'),
        ('Tracking features in satellite radar',
         'Synthetic aperture radar (SAR) satellites image the same glacier on different passes. Matching patterns between the two images, called offset tracking, gives how far each part of the ice has moved. This covers a whole glacier, not just single points.'),
        ('Mass balance and loss',
         'Mass balance is the gain from snowfall minus the loss from melting and from ice breaking off at the edge. A negative balance means a glacier is shrinking. Gravity satellites such as GRACE tracked changes in ice mass over large regions from 2002 to 2017.'),
        ('Why it matters',
         'Measuring glacier motion helps scientists estimate future sea level, plan water supply in mountain regions and warn of hazards. Each method has limits, so researchers combine several of them.'),
    ],
    "test": [
        ('What mainly makes a glacier move?',
         [('a', 'Wind blowing across the surface'), ('b', 'Ice deforming under its own weight, sometimes sliding over bedrock'), ('c', 'Ocean tides pulling it'), ('d', 'Sunlight melting it from below')], 'b'),
        ('What does GNSS measure on a glacier?',
         [('a', 'The temperature of the ice'), ('b', 'The thickness of the snow'), ('c', 'The colour of the ice'), ('d', 'The position of a receiver over time')], 'd'),
        ('What does offset tracking compare?',
         [('a', 'Sound waves from the ice'), ('b', 'Air temperature records'), ('c', 'Two radar images of the same ice taken at different times'), ('d', 'Samples of sea water')], 'c'),
        ('Mass balance is the gain from snowfall minus what?',
         [('a', 'The loss from melting and from ice breaking off'), ('b', 'The depth of the bedrock'), ('c', 'The speed of the wind'), ('d', 'The amount of sunlight')], 'a'),
        ('What is GRACE?',
         [('a', 'A type of glacier'), ('b', 'A pair of gravity satellites that track changes in ice mass'), ('c', 'A kind of GNSS receiver made of ice'), ('d', 'A radar that measures sea depth')], 'b'),
    ],
}
