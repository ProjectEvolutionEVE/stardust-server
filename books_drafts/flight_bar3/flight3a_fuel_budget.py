"""Fuel, Hours and the Pilot's Budget: what a craft costs to fly, and how to choose between paying by the hour and a weekly lease."""
CODE = 'flight3a_fuel_budget'
BOOK = {
    "title": "Fuel, Hours and the Pilot's Budget",
    "subtitle": 'What a craft costs to fly, and how to choose between paying by the hour and a weekly lease',
    "chapters": [
        ('Fuel is a heavy bill',
         "Fuel is one of the largest and most important costs of any flight. The more you burn, the more fuel you must carry, and the heavier the craft becomes. Every burn you plan is a cost you can count before you make it."),
        ('Two ways to pay',
         "The WSC owns the craft, so you pay to fly it. You can pay by the hour: 50 credits for each hour in the air, with fuel included. Or you can take a weekly lease: 500 credits a week, paid up front on a 28-day contract that renews automatically."),
        ('The break-even hour',
         "Divide the weekly lease by the hourly rate to find the break-even point: 500 divided by 50 is 10 hours. Fly more than 10 hours a week and the lease is cheaper. Fly fewer than that and the hourly rate costs less."),
        ('Watch the fuel bar',
         "On the flight screen, the fuel bar drops slowly while the craft is out, and more slowly when it is parked. Each return to the Starship tops it up. If the bar runs dry in space, the craft must be towed back in, and the tow costs a great deal, so plan the trip to come home."),
        ('Hydrogen from ice',
         "Water ice can be split by electrolysis into hydrogen and oxygen. By weight, one kilogram of water gives about 111 grams of hydrogen and about 889 grams of oxygen. Hydrogen runs the small mining craft, so ice in a debris field has real value."),
        ('Save for the flight',
         "Set aside part of each week's earnings for fuel, the lease and repairs before you spend on anything else. A pilot who budgets for the flight, and not just for the cargo, keeps on flying."),
    ],
    "test": [
        ('What is the hourly price of flying the craft?',
         [('a', '500 credits an hour'), ('b', '5 credits an hour'), ('c', '50 credits an hour'), ('d', '10 credits an hour')], 'c'),
        ('Roughly how many hours a week is the break-even point for the weekly lease?',
         [('a', '5 hours'), ('b', '7 hours'), ('c', '10 hours'), ('d', '100 hours')], 'c'),
        ('What happens to the fuel bar while the craft is parked?',
         [('a', 'It ticks down more slowly'), ('b', 'It drains faster'), ('c', 'It fills up'), ('d', 'It breaks')], 'a'),
        ('If the fuel bar runs dry out in space, what happens?',
         [('a', 'Nothing happens'), ('b', 'The crew is paid'), ('c', 'The craft sails on for ever'), ('d', 'The craft is towed back in, at a cost')], 'd'),
        ('About how much hydrogen comes from one kilogram of water, by weight?',
         [('a', 'About 111 grams'), ('b', 'About 889 grams'), ('c', 'About one kilogram'), ('d', 'About 11 kilograms')], 'a'),
    ],
}
