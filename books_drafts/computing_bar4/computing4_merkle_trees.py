"""Merkle Trees: a tree of hashes that proves what is inside."""
CODE = "computing4_merkle_trees"
BOOK = {
    "title": "Merkle Trees",
    "subtitle": "A tree of hashes that proves what is inside",
    "chapters": [
        ("A tree of hashes", "A hash is a short fingerprint of some data. A Merkle tree hashes each piece of data, then hashes pairs of those hashes, and so on up to a single root hash. The root summarises the whole set."),
        ("Inclusion proofs", "To prove one item is in the set, you show the item and the few hashes along its path to the root. Anyone can recompute the root and check that it matches. The proof stays short even for a very large set."),
        ("A large set with a small root", "The root is a single fixed-size value. If any item changes, the root changes too. Comparing two roots tells you quickly whether two sets are the same."),
        ("Sync protocols", "Two computers can compare their trees from the top down. Matching hashes mean matching parts, so only the differing branches need sending. This saves transferring large amounts of data."),
        ("Versioned stores", "Some storage systems use Merkle trees to record versions. Each version has a root that links to the content before it. Old versions stay checkable without being fully copied."),
        ("Limits", "A Merkle tree proves that an item is in a set, but it does not show the set is complete unless extra structure is added. Whoever keeps the tree must still store the hashes. The design has costs as well as benefits."),
    ],
    "test": [
        ("What is a hash?",
         [("a", "A short fingerprint of some data"), ("b", "A kind of ship"), ("c", "A full copy of the data"), ("d", "A map of the galaxy")], "a"),
        ("What does a Merkle tree's root summarise?",
         [("a", "The whole set of items below it"), ("b", "Only the first item"), ("c", "The screen colour"), ("d", "The player's wallet")], "a"),
        ("What is needed to prove one item is in the set?",
         [("a", "The whole set"), ("b", "A password written on paper"), ("c", "The item and the hashes along its path to the root"), ("d", "Nothing at all")], "c"),
        ("What happens to the root if any item changes?",
         [("a", "It changes too"), ("b", "It stays the same"), ("c", "It is deleted"), ("d", "It doubles")], "a"),
        ("What does a sync protocol send when two trees have matching roots?",
         [("a", "Everything, every time"), ("b", "Only the screen"), ("c", "A new root for the player"), ("d", "Nothing, since matching hashes mean matching parts")], "d"),
    ],
}
