"""Thermoelectric Cooling and Generation: the Seebeck and Peltier effects, figure of merit, module design, and efficiency limits."""
CODE = 'engineering5_teg'
BOOK = {'title': 'Thermoelectric Cooling and Generation',
 'subtitle': 'Seebeck and Peltier effects, figure of merit, and the limits of efficiency',
 'chapters': [('Two effects, one material',
               'A thermoelectric device uses the link between heat and electricity inside certain solids. '
               'The Seebeck effect makes a voltage when the two ends of a material are at different '
               'temperatures. The Peltier effect does the reverse: passing a current through a junction '
               'carries heat from one side to the other.'),
              ('The figure of merit',
               'Engineers judge a thermoelectric material by a single number called the figure of merit, '
               'written ZT. A good material conducts electricity well but conducts heat poorly, so the hot '
               'and cold ends stay apart. Bismuth telluride is the classic choice near room temperature, and '
               'many practical modules reach a ZT near one.'),
              ('How a module is built',
               'A module links many small blocks of p-type and n-type material. The blocks are wired '
               'electrically in series, so the voltages add, and set thermally side by side between a hot '
               'plate and a cold plate. Designers choose the block length and count to match the load.'),
              ('The efficiency limit',
               'No heat engine can beat the Carnot limit, which depends only on the hot and cold '
               'temperatures. Real thermoelectric generators fall far short of that limit, and typical units '
               'convert only a few to around ten percent of the heat that passes through them. Their '
               'strength is reliability, not efficiency.'),
              ('The money side',
               'Thermoelectric modules cost more per watt than a turbine or an engine, so they are chosen '
               'only where their strengths count. A careful engineer compares the price of the module with '
               'the price of the fuel it saves over its working life. A cheap, quiet, never-failing part can '
               'be worth more than a cheap, efficient one that needs servicing.'),
              ('Where they fly',
               'Radioisotope thermoelectric generators use heat from the slow decay of a radioactive fuel to '
               'make electricity with no moving parts. The Voyager spacecraft carried them and still draw '
               'power from them decades after launch. Their long, quiet life is the reason they were '
               'chosen.')],
 'test': [('What does the Seebeck effect do?',
           [('a', 'It turns a temperature difference into a voltage'),
            ('b', 'It stops heat from flowing'),
            ('c', 'It turns light into sound'),
            ('d', 'It pumps water uphill')],
           'a'),
          ('Which property makes a good thermoelectric material?',
           [('a', 'It conducts heat well and electricity badly'),
            ('b', 'It is always a liquid'),
            ('c', 'It conducts electricity well and heat poorly'),
            ('d', 'It is made only of gold')],
           'c'),
          ('How are the blocks in a thermoelectric module usually wired electrically?',
           [('a', 'All in parallel only'),
            ('b', 'In series, so the voltages add'),
            ('c', 'Not connected at all'),
            ('d', 'Through a single wire to the Sun')],
           'b'),
          ('What does the Carnot limit depend on?',
           [('a', 'The colour of the device'),
            ('b', 'The name of the designer'),
            ('c', 'The weight of the module alone'),
            ('d', 'The hot and cold temperatures')],
           'd'),
          ('Why were radioisotope thermoelectric generators chosen for Voyager?',
           [('a', 'They are fast and loud'),
            ('b', 'They need frequent servicing'),
            ('c', 'They have no moving parts and last for decades'),
            ('d', 'They run on sunlight only')],
           'c')]}
