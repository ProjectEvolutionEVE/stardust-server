"""Planning for Retirement: time horizon, savings rates, pensions, drawdown, inflation and living longer."""
CODE = "flight5_m_retire"
BOOK = {
    "title": "Planning for Retirement",
    "subtitle": "Time, savings, pensions and the risk of living a long life",
    "chapters": [
        ("The time horizon",
         "Your time horizon is how many years you have before you need the money. The longer the horizon, the more risk you can usually carry, because there is time to recover from a fall. A short horizon calls for safer savings."),
        ("How much to save",
         "The savings rate, the share of income you put aside, matters more than most people expect. Saving a steady share from your first job gives compounding the most time to work. Starting late means saving more each month to reach the same goal."),
        ("Pensions and state support",
         "Many countries offer a state pension, and many employers offer workplace pensions. Some are defined benefit plans, which pay a set amount, and some are defined contribution plans, where the final sum depends on what was saved and how it grew. Know which kind you have."),
        ("Drawing the money down",
         "Once you stop working, you take money out, which is called drawdown. Taking too much early can leave too little later. A slower, planned withdrawal, reviewed each year, is safer than a large one."),
        ("Inflation and living longer",
         "Inflation means prices rise over time, so the same money buys less. Many people now live into their late eighties or beyond. A plan should cover many years of living costs, and it should keep up with rising prices."),
        ("Keeping the plan honest",
         "Write down your goal, check the plan each year, and adjust when your income, health or needs change. Small steps taken early are easier than large repairs made late."),
    ],
    "test": [
        ("What does a long time horizon usually allow?",
         [("a", "No savings at all"), ("b", "Guaranteed returns"), ("c", "Skipping inflation"), ("d", "More room to carry risk, since there is time to recover")], "d"),
        ("Why does starting to save early help?",
         [("a", "Prices stop rising"), ("b", "Pensions are paid early"), ("c", "Compounding has more years to work"), ("d", "Taxes are waived")], "c"),
        ("What is drawdown?",
         [("a", "Taking money out of savings after you stop working"), ("b", "Paying a fee to a bank"), ("c", "Buying a house"), ("d", "Drawing a picture of a budget")], "a"),
        ("What does inflation do to money kept in cash?",
         [("a", "It makes it grow"), ("b", "It is locked away by law"), ("c", "It buys less over time as prices rise"), ("d", "It turns into shares")], "c"),
        ("Why should a retirement plan cover many years?",
         [("a", "Pensions only last one year"), ("b", "Many people live a long time after they stop working"), ("c", "Savings must be spent in the first year"), ("d", "Banks require it")], "b"),
    ],
}
