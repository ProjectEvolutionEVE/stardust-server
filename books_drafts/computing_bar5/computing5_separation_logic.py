"""Separation Logic: proofs about memory that track who owns which part of the heap."""
CODE = 'computing5_separation_logic'
BOOK = {
    "title": 'Separation Logic',
    "subtitle": 'Proofs about memory that track who owns which part of the heap',
    "chapters": [
        ('Proofs about memory', 'Programs that use pointers keep data at memory addresses on the heap. Ordinary logic struggles to say what a program does to such memory. Separation logic adds a way to write facts about pieces of memory and to say which pieces are separate.'),
        ('Heap assertions', 'A heap assertion says that a certain address holds a certain value, and that is all it claims. Two assertions can sit side by side only if they describe separate parts of memory. This keeps each claim small and clear.'),
        ('Ownership in proofs', 'A piece of memory that a part of the program owns is written into the proof. Ownership means no other part can change it at the same time. That makes reasoning about each part simpler.'),
        ('The frame rule', 'The frame rule says that if a piece of code is proved to work on a small part of memory, it still works when extra, separate memory is left alone. This lets a proof be reused in bigger programs without redoing the work.'),
        ('Concurrent separation', 'When several threads run, each thread can own its own pieces, and shared pieces are guarded by rules about when they may be touched. This extends separation logic to programs that run in parallel.'),
        ('Tools and pointer programs', 'Research tools such as VeriFast and Iris help check these proofs. The method has been used on programs that manipulate linked lists and trees, where one wrong pointer can crash a system. Writing the proofs is slow, but it gives strong guarantees.'),
    ],
    "test": [
        ('What does a heap assertion describe?',
         [('a', 'A particular address and the value held there'), ('b', 'The room temperature'), ('c', "The programmer's mood"), ('d', 'The file size of a picture')], 'a'),
        ('When can two heap assertions sit side by side?',
         [('a', 'Never'), ('b', 'When they describe separate parts of memory'), ('c', 'Only on Sundays'), ('d', 'When they describe the same address')], 'b'),
        ('What does the frame rule let a proof do?',
         [('a', 'Ignore all memory'), ('b', 'Delete the heap'), ('c', 'Be reused when extra separate memory is left alone'), ('d', 'Stop threads')], 'c'),
        ('What does separation logic guard in concurrent programs?',
         [('a', 'Shared pieces of memory, with rules about access'), ('b', 'The colour of the screen'), ('c', 'Printer paper'), ('d', 'The date')], 'a'),
        ('What kind of program does the method suit well?',
         [('a', 'Programs that manipulate linked data through pointers'), ('b', 'Programs that only print sums'), ('c', 'Programs with no memory'), ('d', 'Recipes')], 'a'),
    ],
}
