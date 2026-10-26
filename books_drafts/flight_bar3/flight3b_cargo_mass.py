"""Cargo Mass and Balance: why a heavy load changes how a craft speeds up, stops and turns, and why the centre of mass matters."""
CODE = 'flight3b_cargo_mass'
BOOK = {
    "title": 'Cargo Mass and Balance',
    "subtitle": 'Why a heavy load changes how a craft speeds up, stops and turns',
    "chapters": [
        ('Mass is not the same as space',
         'A hold has room measured in cubic metres, and a load has mass measured in kilograms. The two are different. A hold can be full by volume and still light, or half empty and very heavy. A pilot checks both before loading.'),
        ('Heavy things are slow to change',
         'Newton showed that the push needed to change a craft\'s speed depends on its mass. A heavier craft needs more push to speed up, and more distance to stop. Load it heavily, and the same engine gives you a slower, longer change in speed.'),
        ('Where the mass comes from',
         'The game works out a piece\'s mass from its real density, so a piece of water ice weighs far less than the same volume of iron ore. Water ice has a density of about 917 kilograms per cubic metre. Hematite, a common iron ore, is about 5,300. Heavier material fills the hold with much more mass.'),
        ('Centre of mass',
         'Every craft has a centre of mass, the point where its weight seems to act. A load placed far to one side pulls the balance toward that side. The craft then turns and responds differently, and you must correct for it with the controls.'),
        ('Loads move and fuel burns',
         'Cargo that shifts in flight moves the centre of mass, and so does fuel. As fuel is burned, the craft gets lighter, and its balance changes too. Expect the handling to change over a long flight, and check it again after each big burn.'),
        ('Plan the load',
         'Before you leave, weigh the load, place the heavy pieces low and near the middle, and fill the hold evenly. Note the total mass in your log. A balanced load is easier to fly, cheaper to move and safer to stop.'),
    ],
    "test": [
        ('What is the difference between hold space and mass?',
         [('a', 'Space is measured in kilograms and mass in metres'), ('b', 'Space is the room in cubic metres and mass is the weight in kilograms'), ('c', 'They are the same thing'), ('d', 'Space is the colour and mass is the speed')], 'b'),
        ('What happens to a heavier craft with the same engine?',
         [('a', 'It speeds up more quickly'), ('b', 'It becomes invisible'), ('c', 'It changes speed more slowly and needs more distance to stop'), ('d', 'It stops using fuel')], 'c'),
        ('Roughly what is the density of water ice in the game\'s figures?',
         [('a', 'About 1 gram per cubic metre'), ('b', 'About 91.7 kilograms per cubic metre'), ('c', 'About 9,170 kilograms per cubic metre'), ('d', 'About 917 kilograms per cubic metre')], 'd'),
        ('What does a load placed far to one side do?',
         [('a', 'Moves the centre of mass toward that side, so the craft handles differently'), ('b', 'Makes the craft transparent'), ('c', 'Lowers the price of fuel'), ('d', 'Stops the engine')], 'a'),
        ('Why should the handling be checked again after a big burn?',
         [('a', 'Because burning fuel adds paint to the hull'), ('b', 'Because burning fuel makes the craft lighter and changes its balance'), ('c', 'Because the stars change position'), ('d', 'Because the Tower must see the fuel')], 'b'),
    ],
}
