"""Accelerated Life Testing: making parts age faster in the test rig, and knowing the limits of that trick."""
CODE = 'engineering3c_accelerated_life'
BOOK = {
    "title": 'Accelerated Life Testing',
    "subtitle": 'Making parts age faster in the test rig, and knowing the limits of that trick',
    "chapters": [
        ('Why speed it up',
         "A part may need years of field use before it fails. Accelerated life testing runs the part harder, hotter or more often, so that it fails in weeks instead. The results then tell you how it is likely to behave in normal use."),
        ('Heat speeds ageing',
         "Many failures are chemical, and chemical change speeds up with heat. A common rule of thumb says that a rise of about 10 degrees roughly doubles the rate of a chemical reaction. Engineers use this idea to estimate how much a higher test temperature shortens the life of a part."),
        ('Cycles and vibration',
         "Parts that flex or vibrate can be cycled faster on a test rig. Each cycle is one load and release, and the rig counts them. A fast rig can deliver thousands of cycles in an afternoon."),
        ('The big rule',
         "Accelerating a test is only safe if it does not change how the part fails. Too much heat can cause a failure that would never happen in service, such as melting a plastic that only softens in use. Check that the failure you find matches a failure seen in the field."),
        ('Reading the results',
         "Test several parts, not one, so you can see the spread of results. Record when each part failed and what broke. A failure you cannot explain means the test is not yet trusted."),
        ('Cost against risk',
         "A test rig costs money, but field failures cost more in repairs and lost work. Compare the cost of the test with the cost of a failure in service. A short test often pays for itself many times over."),
    ],
    "test": [
        ('Why run a life test faster?',
         [('a', 'To make parts cheaper'), ('b', 'To hide faults'), ('c', 'To see how a part will behave over years in a few weeks'), ('d', 'To avoid writing records')], 'c'),
        ('What rule of thumb is often used for heat and chemical change?',
         [('a', 'A rise of about 10 degrees roughly doubles the rate'), ('b', 'Heat stops all change'), ('c', 'Heat has no effect'), ('d', 'Only cold speeds change')], 'a'),
        ('What is one way parts that flex or vibrate can be aged faster?',
         [('a', 'By painting them'), ('b', 'By freezing them'), ('c', 'By storing them dry'), ('d', 'By cycling them more often on a test rig')], 'd'),
        ('What is the big rule of accelerated testing?',
         [('a', 'Always use the highest heat you can'), ('b', 'It is only safe if the accelerated test does not change how the part fails'), ('c', 'Never test more than one part'), ('d', 'Ignore the field records')], 'b'),
        ('Why test several parts, not just one?',
         [('a', 'To use more paint'), ('b', 'To make the test cheaper'), ('c', 'To see the spread of the results'), ('d', 'To hide failures')], 'c'),
    ],
}
