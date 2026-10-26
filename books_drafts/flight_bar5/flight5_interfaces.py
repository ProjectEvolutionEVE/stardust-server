"""Interface Management: agreeing exactly how parts connect, so that they fit and work together."""
CODE = 'flight5_interfaces'
BOOK = {
    'title': 'Interface Management',
    'subtitle': 'How parts agree to connect',
    'chapters': [
        ('Where parts meet', 'An interface is the boundary where two parts or two teams meet. It can be a physical joint, an electrical connection, a data message or a shared procedure. Most surprises happen at interfaces.'),
        ('Interface control documents', 'An interface control document, or ICD, records every detail of an interface: its size, its loads, its signals and its units. Both sides sign it, and each change goes through control.'),
        ('Docking standards', 'Docking systems have standard interfaces so that craft built by different teams can meet. A shared standard lets parts be swapped and tested separately.'),
        ('Units', "A mismatch of units can destroy a mission. The Mars Climate Orbiter was lost in 1999 when one team's software used pound-force seconds and another used newton seconds. Always state and check the unit."),
        ('Test fit', 'A test fit checks that parts physically join before they are sent for final use. It finds problems while they are still cheap to fix.'),
        ('Ariane 5', 'In 1996, the Ariane 5 rocket was destroyed after a software conversion from an older design caused an overflow in reused code. The lesson is that interfaces with old software need as much checking as new work.'),
    ],
    'test': [
        ('What is an interface?', [('a', 'A type of rocket fuel'), ('b', 'A kind of crew uniform'), ('c', 'A bright planet'), ('d', 'A boundary where two parts or teams meet')], 'd'),
        ('What does an interface control document record?', [('a', 'A list of holidays'), ('b', 'The details of an interface, agreed by both sides'), ('c', 'The price of food'), ('d', 'The weather report')], 'b'),
        ('What caused the loss of the Mars Climate Orbiter in 1999?', [('a', 'A mismatch between pound-force seconds and newton seconds'), ('b', 'A loss of colour on the screen'), ('c', 'A crew shortage'), ('d', 'A broken window')], 'a'),
        ('What is a test fit?', [('a', "A check of the crew's clothes"), ('b', 'A test of the paint'), ('c', 'A check that parts physically join before final use'), ('d', 'A race between craft')], 'c'),
        ('What does the Ariane 5 case show about old software?', [('a', 'Old software never fails'), ('b', 'Interfaces with old software need as much checking as new work'), ('c', 'Old software should be deleted at once'), ('d', 'Old software needs no tests')], 'b'),
    ],
}
