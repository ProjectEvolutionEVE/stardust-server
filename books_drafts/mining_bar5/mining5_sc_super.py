"""Single Crystal Superalloys: turbine blades cast as one crystal, so they hold their shape at the highest temperatures."""
CODE = 'mining5_sc_super'
BOOK = {
    "title": 'Single Crystal Superalloys',
    "subtitle": 'Turbine blades cast as one crystal, for the hottest parts of an engine',
    "chapters": [
        ('Why one crystal', 'A turbine blade in a jet engine sees very high heat and stress. Grain boundaries are weak points at high temperature. Casting the blade as one single crystal removes them.'),
        ('Crystal growth', 'The blade is cast so that a single crystal grows from one end. Special furnaces and starter sections control the growth. The result is a blade with no grain boundaries to crack.'),
        ('Lattice mismatch', 'The two phases in a superalloy have slightly different crystal spacings, called lattice mismatch. The mismatch affects how the phases pack and how the alloy deforms. Alloy designers balance it carefully.'),
        ('Rafting', 'Under heat and stress, the strengthening particles can line up into rafts. Rafting changes the way the alloy deforms. Controlling it is part of the design.'),
        ('Creep', 'At very high temperature, blades slowly creep under load. Single crystals resist creep better than cast blades with grain boundaries. Creep life is one of the main tests for a new alloy.'),
        ('Alloy design', 'Single crystal alloys are based on nickel with additions of many elements. Each addition is chosen to tune strength, oxidation resistance and the phase balance. Designers test many combinations before choosing one.'),
    ],
    "test": [
        ('Why are single crystal blades used?', [('a', 'Grain boundaries, which are weak at high temperature, are removed'), ('b', 'They are cheaper to paint'), ('c', 'They are lighter than air'), ('d', 'They make the engine louder')], 'a'),
        ('What is lattice mismatch?', [('a', 'A mismatch of shoes'), ('b', 'A small difference in crystal spacing between two phases'), ('c', 'A mismatch of paint colours'), ('d', 'A mistake in a menu')], 'b'),
        ('What is rafting?', [('a', 'Boats on a lake'), ('b', 'A kind of swimming'), ('c', 'Strengthening particles lining up into rafts under heat and stress'), ('d', 'A paper toy')], 'c'),
        ('What does creep mean for a blade?', [('a', 'A quick snap'), ('b', 'A bright flash'), ('c', 'A sudden shine'), ('d', 'Slow stretching under load at very high temperature')], 'd'),
        ('What is the usual base metal of these superalloys?', [('a', 'Nickel'), ('b', 'Sugar'), ('c', 'Wood'), ('d', 'Cotton')], 'a'),
    ],
}
