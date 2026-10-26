"""Interfaces: where subsystems meet, and the agreed shape, power, signals and timing at each join."""
CODE = 'engineering3c_interfaces'
BOOK = {
    "title": 'Interfaces: Where Subsystems Meet',
    "subtitle": 'Agreeing the shape, power, signals and timing at each join between parts',
    "chapters": [
        ('Subsystems and their joins',
         "A machine is made of subsystems: the power, the controls, the cooling, the structure. Each one joins the others at an interface. In complex builds, many failures happen at the joins rather than inside the parts."),
        ('Mechanical interfaces',
         "A mechanical interface says how parts fit together: the bolt pattern, the size, the weight and the space each part is allowed. Two parts that each work alone may not fit when they are put together. Measure the join, not only the parts."),
        ('Electrical interfaces',
         "An electrical interface states the voltage, the current limit, the connector type and the wire colours. Connecting the wrong voltage can destroy a part at once. Label every connector and check it before the power goes on."),
        ('Data and timing',
         "A signal interface says what each message means, how quickly it must arrive and what happens if it does not. Two systems can each be correct and still misunderstand one another. Agree the meaning and the timing in writing."),
        ('The interface control document',
         "An interface control document is a written agreement of these details, signed off by both sides. Any change to either part goes through it. It turns a handshake into a record."),
        ('Testing the join',
         "Test the interfaces together, not only each part alone. Put the joined parts through a normal cycle and watch the points where they meet. A join that passes alone can still fail in use."),
    ],
    "test": [
        ('Where do most failures in complex builds tend to happen?',
         [('a', 'At the joins between subsystems'), ('b', 'In the paint'), ('c', "In the crew's rooms"), ('d', 'In the sunlight')], 'a'),
        ('What does an electrical interface specify?',
         [('a', 'The colour of the cabinet'), ('b', 'The names of the crew'), ('c', 'The voltage, current limit, connector type and wire colours'), ('d', 'The price of wire')], 'c'),
        ('Why can two correct systems still fail together?',
         [('a', 'They are always too strong'), ('b', "They may misunderstand each other's messages, timing or meaning"), ('c', 'They have the same paint'), ('d', 'They are too cheap')], 'b'),
        ('What is an interface control document?',
         [('a', 'A spreadsheet of wages'), ('b', 'A map of the hold'), ('c', 'A letter to the WSC'), ('d', 'A written agreement of all the interface details, signed off by both sides')], 'd'),
        ('How should the joins be tested?',
         [('a', 'Each part alone, and never together'), ('b', 'Together, through a normal cycle, watching where the parts meet'), ('c', 'Only on paper'), ('d', 'Only after the build is sold')], 'b'),
    ],
}
