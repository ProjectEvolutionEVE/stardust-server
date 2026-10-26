"""Chemical Equilibrium: when a reaction runs both ways at once, and how to nudge the balance. Science career, bar 3 (Senior Scientist), part B."""
CODE = 'science3b_equilibrium'
BOOK = {
    "title": 'Chemical Equilibrium',
    "subtitle": 'When a reaction runs both ways at once, and how to nudge the balance',
    "chapters": [
        ('Reactions that run both ways',
         'Some reactions can go forward and backward. They are reversible, and a double arrow shows it. When the forward and backward reactions run at the same rate, the system is at equilibrium.'),
        ('Balance, not stillness',
         'At equilibrium, nothing has stopped. Particles keep reacting in both directions. What stays steady is the amount on each side. Equilibrium means a steady balance, not equal amounts.'),
        ("Le Chatelier's principle",
         'If you disturb a system at equilibrium, it shifts to ease the disturbance. Add more of one substance, and the reaction tends to use some of it up. This principle is a handy guide that predicts the direction of the shift.'),
        ('Pressure and gas counts',
         'In a reaction between gases, pressure favours the side with fewer gas molecules. The Haber process makes ammonia from nitrogen and hydrogen. Four gas molecules become two, so high pressure helps the yield.'),
        ('Temperature and the balance',
         'The Haber reaction gives off heat. For a reaction like that, raising the temperature pushes the balance back toward the reactants. Industry often picks a compromise temperature, to balance the yield against the speed.'),
        ('Equilibrium in a fizzy drink',
         'Carbon dioxide in a sealed fizzy drink is in equilibrium with the gas above it. When you open the bottle, the gas escapes and the balance shifts, so more gas leaves the liquid. That is why an open drink goes flat.'),
    ],
    "test": [
        ('Which symbol shows a reaction that can run both ways?',
         [('a', 'A single arrow'), ('b', 'A double arrow'), ('c', 'An equals sign'), ('d', 'A dash')], 'b'),
        ('At equilibrium, what stays steady?',
         [('a', 'Nothing happens at all'), ('b', 'The forward and backward reactions stop'), ('c', 'The temperature of the mixture is zero'), ('d', 'The amount on each side')], 'd'),
        ("What does Le Chatelier's principle predict?",
         [('a', 'A system at equilibrium shifts to ease a disturbance'), ('b', 'Every reaction gives off heat'), ('c', 'Catalysts are always used up'), ('d', 'Gases never react')], 'a'),
        ('Why does high pressure favour ammonia in the Haber process?',
         [('a', 'Ammonia is heavier than hydrogen'), ('b', 'Pressure turns gas into a solid'), ('c', 'Four gas molecules become two, and the side with fewer gas molecules is favoured'), ('d', 'Pressure works exactly like a catalyst')], 'c'),
        ('Why does an open bottle of fizzy drink go flat?',
         [('a', 'The sugar sinks'), ('b', 'The drink freezes'), ('c', 'Gas is stored as a solid in the drink'), ('d', 'Carbon dioxide escapes, shifting the balance so more gas leaves the liquid')], 'd'),
    ],
}
