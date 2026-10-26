"""The Sumitomo Copper Scandal: Yasuo Hamanaka, the 1996 discovery, hidden positions, the effect on prices, the loss and the missing controls."""
CODE = 'business5_sumitomo'
BOOK = {
    "title": 'The Sumitomo Copper Scandal',
    "subtitle": 'A trader, hidden positions and a loss that rocked the metals market',
    "chapters": [
        ('The copper trader',
         'Yasuo Hamanaka was a senior copper trader at the Japanese trading house Sumitomo Corporation. He was known in the market as Mr Copper, and for years he was one of the biggest players in the metal. His trades were large enough to move prices.'),
        ('Hidden positions',
         'Hamanaka made large unauthorised trades and hid their losses from his bosses for years. He used fake and off-book records to keep the true position out of sight. The gap between what was reported and what was real kept growing.'),
        ('The price effect',
         'His buying pushed up copper prices for a time, because the market saw a huge buyer. When his positions had to be unwound, prices moved the other way. Other traders felt the swings, and the market grew nervous about where the losses sat.'),
        ('The 1996 discovery',
         'In June 1996, Sumitomo announced that it had lost very large sums through copper trading. Hamanaka was removed from his post and later prosecuted. The announcement sent copper prices sharply lower in the days that followed.'),
        ('The size of the loss',
         "Sumitomo reported losses running into billions of dollars over the affair. Such a loss is a warning that one trader can carry a whole firm into danger. Large trading books need to be watched by people who do not share the trader's incentives."),
        ('Controls that were missing',
         'The scandal showed that checks were weak. The same person traded and kept the records, and the reporting did not catch unauthorised positions. Good firms separate trading from record-keeping, limit position sizes, and check every position from outside the desk.'),
    ],
    "test": [
        ('What nickname was Yasuo Hamanaka known by in the market?',
         [('a', 'Mr Copper'), ('b', 'Mr Gold'), ('c', 'Mr Silver'), ('d', 'Mr Tin')], 'a'),
        ('What did Hamanaka do with his losses?',
         [('a', 'Reported them honestly every day'), ('b', 'Hid them from his bosses for years'), ('c', 'Gave them to charity'), ('d', 'Sold them to the Sun')], 'b'),
        ('When did Sumitomo announce the huge copper losses?',
         [('a', 'June 1776'), ('b', 'June 2020'), ('c', 'June 1996'), ('d', 'June 1929')], 'c'),
        ('Why did his large buying move copper prices?',
         [('a', 'Copper was banned'), ('b', 'Copper stopped being used'), ('c', 'It was raining'), ('d', 'The market saw a huge buyer and prices rose')], 'd'),
        ('What control was missing that let the scandal grow?',
         [('a', 'Separating trading from record-keeping and checking positions from outside the desk'), ('b', 'A bigger office'), ('c', 'More lunch breaks'), ('d', 'A ban on copper ships')], 'a'),
    ],
}
