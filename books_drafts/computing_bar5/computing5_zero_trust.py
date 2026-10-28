"""Zero trust architecture: no implicit trust from network location, identity and device checks, least privilege and continuous verification."""
CODE = 'computing5_zero_trust'
BOOK = {
    "title": 'Zero Trust Architecture',
    "subtitle": 'Never trust by default: check identity, device and access every time',
    "chapters": [
        ('The old idea',
         'For years, many companies built a wall around their network. Anyone inside the wall was trusted, and anyone outside was not. Once an attacker got past the wall, they could often move around freely.'),
        ('The new rule',
         'Zero trust starts from one rule: never trust a request just because of where it comes from. Every user, device and service must prove who it is each time it asks for something.'),
        ('Least privilege',
         'Each person and program gets only the access it needs for its job, and no more. Access is narrow, so a stolen login opens fewer doors.'),
        ('Checking the device',
         'A zero trust system also looks at the device. Is it up to date, encrypted, and known to the company? A trusted person on an unsafe device can still be refused.'),
        ('Continuous checks',
         'Trust is not granted once and kept forever. The system watches for changes, such as a login from an unusual place or a sudden burst of downloads, and can ask for a new check or cut access.'),
        ('Migration and limits',
         'Few firms switch at once. They start with their most important systems and move step by step. Zero trust does not remove every risk, and older equipment and habits can make it hard to put in place.'),
    ],
    "test": [
        ('What is the core rule of zero trust?',
         [('a', 'Trust everyone inside the company network'), ('b', 'Never trust a request just because of where it comes from'), ('c', 'Trust only people who work in the head office'), ('d', 'Trust a device forever after one check')], 'b'),
        ('What does least privilege mean?',
         [('a', 'Everyone gets full access to save time'), ('b', 'Access is limited to what each person or program needs'), ('c', 'Only the boss can open files'), ('d', 'Access is removed after one day')], 'b'),
        ('Why does zero trust check the device as well as the person?',
         [('a', 'Devices never break'), ('b', 'Devices are always cheaper to replace'), ('c', 'A device is only a screen'), ('d', 'A trusted person on an unsafe device can still cause harm')], 'd'),
        ('Why are continuous checks used?',
         [('a', 'To make logins slower for fun'), ('b', 'To print reports'), ('c', 'Trust can change, so access is checked again over time'), ('d', 'To replace passwords with keys made of paper')], 'c'),
        ('Why do many firms move to zero trust one step at a time?',
         [('a', 'Older systems and habits make a full switch hard'), ('b', 'Zero trust is banned from big changes'), ('c', 'The network is unplugged'), ('d', 'Staff are not allowed to log in')], 'a'),
    ],
}
