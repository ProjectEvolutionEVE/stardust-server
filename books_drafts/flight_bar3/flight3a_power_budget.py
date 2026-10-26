"""The Power Budget: where a craft gets its electricity, and how a pilot keeps the books balanced."""
CODE = 'flight3a_power_budget'
BOOK = {
    "title": 'The Power Budget',
    "subtitle": 'Where a craft gets its electricity, and how a pilot keeps the books balanced',
    "chapters": [
        ('Power in, power out',
         "A craft needs electrical power for its computers, heaters, sensors and radio. Power comes from solar arrays that turn sunlight into electricity, with batteries to store it. A pilot must keep the power coming in at least equal to the power going out."),
        ('The daily cycle',
         "A craft in a low orbit passes into the planet's shadow on each lap. In shadow the solar arrays make no power, so the batteries carry the load. The batteries must be charged back up in sunlight before the next shadow comes."),
        ('A power budget',
         "A power budget lists every load and how much it draws, then compares the total with the supply. It works like a household budget: spending must fit the income. Planning early prevents switching things off in a hurry."),
        ('Arrays wear over time',
         "Solar cells slowly lose output as they age and as particles from space strike them. A craft that made enough power at launch may make less after several years. Pilots track the trend, not just today's reading."),
        ('Shedding loads',
         "When power runs short, the craft sheds loads: it switches off the least needed systems first. That order is set in advance, so the most important systems stay on. Shedding is a last resort, not a habit."),
        ('Power has a cost',
         "Power is never free, because arrays and batteries cost money to build and to replace. Using less power saves the batteries and delays the next replacement. A wise pilot counts the cost of every extra hour of heating or lighting."),
    ],
    "test": [
        ('What is the main source of power on many spacecraft?',
         [('a', 'Burning coal'), ('b', 'Wind'), ('c', 'Solar arrays that turn sunlight into electricity'), ('d', 'Gold bars')], 'c'),
        ('Why do batteries matter in a low orbit?',
         [('a', 'They power the craft while it is in the planet\'s shadow'), ('b', 'They make the hull shine'), ('c', 'They pay the crew'), ('d', 'They hold the air')], 'a'),
        ('What is a power budget?',
         [('a', 'A map of the stars'), ('b', 'A list of every load and its draw, compared with the supply'), ('c', 'A list of crew names'), ('d', 'A price list for fuel')], 'b'),
        ('Why do solar arrays give less power after several years?',
         [('a', 'They are painted over'), ('b', 'They are too cold'), ('c', 'They are moved into the shade'), ('d', 'They age and are struck by particles from space')], 'd'),
        ('What is load shedding?',
         [('a', 'Switching off the least needed systems first when power is short'), ('b', 'Adding more crew to the craft'), ('c', 'Dropping cargo into space'), ('d', 'Turning up the heat')], 'a'),
    ],
}
