"""The Efficient Market Hypothesis: can anyone beat a price that already knows everything?"""
CODE = "business4_emh"
BOOK = {
    "title": "The Efficient Market Hypothesis",
    "subtitle": "Can anyone beat a price that already knows everything?",
    "chapters": [
        ("An idea from the 1960s",
         "Eugene Fama developed the idea in the 1960s and early 1970s. The claim is that in a well-run market, prices already reflect the information available. New news moves prices quickly, often before most people have read it."),
        ("Three forms",
         "The weak form says past prices tell you nothing reliable about the future. The semi-strong form says all public information, such as company reports and news, is already in the price. The strong form says even private information is in the price."),
        ("Random walks",
         "If prices react only to new and unexpected news, they move in a random walk. Tomorrow's move cannot be reliably predicted from today's. This does not mean prices make no sense. It means no one can reliably guess the next small move from the last one."),
        ("Evidence for it",
         "Many professional fund managers have failed to beat a broad market index over long periods, after their costs. Studies of company announcements show that prices adjust within minutes or hours of major news."),
        ("Evidence against it",
         "Bubbles and crashes are hard to square with perfect pricing. Some patterns, such as prices continuing to move in the same direction for months, and effects linked to company size, have been documented. Researchers still argue whether these are real mispricings or a reward for extra risk."),
        ("What it means for an investor",
         "If the hypothesis holds closely, paying high fees for stock picking is hard to justify. A simple, low-cost, diversified plan is a sensible default. This is general education, not personal advice, and no market is perfectly efficient at all times."),
    ],
    "test": [
        ("What does the semi-strong form say?",
         [("a", "Past prices predict the future"), ("b", "Private information is always priced in"), ("c", "Public information is already reflected in prices"), ("d", "Prices never change")], "c"),
        ("What is a random walk?",
         [("a", "A walk around a park"), ("b", "Tomorrow's moves cannot be reliably predicted from past moves"), ("c", "Prices always rise"), ("d", "A rule that forbids trading")], "b"),
        ("Which is harder to square with a perfectly efficient market?",
         [("a", "Prices reacting quickly to news"), ("b", "Large bubbles that rise and then collapse"), ("c", "Index funds tracking the market"), ("d", "Small random price moves")], "b"),
        ("What does the weak form say?",
         [("a", "Past prices tell you nothing reliable about the future"), ("b", "Prices never move"), ("c", "All private information is priced in"), ("d", "Only the government sets prices")], "a"),
        ("Which choice does the hypothesis make hard to justify?",
         [("a", "Diversified, low-cost investing"), ("b", "Reading company reports"), ("c", "Saving regularly"), ("d", "Paying high fees for stock picking")], "d"),
    ],
}
