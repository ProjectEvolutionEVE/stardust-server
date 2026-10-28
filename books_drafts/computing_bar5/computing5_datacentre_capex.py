"""Capital Budgeting for Data Centres: whether to build or lease capacity, and how power, lead times and depreciation shape the decision."""
CODE = "computing5_datacentre_capex"
BOOK = {
    "title": "Capital Budgeting for Data Centres",
    "subtitle": "Building or leasing capacity, and how power, lead times and depreciation shape the choice",
    "chapters": [
        ("Building or leasing capacity",
         "A team can build its own data centre or lease space and equipment from a provider. Building needs large upfront spending but may cost less per year later. Leasing spreads costs but adds a long-term commitment."),
        ("Power costs",
         "Power is one of the largest running costs of a data centre. The price of electricity and the efficiency of the equipment both matter. Include power in every comparison, over the full life."),
        ("Lead times",
         "Lead time is the wait between ordering equipment or space and having it ready. Long waits delay growth and can force costly stopgaps. Plan well ahead of demand."),
        ("Depreciation",
         "Buildings and equipment are depreciated over their useful lives, which spreads their cost. Equipment often wears out faster than buildings. Match the life assumptions to what will really be used."),
        ("Cash timing",
         "Capital spending needs cash at the start, while returns arrive over many years. Model when each payment falls due. A plan that is sound on paper can still fail if cash runs short."),
        ("Risk",
         "Risks include demand falling, prices changing and projects overrunning. Compare the options under a few different scenarios. Choose the option that copes best with the risks you cannot control."),
    ],
    "test": [
        ("What is a main trade-off between building and leasing capacity?",
         [("a", "Leasing is always free"), ("b", "Building needs large upfront spending, while leasing spreads costs and adds a commitment"), ("c", "Building never costs money"), ("d", "Neither option has any cost")], "b"),
        ("Why is power important in data centre planning?",
         [("a", "It has no cost at all"), ("b", "It only matters for lighting"), ("c", "It is only a problem in winter"), ("d", "It is one of the largest running costs")], "d"),
        ("What is lead time?",
         [("a", "The wait between ordering equipment or space and having it ready"), ("b", "The time for a lunch break"), ("c", "The length of a film"), ("d", "The time a server is turned off")], "a"),
        ("What does depreciation spread?",
         [("a", "The office chairs across the floor"), ("b", "The staff across the country"), ("c", "The cost of an asset over its useful life"), ("d", "The weather across the year")], "c"),
        ("What is a sound check on a capital plan?",
         [("a", "Whether the building has a blue door"), ("b", "Whether cash is available when each payment falls due"), ("c", "Whether the plan is printed in colour"), ("d", "Whether the plan has no numbers")], "b"),
    ],
}
