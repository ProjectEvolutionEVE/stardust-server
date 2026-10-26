"""The Geostationary Ring: why a satellite can hang over one spot, and how the slots are shared."""
CODE = 'flight5_a_geostationary'
BOOK = {
    "title": 'The Geostationary Ring',
    "subtitle": 'Satellites that stay over one spot on the Earth',
    "chapters": [
        ('Arthur C. Clarke',
         'In 1945 the writer Arthur C. Clarke described satellites placed high above the equator that would stay over one spot. The idea is now called geostationary orbit. It is a simple result of gravity and the Earth turning once a day.'),
        ('The altitude',
         'A satellite that circles the Earth once every 24 hours, over the equator, stays above one point on the ground. That height is about 35,800 kilometres above sea level. At this height the craft moves at roughly three kilometres a second.'),
        ('Slots along the ring',
         'The geostationary ring is a single line of positions over the equator, and each satellite takes a slot along it. Slots are limited, so countries and companies must agree how to share them through the International Telecommunication Union.'),
        ('Drift',
         "Small pulls from the Moon, the Sun and the Earth's uneven shape push a satellite slowly out of its slot. Operators fire small thrusters from time to time to keep it in place. This station keeping uses fuel, which is why fuel often sets a satellite's life."),
        ('The graveyard orbit',
         'When a geostationary satellite is worn out, it is moved to a slightly higher orbit, often called the graveyard orbit, so that it does not block a useful slot. The move uses the last of its fuel. It is a responsible way to clear the ring.'),
        ('Congestion',
         'Because so many satellites use the same ring, interference and crowding are real concerns. Rules and planning help keep the slots usable for everyone. The ring is valuable, so it is handled with care.'),
    ],
    "test": [
        ('What is the altitude of a geostationary orbit, roughly?',
         [('a', 'About 400 kilometres'), ('b', 'About 3,500 kilometres'), ('c', 'About 350,000 kilometres'), ('d', 'About 35,800 kilometres')], 'd'),
        ('Who described the idea of satellites that stay over one spot in 1945?',
         [('a', 'Arthur C. Clarke'), ('b', 'Isaac Newton'), ('c', 'Johannes Kepler'), ('d', 'Yuri Gagarin')], 'a'),
        ('Why does a geostationary satellite need thruster firings from time to time?',
         [('a', 'To keep it in its slot against small pulls'), ('b', 'To make it turn faster'), ('c', 'To stop it from making power'), ('d', 'To change its colour')], 'a'),
        ('What is the graveyard orbit used for?',
         [('a', 'A place where spare parts are stored'), ('b', 'A slightly higher place for worn-out satellites, which clears the slot'), ('c', 'A training orbit for new pilots'), ('d', 'A lower orbit for weather balloons')], 'b'),
        ('Why is the ring shared through international agreement?',
         [('a', 'Because the ring is inside the air'), ('b', 'Because the Moon owns the slots'), ('c', 'Because the slots are limited and crowding causes interference'), ('d', 'Because satellites cannot move')], 'c'),
    ],
}
