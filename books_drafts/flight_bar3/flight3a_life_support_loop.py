"""The Air and Water Loop: how a crew keeps breathing and drinking on a long flight."""
CODE = 'flight3a_life_support_loop'
BOOK = {
    "title": 'The Air and Water Loop',
    "subtitle": 'How a crew keeps breathing and drinking on a long flight',
    "chapters": [
        ('A closed loop',
         "On a long flight, a craft cannot carry all its air and water from home, because that is not practical. Instead it runs a loop, in which air and water are cleaned and used again. Every loop leaks a little and needs topping up, so the pilot watches it closely."),
        ('Carbon dioxide',
         "People breathe out carbon dioxide, which builds up quickly in a closed space. Scrubbers use chemicals that take up the gas, and the cleaned air goes back into the cabin. A full or failing scrubber lets the level rise, which is a warning sign."),
        ('Making oxygen',
         "Oxygen can be made by splitting water with electricity, a process called electrolysis. It gives both hydrogen and oxygen, and the oxygen goes back into the air. The process needs a steady supply of power, so it sits in the power budget."),
        ('Water gets reused',
         "Water is recovered from wastes and from moisture in the air, cleaned, and drunk again. The International Space Station recovers most of the water its crew uses in this way. The Starship's water plant follows the same idea and makes water aboard."),
        ('Watch the levels',
         "The pilot watches the air pressure, the oxygen level, the carbon dioxide level and the water tanks. A slow change over several days points to a part that needs care. A sudden change needs an immediate check."),
        ('Plants help the loop',
         "Growing plants take in carbon dioxide and release oxygen while they grow, and they can add food and water to the loop. A greenhouse makes the loop more balanced, but it does not replace the scrubbers and the checks. The Starship's greenhouse is part of this same loop."),
    ],
    "test": [
        ('Why does a long flight run a loop of air and water?',
         [('a', 'Water is poisonous'), ('b', 'The Sun makes the air'), ('c', 'It is a rule of colour'), ('d', 'Carrying all of it from home is not practical for a long trip')], 'd'),
        ('What do scrubbers remove from the air?',
         [('a', 'Oxygen'), ('b', 'Carbon dioxide'), ('c', 'Warmth'), ('d', 'Sunlight')], 'b'),
        ('How can oxygen be made from water?',
         [('a', 'Boiling it in a pan'), ('b', 'Shaking it hard'), ('c', 'Electrolysis, which splits water with electricity'), ('d', 'Freezing it')], 'c'),
        ('What does the International Space Station do with much of its water?',
         [('a', 'Throws it away each day'), ('b', 'Stores it in the cabin walls'), ('c', 'Sends it to Earth each day'), ('d', 'Recovers most of it and reuses it')], 'd'),
        ('Why does a sudden change in a level need an immediate check?',
         [('a', 'A sudden change can mean a fault that is getting worse'), ('b', 'Levels are never checked'), ('c', 'The colour of the air changes'), ('d', 'It does not matter at all')], 'a'),
    ],
}
