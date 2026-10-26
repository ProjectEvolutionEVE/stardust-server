"""Matching a Pump to Its System: pump curves, system curves and the point where they cross."""
CODE = 'engineering3c_pump_matching'
BOOK = {
    "title": 'Matching a Pump to Its System',
    "subtitle": 'Pump curves, system curves and the point where they cross',
    "chapters": [
        ("The pump's curve",
         "Every pump has a curve. The more it must push against, the less fluid it moves. Read the curve as head, the height or pressure a pump can add, against flow. A pump chosen from a catalogue still runs at a point set by the pipes it is joined to."),
        ("The system's curve",
         "A pipe system has a curve of its own. The more fluid you push through it, the more friction it makes, so the pressure needed rises with the flow, roughly with the square of the flow. Long pipes, narrow pipes, bends and valves all make this curve steeper."),
        ('The operating point',
         "The pump runs where its curve crosses the system's curve. That crossing is the only flow you will actually get. Change the pipes or the valve setting and the crossing moves, so the flow moves with it."),
        ('Pumps side by side',
         "Two identical pumps in parallel roughly double the flow at the same pressure, as long as the system does not become much more restrictive. Two pumps in series add pressure at the same flow. Pick the arrangement from the system curve, not from the headline numbers on the pump."),
        ('Running cost',
         "A pump that is too big for the job wastes energy. Often it has to be throttled with a valve, which burns the extra power as heat. Over the years, the electricity bill can cost more than the pump itself. Size the pump for normal flow and treat full flow as a rare case."),
        ('Checking the match',
         "Measure the real flow and pressure once the system runs, and compare them with the maker's curve. A pump that runs far from its best point wastes energy and wears out early. Write the operating point in the records, so the next engineer knows what the system was built to do."),
    ],
    "test": [
        ("Where is a pump's operating point?",
         [('a', 'On the price label'), ('b', "Where the pump's curve crosses the system's curve"), ('c', 'At the very top of the pump curve, always'), ('d', 'At the end of the longest pipe')], 'b'),
        ('As the flow through a pipe system rises, what happens to the pressure the system needs?',
         [('a', 'It falls to zero'), ('b', 'It stays exactly the same'), ('c', 'It rises by the same amount each time'), ('d', 'It rises, roughly with the square of the flow')], 'd'),
        ('What does putting two identical pumps in parallel mainly give you?',
         [('a', 'Roughly double the flow at the same pressure, if the system allows it'), ('b', 'Double the pressure at the same flow'), ('c', 'Half the flow'), ('d', 'No change at all')], 'a'),
        ('Why can an oversized pump waste energy?',
         [('a', 'It runs colder'), ('b', 'It has more paint on it'), ('c', 'It is often throttled with a valve, which turns the spare power into heat'), ('d', 'It makes the pipes shorter')], 'c'),
        ('What is the best way to choose a pump size?',
         [('a', 'The biggest one in stock'), ('b', 'Size it for normal flow against the real system curve'), ('c', 'The smallest one you can find'), ('d', 'Whichever one sells most')], 'b'),
    ],
}
