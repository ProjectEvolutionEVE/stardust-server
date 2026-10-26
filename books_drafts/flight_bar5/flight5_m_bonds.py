"""Bonds: a loan in the form of a tradable paper, with regular coupons, a due date, and a price that moves with rates."""
CODE = 'flight5_m_bonds'
BOOK = {
    'title': 'Bonds',
    'subtitle': 'Lending money in the form of tradable paper',
    'chapters': [
        ('What a bond is', 'A bond is a loan that can be bought and sold. The buyer lends money to the issuer, which is usually a government or a company. In return, the issuer promises regular payments and the return of the money at a set date.'),
        ('Coupons', 'The coupon is the regular interest payment, usually once or twice a year. It is set as a share of the face value when the bond is issued. The coupon does not change, whatever the price of the bond does.'),
        ('Yield', 'The yield is the return you get from buying the bond at its current price. If you buy at a price below face value, the yield is higher than the coupon. If you pay above face value, the yield is lower.'),
        ('Price against rate', 'When market interest rates rise, existing bonds with lower coupons become less attractive, so their prices fall. When rates fall, their prices rise. This is one of the most important rules in bonds.'),
        ('Ratings and default', "Rating agencies grade a bond's chance of being repaid. A higher grade means lower risk and usually a lower yield. A default is a failure to make a promised payment, and it can cost the holder much of the money."),
        ('Maturity', 'Maturity is the date the bond must be repaid. Longer bonds usually pay more interest to make up for the wait and the risk. A bond held to maturity returns the face value, if the issuer does not default.'),
    ],
    'test': [
        ('What is a bond?', [('a', "A type of ship's sail"), ('b', 'A kind of fuel'), ('c', 'A promise to paint a hull'), ('d', 'A loan that can be bought and sold')], 'd'),
        ('What is a coupon?', [('a', 'A shopping voucher'), ('b', 'The regular interest payment'), ('c', 'The price of the paper'), ('d', "A crew member's name")], 'b'),
        ("What happens to a bond's price when market interest rates rise?", [('a', 'It falls, since existing bonds become less attractive'), ('b', 'It rises by the same amount'), ('c', 'It never changes'), ('d', 'It becomes a coupon')], 'a'),
        ('What is a default?', [('a', 'Paying early with a gift'), ('b', 'Choosing the colour of a bond'), ('c', 'Failing to make a promised payment'), ('d', 'Receiving a coupon on time')], 'c'),
        ('What is maturity?', [('a', "The age of the issuer's founder"), ('b', 'The date the bond must be repaid'), ('c', 'The weight of the paper'), ('d', 'The number of coupons in a year')], 'b'),
    ],
}
