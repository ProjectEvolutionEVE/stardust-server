"""Power distribution aboard a ship: how power is shared from its sources to every system, and how a fault is kept from spreading."""
CODE = 'engineering3b_ship_power_distribution'
BOOK = {
    "title": 'Power Distribution Aboard a Ship',
    "subtitle": 'How power is shared out from its source to every system, and how a fault is kept from spreading',
    "chapters": [
        ('Sources and the switchboard',
         'A ship makes its power in its own generators and stores, and the power comes together at a main switchboard. From there, cables carry it to every system. The switchboard is the one place where power can be seen, switched and shared out.'),
        ('Busbars',
         'A busbar is a thick bar of copper or aluminium that carries power inside a switchboard, and each branch circuit takes its supply from it. A busbar is sized to carry a large current with little heat. Its joints must stay clean and tight, because a loose joint heats up.'),
        ('Protection that trips the right breaker',
         'Each circuit has a breaker that trips if it carries too much current. Good design is selective: a fault trips the breaker closest to it, so the rest of the ship keeps its power. If a fault takes out a whole section, the protection is not selective enough.'),
        ('Priority loads',
         'Not every system matters equally. Essential systems, such as steering, life support and navigation, are fed first. When the generators run short, load shedding switches off the less important loads, so the vital ones stay up.'),
        ('Two paths, or a ring',
         'Important supplies are often fed from two directions, or from a ring that can be cut at any point. If one cable is damaged, the power still reaches the load by the other path. An emergency source that starts on its own, and is kept separate from the main plant, covers the worst case.'),
        ('Plan the load as a budget',
         'Add up the power each system draws, including the surge it draws when it starts, and keep a margin below the rating of the generators. Over a day, the same loads set the energy bill, so every saving on the load also saves money. Treat the ship\'s power as a budget, with a margin kept back for surprises.'),
    ],
    "test": [
        ('What is a main switchboard for?',
         [('a', 'Cooking food'), ('b', 'Storing water'), ('c', 'Growing plants'), ('d', 'Bringing power together and sharing it out to every system')], 'd'),
        ('What is a busbar?',
         [('a', 'A seat for the crew on a bus'), ('b', 'A thick bar of copper or aluminium that carries power inside a switchboard'), ('c', 'A type of paint'), ('d', 'A radio aerial')], 'b'),
        ('What does selective protection aim to do?',
         [('a', 'Trip every breaker at once'), ('b', 'Switch off the whole ship on any fault'), ('c', 'Trip only the breaker closest to a fault, so the rest keeps its power'), ('d', 'Stop the generators')], 'c'),
        ('What is load shedding?',
         [('a', 'Switching off less important loads when power runs short'), ('b', 'Dropping cargo overboard'), ('c', 'Painting over the cables'), ('d', 'Shedding paint from the hull')], 'a'),
        ('Why are important supplies often fed from two directions?',
         [('a', 'So the cables look neater'), ('b', 'So power still reaches them if one cable is damaged'), ('c', 'So they weigh more'), ('d', 'So they cost less to run')], 'b'),
    ],
}
