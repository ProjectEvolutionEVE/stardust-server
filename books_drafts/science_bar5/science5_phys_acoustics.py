"""Acoustics and Wave Propagation: sound speed, acoustic impedance, reflection and absorption, room acoustics, ultrasonic testing and nonlinear acoustics."""
CODE = 'science5_phys_acoustics'
BOOK = {
    "title": 'Acoustics and Wave Propagation',
    "subtitle": 'How sound travels, bounces and fades through materials and rooms',
    "chapters": [
        ('Sound as a wave',
         'Sound is a wave of pressure that travels through a material. It needs a medium such as air, water or metal to move. The speed depends on how stiff and how dense the medium is.'),
        ('Speed of sound',
         'In dry air at room temperature, sound travels at about 343 metres per second. It is faster in water and faster still in most solids. Temperature changes the speed in air, which is why sound carries differently on hot and cold days.'),
        ('Acoustic impedance',
         'Acoustic impedance measures how much a medium resists the flow of sound. When a wave meets a boundary between two materials with different impedance, part of it reflects. The bigger the mismatch, the more reflects.'),
        ('Reflection and absorption',
         'Hard, smooth surfaces reflect sound, while soft, porous materials absorb it. Acoustic foam and thick curtains absorb energy, turning it into small amounts of heat. Designers choose materials to control echoes.'),
        ('Room acoustics',
         'In a room, sound bounces many times, and the reverberation time describes how long it lingers. Concert halls aim for a balance, so music sounds clear and full. Too much echo blurs speech.'),
        ('Ultrasonic testing',
         'Ultrasound is sound above the range of human hearing. Engineers send ultrasonic pulses into metal or concrete and read the echoes. The pattern of reflections reveals cracks and flaws inside the material without cutting it open.'),
    ],
    "test": [
        ('What does sound need in order to travel?',
         [('a', 'Empty space only'), ('b', 'Bright light'), ('c', 'A medium such as air, water or metal'), ('d', 'A magnetic field')], 'c'),
        ('About how fast does sound travel in dry air at room temperature?',
         [('a', 'About 3 metres per second'), ('b', 'About 343 metres per second'), ('c', 'About 3 million metres per second'), ('d', 'It does not move at all')], 'b'),
        ('What does acoustic impedance measure?',
         [('a', 'How bright a room looks'), ('b', 'How many people sit in a hall'), ('c', 'How much a medium resists the flow of sound'), ('d', 'How cold a wall is')], 'c'),
        ('Which materials absorb sound best?',
         [('a', 'Soft, porous materials'), ('b', 'Smooth metal sheets'), ('c', 'Mirror glass'), ('d', 'Polished stone floors')], 'a'),
        ('What is ultrasonic testing used for?',
         [('a', 'Making music louder'), ('b', 'Cooking food in a pan'), ('c', 'Measuring the weight of bricks'), ('d', 'Finding flaws inside materials by reading echoes')], 'd'),
    ],
}
