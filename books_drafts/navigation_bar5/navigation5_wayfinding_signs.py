"""Signage and Wayfinding Design: how signs are placed, written and tested so that people can find their way through a building or a place."""
CODE = 'navigation5_wayfinding_signs'
BOOK = {
    "title": 'Signage and Wayfinding Design',
    "subtitle": 'Sign placement, decisions, typography, testing, accessibility and standards',
    "chapters": [
        ('What wayfinding is',
         'Wayfinding is how people find their way from one place to another. Signs are one of the main tools, along with layout, lighting and maps. Good wayfinding means a visitor rarely needs to ask for help.'),
        ('Placing signs',
         'Signs should appear where a person must make a decision, such as at a junction or a lift lobby. A sign placed too late gives people no time to act. Repeating signs at key points builds confidence.'),
        ('Decision points',
         'At each decision, the sign should name the choices clearly, with arrows and destinations in a logical order. Too many choices on one sign slow people down.'),
        ('Typography',
         'Letters should be large enough to read at the distance where a person needs them. Clear sans-serif type with good contrast works well. Short words and simple layouts are easier to read at a glance.'),
        ('Testing',
         'Signs should be tested with real people before they are fixed in place. Watching someone try to find a room shows problems that a designer may miss. Testing is quick and inexpensive compared with replacing signs.'),
        ('Accessibility and standards',
         'Signs must be usable by people with low vision, colour blindness and other needs. Standards set minimum sizes, contrast and tactile features. Following them makes a building open to more people.'),
    ],
    "test": [
        ('What is wayfinding?',
         [('a', 'A type of paint'), ('b', 'A kind of door lock'), ('c', 'How people find their way from one place to another'), ('d', 'A brand of coffee')], 'c'),
        ('Where should a sign appear?',
         [('a', 'On the floor'), ('b', 'Where a person must make a decision, such as a junction'), ('c', 'Inside a closed cupboard'), ('d', 'Only at the exit')], 'b'),
        ('Why is too many choices on one sign a problem?',
         [('a', 'It slows people down'), ('b', 'It makes the sign lighter'), ('c', 'It makes the sign cheaper'), ('d', 'It changes the weather')], 'a'),
        ('Why should signs be tested with real people?',
         [('a', 'Because testing makes signs bigger'), ('b', 'Because testing is never needed'), ('c', 'Because testing changes the language'), ('d', 'Because testing shows problems the designer may miss')], 'd'),
        ('What do accessibility standards cover for signs?',
         [('a', 'Minimum sizes, contrast and tactile features'), ('b', 'The colour of the building'), ('c', 'The price of the sign'), ('d', 'The number of windows')], 'a'),
    ],
}
