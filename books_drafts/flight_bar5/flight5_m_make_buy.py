"""Make or Buy: core skills, supplier risk, total cost, lock-in, case examples and a simple decision test."""
CODE = "flight5_m_make_buy"
BOOK = {
    "title": "Make or Buy",
    "subtitle": "Should you build it yourself, or buy it from someone else?",
    "chapters": [
        ("The question",
         "Every organisation must decide which parts of its work to do itself and which to buy from others. Making in house gives control. Buying from a supplier can be cheaper and faster, and lets you focus on your own strengths."),
        ("Core skills",
         "Keep in house the work that gives you an edge or that you cannot risk losing. Buy in the work that others do better or more cheaply. Core skills are often the hardest to rebuild once lost."),
        ("Supplier risk",
         "A supplier can fail, raise prices, or deliver late. Relying on one supplier for a vital part is a risk. Check the supplier's finances, its quality record and whether it has a backup."),
        ("Total cost",
         "Compare the full cost of each choice. Making in house includes staff, space, tools and training. Buying includes the price, delivery, checking, and the cost of managing the supplier."),
        ("Lock-in",
         "Lock-in is the cost of being tied to one supplier or one design. Switching may be slow or expensive. Before choosing, ask how hard it would be to change course later."),
        ("A decision test",
         "Ask four questions: is it a core skill, can we buy it reliably, is the total cost lower, and could we switch if needed. If the answers point the same way, the choice is clearer."),
    ],
    "test": [
        ("What is a make-or-buy decision?",
         [("a", "Choosing which bank to use"), ("b", "Choosing whether to produce a part in house or buy it from a supplier"), ("c", "Choosing a holiday"), ("d", "Choosing a logo")], "b"),
        ("Why keep core skills in house?",
         [("a", "They are always cheaper to buy"), ("b", "They are illegal to outsource"), ("c", "They do not matter"), ("d", "They give an edge and are hard to rebuild once lost")], "d"),
        ("What does lock-in mean?",
         [("a", "Locking the doors of a factory"), ("b", "Paying in advance"), ("c", "Being tied to one supplier or design, so switching is hard"), ("d", "Sharing profits")], "c"),
        ("Which costs should a total cost comparison include?",
         [("a", "Every cost of each option, including management and checking"), ("b", "Only the colour of the product"), ("c", "Only the supplier's logo"), ("d", "Only the price on the day")], "a"),
        ("What is supplier risk?",
         [("a", "The chance of rain on the day"), ("b", "The risk of a free gift"), ("c", "The chance a supplier fails, raises prices or delivers late"), ("d", "The risk that customers pay")], "c"),
    ],
}
