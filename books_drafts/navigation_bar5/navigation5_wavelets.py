"""Wavelets for Sensor Signals: how a signal is studied at several scales at once, and how it is cleaned of noise."""
CODE = 'navigation5_wavelets'
BOOK = {
    "title": 'Wavelets for Sensor Signals',
    "subtitle": 'Time-frequency analysis, multiresolution, denoising, sensor data and choice',
    "chapters": [
        ('Two views of a signal',
         'A signal can be looked at over time, or by the frequencies it contains. Some events are short and sharp, and others are slow and steady. A good tool must show both.'),
        ('Time and frequency together',
         'Wavelets are small wave shapes that are stretched and shifted along a signal. They show when a frequency happens as well as what the frequency is. This is useful for signals that change over time.'),
        ('Multiresolution',
         'Multiresolution means looking at a signal at many scales, from coarse to fine. Coarse levels show the overall trend and fine levels show the detail. Each level can be studied on its own.'),
        ('Denoising',
         'Noise often shows up as small, fine detail. By reducing the small wavelet coefficients, the noise is removed while the main shape is kept. The choice of cutoff decides how much is removed.'),
        ('Sensor data',
         'Sensors on ships, vehicles and instruments produce noisy signals with sudden events. Wavelet methods can clean these signals and find the events, such as a jolt or a sudden change in reading.'),
        ('Choosing and using wavelets',
         'Different wavelet shapes suit different signals, so the choice matters. A poor choice can blur real events or leave noise behind. Testing on known data helps make the right choice.'),
    ],
    "test": [
        ('What two views of a signal are combined in wavelet analysis?',
         [('a', 'Colour and size'), ('b', 'Time and frequency'), ('c', 'Price and weight'), ('d', 'Left and right')], 'b'),
        ('What does multiresolution mean?',
         [('a', 'Looking at a signal at many scales, from coarse to fine'), ('b', 'Using many screens at once'), ('c', 'Printing the signal twice'), ('d', 'Doubling the volume')], 'a'),
        ('How does wavelet denoising usually remove noise?',
         [('a', 'By adding more noise'), ('b', 'By painting the signal'), ('c', 'By shrinking the small coefficients that carry fine noise'), ('d', 'By removing the time')], 'c'),
        ('What kind of event can wavelets help find in sensor data?',
         [('a', 'The name of the sensor'), ('b', 'The price of the sensor'), ('c', 'The colour of the box'), ('d', 'A sudden jolt or change in reading')], 'd'),
        ('What happens if the wavelet shape is a poor choice?',
         [('a', 'It can blur real events or leave noise behind'), ('b', 'It always improves the signal'), ('c', 'It makes the sensor cheaper'), ('d', 'It changes the weather')], 'a'),
    ],
}
