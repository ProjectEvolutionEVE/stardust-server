"""Funding Rounds and Dilution: how a company raises money, what a term sheet says, and how new shares reduce existing stakes."""
CODE = "computing5_funding_rounds"
BOOK = {
    "title": "Funding Rounds and Dilution",
    "subtitle": "How companies raise money, and what each new round does to existing owners",
    "chapters": [
        ("Stages of funding",
         "Companies often raise money in stages, from early savings and friends, through to larger rounds as they grow. Each stage usually brings in investors with a different appetite for risk. Each round is a sale of part of the company."),
        ("Term sheets",
         "A term sheet is a short, mostly non-binding summary of the main terms of an investment. It covers the price, the amount and the rights the investor will hold. Read every term, because the details matter later."),
        ("Dilution arithmetic",
         "Dilution is the fall in an owner's share when new shares are issued. If you own all of a company and new investors buy 20 per cent of the new total, your share falls to 80 per cent. Your stake is smaller, but it may be worth more if the company grows."),
        ("Investor rights",
         "Investors may gain rights such as a seat on the board or priority when the company is sold. Some rights can affect the founders' control. Check how much control each right takes away."),
        ("Runway",
         "Runway is how long the company can keep operating before its cash runs out. It is found by dividing the cash in hand by the monthly spending. A short runway means the next round must be planned early."),
        ("Founder choices",
         "Founders choose how much to raise, from whom, and on what terms. Raising too little can force another round too soon. Raising too much can mean giving away more of the company than needed."),
    ],
    "test": [
        ("What is a term sheet?",
         [("a", "A spreadsheet of staff holidays"), ("b", "A short summary of the main terms of an investment"), ("c", "A list of office furniture"), ("d", "A map of the building")], "b"),
        ("If you own all of a company and new shares give investors 20 per cent of the new total, what share do you keep?",
         [("a", "100 per cent"), ("b", "50 per cent"), ("c", "20 per cent"), ("d", "80 per cent")], "d"),
        ("What is dilution?",
         [("a", "A fall in an owner's share when new shares are issued"), ("b", "A rise in office rent"), ("c", "A type of tea"), ("d", "A new office policy")], "a"),
        ("How is runway worked out?",
         [("a", "The number of staff multiplied by the year"), ("b", "The price of the office divided by two"), ("c", "Cash in hand divided by monthly spending"), ("d", "The number of coffee cups")], "c"),
        ("What can raising too little money cause?",
         [("a", "A longer runway for free"), ("b", "Another round being needed too soon"), ("c", "Profit with no effort"), ("d", "No need for planning")], "b"),
    ],
}
