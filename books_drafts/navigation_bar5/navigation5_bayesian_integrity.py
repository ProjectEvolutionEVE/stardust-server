"""Bayesian Integrity Risk: how a navigation system proves it will not mislead the people who trust it."""
CODE = 'navigation5_bayesian_integrity'
BOOK = {
    "title": 'Bayesian Integrity Risk',
    "subtitle": 'Hazardous error probability, risk allocation, alert limits, monitoring, uncertainty and standards',
    "chapters": [
        ('The probability of hazardous error',
         'Integrity asks a simple question. How likely is it that the system gives a wrong position and does not warn the user? That probability is the integrity risk, and it must be very small.'),
        ('Risk allocation',
         'The total risk allowed is split among the parts of the system. Each part gets a share, such as a share for each sensor and for each mode of operation. The shares must add up to no more than the total.'),
        ('Alert limits',
         'An alert limit is the error size beyond which the user must be warned. If the uncertainty is larger than the limit, the system raises an alert. The limit is chosen to match what the user can safely tolerate.'),
        ('Monitoring',
         'The system keeps checking itself while it runs. It compares its measurements with each other and with its model. If a check fails, the system flags the position as unsafe.'),
        ('Uncertainty',
         'Integrity needs an honest estimate of how uncertain the position is. If the uncertainty is too small, the system may miss a real danger. Bayesian methods combine prior knowledge with new data to produce that estimate.'),
        ('Standards',
         'Standards set the level of safety that must be shown before a system can be used. Aviation and maritime users follow published requirements for this. A design is tested against them before it is approved.'),
    ],
    "test": [
        ('What is integrity risk?',
         [('a', 'The risk of losing a phone'), ('b', 'The risk of running out of fuel'), ('c', 'The probability that the system gives a hazardous, misleading position without warning'), ('d', 'The risk of traffic')], 'c'),
        ('What is risk allocation?',
         [('a', 'Sharing out pay'), ('b', 'Choosing paint colours'), ('c', 'Dividing up a seat plan'), ('d', 'Splitting an allowed total risk among the parts of a system')], 'd'),
        ('What is an alert limit?',
         [('a', 'A speed limit'), ('b', 'The error size beyond which the user must be warned'), ('c', 'A number of satellites'), ('d', 'The price of a sensor')], 'b'),
        ('Why does a standard matter for integrity?',
         [('a', 'It sets the level of safety that must be shown'), ('b', 'It sets the price of the user\'s car'), ('c', 'It fixes the colour of a map'), ('d', 'It stops sensors from working')], 'a'),
        ('Why is honest uncertainty important for integrity?',
         [('a', 'It makes errors disappear'), ('b', 'It lets people skip checks'), ('c', 'It is needed to judge whether a position can be trusted'), ('d', 'It only matters for the weather')], 'c'),
    ],
}
