"""SmartNICs and Offload: network cards with their own processors, taking work off the main computer."""
CODE = 'computing5_smartnics'
BOOK = {
    "title": 'SmartNICs and Offload',
    "subtitle": 'Network cards with their own processors, taking work off the main computer',
    "chapters": [
        ('Network cards with processors', 'A SmartNIC is a network card that has its own processor, often with programmable parts. Instead of only moving packets, it can run tasks that the main computer would otherwise do itself.'),
        ('Offloading encryption and storage', 'Common offloads include encryption, packet filtering and some storage work. Moving them to the card frees the main processor for the application. In many cases the card can handle these tasks at full line speed.'),
        ('Programmable datapaths', 'A programmable datapath lets operators define how packets are handled, such as routing rules or monitoring. Changes can be made in software rather than in new hardware. This flexibility suits cloud providers with changing needs.'),
        ('Trade-offs', 'Offload is not free: the card has limited memory and speed, and programming it takes special skill. Some tasks run better on the main processor. Engineers decide what to move based on measured results.'),
        ('Security boundaries', 'A card that runs code is part of the system security boundary. If it were compromised, it could see or change traffic. Designers must protect the card firmware and limit its access, just as they would for any trusted component.'),
        ('Cost', 'SmartNICs cost more than plain cards, and the saving must justify the extra price and effort. The benefit is often clearest in large data centres, where a small gain across many machines adds up.'),
    ],
    "test": [
        ('What is a SmartNIC?',
         [('a', 'A smart phone'), ('b', 'A type of printer'), ('c', 'A calculator'), ('d', 'A network card with its own processor')], 'd'),
        ('What kind of work is often offloaded?',
         [('a', 'Painting'), ('b', 'Cooking'), ('c', 'Music'), ('d', 'Encryption and packet filtering')], 'd'),
        ('What is a programmable datapath?',
         [('a', 'A road'), ('b', 'A bus route'), ('c', 'A way to define how packets are handled'), ('d', 'A keyboard layout')], 'c'),
        ('What is a security concern with a SmartNIC?',
         [('a', 'It needs no firmware'), ('b', 'It cannot connect'), ('c', 'It makes screens bright'), ('d', 'If compromised, it could see or change traffic')], 'd'),
        ('Where is the benefit often clearest?',
         [('a', 'Small kitchens'), ('b', 'Large data centres'), ('c', 'Quiet libraries'), ('d', 'Flower shops')], 'b'),
    ],
}
