"""Atomic Clocks and Precision Timekeeping: atomic transitions, the caesium standard, optical clocks, clock stability, relativistic shifts and time transfer."""
CODE = 'science5_phys_clocks'
BOOK = {
    "title": 'Atomic Clocks and Precision Timekeeping',
    "subtitle": 'Keeping time with the steady beat of atoms',
    "chapters": [
        ('Time from atoms',
         'An atomic clock keeps time by counting the oscillations of light or microwaves that match a very stable transition inside an atom. Because every atom of the same type behaves the same way, the beat is the same everywhere.'),
        ('The caesium standard',
         'Since 1967, the second has been defined by the caesium-133 atom. One second is the time for 9,192,631,770 cycles of the microwave transition between two of its hyperfine levels. This definition is the basis of time worldwide.'),
        ('Optical clocks',
         'Optical clocks use transitions at higher frequencies, in the range of visible light. Because they tick many more times per second, they can be far more precise. Several optical clocks now beat the caesium standard in stability.'),
        ('Clock stability',
         'Stability means how well a clock keeps the same rate over time. Engineers measure it with the Allan deviation, which compares tick rates over different averaging times. A good clock drifts by very little over long periods.'),
        ('Relativistic shifts',
         'Clocks run at different rates depending on their speed and their height in a gravitational field. A clock on a mountain runs slightly faster than one at sea level. Precise clocks can measure these shifts, which confirm general relativity.'),
        ('Time transfer',
         "Time transfer compares clocks over long distances, using satellite signals or optical fibres. Accurate transfer keeps the world's clocks aligned, supports navigation, and helps test physics across distant sites."),
    ],
    "test": [
        ('What does an atomic clock count?',
         [('a', 'Raindrops on a window'), ('b', 'Footsteps on a stair'), ('c', 'Coins in a jar'), ('d', 'Oscillations of light or microwaves from a stable atomic transition')], 'd'),
        ('Which atom defines the second since 1967?',
         [('a', 'Caesium-133'), ('b', 'Gold'), ('c', 'Helium'), ('d', 'Lead')], 'a'),
        ('Why can optical clocks be more precise?',
         [('a', 'They are made of wood'), ('b', 'They have no moving parts because they are slow'), ('c', 'They use only sound waves'), ('d', 'They tick many more times per second, at visible light frequencies')], 'd'),
        ("What does a clock's stability describe?",
         [('a', 'How tall it stands'), ('b', 'How well it keeps the same rate over time'), ('c', 'How bright its face is'), ('d', 'How heavy it weighs')], 'b'),
        ('What do relativistic shifts show?',
         [('a', 'Clocks always run at the same rate everywhere'), ('b', 'Clocks run at different rates depending on speed and gravity'), ('c', 'Clocks stop at night'), ('d', 'Clocks only run on sunny days')], 'b'),
    ],
}
