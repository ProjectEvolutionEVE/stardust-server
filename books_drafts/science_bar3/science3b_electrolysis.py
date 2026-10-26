"""Electrolysis: Splitting Water: pushing electric current through water to split it into hydrogen and oxygen, and what that costs. Science career, bar 3 (Senior Scientist), part B."""
CODE = 'science3b_electrolysis'
BOOK = {
    "title": 'Electrolysis: Splitting Water',
    "subtitle": 'Pushing electric current through water to split it into hydrogen and oxygen',
    "chapters": [
        ('Electricity can break a compound',
         'Electrolysis uses an electric current to force a reaction that would not happen by itself. Passing current through water splits it into hydrogen and oxygen. The water is not burned; it is pulled apart.'),
        ('Two electrodes, two gases',
         'Two electrodes sit in the water. Hydrogen bubbles form at the cathode, the negative electrode, and oxygen bubbles form at the anode, the positive one. Oxidation happens at the anode and reduction at the cathode, the same rule as in a cell.'),
        ('The two-to-one ratio',
         'The equation 2H2O → 2H2 + O2 shows the ratio. For every two volumes of hydrogen made, one volume of oxygen forms, when both gases are at the same temperature and pressure. Measuring the gases in that ratio is a simple way to check the work.'),
        ('Pure water is a poor conductor',
         'Pure water carries very little current, so a little acid or salt is often added. The added ions help the current pass, and the reaction then runs far more easily.'),
        ('Ice in the game',
         'Rule 38 says water ice from the debris is split into hydrogen and oxygen, and that hydrogen is the fuel for the small mining craft. Splitting water needs a lot of electricity, so the energy cost is part of what the fuel really costs.'),
        ('Safety with hydrogen and oxygen',
         'Hydrogen is very flammable, and a mix of hydrogen and oxygen can burn or explode when a spark reaches it. Seal the gas lines, ventilate the room, and keep flames and sparks well away. Careful planning is part of the true cost of making fuel.'),
    ],
    "test": [
        ('What does electrolysis use to force a reaction?',
         [('a', 'Heat from a fire'), ('b', 'Electric current'), ('c', 'A magnet'), ('d', 'Sunlight only')], 'b'),
        ('Where does hydrogen form during the electrolysis of water?',
         [('a', 'At the anode'), ('b', 'On the glass'), ('c', 'In the middle of the water'), ('d', 'At the cathode')], 'd'),
        ('What volume ratio of hydrogen to oxygen does splitting water give?',
         [('a', '1 to 1'), ('b', '2 to 1'), ('c', '1 to 2'), ('d', '3 to 1')], 'b'),
        ('Why is a little acid or salt often added to water before electrolysis?',
         [('a', 'To make the water warmer'), ('b', 'To change the water into ice'), ('c', 'Pure water carries little current, and the added ions help it conduct'), ('d', 'To stop the bubbles')], 'c'),
        ('Why must hydrogen gas be handled with great care?',
         [('a', 'It is very flammable, and a mix with oxygen can burn or explode when a spark reaches it'), ('b', 'It is a liquid at room temperature'), ('c', 'It turns metal into stone'), ('d', 'It has no weight at all')], 'a'),
    ],
}
