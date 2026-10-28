"""Mercury Capture From Smelter Gas: keeping mercury out of smelter exhaust and out of the acid plant."""
CODE = 'mining5_mercury_capture'
BOOK = {
    "title": 'Mercury Capture From Smelter Gas',
    "subtitle": 'Keeping mercury out of smelter exhaust and out of the acid plant',
    "chapters": [
        ('Mercury in the ore', 'Some ores carry small amounts of mercury. When they are roasted or smelted, the mercury leaves in the gas. Mercury is toxic, so plants must catch it before it reaches the air or the acid.'),
        ('Mercury species', 'Mercury can leave a smelter as elemental vapour or as compounds. Each form behaves differently when it meets a sorbent or a scrubber. Plants test to know which forms are present.'),
        ('Sorbent injection', 'One method is to inject activated carbon into the gas stream. The carbon grabs mercury and is then collected by filters. The loaded carbon must be handled and stored safely.'),
        ('Wet scrubbing', 'Some plants use wet scrubbers that wash the gas with a liquid that captures mercury. The liquid is then treated to remove the mercury before reuse. Scrubbing also helps remove other gases.'),
        ('Monitoring', 'Continuous analysers track mercury in the gas and in the acid. Operators use the data to adjust sorbent doses and scrubber settings. Records are kept for the regulators.'),
        ('Disposal', 'Captured mercury is stabilised and placed in secure storage or sent for treatment. It must never be thrown into an ordinary landfill. The disposal plan is part of every permit.'),
    ],
    "test": [
        ('Why must mercury be caught in smelter gas?', [('a', 'It makes the gas sweet'), ('b', 'It cools the plant'), ('c', 'It makes the ore lighter'), ('d', 'It is toxic and must not reach the air or acid')], 'd'),
        ('What is injected into the gas to grab mercury?', [('a', 'Activated carbon'), ('b', 'Sugar'), ('c', 'Flour'), ('d', 'Cooking oil')], 'a'),
        ('What does a wet scrubber use to capture mercury?', [('a', 'A dry wooden board'), ('b', 'A liquid that washes the gas'), ('c', 'A sheet of paper'), ('d', 'A heap of sand')], 'b'),
        ('Why do plants run continuous analysers?', [('a', 'To make the gas louder'), ('b', 'To change the colour of the acid'), ('c', 'To track mercury and adjust the sorbent and scrubber settings'), ('d', 'To count the birds')], 'c'),
        ('How must captured mercury be disposed of?', [('a', 'Thrown into a normal landfill'), ('b', 'Poured into a river'), ('c', 'Burned in a backyard'), ('d', 'Stabilised and stored securely or sent for treatment')], 'd'),
    ],
}
