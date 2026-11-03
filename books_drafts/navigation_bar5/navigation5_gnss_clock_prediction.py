"""Predicting Satellite Clocks: the clock model, drift and ageing, prediction error, broadcast parameters, how users apply them and how updates are sent."""
CODE = 'navigation5_gnss_clock_prediction'
BOOK = {
    "title": 'Predicting Satellite Clocks',
    "subtitle": 'How ground stations forecast a satellite clock, and how your receiver uses the forecast',
    "chapters": [
        ('The clock model',
         'Each satellite clock is described by a simple model. The model has an offset, a rate and a rate of change of that rate. Ground stations fit these numbers to the measurements they receive.'),
        ('Drift and ageing',
         'Atomic clocks drift slowly, and their rate changes as they age. Temperature and radiation in space can also cause small changes. The model must follow these changes to stay accurate.'),
        ('Prediction error',
         'A forecast becomes less certain the further ahead it reaches. A prediction made several days ago is less accurate than one made today, so the broadcast is refreshed regularly.'),
        ('Broadcast parameters',
         'The satellite broadcasts the coefficients of its clock model inside its navigation message. Each receiver reads those numbers and uses them to correct the time signal from that satellite.'),
        ('The users',
         'A phone or a car receiver reads the navigation message, applies the clock correction, and then works out its position from the timing of signals from several satellites. The correction is essential to the answer.'),
        ('Updates',
         'Ground control uploads new predictions to each satellite regularly, often every day. This keeps the broadcast close to the true state of the clock.'),
    ],
    "test": [
        ('How is a satellite clock modelled?',
         [('a', 'With a picture of the clock'), ('b', 'With a simple polynomial of offset, rate and change of rate'), ('c', 'With a colour code'), ('d', 'With a paper map')], 'b'),
        ('What makes a clock prediction less accurate?',
         [('a', 'A sunny day'), ('b', 'A full moon'), ('c', 'A clear sky'), ('d', 'Looking further ahead in time')], 'd'),
        ('What does the satellite broadcast to users?',
         [('a', 'The clock model coefficients, inside its navigation message'), ('b', 'Live video of the ground'), ('c', 'A map of the Earth'), ('d', 'Music')], 'a'),
        ('What does a receiver do with the clock correction?',
         [('a', 'It ignores the correction'), ('b', 'It stores the correction for a year'), ('c', 'It applies the correction to the satellite time signal before working out position'), ('d', 'It sends the correction back to the satellite')], 'c'),
        ('How often do ground stations usually upload fresh predictions?',
         [('a', 'Regularly, often every day'), ('b', 'Once every ten years'), ('c', 'Never, after launch'), ('d', 'Exactly once an hour')], 'a'),
    ],
}
