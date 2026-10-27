"""Transformers and self-attention: attention weights, queries, keys and values, multi-head attention, positional encoding, scaling and cost."""
CODE = 'computing5_transformers'
BOOK = {
    "title": 'Transformers and Self-Attention',
    "subtitle": 'How attention lets every word look at every other word at once',
    "chapters": [
        ('Attention',
         'Attention lets a model weigh how much each part of its input matters for each output. A word can look at the words around it and decide which ones matter most.'),
        ('Queries, keys and values',
         'Each word is turned into a query, a key and a value. Queries are compared with keys to get weights, and the weights mix the values.'),
        ('Multi-head attention',
         'Several attention heads run in parallel, each learning a different kind of link, such as grammar or meaning. Their results are combined.'),
        ('Positional encoding',
         'Attention alone does not know word order, so position information is added to each word. Without it, the model would see a bag of words.'),
        ('Scaling',
         'Research on scaling laws, from 2020 onward, found that performance improves in a fairly predictable way as models, data and compute grow. Training the largest models costs a great deal of computing power.'),
        ('Limits',
         'Attention compares every pair of positions, so cost grows quickly with long inputs. Engineers keep working on ways to lower this cost.'),
    ],
    "test": [
        ('What does attention do?',
         [('a', 'Weighs how much each part of the input matters'), ('b', 'Prints the input'), ('c', 'Deletes the input'), ('d', 'Turns input into sound')], 'a'),
        ('What are the three parts each word becomes?',
         [('a', 'Red, green and blue'), ('b', 'Input, output and paper'), ('c', 'Query, key and value'), ('d', 'Start, middle and end')], 'c'),
        ('What do multiple attention heads do?',
         [('a', 'Turn off the model'), ('b', 'Repeat the same link'), ('c', 'Print the heads'), ('d', 'Each learn a different kind of link')], 'd'),
        ('Why is positional encoding needed?',
         [('a', 'To change colours'), ('b', 'Attention alone does not know word order'), ('c', 'To store passwords'), ('d', 'To shrink the model to nothing')], 'b'),
        ('What do scaling laws describe?',
         [('a', 'How to build a ladder'), ('b', 'How to print money'), ('c', 'How performance grows with models, data and compute'), ('d', 'How to cool a room')], 'c'),
    ],
}
