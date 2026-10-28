"""Retrieval-Augmented Generation: how a language model can answer from documents it looks up, and how those answers go wrong."""
CODE = 'computing5_rag'
BOOK = {
    "title": 'Retrieval-Augmented Generation',
    "subtitle": 'Looking up the right documents before the model answers',
    "chapters": [
        ('Why retrieval helps',
         'A language model knows only what it learned in training, and that knowledge goes out of date. Retrieval-augmented generation looks up relevant documents first and gives them to the model along with the question. The model can then answer from those sources.'),
        ('Chunking the documents',
         "Long documents are cut into chunks, each small enough to fit in the model's input. Chunk size matters: too small and the context is lost, too large and the search becomes less precise. Good chunking keeps related sentences together."),
        ('Searching and ranking',
         'Each chunk is turned into a vector, and a query is matched against the stored vectors. Ranking then orders the candidates, often with a second, more careful model. The top few chunks are passed on.'),
        ('Grounding the answer',
         'Grounding means the answer is supported by the retrieved text, and the system can point to where each claim came from. Prompts usually tell the model to answer only from the given sources. Citations let a reader check the claim.'),
        ('Evaluating a system',
         'Teams measure whether the right chunks were found, and whether the final answer is correct and supported. These are separate tests, because a system can retrieve well and still answer badly. Test sets should include questions the documents cannot answer.'),
        ('Failure modes',
         'A system can retrieve nothing relevant, retrieve out-of-date text, or mix up two similar documents. The model may still write a fluent answer that is not in the sources. Monitoring real questions and checking the citations are the practical defences.'),
    ],
    "test": [
        ('What problem does retrieval address for a language model?',
         [('a', 'The model cannot display colour'), ('b', 'The model is too small to read text'), ('c', 'The training knowledge can be out of date or missing'), ('d', 'The keyboard is too slow')], 'c'),
        ('Why are documents split into chunks?',
         [('a', "So each piece fits in the model's input and stays focused"), ('b', 'So the files can be printed on paper'), ('c', 'So the model forgets the sources'), ('d', 'So every chunk has the same author')], 'a'),
        ('What does grounding an answer mean?',
         [('a', 'The answer is written in the largest font'), ('b', 'The answer is never longer than one line'), ('c', 'The answer is spoken aloud'), ('d', 'The answer is supported by the retrieved text')], 'd'),
        ('Why should retrieval and answer quality be tested separately?',
         [('a', 'Retrieval never affects the answer'), ('b', 'A system can find the right text and still answer badly, or the reverse'), ('c', 'Only answers can be measured'), ('d', 'Test sets must be printed')], 'b'),
        ('Which is a typical failure of a retrieval system?',
         [('a', 'It always uses the wrong colour scheme'), ('b', 'It needs no documents at all'), ('c', 'It retrieves nothing relevant, yet still writes a fluent answer'), ('d', 'It refuses to store any text')], 'c'),
    ],
}
