"""Inverted Indexes and Search: from words to the documents that contain them."""
CODE = "computing4_inverted_index"
BOOK = {
    "title": "Inverted Indexes and Search",
    "subtitle": "From words to the documents that contain them",
    "chapters": [
        ("Word-to-document lists", "An inverted index maps each word to the list of documents where it appears. Searching for a word becomes a lookup, not a scan of every document. The name comes from flipping the usual document-to-words view."),
        ("Postings and positions", "Each entry in a word's list is a posting, often holding a document number and a count. Storing positions lets a search find words that appear next to each other. Positions cost more space, but they make phrase search possible."),
        ("Query evaluation", "A query with several words combines their posting lists, often by intersecting them for AND or merging them for OR. Starting with the shortest list speeds things up. The result is a set of matching documents."),
        ("Ranking basics", "Matching documents are put in order by a score. Common scoring ideas weigh how often a word appears in a document and how rare it is across all documents. Rare words usually say more about a document."),
        ("Index build pipelines", "Building an index means reading documents, breaking them into words and writing sorted postings. Large indexes are built in batches and then merged. Pipelines must cope with updates as new documents arrive."),
        ("Search engine architecture", "A search engine splits the index across many machines, sends each query to them and combines the top results. Caches keep popular queries fast. The design balances speed, freshness and cost."),
    ],
    "test": [
        ("What does an inverted index map?",
         [("a", "Each word to the documents where it appears"), ("b", "Each player to a ship"), ("c", "Each colour to a number"), ("d", "Each file to its size")], "a"),
        ("What is a posting?",
         [("a", "A letter sent by mail"), ("b", "A type of screen"), ("c", "An entry in a word's list, such as a document number"), ("d", "A kind of ship")], "c"),
        ("How is an AND query often evaluated?",
         [("a", "By deleting the lists"), ("b", "By printing each one"), ("c", "By choosing one at random"), ("d", "By intersecting the posting lists")], "d"),
        ("What do ranking scores often weigh?",
         [("a", "The colour of the page"), ("b", "How often a word appears and how rare it is"), ("c", "The length of the title only"), ("d", "The time of day for the player")], "b"),
        ("Why are indexes often split across machines?",
         [("a", "To make the screen brighter"), ("b", "To remove the words"), ("c", "To handle large amounts of data and many queries"), ("d", "To stop all search")], "c"),
    ],
}
