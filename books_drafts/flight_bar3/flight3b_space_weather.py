"""Watches and Warnings: how space weather is forecast, why flares and storms arrive at different times, and what a pilot does about each."""
CODE = 'flight3b_space_weather'
BOOK = {
    "title": 'Watches and Warnings',
    "subtitle": 'How space weather is forecast, and what a pilot does about each warning',
    "chapters": [
        ('Forecasters watch the Sun',
         'Space weather forecasters watch the Sun, the solar wind and the magnetic field around Earth. They issue watches when a storm may come and warnings when one is on the way. A watch is a time to prepare, and a warning is a time to act.'),
        ('Flares arrive fast',
         'A solar flare sends light and X-rays toward Earth, and they arrive in about eight minutes. That gives almost no warning, so the flare itself cannot be planned around. Its effects, such as radio blackouts on the sunlit side, must be handled as they happen.'),
        ('Storms arrive later',
         'A coronal mass ejection is a huge cloud of solar material. It usually takes one to three days to reach Earth, which gives time to plan. Its particles and magnetic effects can disturb radio, navigation signals and power systems.'),
        ('Three scales',
         'The United States Space Weather Prediction Center rates radio blackouts, solar radiation storms and geomagnetic storms on scales from 1 to 5. A higher number means a stronger effect. Learn the scales, so a warning tells you what to expect.'),
        ('What to do',
         'When a watch is issued, check the crew, the fuel and the schedule, and pause long burns that would keep you exposed. When a warning is issued, move the crew to the most shielded part of the craft, and keep to the plan that you wrote before the storm.'),
        ('Plan before the weather',
         'Keep a short list of what to do for each scale, and read it before you fly, not during a storm. A pilot who has a plan can act calmly when the warning comes.'),
    ],
    "test": [
        ('What is the difference between a space weather watch and a warning?',
         [('a', 'A watch is a list of prices'), ('b', 'A watch means a storm may come, and a warning means one is on the way'), ('c', 'A warning is a type of fuel'), ('d', 'They are the same thing')], 'b'),
        ('About how long does a solar flare take to reach Earth?',
         [('a', 'About eight months'), ('b', 'About eight days'), ('c', 'About eight minutes'), ('d', 'About eight hours')], 'c'),
        ('About how long does a coronal mass ejection usually take to reach Earth?',
         [('a', 'It never reaches Earth'), ('b', 'Less than a second'), ('c', 'About a year'), ('d', 'One to three days')], 'd'),
        ('What does a higher number on a space weather scale mean?',
         [('a', 'A stronger effect'), ('b', 'A weaker effect'), ('c', 'A shorter day'), ('d', 'A cheaper lease')], 'a'),
        ('What should the crew do when a storm warning is issued?',
         [('a', 'Go out to watch the storm'), ('b', 'Move to the most shielded part of the craft and keep to the plan'), ('c', 'Start every long burn at once'), ('d', 'Switch off the radio and sleep in the open')], 'b'),
    ],
}
