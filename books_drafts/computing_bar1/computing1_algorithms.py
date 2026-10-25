"""Algorithms: step-by-step instructions, sorting and searching, and why the order of steps matters."""
CODE = 'computing1_algorithms'
BOOK = {
    "title": 'Algorithms',
    "subtitle": 'Step-by-step instructions, sorting, searching and why order matters',
    "chapters": [
        ('A recipe for a computer',
         'An algorithm is a clear list of steps that solves a problem, and that works every time it is followed. A recipe is an algorithm, and so is a set of directions. A computer can only follow an algorithm exactly as it is written.'),
        ('Steps must be exact',
         'Each step has to be simple enough to do without guessing. "Find the biggest number" is not yet a good step; "look at each number in turn, and keep the largest one you have seen so far" is. A good algorithm also always reaches an end.'),
        ('Searching',
         'Suppose you need one name in a list of ten thousand. Checking each name from the top, one at a time, is called a linear search. It always works, but in the worst case it can take ten thousand checks.'),
        ('Halving the list',
         'If the list is sorted, you can check the middle name first. If it is the one you want, stop. If the name you want comes before the middle, throw away the second half and repeat on the first. This is binary search, and it needs only about 14 checks for ten thousand names.'),
        ('Sorting',
         'Sorting puts items in order, such as a list of prices from lowest to highest. A simple method called bubble sort swaps neighbours that are out of order and repeats until nothing moves. Smarter methods handle very large lists far faster.'),
        ('Why order matters',
         'Binary search only works on a sorted list, and on an unsorted one it can give the wrong answer. The order of steps changes results in general: taking a 10% discount before adding tax is not the same as adding tax first.'),
    ],
    "test": [
        ('What is an algorithm?',
         [('a', 'A kind of computer part'), ('b', 'A type of screen'), ('c', 'A clear list of steps for solving a problem'), ('d', 'A unit of memory')], 'c'),
        ('A linear search checks a list of 1,000 names one at a time. What is the most checks it might need?',
         [('a', 'All 1,000'), ('b', 'About 10'), ('c', 'About 500'), ('d', 'Just 1')], 'a'),
        ('Why does binary search need the list to be sorted first?',
         [('a', 'So the computer can count the names'), ('b', 'So the computer has enough memory'), ('c', 'Because sorted lists are shorter'), ('d', 'Because it compares with the middle item to decide which half to throw away, and that only works in order')], 'd'),
        ('About how many checks does binary search need for a sorted list of 10,000 names?',
         [('a', '10,000'), ('b', 'About 14'), ('c', 'About 100'), ('d', 'About 2')], 'b'),
        ('Which simple sorting method swaps neighbouring items that are out of order until nothing moves?',
         [('a', 'Bubble sort'), ('b', 'Binary search'), ('c', 'Truth tables'), ('d', 'Linear search')], 'a'),
    ],
}
