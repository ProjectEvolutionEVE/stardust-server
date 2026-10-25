"""What a Computer Does: input, processing, memory, storage and output, the loop every computer runs."""
CODE = 'computing1_computer'
BOOK = {
    "title": 'What a Computer Does',
    "subtitle": 'Input, processing, memory, storage and output',
    "chapters": [
        ('A machine that follows steps',
         'A computer takes in information, works on it and gives back a result. It does this by following instructions called a program. Everything you do on a computer, from a game to a spreadsheet, is this same loop.'),
        ('Input',
         'Input is how information gets in: a keyboard, a mouse, a touchscreen, a microphone or a sensor. A scanner reading the sky is input too. Input only brings the data in; it does not do the thinking.'),
        ('Processing',
         'The processor, also called the CPU, is the part that does the work. It carries out simple operations such as adding two numbers, comparing two values and moving data from one place to another. A modern chip can do billions of these every second.'),
        ('Memory',
         'Memory, usually called RAM, holds the data and the program the processor is using right now. It is very fast, but it is cleared when the power goes off. Think of it as the desk you are working at, not the filing cabinet.'),
        ('Storage',
         'Storage keeps information even when the power is off. A hard drive, a solid-state drive or a memory card are all storage. It is slower than memory, but it holds far more, and saved files live there.'),
        ('Output',
         'Output is how results get out: a screen, a speaker or a printer. The whole cycle is input, processing with memory and storage, then output, and a modern computer can run it many times in a fraction of a second.'),
    ],
    "test": [
        ('Which part of a computer does the actual calculating and carries out the program\'s instructions?',
         [('a', 'The processor, or CPU'), ('b', 'The mouse'), ('c', 'The speaker'), ('d', 'The power cable')], 'a'),
        ('What happens to data that is held only in memory (RAM) when the power is switched off?',
         [('a', 'It is saved to storage automatically'), ('b', 'It is printed out'), ('c', 'It is lost, because memory is cleared when the power goes off'), ('d', 'It moves to the output')], 'c'),
        ('Which of these is a form of input rather than output?',
         [('a', 'A printer'), ('b', 'A speaker'), ('c', 'A screen'), ('d', 'A microphone')], 'd'),
        ('A printer and a speaker are both examples of which part of the loop?',
         [('a', 'Input'), ('b', 'Output'), ('c', 'Memory'), ('d', 'Storage')], 'b'),
        ('Why is memory faster than storage, yet not used to keep your files?',
         [('a', 'Memory is bigger than storage'), ('b', 'Memory is made of paper'), ('c', 'Memory is quick to use, but it loses its data when the power is off'), ('d', 'Storage cannot hold anything at all')], 'c'),
    ],
}
