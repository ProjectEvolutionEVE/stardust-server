"""Storm Surge Forecasting: predicting how wind and pressure raise the sea, and what that means for ships and coasts."""
CODE = 'navigation5_storm_surge'
BOOK = {
    "title": 'Storm Surge Forecasting',
    "subtitle": 'Wind setup, pressure effects, coastal flooding, models, forecast uncertainty and navigation impact',
    "chapters": [
        ('Wind setup',
         'Wind blowing across the sea pushes the water ahead of it. The water piles up on the downwind shore. This wind setup can raise the sea level by a large amount in a strong storm.'),
        ('Pressure effects',
         'Low air pressure lets the sea surface rise a little. This is called the inverse barometer effect. A deep storm therefore adds to the surge.'),
        ('Coastal flooding',
         'A surge rising on top of the tide can flood low coasts and harbours. The timing matters, because a surge at high tide is the most dangerous. Forecasts help people prepare in time.'),
        ('Models',
         'Forecast models combine wind, pressure, tide and the shape of the coast. They are run on computers with the latest weather data. Their results are compared with observed water levels.'),
        ('Forecast uncertainty',
         'The storm track and wind strength can change at short notice. A forecast therefore carries a range of likely levels. Honest forecasts show that range, not just one number.'),
        ('Navigation impact',
         'Surges can change water depths and the safe width of channels. Ships may need to wait or change course. Harbour pilots and ship crews use forecasts to plan safe passage.'),
    ],
    "test": [
        ('What is wind setup?',
         [('a', 'Hair style'), ('b', 'Water piled up by wind blowing across a sea or lake'), ('c', 'A sail'), ('d', 'A shop')], 'b'),
        ('What is the inverse barometer effect?',
         [('a', 'A broken glass'), ('b', 'A baking method'), ('c', 'A fish trap'), ('d', 'A rise in sea level under low air pressure')], 'd'),
        ('What causes coastal flooding in a surge?',
         [('a', 'A surge rising on top of the tide'), ('b', 'Clear skies'), ('c', 'Warm bread'), ('d', 'Quiet waters')], 'a'),
        ('What uncertainty do surge forecasts have?',
         [('a', 'None'), ('b', 'Only in the colour'), ('c', 'The storm track and wind can change, so forecasts carry a range'), ('d', 'Only in the time')], 'c'),
        ('How can a surge affect navigation?',
         [('a', 'It helps ships fly'), ('b', 'It adds paint'), ('c', 'It lowers the sun'), ('d', 'It can change water depths and channel safety')], 'd'),
    ],
}
