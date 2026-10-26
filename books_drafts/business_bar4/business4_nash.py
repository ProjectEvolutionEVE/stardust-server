"""Game Theory and the Nash Equilibrium: how players choose when outcomes depend on each other."""
CODE = "business4_nash"
BOOK = {
    "title": "Game Theory and the Nash Equilibrium",
    "subtitle": "How rational players choose when outcomes depend on each other",
    "chapters": [
        ("Players, moves and payoffs",
         "A game has players, the moves each one can make, and the payoff each gets from every combination of moves. Game theory studies how rational players choose when the results depend on what the others do."),
        ("The payoff table",
         "A simple game can be drawn as a grid. The rows are one firm's options, the columns are the other firm's, and each cell shows both payoffs. Reading the grid shows which choice each player prefers, given what the other might do."),
        ("Nash's idea",
         "John Nash showed in 1950 that every finite game has at least one equilibrium: a set of strategies where no player gains by changing alone. He shared the Nobel Prize in Economics in 1994."),
        ("Dominant strategies",
         "A dominant strategy is best for a player whatever the other player does. When both players have one, the equilibrium is easy to find. Many real situations have no dominant strategy, so players must predict what the other will do."),
        ("Mixed strategies",
         "Sometimes the best play is to randomise, choosing each move with a set probability. This keeps the other side guessing. In some games, a mixed strategy is the only equilibrium."),
        ("Business uses",
         "Firms use game theory to think about pricing, bidding, entering new markets and negotiation. Asking what a rival will do in response to each move helps avoid surprises. The model is a thinking tool, not a crystal ball."),
    ],
    "test": [
        ("What does a payoff table show?",
         [("a", "The rent of a shop"), ("b", "Each player's results for every combination of moves"), ("c", "The price of shares"), ("d", "The staff list")], "b"),
        ("What is a Nash equilibrium?",
         [("a", "A winning party"), ("b", "A tax rate"), ("c", "A point where no player gains by changing their move alone"), ("d", "A price list")], "c"),
        ("What is a dominant strategy?",
         [("a", "A strategy used by the largest firm"), ("b", "A strategy that is best whatever the other player does"), ("c", "A strategy that is always illegal"), ("d", "A random choice")], "b"),
        ("What is a mixed strategy?",
         [("a", "Mixing two products"), ("b", "Changing the rules"), ("c", "Doubling prices"), ("d", "Choosing moves at random with set probabilities")], "d"),
        ("In what year did Nash show that every finite game has an equilibrium?",
         [("a", "1950"), ("b", "1900"), ("c", "1994"), ("d", "1975")], "a"),
    ],
}
