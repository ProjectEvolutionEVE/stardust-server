"""Register Allocation: fitting a program working values into the few fast slots a processor has."""
CODE = 'computing5_register_allocation'
BOOK = {
    "title": 'Register Allocation',
    "subtitle": 'Fitting a program working values into the few fast slots a processor has',
    "chapters": [
        ('Few fast slots', 'A processor has a small number of registers, the fastest places to keep numbers while it works. A program may use far more values than that, so the compiler must choose which values live in registers and which wait in slower memory.'),
        ('Live ranges', 'A value is live from the time it is made until it is last used. Two values whose live ranges overlap cannot share a register at the same moment. Finding these ranges is the first step of the job.'),
        ('Graph colouring', 'Classic allocators draw a graph in which each value is a point and overlapping values are joined. Colouring the points with as many colours as there are registers, so that no joined pair shares a colour, gives a valid allocation. Gregory Chaitin made this approach practical in the early 1980s.'),
        ('Spilling', 'When there are too many values, some must be spilled, which means stored in memory and loaded when needed. Choosing which to spill is a trade-off, since spilled values slow the program. Good choices keep the busiest values in registers.'),
        ('Linear scan', 'Linear scan is a faster method that walks through the program once, handing out registers as values start and taking them back as values end. It gives good results quickly, which matters for compilers that must work fast.'),
        ('The quality of the code', 'The quality of register allocation shapes how fast the final program runs. Poor choices cause many slow memory accesses, while good ones let the processor work at full speed. It is one place where a compiler cleverness shows up in everyday software.'),
    ],
    "test": [
        ('What are registers?',
         [('a', 'The fastest small storage places inside a processor'), ('b', 'Printers'), ('c', 'Holiday calendars'), ('d', 'Sound cards')], 'a'),
        ('When does a value live range end?',
         [('a', 'When it is first made'), ('b', 'At midnight'), ('c', 'When it is last used'), ('d', 'When the screen goes off')], 'c'),
        ('In graph colouring, what must joined values avoid?',
         [('a', 'Being spilled'), ('b', 'Sharing the same colour, which means the same register'), ('c', 'Being printed'), ('d', 'Being shown on screen')], 'b'),
        ('What does spilling mean?',
         [('a', 'Spilling coffee on a keyboard'), ('b', 'Deleting all values'), ('c', 'Printing a report'), ('d', 'Storing a value in memory when registers run out')], 'd'),
        ('What is a benefit of linear scan?',
         [('a', 'It is slow but perfect'), ('b', 'It gives good results quickly'), ('c', 'It needs no processor'), ('d', 'It removes the need for memory')], 'b'),
    ],
}
