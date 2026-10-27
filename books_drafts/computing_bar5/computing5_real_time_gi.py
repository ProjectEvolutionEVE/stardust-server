"""Real-Time Global Illumination: approximate indirect light, drawn fast enough for games, within a fixed frame budget."""
CODE = 'computing5_real_time_gi'
BOOK = {
    "title": 'Real-Time Global Illumination',
    "subtitle": 'Indirect light, approximated within a frame budget',
    "chapters": [
        ('What indirect light is',
         'Indirect light is light that has bounced off one surface before reaching another. It fills shadows and gives scenes their soft, natural glow. Leaving it out makes a scene look flat and unreal.'),
        ('Light probes',
         'A light probe records the light arriving at a point in space. Nearby objects can borrow that light, which is much cheaper than tracing it again. Probes are placed through the scene and updated as needed.'),
        ('Screen-space methods',
         'Screen-space methods estimate indirect light using only what is already visible on the screen. They are fast and cheap. They fail when the needed information is off-screen or hidden behind other objects.'),
        ('Voxel cone tracing',
         'Voxel cone tracing stores the scene in a grid of voxels, each holding averaged light. Cones are traced through the grid to gather blurred light from many directions. It gives smooth results at a cost in memory and update time.'),
        ('Cost budgets',
         'A game has a fixed time for each frame, often sixteen or thirty-three milliseconds. Every lighting technique must fit inside its share of that budget. Developers measure and trim each technique to keep the game smooth.'),
        ('Hybrid techniques',
         'Most real games combine methods, using a cheap approximation in one place and a more costly one where it matters most. Hybrids balance quality against speed. The best result comes from knowing where players will look.'),
    ],
    "test": [
        ('What is indirect light?',
         [('a', 'Light that has bounced off one surface before reaching another'), ('b', 'Light from a torch held in the hand'), ('c', 'Light that is switched off'), ('d', 'Light used only in printing')], 'a'),
        ('What does a light probe record?',
         [('a', 'The number of players online'), ('b', 'The price of the game'), ('c', 'The light arriving at a point in space'), ('d', 'The sound of the music')], 'c'),
        ('What is a weakness of screen-space methods?',
         [('a', 'They cannot be used on any computer'), ('b', 'They fail when needed information is off-screen or hidden'), ('c', 'They make the frame rate zero'), ('d', 'They remove all colour')], 'b'),
        ("What does a game's frame budget limit?",
         [('a', 'The number of players in a team'), ('b', 'The price of the box'), ('c', 'The length of the story'), ('d', 'The time available to draw each frame')], 'd'),
        ('Why do many games use hybrid techniques?',
         [('a', 'To balance quality against speed where it matters most'), ('b', 'Because one technique can do everything for free'), ('c', 'Because hybrids need no testing'), ('d', 'Because screens cannot show light')], 'a'),
    ],
}
