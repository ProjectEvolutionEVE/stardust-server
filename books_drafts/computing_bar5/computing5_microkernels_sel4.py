"""Microkernels and seL4: keeping the kernel tiny, and proving the small core is correct."""
CODE = 'computing5_microkernels_sel4'
BOOK = {
    "title": 'Microkernels and seL4',
    "subtitle": 'Keeping the kernel tiny, and proving the small core is correct',
    "chapters": [
        ('A small core', 'A microkernel keeps only the most basic jobs in the kernel, such as scheduling and passing messages. Drivers, file systems and network stacks run as ordinary programs outside it. A small core is easier to understand and to check.'),
        ('Services in user space', 'Services in user space are separate programs. If one crashes, the rest of the system can often carry on. The cost is that they must talk to each other by messages, which takes effort.'),
        ('The cost of IPC', 'Inter-process communication, or IPC, is the message passing between programs. Each message costs time, so early microkernels were slow. Modern designs cut that cost with careful, fast messaging paths.'),
        ('The seL4 correctness proof', 'seL4 is a microkernel whose functional correctness has been proved in a theorem prover, with the work first published in 2009. The proof shows that the code matches its formal specification, which removes a whole class of bugs from the kernel.'),
        ('Capabilities', 'seL4 uses capabilities, which are unforgeable tokens that give rights to a resource. A program can use only what it holds a capability for. This makes the security rules clear and checkable.'),
        ('Where microkernels are used', 'Microkernels are used in systems that need high assurance, such as defence and secure embedded work. They suit places where a flaw in the core would be costly, and where a small trusted base matters most.'),
    ],
    "test": [
        ('What does a microkernel keep in the kernel?',
         [('a', 'All games'), ('b', 'All photos'), ('c', 'Every app'), ('d', 'Only the most basic jobs')], 'd'),
        ('Where do services in a microkernel system run?',
         [('a', 'In user space, as separate programs'), ('b', 'Inside the kernel'), ('c', 'Nowhere'), ('d', 'On paper')], 'a'),
        ('What does IPC mean?',
         [('a', 'Internal printer control'), ('b', 'Inter-process communication'), ('c', 'Instant photo capture'), ('d', 'Input power cable')], 'b'),
        ('What did the seL4 proof show?',
         [('a', 'That the code matches its formal specification'), ('b', 'That the kernel is blue'), ('c', 'That the kernel never boots'), ('d', 'That the kernel has no users')], 'a'),
        ('What are capabilities in seL4?',
         [('a', 'Skills of a person'), ('b', 'Printer features'), ('c', 'Unforgeable tokens that give rights to a resource'), ('d', 'Keyboard shortcuts')], 'c'),
    ],
}
