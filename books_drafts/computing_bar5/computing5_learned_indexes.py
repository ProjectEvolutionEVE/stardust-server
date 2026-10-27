"""Learned indexes: predicting key positions with models, error bounds, fallback search, updates and trade-offs."""
CODE = 'computing5_learned_indexes'
BOOK = {
    "title": 'Learned Indexes',
    "subtitle": 'Using a small model to guess where a key sits, then searching a little around the guess',
    "chapters": [
        ('The old way',
         'A classic index, such as a B-tree, finds a value by following a set of signposts down a tree. It works well and is used everywhere.'),
        ('A different idea',
         'A learned index uses a small model that learns how the keys are spread out. Given a key, the model predicts roughly where it sits in a sorted list.'),
        ('Error bounds',
         'The model is not exact, so the system stores the largest miss it has seen. The search then only looks within that small window around the guess.'),
        ('Fallback search',
         'When a key falls outside what the model handles well, the system falls back to a normal search. The result is still correct, only slower.'),
        ('Updates are hard',
         'Inserting new keys can shift many positions, which makes the model out of date. Research systems handle this with buffers and retraining, which adds complexity.'),
        ('Trade-offs',
         'A widely read 2018 paper showed learned indexes using less memory and running faster on some fixed data sets. Later work found that results depend heavily on the data, and traditional indexes remain robust and simple.'),
    ],
    "test": [
        ('What does a learned index predict?',
         [('a', "The user's name"), ('b', 'Roughly where a key sits in sorted data'), ('c', 'The weather for tomorrow'), ('d', 'The price of a product')], 'b'),
        ('Why does a learned index store an error bound?',
         [('a', 'To print the model'), ('b', 'To delete old keys'), ('c', 'Because the model is not exact, so the search window must cover its worst miss'), ('d', 'To make the table bigger')], 'c'),
        ('What happens when a key is outside what the model handles well?',
         [('a', 'The system stops working'), ('b', 'The key is deleted'), ('c', 'The data is sent to a printer'), ('d', 'The system falls back to a normal search')], 'd'),
        ('What makes updates hard for learned indexes?',
         [('a', 'Inserts can shift many positions and make the model out of date'), ('b', 'Keys never change'), ('c', 'They have no memory'), ('d', 'They only store pictures')], 'a'),
        ('What is the main trade-off mentioned for learned indexes?',
         [('a', 'Results depend heavily on the data, while traditional indexes stay robust'), ('b', 'They are always faster on every data set'), ('c', 'They need no computer'), ('d', 'They remove all risk')], 'a'),
    ],
}
