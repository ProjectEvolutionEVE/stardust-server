"""Tolerance stack-up in production: how small errors in several parts add up along a chain, and how to plan for the total."""
CODE = 'engineering3b_tolerance_stack'
BOOK = {
    "title": 'Tolerance Stack-Up in Production',
    "subtitle": 'How small errors in several parts add up along a chain, and how to plan for the total',
    "chapters": [
        ('Parts meet other parts',
         'No two parts come out exactly the same size. Each one has a tolerance, a band of sizes it may fall within. When parts are fitted together in a chain, each small variation adds to the one before, and the total gap can drift a long way from the drawing.'),
        ('Adding up the chain',
         'A stack-up is the total of the tolerances along one path through an assembly. Write down each part\'s size and tolerance, then follow the chain from one end to the other. The sum of those tolerances is the stack-up, and it tells you the range of the final gap.'),
        ('Worst case',
         'The worst-case stack-up adds every tolerance in the most unfavourable direction at once. Three parts, each allowed to be 0.1 millimetres out, can together be 0.3 millimetres out. It is the safe choice, but it can force very tight and costly parts.'),
        ('Statistical stack-up',
         'Real parts rarely all sit at their limits together. If the variations are random and independent, the total is usually smaller, and it can be estimated by taking the square root of the sum of the squares of the tolerances. For the same three parts, that gives about 0.17 millimetres.'),
        ('Tighten the right part',
         'Tightening the tolerance of every part costs money. Instead, find the part that drives the total most and tighten only that one. An adjustment, such as a shim or a slotted hole, can take up what is left over.'),
        ('Measure the real parts',
         'A drawing states the plan, but measured parts show the truth. Record the sizes of a batch of parts and check the fit on real assemblies. A stack-up on paper and a check on the bench should agree, and where they do not, look for the cause.'),
    ],
    "test": [
        ('What is a tolerance?',
         [('a', 'The colour of a part'), ('b', 'The band of sizes allowed around the drawn size'), ('c', 'The weight of a part'), ('d', 'The price per kilogram')], 'b'),
        ('What is a stack-up?',
         [('a', 'The total of the tolerances along one path through an assembly'), ('b', 'A pile of finished parts'), ('c', 'A type of weld'), ('d', 'A list of suppliers')], 'a'),
        ('Three parts are each allowed to be 0.1 millimetres out. What is the worst-case total?',
         [('a', '0.1 millimetres'), ('b', '0.01 millimetres'), ('c', '0.03 millimetres'), ('d', '0.3 millimetres')], 'd'),
        ('What does a statistical stack-up assume?',
         [('a', 'Every part is at its worst limit'), ('b', 'Parts are checked only by weight'), ('c', 'The variations are random and independent'), ('d', 'Tolerances are always zero')], 'c'),
        ('What is often the best way to cut cost when a stack-up is too large?',
         [('a', 'Tighten only the part that drives the total most'), ('b', 'Tighten every part by the same amount'), ('c', 'Ignore the drawing'), ('d', 'Use the largest tolerance for every part')], 'a'),
    ],
}
