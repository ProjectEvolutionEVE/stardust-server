"""Optimising Interplanetary Trajectories: searching for the best launch and flight choices for a journey between planets."""
CODE = 'navigation5_interplanetary_optimisation'
BOOK = {
    "title": 'Optimising Interplanetary Trajectories',
    "subtitle": 'The search, cost functions, gradients, global optimisers, launch windows and results',
    "chapters": [
        ('The search',
         'Planners search through many possible launch dates, flight times and burns. The aim is to find the choices that give the best journey. The search is systematic, so no good option is missed.'),
        ('Cost functions',
         'A cost function is a formula that scores how good a trajectory is. It may count fuel, flight time or both. The search tries to make the score as good as possible.'),
        ('Gradients',
         'A gradient shows the direction in which the score improves most quickly. Following it step by step guides the search toward a better answer. Gradients are a key tool in local searches.'),
        ('Global optimisers',
         'A global optimiser searches widely so it does not get stuck in a poor answer. It tries many starting points or explores broadly. This takes more computing but gives more confidence in the best result.'),
        ('Launch windows',
         'A launch window is a period when the timing of launch and arrival gives a good trajectory. Planets line up favourably only at certain times. Missing a window can mean a long wait.'),
        ('Results',
         'The best result is checked with a more detailed model before it is used. Planners compare several good options as well as the best one. A sound choice also considers risk and margin.'),
    ],
    "test": [
        ('What is the search in trajectory optimisation?',
         [('a', 'A hunt for lost keys'), ('b', 'Searching a shop'), ('c', 'Looking for a window'), ('d', 'A systematic look for launch and flight choices that give the best result')], 'd'),
        ('What is a cost function?',
         [('a', 'A bill'), ('b', 'A formula that scores how good a trajectory is, such as fuel or time'), ('c', 'A shop price'), ('d', 'A sound')], 'b'),
        ('What is a gradient in this work?',
         [('a', 'A hill slope on a map only'), ('b', 'A colour'), ('c', 'The direction in which a score improves most quickly'), ('d', 'A sound level')], 'c'),
        ('What is a global optimiser?',
         [('a', 'A method that searches widely to avoid getting stuck in a poor answer'), ('b', 'A tool for cutting paper'), ('c', 'A kind of lamp'), ('d', 'A map colour')], 'a'),
        ('What is a launch window?',
         [('a', 'A glass window'), ('b', 'A shop window'), ('c', 'A period when launch and arrival timing give a good trajectory'), ('d', 'A computer window')], 'c'),
    ],
}
