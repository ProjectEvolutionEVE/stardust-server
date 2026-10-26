"""Simple Machines: levers, pulleys, gears and screws, and the trade between distance and force."""
CODE = 'engineering2_simple_machines'
BOOK = {
    "title": 'Simple Machines',
    "subtitle": 'Levers, pulleys, gears and screws: trading distance for force',
    "chapters": [
        ('Distance for force',
         "A simple machine changes the size or the direction of a force. It cannot make work for free. If it multiplies "
         "your force, your input point must move farther. Work is force times distance, and in an ideal machine the work "
         "you put in equals the work you get out. Friction takes a little of it, so a real machine gives back a little less."),
        ('Levers',
         "A lever turns on a fixed point called the fulcrum. Its mechanical advantage is the load divided by the effort. "
         "If the effort arm is three times as long as the load arm, you can lift about three times your effort, but your end "
         "moves three times as far. A crowbar and a wheelbarrow both work this way."),
        ('Pulleys',
         "A single fixed pulley changes only the direction of the pull, so you can lift by pulling down. A single movable "
         "pulley halves the effort, because two lengths of rope share the load, but you pull the rope twice as far. Blocks "
         "and tackle stack several pulleys, so each extra supporting rope cuts the effort again, minus friction."),
        ('Gears and gear ratios',
         "Gears with meshing teeth turn each other. The gear ratio is the number of teeth on the driven gear divided by the "
         "number on the driver. A small driver turning a large gear slows the turn and multiplies the force. A large driver "
         "turning a small gear speeds the turn and gives up force. A gear train is a chain of such pairs."),
        ('Screws and wedges',
         "A screw is an inclined plane wrapped around a rod. One full turn moves it forward by its pitch, the distance from "
         "one thread to the next. A fine thread gives more force for each turn, and a coarse thread moves faster. A wedge is "
         "an inclined plane that moves, which is why an axe splits wood: a push at the edge becomes a large sideways force."),
        ('Simple parts, big machines',
         "Almost every machine is built from these few parts, combined. A winch is a drum driven by a gear train, a hoist is "
         "a set of pulleys, and a bolt is a screw. Start with the simple parts and count the trade: what you gain in force, "
         "you pay for in distance, and friction takes a share of both."),
    ],
    "test": [
        ("A lever's effort arm is three times as long as its load arm. Ignoring friction, about how much load can one unit of effort lift?",
         [('a', 'About one third of the effort'), ('b', 'The same as the effort'), ('c', 'About three times the effort'), ('d', 'Ten times the effort')], 'c'),
        ("What does a single fixed pulley change?",
         [('a', 'Only the direction of the pull'), ('b', 'It halves the force needed'), ('c', 'It multiplies the speed of the rope'), ('d', 'It stores energy for later')], 'a'),
        ("What does a gear ratio compare?",
         [('a', 'The colours of the gears'), ('b', 'The weight of each gear'), ('c', 'How fast the vehicle can go'), ('d', 'The teeth on the driven gear to the teeth on the driver')], 'd'),
        ("Why does a wedge split wood?",
         [('a', 'Its edge is painted'), ('b', 'A small push at its edge becomes a large sideways force'), ('c', 'It is heavier than the wood'), ('d', 'It melts the wood as it goes')], 'b'),
        ("A machine multiplies your force. What must it cost you?",
         [('a', 'Distance: your input point must move farther'), ('b', 'Time, for nothing in return'), ('c', 'Energy with no source'), ('d', 'Only the weight of the machine')], 'a'),
    ],
}
