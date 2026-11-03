"""Multiple Hypothesis Tracking: keeping several possible explanations open when the data is ambiguous."""
CODE = 'navigation5_multiple_hypothesis'
BOOK = {
    "title": 'Multiple Hypothesis Tracking',
    "subtitle": 'Ambiguous data, hypotheses, pruning, tracks, many objects and cost',
    "chapters": [
        ('Ambiguous data',
         'Sometimes one measurement could belong to more than one object. A radar blip near two aircraft does not say which one it came from. Tracking must cope with that doubt.'),
        ('Hypotheses',
         'A hypothesis is one possible explanation of which measurements belong to which objects. The tracker keeps several hypotheses alive at once. Each one gets a score based on how well it fits the data.'),
        ('Pruning',
         'The number of hypotheses grows quickly as new data arrives. Pruning removes the ones that are very unlikely or very similar. This keeps the tracker fast enough to run in real time.'),
        ('Tracks',
         'A track is the estimated path of one object over time. Each confirmed track follows one object through the data. A track that stops receiving matching data is eventually dropped.'),
        ('Many objects',
         'With many objects the number of possible matches becomes very large. The tracker must still choose the most sensible set. Good gating limits which measurements may be matched to which track.'),
        ('Cost',
         'The main cost of this method is computing power and memory. The careful work of keeping many hypotheses pays off when objects cross paths. Simpler trackers may be enough when objects are far apart.'),
    ],
    "test": [
        ('What makes data ambiguous in tracking?',
         [('a', 'A clear sky'), ('b', 'When one measurement could belong to more than one object'), ('c', 'A broken clock'), ('d', 'No measurements at all')], 'b'),
        ('What is a hypothesis in MHT?',
         [('a', 'A guess about the weather'), ('b', 'A type of sensor'), ('c', 'A map label'), ('d', 'One possible explanation of which measurements belong to which objects')], 'd'),
        ('Why does the tracker prune hypotheses?',
         [('a', 'To make them grow'), ('b', 'To delete the clock'), ('c', 'To keep the number of hypotheses manageable'), ('d', 'To hide the tracks')], 'c'),
        ('What is a track?',
         [('a', 'The estimated path of one object over time'), ('b', 'A railway'), ('c', 'A file name'), ('d', 'A sound')], 'a'),
        ('What is the main cost of MHT?',
         [('a', 'The paint'), ('b', 'The battery'), ('c', 'The number of hypotheses can grow quickly with many objects'), ('d', 'The screen size')], 'c'),
    ],
}
