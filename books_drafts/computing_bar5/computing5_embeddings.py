"""Embeddings and representation learning: vectors for items, cosine similarity, word2vec, contrastive learning, bias and search."""
CODE = 'computing5_embeddings'
BOOK = {
    "title": 'Embeddings and Representation Learning',
    "subtitle": 'Turning words and items into vectors where similar things sit close together',
    "chapters": [
        ('Vectors for things',
         'An embedding is a list of numbers that stands for an item, such as a word, product or user. Items with similar meaning or use get similar lists.'),
        ('Measuring similarity',
         'Cosine similarity compares the direction of two vectors. Values near one mean the items point the same way, and so are alike.'),
        ('Learning embeddings',
         'Word2vec, published in 2013, learned word vectors from the words that appear near each other. Words used in similar contexts ended up close together.'),
        ('Contrastive learning',
         'Contrastive learning pulls matching pairs together and pushes unrelated pairs apart. It is a common way to learn useful embeddings from images and text.'),
        ('Bias in embeddings',
         'Embeddings learn from their training text, so they can absorb unfair associations in that text. Teams test for these biases and reduce them where they can.'),
        ('Use in search',
         'Search systems compare the embedding of a query with the embeddings of documents. The closest ones are returned, even if they share no exact words.'),
    ],
    "test": [
        ('What does an embedding represent?',
         [('a', 'An item as a list of numbers'), ('b', 'A paper form'), ('c', 'A gold coin'), ('d', 'A phone call')], 'a'),
        ('What does cosine similarity compare?',
         [('a', 'The direction of two vectors'), ('b', 'The colour of two screens'), ('c', 'The age of two users'), ('d', 'The price of two cars')], 'a'),
        ('What did word2vec learn from?',
         [('a', 'Pictures of cats'), ('b', 'Words that appear near each other'), ('c', 'Sound recordings'), ('d', 'Bank statements')], 'b'),
        ('What does contrastive learning do?',
         [('a', 'Deletes all pairs'), ('b', 'Shuffles the colours'), ('c', 'Pulls matching pairs together and pushes unrelated pairs apart'), ('d', 'Prints every pair')], 'c'),
        ('Why can embeddings be unfair?',
         [('a', 'They are made of paper'), ('b', 'They only count the weather'), ('c', 'They use no data'), ('d', 'They learn from training text that can hold unfair links')], 'd'),
    ],
}
