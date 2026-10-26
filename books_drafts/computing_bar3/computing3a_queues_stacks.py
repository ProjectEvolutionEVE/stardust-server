"""Queues and stacks: first in, first out, and last in, first out, two simple orders for waiting things."""
CODE = 'computing3a_queues_stacks'
BOOK = {
    "title": 'Queues and Stacks',
    "subtitle": 'First in, first out, and last in, first out: two simple orders for waiting things',
    "chapters": [
        ('Two orders',
         'A queue and a stack both hold items that are waiting, but they take things out in opposite orders. A queue is first in, first out. A stack is last in, first out. Choosing the right one is often the most important decision in a small program.'),
        ('The queue',
         'A queue works like a checkout line. New items join at the back, and the next item comes from the front. A print queue sends pages in the order they were sent. In the game, blueprint copies go up for auction one at a time, in serial order, which is also a queue.'),
        ('The stack',
         'A stack works like a pile of plates. You add to the top and take from the top, so the last thing added is the first thing removed. An undo button often works this way: each action is pushed onto a stack, and undo pops off the most recent one.'),
        ('The call stack',
         'When a program calls a function, the computer keeps a record of where to return to, and it keeps these records on a stack, called the call stack. When the function finishes, its record is popped and the program carries on where it left off. Very deep recursion can use up the room for these records.'),
        ('Waiting too long',
         'When requests arrive faster than they can be handled, a queue holds the extra ones. A real queue has a size limit, so it can fill up. A full queue must turn new items away or make them wait, and a good design says clearly which one happens.'),
        ('Using them together',
         'A search that wants the nearest answer first uses a queue, as breadth-first search does. A search that goes as deep as it can along one path before turning back can use a stack. The order you choose decides what you find first.'),
    ],
    "test": [
        ('In a queue, which item leaves first?',
         [('a', 'The one added last'), ('b', 'The one added first'), ('c', 'The biggest one'), ('d', 'A random one')], 'b'),
        ('In a stack, which item leaves first?',
         [('a', 'The one at the bottom'), ('b', 'The one added first'), ('c', 'The one added last'), ('d', 'The one with the smallest number')], 'c'),
        ('How does an undo button usually use a stack?',
         [('a', 'Each action is pushed on, and undo pops the most recent one'), ('b', 'All actions are sorted by size'), ('c', 'The whole game is copied after each action'), ('d', 'The first action is removed')], 'a'),
        ('Why does the call stack matter for very deep recursion?',
         [('a', 'Recursion never uses memory'), ('b', 'Every call runs at the same time'), ('c', 'It removes the need for a base case'), ('d', 'Each call adds a record, and a very deep chain can use up the room for them')], 'd'),
        ('Which order does a search need if it must find the nearest answer first?',
         [('a', 'A stack, last in first out'), ('b', 'A queue, first in first out'), ('c', 'A random order'), ('d', 'The biggest weight first')], 'b'),
    ],
}
