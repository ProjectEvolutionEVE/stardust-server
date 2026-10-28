"""Lossless Compression: making data smaller without losing a single bit."""
CODE = "computing4_compression"
BOOK = {
    "title": "Lossless Compression",
    "subtitle": "Making data smaller without losing a single bit",
    "chapters": [
        ("Redundancy in data", "Compression works by finding repetition and predictability in data. A picture with large plain areas, or a text with common words, has room to shrink. Lossless compression can rebuild the original exactly."),
        ("Run-length coding", "Run-length coding replaces a long run of the same value with the value and a count. A line of a hundred black pixels becomes two numbers. It works best when runs are long and common."),
        ("Huffman codes", "Huffman coding gives short codes to common symbols and longer codes to rare ones. The codes are built from the frequencies in the data. No code is the start of another, so decoding is unambiguous."),
        ("Lempel-Ziv dictionaries", "Lempel-Ziv methods replace repeated phrases with a pointer to an earlier copy. The dictionary builds up as the data is read. Many common formats use ideas from this family."),
        ("Formats such as ZIP and PNG", "ZIP archives and PNG images both use DEFLATE, which combines Lempel-Ziv matching with Huffman coding. Each format adds its own container and rules. Using known formats keeps files readable by many tools."),
        ("The limits of compression", "No lossless method can shrink every possible file. Data that is already random or already compressed will not shrink much. Compression finds patterns; it cannot create room where none exists."),
    ],
    "test": [
        ("What does lossless compression keep?",
         [("a", "Only the first half of a file"), ("b", "A lower quality copy"), ("c", "Enough room to rebuild the original exactly"), ("d", "Nothing at all")], "c"),
        ("What does run-length coding store?",
         [("a", "A list of names"), ("b", "A value and a count of how many times it repeats"), ("c", "Only the colours of the sky"), ("d", "A map of the galaxy")], "b"),
        ("What do Huffman codes give to common symbols?",
         [("a", "Short codes"), ("b", "Longer codes than rare ones"), ("c", "No code at all"), ("d", "The same long code as every other symbol")], "a"),
        ("Which method combines Lempel-Ziv matching and Huffman coding?",
         [("a", "The paint program"), ("b", "The payroll system"), ("c", "The compass"), ("d", "DEFLATE, used in ZIP and PNG")], "d"),
        ("What is a real limit of compression?",
         [("a", "Random or already-compressed data will not shrink much"), ("b", "All files can always be halved"), ("c", "Compression makes files bigger every time"), ("d", "Compression deletes the file name")], "a"),
    ],
}
