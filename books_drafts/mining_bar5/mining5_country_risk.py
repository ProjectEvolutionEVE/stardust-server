"""Country Risk and Sovereign Premiums: adding extra return demanded for investing in riskier countries."""
CODE = 'mining5_country_risk'
BOOK = {
    "title": 'Country Risk and Sovereign Premiums',
    "subtitle": 'Why investing in some countries demands a higher return',
    "chapters": [
        ('Country risk premium', 'Investors ask for extra return when they put money into a country with higher risk. This extra is called the country risk premium. It is added on top of the normal return an investor would expect at home.'),
        ('Political and currency risk', "Political risk includes unrest, changes of government and sudden new rules. Currency risk is the chance that the local money loses value against the investor's money. Both can cut the value of a mine's cash flows."),
        ('Rating links', 'Credit rating agencies rate the debt of countries, and these ratings are often used as a starting point for measuring risk. A lower rating usually means a larger premium. Analysts still check the ratings against their own judgement.'),
        ('Tax stability', "A country that changes its tax rules often adds risk for a mine, since the rules can alter the project's returns. Stable, clear tax terms lower the premium an investor needs. Long contracts can also give protection."),
        ('Investment hurdles', 'A hurdle rate is the minimum return a project must earn to be approved. Country risk raises the hurdle rate for projects in riskier places. A project may look good at home but fail the test abroad.'),
        ('Adjusting discount rates', 'Analysts adjust the discount rate used to value a project to reflect its country risk. Some prefer to adjust the cash flows instead, to avoid double counting. Whichever method is used, the logic should be stated clearly.'),
    ],
    "test": [
        ('What is a country risk premium?', [('a', 'A tax on sunshine'), ('b', 'Extra return investors ask for when investing in a riskier country'), ('c', 'A prize for mining gold'), ('d', 'A fee for buying paper')], 'b'),
        ('What does currency risk mean?', [('a', 'The chance that coins are bent'), ('b', 'The chance a bank opens late'), ('c', 'The chance that paper turns yellow'), ('d', "The chance that local money loses value against the investor's money")], 'd'),
        ('What does a lower credit rating usually mean for a premium?', [('a', 'A larger premium'), ('b', 'No premium at all'), ('c', 'A smaller tax bill'), ('d', 'A free mine')], 'a'),
        ('Why does an unstable tax regime add risk?', [('a', 'Taxes make rocks heavier'), ('b', 'Tax forms take up too much space'), ('c', "Changing tax rules can alter the project's returns"), ('d', 'Tax stops all mining forever')], 'c'),
        ('What is a hurdle rate?', [('a', 'A wall at a race track'), ('b', 'The height of a mine shaft'), ('c', 'The speed of a train'), ('d', 'The minimum return a project must earn to be approved')], 'd'),
    ],
}
