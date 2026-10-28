"""Recurrent networks and sequence models: hidden state, LSTM and GRU gates, sequence-to-sequence models, training through time and legacy use."""
CODE = 'computing5_sequence_models'
BOOK = {
    "title": 'Recurrent Networks and Sequence Models',
    "subtitle": 'Networks that carry a memory from one step of a sequence to the next',
    "chapters": [
        ('Order matters',
         'Words, sounds and sensor readings come in order, and meaning depends on what came before. Recurrent networks handle this by passing a hidden state from step to step.'),
        ('LSTM and GRU',
         'LSTM cells, described in 1997, use gates to decide what to keep and what to forget. GRUs, from 2014, are a simpler design with similar aims.'),
        ('Sequence to sequence',
         'A sequence-to-sequence model reads one sequence and writes another, such as translating a sentence. An encoder reads the input and a decoder writes the output.'),
        ('Training through time',
         'Training unrolls the network across the steps and passes errors back through time. Long sequences make this slow and can be unstable.'),
        ('Decline in use',
         'From 2017, transformer models began replacing recurrent networks in many tasks, because they process whole sequences in parallel. Recurrent designs are less common for new large models.'),
        ('Legacy systems',
         'Many older systems still run recurrent models, and engineers must still understand them to maintain and replace them.'),
    ],
    "test": [
        ('What does a recurrent network carry from step to step?',
         [('a', 'A hidden state'), ('b', 'A printed page'), ('c', 'A password'), ('d', 'A video game')], 'a'),
        ('What do LSTM gates decide?',
         [('a', 'Which colour to paint'), ('b', 'The price of data'), ('c', 'The name of the server'), ('d', 'What to keep and what to forget')], 'd'),
        ('What does a sequence-to-sequence model do?',
         [('a', 'Stores only pictures'), ('b', 'Reads one sequence and writes another'), ('c', 'Deletes sequences'), ('d', 'Plays music only')], 'b'),
        ('Why is training through time hard?',
         [('a', 'The model has no numbers'), ('b', 'There are no steps'), ('c', 'Long sequences are slow and can be unstable'), ('d', 'It needs no errors')], 'c'),
        ('When did transformers begin replacing recurrent networks in many tasks?',
         [('a', 'In 1850'), ('b', 'Only in 2000'), ('c', 'Never'), ('d', 'From 2017')], 'd'),
    ],
}
