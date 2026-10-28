"""Copper Electrowinning Cell Design: how an electric cell pulls copper out of acid solution."""
CODE = 'mining5_ep_cell'
BOOK = {
    "title": 'Copper Electrowinning Cell Design',
    "subtitle": 'How an electric cell pulls copper out of acid solution',
    "chapters": [
        ('What electrowinning does', 'Electrowinning uses electricity to deposit copper from a clean acid solution onto cathodes. Copper leaves the solution and sticks to the cathode as metal. The leftover solution goes back to the leach to pick up more copper.'),
        ('Electrolyte', 'The electrolyte is sulfuric acid with dissolved copper and small amounts of additives. Its composition is controlled because it sets how well copper deposits. Too much or too little of any component can spoil the cathode.'),
        ('Anodes', 'Anodes are usually lead alloy plates. Oxygen forms at the anode while copper deposits at the cathode. The anode must resist the acid, and corrosion can add lead to the product, so its condition is checked often.'),
        ('Current efficiency', 'Not every amp of current deposits copper. Some goes into side reactions, such as making hydrogen or reducing iron. Plants measure current efficiency to see how much of the power is doing useful work.'),
        ('Cathode harvesting', 'Cathodes grow over several days and are then lifted out of the cell. Starter sheets are often made of stainless steel so the copper peels off cleanly. Harvesting is careful work to keep the sheets flat and clean.'),
        ('Power and layout', 'Power is the largest running cost, so cell design aims for low resistance and even current. Cells are laid out in long rows so the solution flows evenly. Good layout saves energy and keeps the plant safe.'),
    ],
    "test": [
        ('What does electrowinning do?', [('a', 'It deposits copper from clean acid solution onto cathodes using electricity'), ('b', 'It cooks ore in a furnace'), ('c', 'It grinds rock into sand'), ('d', 'It melts gold')], 'a'),
        ('What is the usual electrolyte acid?', [('a', 'Vinegar'), ('b', 'Sulfuric acid'), ('c', 'Lemon juice'), ('d', 'Milk')], 'b'),
        ('What gas forms at the anode?', [('a', 'Helium'), ('b', 'Neon'), ('c', 'Oxygen'), ('d', 'Argon')], 'c'),
        ('Why is current efficiency measured?', [('a', 'To change the colour of copper'), ('b', 'To count the cells'), ('c', 'To cool the electrolyte'), ('d', 'To see how much current is doing useful copper work')], 'd'),
        ('Why are starter sheets often stainless steel?', [('a', 'So the copper peels off cleanly'), ('b', 'So the copper dissolves faster'), ('c', 'So the sheets float'), ('d', 'So the cells glow')], 'a'),
    ],
}
