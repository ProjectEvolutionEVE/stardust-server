"""Path Integration in Animals: how animals keep track of where they are by adding up the steps and turns they have made."""
CODE = 'navigation5_path_integration'
BOOK = {
    "title": 'Path Integration in Animals',
    "subtitle": 'The home vector, odometry, errors, desert ants, experiments and models',
    "chapters": [
        ('Keeping a running total',
         'Path integration is the way an animal tracks its position by adding up the steps and turns it has made. It works without needing landmarks, so it can be used in open country or in the dark.'),
        ('The home vector',
         'From its running total, an animal can compute a home vector, a straight line back to its starting point. Following this vector brings it home in a direct line, if the total is accurate.'),
        ('Odometry',
         'Odometry is the measure of distance travelled. Animals may count steps, limb movements or the flow of images past their eyes. Each method gives a rough measure, which adds up to a total with some error.'),
        ('Errors',
         'Every step adds a small error. Over a long path the errors build up, so the home vector drifts. Animals reduce this by using landmarks or other cues when they can.'),
        ('Desert ants',
         'Desert ants are a famous example. They leave their nest, search for food and then head straight back, even across featureless ground. Experiments show they use a running total of their movements.'),
        ('Experiments and models',
         'Experiments move animals to new places or change their steps, and then watch where they go. Models of the process predict the path, and comparing them with the data tests the idea.'),
    ],
    "test": [
        ('What is path integration?',
         [('a', 'Tracking position by adding up the steps and turns made'), ('b', 'Joining two rivers'), ('c', 'Sewing a coat'), ('d', 'Painting a map')], 'a'),
        ('What is a home vector?',
         [('a', 'A type of sail'), ('b', 'A kind of nest'), ('c', 'A map legend'), ('d', 'A straight line back to the starting point')], 'd'),
        ('Why does path integration drift over long paths?',
         [('a', 'Because animals stop walking'), ('b', 'Because small errors add up with each step'), ('c', 'Because the ground gets warmer'), ('d', 'Because the sun is bright')], 'b'),
        ('What do desert ants do after searching for food?',
         [('a', 'Stay where they found food'), ('b', 'Swim across the sea'), ('c', 'Head straight back to the nest using their running total'), ('d', 'Fly to the moon')], 'c'),
        ('How do scientists test a path integration model?',
         [('a', 'By painting the animals'), ('b', 'By comparing its predictions with what animals actually do'), ('c', 'By counting the clouds'), ('d', 'By weighing the sand')], 'b'),
    ],
}
