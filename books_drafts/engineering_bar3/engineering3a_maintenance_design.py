"""Designing for Maintenance: laying out a part so that it can be checked, cleaned, adjusted and replaced."""
CODE = 'engineering3a_maintenance_design'
BOOK = {
    "title": 'Designing for Maintenance',
    "subtitle": 'How a part is laid out so it can be checked, cleaned, adjusted and replaced',
    "chapters": [
        ('Machines need looking after',
         'Every machine needs regular attention: checking, cleaning, lubricating and replacing worn parts. A design that makes this hard is a design that gets neglected. Plan for maintenance from the first sketch, not after the parts are built.'),
        ('Reach and access',
         'Put the parts that wear, such as filters, seals and bearings, where a hand and a tool can reach them. Leave room to swing a spanner or lift out a module. Check on paper, or with a cardboard model, that a real tool fits in the space.'),
        ('Standard parts',
         "Use standard fasteners, seals and bearings wherever you can. A standard part is easier to find and replace, while a special one may take a long time to make again. Record each part's size so that a replacement matches exactly."),
        ('Modules you can swap',
         'Build a machine from modules that come off as a whole, such as a pump on a plate or a drive unit on a frame. A broken module can be swapped in one visit, and the repair can be done at a bench later. Label every connection so that it goes back the right way.'),
        ('Service intervals',
         'Write a service schedule with the design: what to check, lubricate or replace, and how often. Base the intervals on the hours run or the cycles counted, not only on the calendar. Keep the schedule with the drawing so the next crew can follow it.'),
        ('Plan the upkeep money',
         "Upkeep costs are part of a design's cost. Set aside a share of each week's running costs for servicing, spares and replacement parts. A part that is cheap to buy but hard to reach can cost more over its life than one that costs more and lasts."),
    ],
    "test": [
        ('Why plan maintenance from the first sketch?',
         [('a', 'Maintenance is never needed'), ('b', 'It makes the drawing bigger'), ('c', 'Hard-to-reach parts are often neglected'), ('d', 'It stops all wear')], 'c'),
        ('What is a good reason to use standard fasteners and bearings?',
         [('a', 'They are painted in the same colour'), ('b', 'They never wear out'), ('c', 'They make the machine heavier'), ('d', 'They can be replaced quickly and matched exactly')], 'd'),
        ('Why label the connections on a module?',
         [('a', 'To make the module shine'), ('b', 'So that parts go back the right way'), ('c', 'To add weight to the frame'), ('d', 'To stop the module from being removed')], 'b'),
        ('What should service intervals be based on?',
         [('a', 'The hours run or the cycles counted, not only the calendar'), ('b', 'The colour of the machine'), ('c', 'The number of people in the crew'), ('d', 'The size of the drawing')], 'a'),
        ('Why can a cheap part cost more over its life?',
         [('a', 'Because it is always the heaviest part'), ('b', 'Because cheap parts cannot be drawn'), ('c', 'Because it has no name'), ('d', 'Because it is hard to reach, so servicing costs more')], 'd'),
    ],
}
