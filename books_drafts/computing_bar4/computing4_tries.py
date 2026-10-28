"""Tries and Prefix Search: trees of characters for fast prefix lookups."""
CODE = "computing4_tries"
BOOK = {
    "title": "Tries and Prefix Search",
    "subtitle": "Trees of characters for fast prefix lookups",
    "chapters": [
        ("Trees of characters", "A trie stores words one letter at a time along paths in a tree. Words that share a beginning share the same path. Each node may be marked as the end of a word."),
        ("Prefix lookup", "To find all words that start with a prefix, walk down the tree along its letters. Everything below that point is a word with the prefix. The search takes time based on the prefix length, not the size of the list."),
        ("Autocomplete", "Typing assistants use this idea to offer suggestions as you type. Each letter narrows the choices. The suggestions come from the part of the tree you have reached."),
        ("Memory trade-offs", "A plain trie can use a lot of memory, because each node holds links for many letters and many nodes may have only one or two children. This trade-off gives fast lookups at the cost of space."),
        ("Compressed tries", "A compressed trie merges chains of single-child nodes into one longer label. This saves memory while keeping the same lookup idea. Radix trees are a common form."),
        ("Spell checking and routing tables", "Spell checkers use tries to test whether a word exists and to suggest close matches. Network routers use related prefix trees to match addresses. The shared idea is fast matching on prefixes."),
    ],
    "test": [
        ("What does a trie store?",
         [("a", "Pictures of towns"), ("b", "Words, one letter at a time along paths"), ("c", "Only numbers in a row"), ("d", "Sound files")], "b"),
        ("How does prefix lookup take its time?",
         [("a", "Based on the colour of the screen"), ("b", "Always exactly one second"), ("c", "Based on the number of players"), ("d", "Based on the prefix length, not the size of the list")], "d"),
        ("What is the main memory trade-off of a plain trie?",
         [("a", "Many nodes may hold few children and waste space"), ("b", "It stores nothing at all"), ("c", "It needs a printer"), ("d", "It uses no memory")], "a"),
        ("What does a compressed trie do?",
         [("a", "Deletes every word"), ("b", "Adds random letters"), ("c", "Merges chains of single-child nodes into one label"), ("d", "Stores words in a photo")], "c"),
        ("Which task uses a trie idea?",
         [("a", "Painting a room"), ("b", "Spell checking"), ("c", "Cooking rice"), ("d", "Folding laundry")], "b"),
    ],
}
