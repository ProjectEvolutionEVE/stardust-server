"""GRACE Gravimetry: twin satellites, the inter-satellite range, gravity changes, ice and water mass, monthly gravity fields and resolution."""
CODE = 'navigation5_grace_gravity'
BOOK = {
    "title": 'GRACE Gravimetry',
    "subtitle": 'Two satellites that weighed the ice sheets and the groundwater from orbit',
    "chapters": [
        ('Twin satellites',
         'The GRACE mission used two satellites that flew in the same orbit, one behind the other, about 200 kilometres apart. The pair acted as one instrument for measuring gravity.'),
        ('The inter-satellite range',
         'The distance between the two craft changed as they passed over areas of different gravity. Those changes were measured with microwave ranging, with very fine precision.'),
        ('Gravity changes',
         'Changes in gravity reflect how mass moves. When ice melts or water shifts from one region to another, the gravity field changes as well.'),
        ('Ice and water mass',
         'GRACE measured the loss of ice from Greenland and Antarctica, and changes in groundwater. Those results showed mass leaving the ice sheets and water moving between regions.'),
        ('Monthly fields',
         'GRACE produced a new gravity map about once a month. The series of maps showed how mass moved over the years.'),
        ('Resolution',
         'The maps had good resolution at large scales, showing features hundreds of kilometres across. Finer detail requires newer and closer measurements.'),
    ],
    "test": [
        ('What did GRACE use?',
         [('a', 'One very large telescope'), ('b', 'A single ship at sea'), ('c', 'A camera on the ground'), ('d', 'Two satellites following each other')], 'd'),
        ('What did the twin satellites measure?',
         [('a', 'The colour of ice'), ('b', 'The taste of water'), ('c', 'Changes in the distance between them'), ('d', 'The temperature of the Sun')], 'c'),
        ('What do gravity changes reflect?',
         [('a', 'How mass moves'), ('b', 'How loud the wind is'), ('c', 'How many birds there are'), ('d', 'The colour of the sky')], 'a'),
        ('What did GRACE track?',
         [('a', 'Plant growth in forests'), ('b', 'Ice loss and changes in groundwater'), ('c', 'The colour of the ocean'), ('d', 'Traffic on roads')], 'b'),
        ('How often did GRACE produce a new gravity map?',
         [('a', 'Every hundred years'), ('b', 'Once a day at noon'), ('c', 'About once a month'), ('d', 'Only once, at launch')], 'c'),
    ],
}
