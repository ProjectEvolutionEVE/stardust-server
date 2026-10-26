"""Case Study: Three Mile Island. A stuck valve, a misleading light, operator action, the response, the Kemeny report and the changes."""
CODE = 'flight5_three_mile'
BOOK = {
    "title": 'Case Study: Three Mile Island',
    "subtitle": 'A stuck valve, a misleading reading and the lessons for control rooms',
    "chapters": [
        ('A stuck valve',
         'On 28 March 1979 a relief valve at the Three Mile Island plant in Pennsylvania stuck open after a small problem in the cooling system. Cooling water drained from the reactor core. The valve should have closed, but it did not.'),
        ('A misleading light',
         'The control room showed a light that meant the valve had been told to close. It did not show that the valve was actually still open. Operators read the light as a sign that the valve was shut, and the picture they had was wrong.'),
        ('Operator action',
         'The operators did not know the valve was open, and they cut back the flow of cooling water. This made the problem worse, and part of the core was left uncovered and overheated. The chain of events was hard to follow in the control room.'),
        ('The response',
         'Over several days the plant was brought under control, and the core was cooled. A partial meltdown had taken place inside the reactor, but the containment building held. Local radiation releases were small, and studies found no clear health effect on the public.'),
        ('The Kemeny report',
         'A commission led by John Kemeny studied the accident and its causes. Its report found that human factors and the design of the control room played large parts in the event. It called for big changes in how plants were run and how people were trained.'),
        ('Changes',
         'Control rooms were redesigned so that the true state of valves and systems is shown clearly. Operators were trained in how to read and test the picture they were given. For players, the lesson is that a display must show what is true, not only what was asked for.'),
    ],
    "test": [
        ('In what year did the accident at Three Mile Island happen?',
         [('a', '1979'), ('b', '1949'), ('c', '1989'), ('d', '2009')], 'a'),
        ('What was stuck open at the start of the problem?',
         [('a', 'A front door'), ('b', 'A relief valve'), ('c', 'A fuel truck'), ('d', 'A window')], 'b'),
        ('What did the misleading light show?',
         [('a', 'That the plant had been turned off'), ('b', 'That the weather was fine'), ('c', 'That the valve had been told to close, not that it had closed'), ('d', 'That the crew was on break')], 'c'),
        ('Who led the commission that studied the accident?',
         [('a', 'Lord Cullen'), ('b', 'Fletcher Christian'), ('c', 'Ferdinand Magellan'), ('d', 'John Kemeny')], 'd'),
        ('What change followed the accident?',
         [('a', 'Control rooms were redesigned to show the true state of systems'), ('b', 'All reactors were closed forever'), ('c', 'Control rooms were removed'), ('d', 'Operators were no longer trained')], 'a'),
    ],
}
