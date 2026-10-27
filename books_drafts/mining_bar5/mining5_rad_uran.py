"""Radiation protection in uranium mines: radon, dose limits, ventilation, dust control, monitoring and worker records."""
CODE = 'mining5_rad_uran'
BOOK = {
    'title': 'Radiation Protection in Uranium Mines',
    'subtitle': 'Controlling radon, dust and dose so workers are kept safe',
    "chapters": [
        ('The hazard', 'Uranium ore gives off radon gas, and its dust can carry radioactive material. Controls keep both out of the air workers breathe.'),
        ('Radon', 'Radon is a radioactive gas. Its decay products can damage lung tissue if they are breathed in.'),
        ('Dose limits', 'Regulators set dose limits for workers. Mines plan their work so that workers stay well within those limits.'),
        ('Ventilation and dust', 'Ventilation dilutes radon and clears dust. Dust control also reduces the amount of particles breathed in.'),
        ('Monitoring', 'Air, dust and personal dosimeters are measured regularly. The results show whether the controls are working.'),
        ('Worker records', "Each worker's exposure is recorded over their working life. The record can be reviewed by the worker and by the regulator."),
    ],
    "test": [
        ('What is radon?', [('a', 'A metal used in wiring'), ('b', 'A radioactive gas'), ('c', 'A type of fuel'), ('d', 'A kind of rope')], 'b'),
        ('What does ventilation do for radon in a uranium mine?', [('a', 'Dilutes it and clears dust'), ('b', 'Makes it denser'), ('c', 'Turns it into ore'), ('d', 'Puts it into the water supply')], 'a'),
        ('What do regulators set for workers?', [('a', 'Shift colours'), ('b', 'Lunch menus'), ('c', 'Dose limits'), ('d', 'Tool prices')], 'c'),
        ('What is measured to check that the controls work?', [('a', 'Only the temperature of the canteen'), ('b', 'Only the number of trucks'), ('c', 'Only the length of the rope'), ('d', 'Air, dust and personal dosimeters')], 'd'),
        ("What is recorded over a worker's working life?", [('a', 'Their exposure'), ('b', 'Their favourite songs'), ('c', 'Their hobbies'), ('d', 'Their shoe size')], 'a'),
    ],
}
