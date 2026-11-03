"""Star Clusters and Stellar Populations: groups of stars born together, how their light is modelled, and what they reveal about the ages of stars."""
CODE = 'science5_astro_clusters'
BOOK = {
    "title": 'Star Clusters and Stellar Populations',
    "subtitle": 'Families of stars born together',
    "chapters": [
        ('Open and globular',
         'Open clusters are loose groups of young stars, often found in the galactic disc. Globular clusters are dense balls of old stars that orbit the galaxy. The two types tell very different stories.'),
        ('Stellar population synthesis',
         'Stellar population synthesis builds a model of a cluster\'s light by adding up many stars of different masses and ages. The model is compared with the cluster\'s measured light. A good match confirms our picture of the stars.'),
        ('Ages from turnoffs',
         'On a colour-magnitude diagram, stars leave the main sequence at a point called the turnoff. The brightness of the turnoff reveals the cluster\'s age. Older clusters have turnoffs at lower brightness.'),
        ('The initial mass function',
         'The initial mass function describes the spread of masses with which stars form. Most stars are low-mass, and only a few are massive. Knowing this spread is essential for counting stars and predicting their light.'),
        ('Cluster dynamics',
         'Gravity pulls the stars in a cluster together, and close encounters between them change their orbits. Over time, clusters lose stars and spread out. This slow evolution is called cluster dynamics.'),
        ('Population models',
         'Models of stellar populations combine stellar evolution, the mass function and the cluster\'s age. They predict how colour and brightness change over time. These models are used across astronomy.'),
    ],
    "test": [
        ('What is the difference between open and globular clusters?',
         [('a', 'Open clusters are loose and young, and globular clusters are dense and old'), ('b', 'Open clusters are made of ice'), ('c', 'Globular clusters are bigger than galaxies'), ('d', 'They are the same thing')], 'a'),
        ('What is stellar population synthesis?',
         [('a', 'Counting planets around stars'), ('b', 'Making a cluster from scratch'), ('c', 'Reading a menu'), ('d', 'Building a model of a cluster\'s light by adding up stars of different masses and ages')], 'd'),
        ('What does the turnoff point on a colour-magnitude diagram reveal?',
         [('a', 'Turnoffs stop the stars from shining'), ('b', 'Turnoffs show the cluster\'s distance only'), ('c', 'The cluster\'s age'), ('d', 'Turnoffs are where comets form')], 'c'),
        ('What is the initial mass function?',
         [('a', 'The price of stars'), ('b', 'The spread of masses with which stars form'), ('c', 'The colour of the dust'), ('d', 'The speed of light in a cluster')], 'b'),
        ('What drives changes in a cluster over time?',
         [('a', 'Music played near clusters'), ('b', 'Gravity pulling stars together and close encounters between them'), ('c', 'Heat from the Moon'), ('d', 'Paint on telescopes')], 'b'),
    ],
}
