"""Audio Cues for Wayfinding: how sound can guide people through places, and how such cues are designed and tested."""
CODE = 'navigation5_audio_wayfinding'
BOOK = {
    "title": 'Audio Cues for Wayfinding',
    "subtitle": 'Sound beacons, spatialised audio, speech, privacy, design and testing',
    "chapters": [
        ('Sound as a guide',
         'Sound can tell people where to go, especially when they cannot see signs. Audio cues can supplement signs and maps. They work well in busy places where a sign may be hard to spot.'),
        ('Sound beacons',
         'A sound beacon is a fixed source that repeats a short tone or pattern. Listeners can find its direction by hearing it. Beacons placed at entrances, crossings and exits help people locate them.'),
        ('Spatialised audio',
         'Spatialised audio makes a sound seem to come from a particular direction. Using timing and loudness differences between the ears, the sound can guide a person toward a point. The effect needs careful setup to work well.'),
        ('Speech',
         'Spoken directions can give clear information, such as the next stop or the way out. Speech must be short, slow enough to follow and loud enough to hear over background noise.'),
        ('Privacy',
         'Audio guidance can reveal where someone is going to others nearby. Designers should consider what is said aloud and whether the system needs to know personal details at all.'),
        ('Design and testing',
         'Audio cues should be tested in the real place, with the real noise levels. Testing with people who use the system shows whether the cues are heard, understood and useful.'),
    ],
    "test": [
        ('What can audio cues help people do?',
         [('a', 'Find their way when signs are hard to see'), ('b', 'Grow plants faster'), ('c', 'Cook a meal'), ('d', 'Print a book')], 'a'),
        ('What is a sound beacon?',
         [('a', 'A type of lamp for ships'), ('b', 'A kind of radio station'), ('c', 'A fixed source that repeats a tone or pattern to show its position'), ('d', 'A bell in a church only')], 'c'),
        ('How does spatialised audio make a sound seem to come from a direction?',
         [('a', 'Using paint on the speaker'), ('b', 'Using a bigger speaker only'), ('c', 'Using the colour of the room'), ('d', 'Using timing and loudness differences between the ears')], 'd'),
        ('What makes spoken directions easier to follow?',
         [('a', 'Long speeches with no pauses'), ('b', 'Short, clear phrases spoken slowly enough to follow'), ('c', 'Whispers only'), ('d', 'Music with no words')], 'b'),
        ('Why should designers think about privacy in audio guidance?',
         [('a', 'Because sound is always invisible'), ('b', 'Because speakers are always private'), ('c', 'Because others nearby may hear where a person is going'), ('d', 'Because privacy has no effect')], 'c'),
    ],
}
