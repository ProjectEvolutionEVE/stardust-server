"""Process Water Recycling: keeping the water balance of a mine and mill in check, and getting clean water back."""
CODE = 'mining5_proc_water'
BOOK = {
    "title": 'Process Water Recycling',
    "subtitle": 'Keeping the water balance right, and getting clean water back',
    "chapters": [
        ('The water balance', 'A mill uses water to grind ore, carry it through pipes and wash it. Water comes in from rain, rivers and ore moisture, and it leaves in tailings and as vapour. A water balance adds up every flow so the plant knows where its water goes.'),
        ('Cyanide destruction', 'Some gold plants use cyanide to dissolve gold, and any left in the tailings water must be removed. Operators use oxidants such as hydrogen peroxide, or sulfur dioxide with air, to break cyanide down. Testing confirms that levels are low enough before water is reused or released.'),
        ('Salt build-up', 'When water is recycled again and again, salts build up in it. High salt levels can slow flotation and damage pipes and equipment. Plants watch conductivity and bleed off some water to keep salts in check.'),
        ('Membranes', 'Membrane systems can remove salts and fine solids from process water. Reverse osmosis forces water through a very fine membrane and leaves salts behind as a concentrated brine. The brine still needs a plan for disposal.'),
        ('Zero discharge', 'Some plants aim for zero discharge, meaning no water leaves the site except as vapour or within the ore. This needs evaporation, membranes and careful salt handling. Zero discharge is possible, but it is costly.'),
        ('Costs', 'Pumping, treatment chemicals, energy for evaporation and membranes all add to the bill. Water-saving steps often pay back over time, especially in dry places. Plants compare the cost of water with the cost of treatment before choosing a route.'),
    ],
    "test": [
        ('What does a water balance do for a plant?', [('a', 'It paints the pipes'), ('b', 'It sets the price of gold'), ('c', 'It adds up every water flow so the plant knows where its water goes'), ('d', 'It counts the workers')], 'c'),
        ('Which substance must be removed from gold-plant tailings water?', [('a', 'Sugar'), ('b', 'Milk'), ('c', 'Vinegar'), ('d', 'Cyanide')], 'd'),
        ('Why do salts build up when water is recycled?', [('a', 'Water is recycled again and again, so salts stay in it'), ('b', 'Salts are added to the water on purpose'), ('c', 'Salts float away in the wind'), ('d', 'Salts only form in winter')], 'a'),
        ('What does reverse osmosis leave behind as concentrated brine?', [('a', 'Clean air'), ('b', 'Salts'), ('c', 'Gold leaf'), ('d', 'Wood chips')], 'b'),
        ('What does zero discharge mean?', [('a', 'The plant never uses any water'), ('b', 'The plant only uses sea water'), ('c', 'No water leaves the site except as vapour or within the ore'), ('d', 'The plant stops grinding ore')], 'c'),
    ],
}
