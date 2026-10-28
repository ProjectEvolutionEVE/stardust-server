"""Bloom Filters: a quick no-or-maybe test."""
CODE = "computing4_bloom_filters"
BOOK = {
    "title": "Bloom Filters",
    "subtitle": "A quick no-or-maybe test",
    "chapters": [
        ("A quick no-or-maybe test", "A Bloom filter answers whether an item might be in a set. If it says no, the item is certainly absent. If it says maybe, the item may or may not be there. It trades certainty for very small memory use."),
        ("Bit arrays and several hashes", "The filter is a row of bits, all starting at zero. Adding an item sets several bits, chosen by several hash functions. Checking an item looks at the same bits, and all of them must be set for the answer to be maybe."),
        ("False positive rates", "A false positive is a maybe answer for an item that was never added. More bits and more hash functions lower this rate, up to a point. The rate can be predicted from the sizes chosen."),
        ("Sizing a filter", "Choose the expected number of items and the acceptable false positive rate first. Those two numbers set how many bits and hashes are needed. A filter that is too small gives many false maybes."),
        ("Deletion problems", "A standard Bloom filter cannot remove an item cleanly, because clearing its bits could affect other items. Counting filters and other variants allow removal. Each variant costs extra space or complexity."),
        ("Uses in caches and storage", "Systems use Bloom filters to skip lookups that would fail. Databases avoid reading files that cannot hold a key, and web caches check whether an item is stored before searching. The saved work can be large."),
    ],
    "test": [
        ("What does a Bloom filter's answer of no mean?",
         [("a", "A crash of the filter"), ("b", "The item is definitely in the set"), ("c", "The item is very large"), ("d", "The item is certainly not in the set")], "d"),
        ("What does a Bloom filter store?",
         [("a", "A full copy of every item"), ("b", "A photograph of each item"), ("c", "A row of bits set by several hash functions"), ("d", "A list of player names")], "c"),
        ("What is a false positive?",
         [("a", "A crash of the filter"), ("b", "A no answer for an item that was added"), ("c", "A maybe answer for an item that was never added"), ("d", "A file that is too small")], "c"),
        ("What makes a standard Bloom filter hard to change?",
         [("a", "It has no hash functions"), ("b", "It cannot hold any bits"), ("c", "It uses too many colours"), ("d", "It cannot remove an item cleanly")], "d"),
        ("Where are Bloom filters used?",
         [("a", "To skip lookups that would fail, in caches and storage"), ("b", "To paint the sky"), ("c", "To print tickets"), ("d", "To pick music")], "a"),
    ],
}
