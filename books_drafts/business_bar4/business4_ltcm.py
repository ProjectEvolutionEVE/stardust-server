"""Long-Term Capital Management: the 1994 fund, the Nobel founders, leverage, Russia's default in 1998, the rescue, and lessons on models."""
CODE = 'business4_ltcm'
BOOK = {
    "title": 'Long-Term Capital Management',
    "subtitle": 'A fund run by famous economists that a model and heavy borrowing nearly undid',
    "chapters": [
        ('The 1994 fund',
         'Long-Term Capital Management, or LTCM, was a hedge fund founded in 1994 by bond traders and academics. It aimed to profit from small price differences between related bonds, betting that prices would move back together over time.'),
        ('The Nobel founders',
         "Among LTCM's partners were Myron Scholes and Robert Merton, who shared the 1997 Nobel Memorial Prize in Economic Sciences for their work on option pricing. Their reputations drew investors and gave the fund great prestige."),
        ('Leverage',
         'The fund borrowed heavily against its capital to make its small bets pay meaningful sums. High leverage magnified gains in calm times, but it also meant that a modest loss could threaten the whole fund. Its positions were large relative to its capital.'),
        ("Russia's default in 1998",
         'In August 1998 Russia defaulted on its debts and devalued its currency. Markets around the world moved sharply, and the price gaps that LTCM had bet on widened instead of narrowing. The fund suffered very large losses in a short time.'),
        ('The rescue',
         'In September 1998 the Federal Reserve Bank of New York organised a rescue, in which a group of major banks put up capital to take over most of the fund and manage its positions. The aim was to prevent a wider shock to the financial system.'),
        ('Lessons on models',
         "LTCM's models assumed that past patterns and normal conditions would hold. Real markets sometimes move in ways the models do not expect, and they can dry up exactly when they are needed. The lessons include care with leverage and a healthy respect for what models cannot see."),
    ],
    "test": [
        ('In what year was Long-Term Capital Management founded?',
         [('a', '1974'), ('b', '1984'), ('c', '1994'), ('d', '2004')], 'c'),
        ("Which Nobel-winning economists were among LTCM's partners?",
         [('a', 'Milton Friedman and Paul Samuelson'), ('b', 'John Nash and Kenneth Arrow'), ('c', 'James Tobin and Franco Modigliani'), ('d', 'Myron Scholes and Robert Merton')], 'd'),
        ('Why did high leverage make LTCM fragile?',
         [('a', 'A modest loss could threaten the whole fund'), ('b', 'It meant the fund held no positions at all'), ('c', 'It removed all risk'), ('d', 'It made every bet certain to win')], 'a'),
        ("What event in August 1998 hit LTCM's positions?",
         [('a', 'Japan joined the European Union'), ('b', 'Russia defaulted on its debts and devalued its currency'), ('c', 'The Olympic Games were held in London'), ('d', 'A new computer was launched')], 'b'),
        ('What did the 1998 rescue aim to prevent?',
         [('a', 'The founding of new banks'), ('b', 'All bond trading in New York'), ('c', 'A wider shock to the financial system'), ('d', 'The sale of government bonds')], 'c'),
    ],
}
