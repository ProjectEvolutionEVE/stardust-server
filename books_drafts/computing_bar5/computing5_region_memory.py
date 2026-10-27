"""Region-Based and Arena Memory: freeing many things at once, grouped by how long they live."""
CODE = 'computing5_region_memory'
BOOK = {
    "title": 'Region-Based and Arena Memory',
    "subtitle": 'Freeing many things at once, grouped by how long they live',
    "chapters": [
        ('Freeing a group at once', 'Usually each piece of memory is freed on its own. A region or arena is a group of allocations that are all freed together, when the whole region is no longer needed. One step can clear thousands of items.'),
        ('Region inference', 'Some compilers work out regions on their own, by following where values are used. The compiler decides which values belong to a region and when it ends. This removes the need for the programmer to track each piece.'),
        ('Arenas in servers', 'Servers handle many requests, and each request creates temporary data. Putting a request data in an arena means it is all freed when the request ends. This is simple, fast, and avoids leaks from forgotten pieces.'),
        ('Lifetime grouping', 'The method works best when things that die together are kept together. Grouping by lifetime rather than by type is the key idea. A mistake in grouping can keep memory alive longer than it is needed.'),
        ('Fragmentation', 'Freeing many small pieces one by one can leave gaps that waste space. Freeing a whole region at once avoids many of those gaps. However, one long-lived item inside a region can keep the rest from being freed.'),
        ('Trade-offs against garbage collection', 'A garbage collector finds unused memory automatically, but it runs at times of its own choosing. Regions give clear timing and low overhead, but they need the program to match lifetimes to groups. Each approach suits different jobs.'),
    ],
    "test": [
        ('What is a region or arena?',
         [('a', 'A group of allocations freed together'), ('b', 'A type of game'), ('c', 'A kind of cable'), ('d', 'A chart of colours')], 'a'),
        ('What do servers often put in an arena?',
         [('a', 'Pictures of the sky'), ('b', 'Printer settings'), ('c', 'Data for one request, freed when it ends'), ('d', 'Permanent names only')], 'c'),
        ('What is grouping by lifetime?',
         [('a', 'Grouping by colour'), ('b', 'Keeping things that die together in the same group'), ('c', 'Sorting by size'), ('d', 'Counting years')], 'b'),
        ('What can one long-lived item do inside a region?',
         [('a', 'Keep the whole region from being freed'), ('b', 'Shrink the region'), ('c', 'Print the region'), ('d', 'Remove the region from the computer')], 'a'),
        ('What is one benefit of regions over garbage collection?',
         [('a', 'Clear timing with low overhead'), ('b', 'Infinite memory'), ('c', 'No need for any program'), ('d', 'Faster typing')], 'a'),
    ],
}
