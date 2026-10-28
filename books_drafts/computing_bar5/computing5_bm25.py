"""BM25 ranking: term frequency saturation, inverse document frequency, length normalisation, tuning and lexical versus vector search."""
CODE = 'computing5_bm25'
BOOK = {
    "title": 'Full-Text Ranking with BM25',
    "subtitle": 'How search engines decide which documents match a question best',
    "chapters": [
        ('Words in documents',
         'A search engine stores which words appear in which documents. When you search, it must decide which documents answer best.'),
        ('Term frequency',
         'A word that appears often in a document suggests the document is about it. BM25 counts how often each search word appears, but with diminishing returns, so repeating a word many times adds less each time.'),
        ('Inverse document frequency',
         'Rare words carry more meaning than common ones. A search word that appears in few documents gets a bigger weight than one found in almost all.'),
        ('Length normalisation',
         'A long document naturally repeats words more. BM25 adjusts for length so that long documents do not win just by size.'),
        ('Tuning',
         'Two settings control how strongly term frequency levels off and how much length matters. Teams tune them on test queries with known good answers.'),
        ('Lexical versus vector search',
         'BM25 matches the words typed, which is fast and precise for names and codes. Vector search matches meaning, so the two are often combined in a hybrid search.'),
    ],
    "test": [
        ('What does BM25 score?',
         [('a', 'The price of the server'), ('b', "The user's height"), ('c', 'The number of printers'), ('d', 'How well a document matches the search words')], 'd'),
        ('What happens to the extra value of a repeated word?',
         [('a', 'It gets smaller with each repeat'), ('b', 'It doubles each time'), ('c', 'It is removed'), ('d', 'It becomes a picture')], 'a'),
        ('Why are rare words weighted more?',
         [('a', 'They are longer'), ('b', 'They carry more meaning'), ('c', 'They are rarer to type'), ('d', 'They are always in capitals')], 'b'),
        ('What does length normalisation stop?',
         [('a', 'Short queries'), ('b', 'Typing errors'), ('c', 'Long documents winning just by size'), ('d', 'Fast searches')], 'c'),
        ('What does lexical search match?',
         [('a', 'The colour of the page'), ('b', 'The words typed'), ('c', 'The time of day'), ('d', 'The printer model')], 'b'),
    ],
}
