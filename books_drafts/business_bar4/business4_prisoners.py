"""The Prisoner's Dilemma in Business: why rivals often fail to cooperate, and how cooperation can last."""
CODE = "business4_prisoners"
BOOK = {
    "title": "The Prisoner's Dilemma in Business",
    "subtitle": "Why rivals often fail to cooperate, and how cooperation can last",
    "chapters": [
        ("The classic table",
         "Two suspects are held apart, and each may confess or stay silent. Each does best by confessing, whatever the other does. Yet both do better if both stay silent. The table shows the trap: choices that look sensible one by one lead to a worse result for both."),
        ("Price wars",
         "Two firms may both cut prices to win customers. If both cut, both earn less, yet neither can afford to stop first. Mutual price cutting is the business version of the dilemma."),
        ("Repeated games",
         "When the same players meet again and again, the logic changes. Future rounds give a reason to keep cooperating, because a betrayal today can be punished tomorrow. The shadow of the future makes cooperation possible."),
        ("Axelrod's tournaments",
         "In the 1980s, political scientist Robert Axelrod invited computer programs to play the repeated dilemma in tournaments. The simplest strategies often did well. Over many rounds, cooperation often beat betrayal."),
        ("Tit for tat",
         "The winning strategy in Axelrod's early tournaments was tit for tat. It starts by cooperating, then copies the other player's last move. It is generous, quick to punish and quick to forgive. Its simplicity made it easy for others to understand."),
        ("Cooperation that lasts",
         "Cooperation lasts when rivals expect to meet again, when they can see each other's moves, and when punishment is quick and fair. Clear rules and open reporting help keep it stable. The lesson is a practical one for businesses."),
    ],
    "test": [
        ("In the classic dilemma, what does each suspect do best with?",
         [("a", "Staying silent always"), ("b", "Running away"), ("c", "Asking for a lawyer"), ("d", "Confessing, whatever the other does")], "d"),
        ("What tends to happen in a price war?",
         [("a", "Both firms earn more"), ("b", "Both firms earn less"), ("c", "Prices never change"), ("d", "Customers pay nothing")], "b"),
        ("Why does repetition help cooperation?",
         [("a", "Future rounds give a reason to keep cooperating"), ("b", "Players forget the rules"), ("c", "Prices rise by law"), ("d", "Each round is random")], "a"),
        ("Who ran the computer tournaments of repeated dilemma strategies?",
         [("a", "Adam Smith"), ("b", "Milton Friedman"), ("c", "Robert Axelrod"), ("d", "John Nash")], "c"),
        ("What does tit for tat do?",
         [("a", "Always defects"), ("b", "Starts by cooperating, then copies the other player's last move"), ("c", "Chooses at random"), ("d", "Refuses all games")], "b"),
    ],
}
