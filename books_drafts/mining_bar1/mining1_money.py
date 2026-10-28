"""A Miner's Income: what a trip earns against what it costs, how prices move, and how to keep money steady through thin weeks."""
CODE = 'mining1_money'
BOOK = {
    "title": "A Miner's Income",
    "subtitle": 'What a trip earns against what it costs, and how to make the money last',
    "chapters": [
        ('Income minus costs',
         'A miner\'s profit is the income from a trip minus the costs of making it. Costs are everything that goes out: loan payments, food and drink, and the upkeep of your kit, as in real life. Write both down each week, and keep your receipts, because every transfer of goods gives you one and they are kept in your filing cabinet. Credits in the game are for play only and never turn into real money.'),
        ('Prices rise and fall',
         'Ore is sold on a market where buyers and sellers set the price, and the Starship bank trades there too. Prices move with what is waiting to be bought and sold, and they lean back toward a reference price over time. Every item has a floor, and nothing trades below it: copper ore is listed at 600 credits a 100 kg lot, with a floor of 300. A high price this week does not promise one next week.'),
        ('Saving through the lean weeks',
         'A miner\'s income comes in lumps, with a big haul one week and a thin one the next. A savings account smooths this out: it pays 4% APR, a year\'s rate, and you can take money out at any time. 10,000 credits in savings earn about 7.69 credits a week. Keep an emergency fund there, enough to cover your costs for several weeks, so a thin week never forces you to sell in a hurry. Savings goals, such as a new ship, tell you what you are saving toward.'),
        ('Interest earned and interest paid',
         'Interest works both ways. Every Bank rate is an APR, and each week the Bank pays or charges the APR divided by 52 on the balance. The Bank pays you on deposits: 4% APR in a savings account, and 5%, 6% or 7% APR in a term deposit locked for 2, 4 or 8 weeks. A term deposit pays its interest only when the term ends in full, so closing it early returns only what you put in. Only the Bank lends, and only to a player wearing the Business uniform from the Closet. The APR falls with the bars on that uniform, from 16% with one bar to 8% with five, and it is charged on what you still owe. If the top Business bar is silver, the Bank lends 80% and you pay 20% down; gold waives it.'),
        ('When a loan pays for itself',
         'Borrowing for a bigger hold makes sense only when the extra income it brings, after the weekly payments, is more than the loan costs. Before you sign, the Bank shows you the total cost of the loan, and you should ask what the purchase will really earn. Borrowing for something that earns nothing is a cost, not an investment. A missed payment adds a late fee to what you owe and lowers your credit standing, which makes your next loan dearer. Paying a loan off early saves the interest you would have paid later. At a fair APR a short loan costs little: 1,000 credits at 16% APR over 8 weeks costs 14 in interest, where a payday-style loan at 400% APR would cost 376.'),
        ('Do not sell at the bottom',
         'When prices are low and you need cash, it is tempting to sell everything at once. That locks in the lowest price on the day you were most pressed. A limit order names the lowest price you will accept, and selling in lots spreads your sales over time. An emergency fund is what lets you wait for a fair price.'),
    ],
    "test": [
        ("How do you work out a miner's profit for a trip?",
         [('a', 'Add the costs to the income'), ('b', 'Take the costs away from the income'), ('c', 'Divide the costs by the price of the ore'), ('d', 'Count the income only, before any costs')], 'b'),
        ("What does an item's floor price mean on the market?",
         [('a', 'It is the highest price the item can ever reach'), ('b', 'The Bank must buy any amount at that price'), ('c', 'The price is set once and never changes'), ('d', 'Nothing trades below it')], 'd'),
        ('Why is an emergency fund useful to a miner whose income comes in lumps?',
         [('a', 'It covers costs in a thin week, so you need not sell in a hurry'), ('b', 'It stops prices from moving'), ('c', 'It pays a fixed wage every week'), ('d', 'It must be spent before any loan')], 'a'),
        ('Which statement about interest is true?',
         [('a', 'Interest you pay makes your money grow'), ('b', 'A term deposit pays its interest every week, even if you close it early'), ('c', 'A loan charges interest on what you still owe, so paying it off early saves interest'), ('d', 'A late payment costs nothing except a little time')], 'c'),
        ('When does borrowing for a bigger hold make sense?',
         [('a', 'Whenever a loan is on offer'), ('b', 'When the extra income it brings, after the weekly payments, is more than the loan costs'), ('c', 'Only when prices are at their highest'), ('d', 'Never, because loans always lose money')], 'b'),
    ],
}
