"""Time-Domain Transient Surveys: sky surveys that watch for things that change, how they sort the flashes, and how fast alerts let other telescopes follow up."""
CODE = 'science5_astro_transients'
BOOK = {
    "title": 'Time-Domain Transient Surveys',
    "subtitle": 'Watching the sky for things that change',
    "chapters": [
        ('Things that change',
         'Some objects in the sky flare, fade or move suddenly. These are transients. Time-domain surveys look for them by watching the same part of the sky again and again.'),
        ('Survey cadence',
         'Survey cadence is how often a survey revisits the same part of the sky. A fast cadence catches short events. A slow cadence misses them.'),
        ('Transient classification',
         'Transient classification sorts a flash into a type, such as a supernova, a flare or a moving asteroid. Classification uses colour, brightness changes and location. Each type needs its own follow-up.'),
        ('False positives',
         'Many detections are not real astronomical events. Passing satellites, camera faults and cosmic-ray hits can look like real events. False positives must be filtered out before follow-up.'),
        ('Alert systems',
         'Alert systems send fast notices to the community about new transients. Other telescopes can then study the event while it is still bright. Speed is the key to these alerts.'),
        ('Event rates',
         'An event rate is how many events of a type occur in a given volume and time. Event rates tell us how common rare explosions are. They help plan surveys and test theories.'),
    ],
    "test": [
        ('What is survey cadence?',
         [('a', 'The rhythm of music'), ('b', 'A type of drum'), ('c', 'The speed of a train'), ('d', 'How often a survey revisits the same part of the sky')], 'd'),
        ('What does transient classification do?',
         [('a', 'Sorts a flash in the sky into a type, such as a supernova or a flare'), ('b', 'Makes new stars'), ('c', 'Counts clouds'), ('d', 'Paints the sky')], 'a'),
        ('Why are false positives a problem in transient surveys?',
         [('a', 'They make the sky brighter'), ('b', 'They are useful for cooking'), ('c', 'Non-astronomical artifacts can look like real events, so they must be filtered out'), ('d', 'They have no effect')], 'c'),
        ('What are alert systems for?',
         [('a', 'Warning about rain'), ('b', 'Sending fast notices so other telescopes can follow up quickly'), ('c', 'Ringing bells in observatories'), ('d', 'Sending emails to friends')], 'b'),
        ('What is an event rate?',
         [('a', 'The price of events'), ('b', 'A speed limit'), ('c', 'How many events of a type occur in a given volume and time'), ('d', 'A type of camera')], 'c'),
    ],
}
