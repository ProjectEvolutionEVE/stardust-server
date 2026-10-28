"""Discrete element modelling of grinding mills: particle contacts, charge motion, liner design, power draw and calibration."""
CODE = 'mining5_dem'
BOOK = {
    'title': 'Discrete Element Modelling of Mills',
    'subtitle': 'Simulating the grinding charge particle by particle',
    "chapters": [
        ('Particles as a crowd', "Discrete element modelling, or DEM, tracks many particles one by one. It follows each particle's contacts with its neighbours."),
        ('Contacts', 'Each contact has a force. The force depends on how hard the particles press together and on their material properties.'),
        ('Charge motion', 'The charge is the mix of grinding media and ore inside a mill. DEM shows how that charge moves as the mill turns.'),
        ('Liner design', 'The shape of the liners changes how the charge lifts and falls. Models help design liners that protect the shell and grind well.'),
        ('Power draw and calibration', 'Power draw is the power the mill uses. A model must be calibrated against measured data before it is trusted.'),
        ('Use', 'DEM lets designers test ideas cheaply before anything is built. Its results still have to be matched against what real mills do.'),
    ],
    "test": [
        ('What does DEM track?', [('a', 'Only the weight of the mill'), ('b', 'Only the colour of the ore'), ('c', 'Only the price of the power'), ('d', 'Many particles one by one')], 'd'),
        ('What does the force in a contact depend on?', [('a', 'The colour of the liner'), ('b', 'The day of the week'), ('c', 'How hard particles press together and their material properties'), ('d', 'The name of the operator')], 'c'),
        ('What is the charge in a mill?', [('a', 'The fuel in the truck'), ('b', 'The mix of grinding media and ore'), ('c', 'The water in the office'), ('d', 'The paint on the mill shell')], 'b'),
        ('What must a DEM model be before it is trusted?', [('a', 'Calibrated against measured data'), ('b', 'Printed in colour'), ('c', 'Shown on a large screen'), ('d', 'Sold to the market')], 'a'),
        ('Why are DEM results still checked against real mills?', [('a', 'Models must be proven against what real mills do'), ('b', 'Real mills have no data'), ('c', 'Models never need checking'), ('d', 'Mills are always too small to test')], 'a'),
    ],
}
