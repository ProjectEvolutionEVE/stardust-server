"""RDMA and Kernel Bypass: moving data between machines straight into memory, skipping much of the usual network work."""
CODE = 'computing5_rdma'
BOOK = {
    "title": 'RDMA and Kernel Bypass',
    "subtitle": 'Moving data between machines straight into memory, skipping much of the usual network work',
    "chapters": [
        ('Direct memory across machines', 'Remote direct memory access, or RDMA, lets one machine read or write memory on another machine without much help from the other processor. The network card moves the data straight into the right place in memory.'),
        ('Queue pairs', 'Applications talk to the network card through queue pairs: a send queue and a receive queue. The application posts work requests, and the card reports completions through completion queues. This keeps the processor out of the way.'),
        ('Zero copy', 'Because data moves directly into the destination memory, it is not copied several times between buffers. Avoiding copies saves processor time and memory bandwidth. This is what makes RDMA fast for large transfers.'),
        ('Kernel-bypass networking', 'Kernel bypass means the application sends and receives packets without going through the usual operating system path for each message. That lowers delay, though the application then takes on more responsibility for the details.'),
        ('Reliability', 'RDMA networks can be built to be reliable, so the card handles retries and ordering at the transport level. Applications still need to handle failures of the other machine. Reliability of the link is not the same as reliability of the whole service.'),
        ('Data-centre use', 'Data centres use RDMA for fast storage access, large data movement and tightly coupled computing. It works best on dedicated networks where the hardware is controlled. The gains are large, but the setup is more specialised.'),
    ],
    "test": [
        ('What does RDMA let one machine do?',
         [('a', 'Paint another machine'), ('b', 'Turn off the sun'), ('c', 'Print the other mail'), ('d', 'Read or write memory on another machine')], 'd'),
        ('What are queue pairs?',
         [('a', 'A send queue and a receive queue'), ('b', 'Two cups of tea'), ('c', 'A pair of shoes'), ('d', 'Two printers')], 'a'),
        ('What does zero copy avoid?',
         [('a', 'Copying data several times between buffers'), ('b', 'Using a network'), ('c', 'Using a screen'), ('d', 'Using electricity')], 'a'),
        ('What does kernel bypass avoid?',
         [('a', 'All networks'), ('b', 'The usual operating system path for each message'), ('c', 'All computers'), ('d', 'The screen')], 'b'),
        ('Where are RDMA networks mostly used?',
         [('a', 'Data centres'), ('b', 'Kitchens'), ('c', 'Kayaks'), ('d', 'Libraries of paper')], 'a'),
    ],
}
