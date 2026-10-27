"""Neutron Scattering for Materials: using neutron beams to see magnetism and light atoms."""
CODE = 'mining5_neutron'
BOOK = {
    "title": 'Neutron Scattering for Materials',
    "subtitle": 'Seeing magnetism and light atoms with neutron beams',
    "chapters": [
        ('Why neutrons', 'A neutron has no electric charge, so it passes deep into materials without being stopped by the electrons. It scatters off atomic nuclei and off the tiny magnetic moments of atoms. This makes it a gentle and powerful probe.'),
        ('Magnetic structure', 'Neutrons carry a magnetic moment, so they scatter from the magnetic order in a material. This shows how the atomic spins line up, which X-rays cannot easily reveal. Scientists use this to study magnets and superconductors.'),
        ('Hydrogen sensitivity', 'Neutrons are very sensitive to light atoms such as hydrogen, which X-rays hardly see. This makes neutrons useful for studying water, fuel cell materials and plastics. Isotopes of the same element can also be told apart.'),
        ('Sources', 'Neutrons come from nuclear reactors or from spallation sources, where a beam of particles strikes a heavy metal target. Both produce neutrons that are then slowed and sent down beam lines. These sources are large and expensive.'),
        ('Diffractometers', 'A neutron diffractometer measures how neutrons scatter from a crystal, giving the positions of atoms and their magnetic order. The instrument turns the sample and records the pattern in many directions. Careful alignment gives the cleanest data.'),
        ('Samples and access', 'Neutron measurements often need a larger sample than X-ray work, because neutron beams are less intense. Access to the big sources is usually through a proposal process, shared among many scientists. Planning the sample early saves valuable beam time.'),
    ],
    "test": [
        ('Why can neutrons pass deep into a material?', [('a', 'They have no electric charge'), ('b', 'They are made of gold'), ('c', 'They are very slow and heavy'), ('d', 'They are blocked by all electrons')], 'a'),
        ('What can neutron scattering show that X-rays cannot easily show?', [('a', 'The colour of a sample'), ('b', 'The weight of the air'), ('c', 'How atomic magnetic spins line up'), ('d', 'The price of a metal')], 'c'),
        ('Which light atom do neutrons see well?', [('a', 'Lead'), ('b', 'Gold'), ('c', 'Platinum'), ('d', 'Hydrogen')], 'd'),
        ('What is one source of neutrons mentioned here?', [('a', 'A candle flame'), ('b', 'A nuclear reactor'), ('c', 'A garden hose'), ('d', 'A cooking stove')], 'b'),
        ('What does a neutron diffractometer measure?', [('a', 'The temperature of the room'), ('b', 'The sound of a sample'), ('c', 'How neutrons scatter from a crystal, showing atom positions'), ('d', 'The age of a coin')], 'c'),
    ],
}
