"""Learning Curves: Wright's law, the doubling effect, production runs, aircraft examples, limits and use in planning."""
CODE = "flight5_m_learning_curve"
BOOK = {
    "title": "Learning Curves",
    "subtitle": "Why making more of something makes each one cheaper",
    "chapters": [
        ("What a learning curve is",
         "A learning curve shows how the cost of making one more unit falls as a team gains experience. Workers learn shortcuts, designs are refined and suppliers become more efficient. The curve describes this steady gain."),
        ("Wright's law",
         "In 1936, the aircraft engineer T. P. Wright found that the labour cost per aircraft fell by a fairly steady share each time total output doubled. This pattern is called Wright's law, or the experience curve."),
        ("The doubling effect",
         "If each doubling of total output cuts unit cost by a set share, then large early runs pay off over time. The first units cost the most, and later ones cost less. The rate of cut varies by industry."),
        ("Production runs",
         "Longer production runs can lower unit cost, but they also tie up money and risk making stock nobody wants. Planners weigh the gain from learning against the cost of holding stock."),
        ("Aircraft and other examples",
         "Aircraft, ships and many electronics show clear learning effects. Each new model often benefits from lessons learned in the last. Not every product follows a neat pattern, though."),
        ("Limits and planning",
         "Learning does not last for ever. Designs change, new technologies appear, and the gains flatten. Use learning curves as a guide, check them against real data, and do not count on the same rate for every future project."),
    ],
    "test": [
        ("What does a learning curve show?",
         [("a", "How many hours a team sleeps"), ("b", "The height of a building"), ("c", "How the cost of each unit falls as experience grows"), ("d", "The price of bread")], "c"),
        ("What does Wright's law say?",
         [("a", "Unit cost falls by a fairly steady share each time total output doubles"), ("b", "Costs always rise with output"), ("c", "Aircraft never change"), ("d", "Output can only be halved")], "a"),
        ("In what year did T. P. Wright publish his findings on aircraft costs?",
         [("a", "1776"), ("b", "1969"), ("c", "1936"), ("d", "2008")], "c"),
        ("What is a risk of very long production runs?",
         [("a", "They make the product free"), ("b", "They tie up money and can leave unwanted stock"), ("c", "They remove all costs"), ("d", "They stop the learning effect for ever")], "b"),
        ("Why should learning curves be checked against real data?",
         [("a", "Because they are always exact"), ("b", "Because they are required by law"), ("c", "Because they never change"), ("d", "Because the rate of learning varies and can flatten over time")], "d"),
    ],
}
