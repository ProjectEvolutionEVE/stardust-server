"""The Theory of Constraints: Goldratt's The Goal, the bottleneck, five focusing steps, drum-buffer-rope, throughput, and a worked example."""
CODE = 'business4_toc'
BOOK = {
    "title": 'The Theory of Constraints',
    "subtitle": 'Finding the one step that limits the whole flow, and working on it first',
    "chapters": [
        ("Goldratt's The Goal",
         'Eliyahu Goldratt told the story of a struggling factory in his 1984 novel The Goal. Its manager learns that the real problem is not every machine, but the one that holds back the rest. The book made the Theory of Constraints widely known.'),
        ('The bottleneck',
         'A bottleneck, or constraint, is the step with the least capacity in a chain of steps. It limits how much the whole system can produce. Working hard at other steps that are not the bottleneck adds stock, not output.'),
        ('Five focusing steps',
         'Goldratt set out five steps: identify the constraint, decide how to exploit it, subordinate everything else to it, raise its capacity if needed, and then repeat the search, since a new constraint will appear. The steps give a clear order for action.'),
        ('Drum, buffer, rope',
         'The bottleneck sets the beat, the drum. A small buffer of work is kept in front of it so it never runs dry. A rope ties the release of materials at the start of the line to the pace of the bottleneck, so stock does not pile up.'),
        ('Throughput',
         'Goldratt measured success by throughput, the rate at which the system earns money through sales, along with inventory and operating expense. Improving throughput at the constraint raises profit directly, while local savings elsewhere may not.'),
        ('An example',
         'Suppose a line has three steps that can handle 40, 25 and 60 units an hour. The middle step limits output to 25. Adding speed to the first or last step adds nothing to sales. Adding capacity to the middle step, the constraint, raises the output of the whole line.'),
    ],
    "test": [
        ("In which year was Goldratt's novel The Goal published?",
         [('a', '1964'), ('b', '1984'), ('c', '2004'), ('d', '1914')], 'b'),
        ('What is a bottleneck?',
         [('a', 'A fast step that never needs to be used'), ('b', 'A kind of bank account'), ('c', 'The step with the least capacity that limits the whole system'), ('d', 'A type of tax')], 'c'),
        ('In the drum-buffer-rope idea, what is the drum?',
         [('a', 'The shipping crate'), ('b', 'The office computer'), ('c', 'The company logo'), ('d', 'The bottleneck, which sets the pace')], 'd'),
        ('How did Goldratt measure success?',
         [('a', 'By throughput, the rate at which the system earns money'), ('b', 'By the number of meetings held'), ('c', 'By the size of the car park'), ('d', 'By the length of the staff lunch')], 'a'),
        ('In the three-step example, what limits output to 25 units an hour?',
         [('a', 'The first step'), ('b', 'The middle step'), ('c', 'The last step'), ('d', 'The cleaners')], 'b'),
    ],
}
