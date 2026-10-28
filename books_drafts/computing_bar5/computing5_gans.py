"""Generative adversarial networks: generator and discriminator, training instability, mode collapse, evaluation and misuse risks."""
CODE = 'computing5_gans'
BOOK = {
    "title": 'Generative Adversarial Networks',
    "subtitle": 'Two networks trained against each other to produce realistic new examples',
    "chapters": [
        ('Two players',
         'A GAN has a generator that makes fake examples and a discriminator that tries to tell fake from real. The two are trained against each other.'),
        ('The contest',
         'The generator tries to fool the discriminator, and the discriminator tries to catch it. As both improve, the fakes become harder to tell from real data.'),
        ('Training is unstable',
         'The two networks can oscillate instead of settling, and training can fail. Careful design and tuning are needed to keep it stable.'),
        ('Mode collapse',
         'Sometimes the generator finds a few outputs that fool the discriminator and produces only those. This is called mode collapse, and it means little variety.'),
        ('Evaluating',
         'Judging the quality of generated examples is hard. Measures such as the Frechet Inception Distance compare the statistics of generated and real images.'),
        ('Uses and misuse',
         'GANs have been used for image synthesis and for adding training data. The same ability can make convincing forgeries, so misuse is a real concern.'),
    ],
    "test": [
        ('What does the discriminator do?',
         [('a', 'Tries to tell fake examples from real ones'), ('b', 'Prints the examples'), ('c', 'Stores the pictures'), ('d', 'Plays sounds')], 'a'),
        ('What is mode collapse?',
         [('a', 'The discriminator stops working'), ('b', 'The computer shuts down'), ('c', 'The data is deleted'), ('d', 'The generator produces only a few kinds of output')], 'd'),
        ('What is a known problem in GAN training?',
         [('a', 'Too much silence'), ('b', 'Instability, with the two networks oscillating'), ('c', 'Lack of colour'), ('d', 'Too many users')], 'b'),
        ('What does the Frechet Inception Distance do?',
         [('a', "Measures a room's temperature"), ('b', 'Counts the layers in a printer'), ('c', 'Compares statistics of generated and real images'), ('d', 'Shows the price of a file')], 'c'),
        ('What is a misuse risk of GANs?',
         [('a', 'Better sleep'), ('b', 'Faster printing'), ('c', 'Longer battery life'), ('d', 'Convincing forgeries')], 'd'),
    ],
}
