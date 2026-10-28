"""Atomic Layer Deposition Basics: self-limiting reactions, cycle counts, conformal coatings, film thickness control and throughput limits."""
CODE = "engineering5_ald"
BOOK = {
    "title": "Atomic Layer Deposition Basics",
    "subtitle": "Building a film one atomic layer at a time",
    "chapters": [
        ("Layers of single atoms",
         "Atomic layer deposition, or ALD, builds a film one layer of atoms at a time. The process is very precise. Each cycle adds a film only about one atomic layer thick, often less."),
        ("Self-limiting reactions",
         "Each reaction stops when the surface is full. A gas is pulsed in, reacts with the surface until every site is taken, and the extra gas is pumped away. The reaction limits itself, which is why the layers are so even."),
        ("Cycle counts",
         "One full cycle is two pulses of gas with a purge between them. The film thickness grows with the number of cycles. Counting cycles gives the thickness, and it is the main way the process is controlled."),
        ("Conformal coatings",
         "ALD coats every surface evenly, including deep holes and fine channels. This is called a conformal coating. Few other methods can coat such shapes so well."),
        ("Thickness control",
         "Because each cycle adds a known amount, thickness can be set very accurately. This is useful for thin layers in electronics and protective films where a fraction of a micrometre matters."),
        ("Throughput limits",
         "ALD is slow compared with other coating methods, because each layer takes several steps. It is used where precision and conformal cover matter more than speed. Its cost per part is weighed against what the thin film gives in return."),
    ],
    "test": [
        ("What does ALD build a film from?",
         [("a", "One thick poured layer"), ("b", "Sheets of paper"), ("c", "One layer of atoms at a time"), ("d", "Wet paint")], "c"),
        ("What does self-limiting mean for an ALD reaction?",
         [("a", "The reaction never stops"), ("b", "The reaction only works in the dark"), ("c", "The reaction needs no gas"), ("d", "The reaction stops when the surface is full")], "d"),
        ("How is ALD thickness mainly controlled?",
         [("a", "By counting cycles"), ("b", "By the colour of the gas"), ("c", "By the size of the room"), ("d", "By the price of the part")], "a"),
        ("What is a conformal coating?",
         [("a", "A coating that covers only the top"), ("b", "A coating that covers every surface evenly, even in deep holes"), ("c", "A coating made of wood"), ("d", "A coating that is never applied")], "b"),
        ("What is the main limit on ALD for production?",
         [("a", "It cannot make any film at all"), ("b", "It only works on paper"), ("c", "It is slow, because each layer takes several steps"), ("d", "It has no limit")], "c"),
    ],
}
