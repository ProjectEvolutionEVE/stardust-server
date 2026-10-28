"""Persistent Memory: memory that keeps its contents through power loss, and the care needed to keep it correct."""
CODE = 'computing5_persistent_memory'
BOOK = {
    "title": 'Persistent Memory',
    "subtitle": 'Memory that keeps its contents through power loss, and the care needed to keep it correct',
    "chapters": [
        ('Memory that survives', 'Persistent memory keeps its contents when the power goes off, like a disk, but it can be read and written at the byte level, like ordinary memory. Programs can treat it as a place to keep data for good.'),
        ('Persistence ordering', 'Writes to memory may reach the storage in a different order from the one the program issued them. Programmers must make sure important writes land in the right order before data is considered saved. Without that, a crash can leave a half-updated structure.'),
        ('Flush instructions', 'Processors have instructions that flush cached data out to persistent memory. Programs use them, along with fences, to force writes to finish in order. These instructions are the building blocks of safe persistent code.'),
        ('Crash consistency', 'Crash consistency means that after a crash, the data is in a valid state. Techniques such as logging or copy-on-write let a program roll back or finish a half-done change. The aim is that the program never sees a broken structure.'),
        ('Programming models', 'Libraries and models help programmers use persistent memory without handling every flush by hand. They provide transactions or safe structures that take care of ordering. Good models make the safe way the easy way.'),
        ('Hardware history', 'Byte-addressable persistent memory products have appeared in recent years, but their market has been small and uncertain. The ideas remain useful, since the same ordering and crash problems also appear with ordinary caches and storage.'),
    ],
    "test": [
        ('What does persistent memory keep?',
         [('a', 'Pictures of cats'), ('b', 'Nothing'), ('c', 'Only errors'), ('d', 'Contents through power loss')], 'd'),
        ('Why must programmers care about write order?',
         [('a', 'Writes are always in colour'), ('b', 'Writes make the screen hot'), ('c', 'Writes may reach storage in a different order from the one issued'), ('d', 'Writes stop the printer')], 'c'),
        ('What are flush instructions used for?',
         [('a', 'Forcing cached writes out to persistent memory'), ('b', 'Cleaning the floor'), ('c', 'Washing dishes'), ('d', 'Mixing paint')], 'a'),
        ('What does crash consistency mean?',
         [('a', 'The computer never crashes'), ('b', 'The data is in a valid state after a crash'), ('c', 'The screen never breaks'), ('d', 'Data is always deleted')], 'b'),
        ('What do programming models provide?',
         [('a', 'Transactions or safe structures that handle ordering'), ('b', 'Music tracks'), ('c', 'Only colour themes'), ('d', 'Lunch menus')], 'a'),
    ],
}
