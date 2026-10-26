"""Auctions in Depth (Broker, bar 2): the three main kinds of auction, the Starship's own clock, and the winner's curse."""
CODE = "business2_auctions"
BOOK = {
    "title": "Auctions in Depth",
    "subtitle": "Three kinds of auction, the winner's curse, and the clock",
    "chapters": [
        ("Three kinds of auction",
         "In an English auction, the price starts low and bidders raise it in turn until no one will go higher. In a Dutch auction, the price starts high and falls until someone accepts. In a sealed-bid auction, everyone writes one secret bid, and the highest bid wins. The Dutch method is still used to sell flowers in the Netherlands."),
        ("The Starship's auction is English",
         "A blueprint copy sells in the English style. Bids rise, and each new top bid must beat the one before by at least 1 credit. Every new top bid starts the clock again, so a copy closes 5 minutes after its last top bid."),
        ("The clock and the first bid",
         "A copy waits 5 minutes for its first bid. If no bid reaches the floor, the auction stops and holds. The unsold copies stay with the designer, who may schedule a new date and change the floor."),
        ("The winner's curse",
         "When bidders are unsure what an item is worth, the winner is often the one who guessed highest, and so the one who overpaid. Economists call this the winner's curse. A careful bidder decides the most they will pay before the bidding starts."),
        ("Fees on top",
         "The winner pays the bid plus a 2.5% fee, rounded up to whole credits, to the WSC. The designer receives the whole winning bid. A bidder should add the fee to their limit before bidding, so the total they pay is never a surprise."),
        ("The floor in practice",
         "A designer's floor is the lowest a copy can sell for. A high floor protects the price, but it may stop every bid. A low floor draws bids, but it may sell a copy below what it cost to make. A below-cost floor needs a warning box to be ticked, so the designer knows which choice they made."),
    ],
    "test": [
        ("In an English auction, which way does the price move?",
         [("a", "Down until someone accepts"), ("b", "It stays fixed"), ("c", "It is drawn by lot"), ("d", "Up, as bidders raise it")], "d"),
        ("How much must a new top bid beat the current top bid by on the Starship?",
         [("a", "Nothing"), ("b", "1 credit"), ("c", "10%"), ("d", "The whole floor")], "b"),
        ("What is the winner's curse?",
         [("a", "Losing every auction"), ("b", "Losing set-aside credits"), ("c", "Winning, and paying too much because the highest guess wins"), ("d", "A fee of 25%")], "c"),
        ("The winning bid is 370 credits. What is the Starship fee on it?",
         [("a", "9 credits"), ("b", "10 credits"), ("c", "9.25 credits"), ("d", "37 credits")], "b"),
        ("No bid reaches the floor. What happens?",
         [("a", "The copy goes to the WSC"), ("b", "The floor drops to zero"), ("c", "The copy is destroyed"), ("d", "The auction stops and holds, and the copy stays with the designer")], "d"),
    ],
}
