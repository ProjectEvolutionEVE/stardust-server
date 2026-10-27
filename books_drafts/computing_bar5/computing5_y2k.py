"""Y2K: The Millennium Bug: two-digit years, remediation effort, cost estimates, readiness, lessons on legacy code and myths."""
CODE = 'computing5_y2k'
BOOK = {
    "title": 'Y2K: The Millennium Bug',
    "subtitle": 'Two-digit years, a big deadline, and the work that prevented trouble',
    "chapters": [
        ('Two-digit years',
         'For decades many programs stored years with only two digits, such as 98 for 1998, to save costly memory and storage. The practice was common and reasonable at the time. As the year 2000 approached, it threatened to misread dates.'),
        ('Remediation effort',
         'Organisations around the world searched their systems, changed how dates were handled, and tested the results. Much of the work involved old code that few people still fully understood. It was a huge, coordinated effort.'),
        ('Cost estimates',
         'Estimates of the total cost of preparing ran into many billions of dollars worldwide. Much of that money paid for work needed to keep banks, utilities and other essential services running.'),
        ('Readiness',
         'Many organisations and governments drew up contingency plans and checked essential services in advance. When the date arrived, most systems carried on normally. Some people later mistook that calm for proof the threat had been exaggerated.'),
        ('Lessons on legacy code',
         'The episode showed how long-lived code and data formats can outlive the people who wrote them. Hidden assumptions can persist for decades. Documentation and regular review are part of the true cost of software.'),
        ('Myths',
         'Predictions of total collapse did not come true, but that does not mean the risk was imaginary. Preparation is what made the calm outcome possible. Both the myths and the hard work are part of the story.'),
    ],
    "test": [
        ('Why were many programs written with two-digit years?',
         [('a', 'Because computers could not show numbers'), ('b', 'Because the year 2000 was banned'), ('c', 'To save costly memory and storage'), ('d', 'Because of a contract with a printer')], 'c'),
        ('What did the Y2K remediation work mainly involve?',
         [('a', 'Searching systems, changing date handling, and testing'), ('b', 'Painting office walls'), ('c', 'Recruiting actors for television'), ('d', 'Replacing all the electricity cables')], 'a'),
        ('What was true of the cost estimates?',
         [('a', 'They were zero'), ('b', 'They were under one thousand dollars'), ('c', 'They were set by a single clerk'), ('d', 'They ran into many billions of dollars worldwide')], 'd'),
        ('Why did some people later think the threat was exaggerated?',
         [('a', 'Because the systems were all switched off'), ('b', 'Because most systems carried on normally after the date passed'), ('c', 'Because no one had checked anything'), ('d', 'Because calendars were printed in colour')], 'b'),
        ('What did the episode show about legacy code?',
         [('a', 'It never outlives its authors'), ('b', 'It cannot store dates at all'), ('c', 'It can outlive its authors, with hidden assumptions lasting for decades'), ('d', 'It is always easy to understand')], 'c'),
    ],
}
