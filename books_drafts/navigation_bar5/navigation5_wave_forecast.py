"""Wave Forecasting for Navigation: Knowing the sea before the ship meets it."""
CODE = 'navigation5_wave_forecast'
BOOK = {
    'title': 'Wave Forecasting for Navigation',
    'subtitle': 'Knowing the sea before the ship meets it',
    'chapters': [
        ('The sea is a mix of waves', 'At any moment the sea holds many waves of different sizes and lengths. A wave spectrum sorts that mix by frequency, showing how much energy each frequency carries.'),
        ('Wave models', 'Forecast models calculate how wind builds waves and how those waves travel across the ocean. They update the spectrum as the weather changes.'),
        ('Swell', 'Swell is a long, regular wave that travels far from the storm that made it. Swell can reach a coast long after the local wind has died down.'),
        ('Ship response', "A ship moves in waves depending on its size, speed and heading. Rolling and pitching depend on the wave period and the ship's own motion."),
        ('Accuracy', 'Forecasts are good for big waves but less exact for short waves and sudden changes. Crews compare forecasts with what they see on board.'),
        ('Routing', 'Weather routing picks a course that avoids the worst waves, saves fuel and keeps cargo and crew safe. Forecast wave data is one of its main inputs.'),
    ],
    'test': [
        ('What does a wave spectrum show?', [('a', 'The colour of the sea'), ('b', 'How much energy each wave frequency carries'), ('c', 'The number of crew'), ('d', 'The price of fuel')], 'b'),
        ('What is swell?', [('a', 'Long, regular waves that travel far from their storm'), ('b', 'Waves inside a harbour only'), ('c', 'Ice on the surface'), ('d', 'Calm water')], 'a'),
        ('What affects how a ship moves in waves?', [('a', 'Its paint colour'), ('b', 'The number of lamps'), ('c', 'Its size, speed and heading'), ('d', 'The name of the port')], 'c'),
        ('Forecasts are generally less exact for:', [('a', 'Big ocean swells'), ('b', 'Calm lakes'), ('c', 'Sunny days'), ('d', 'Short waves and sudden changes')], 'd'),
        ('What does weather routing aim to do?', [('a', 'Avoid the worst waves and save fuel'), ('b', 'Make waves bigger'), ('c', 'Stop all ships'), ('d', 'Find treasure')], 'a'),
    ],
}
