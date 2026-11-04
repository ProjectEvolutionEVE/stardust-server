"""Cross-Border Funding and Currency Risk: how exchange rates change the value of international grants, and how to manage that risk."""
CODE = "science5_money_currency"
BOOK = {
    "title": "Cross-Border Funding and Currency Risk",
    "subtitle": "Exchange rates, hedging, cross-border grants, conversion costs, reporting currency and funding contracts",
    "chapters": [
        ("Exchange rates", "An exchange rate is the price of one currency in terms of another. When it changes, a grant paid in one currency is worth more or less in another. Exchange rates can move quickly and by a lot."),
        ("Hedging", "Hedging uses a contract or financial instrument to reduce the risk of exchange rate moves. A hedge fixes an exchange rate for a set amount and period. It gives certainty, but it can also cost money and may lose value if rates move the other way."),
        ("Cross-border grants", "A cross-border grant is paid across national borders, often in a currency that differs from the one the team spends. Teams working across borders must plan for the currency gap. The grant contract should say which currency applies."),
        ("Conversion costs", "Conversion costs are the fees and spreads paid when money is changed from one currency to another. They can add up on many transfers, and they reduce the value of the grant. Good planning groups transfers to reduce them."),
        ("Reporting currency", "The reporting currency is the currency used in the accounts and reports. Choosing one keeps accounts consistent and comparable across the whole project. Funders often specify the reporting currency in the contract."),
        ("Funding contracts", "A funding contract should state the currency, the exchange rate method, any currency adjustment and who carries the risk. Clear terms prevent disputes when rates move. Reviewing the terms early avoids unpleasant surprises."),
    ],
    "test": [
        ("What is an exchange rate?",
         [("a", "The fare for a bus journey"), ("b", "The name of a bank"), ("c", "A type of coin"), ("d", "The price of one currency in terms of another")], "d"),
        ("What is hedging?",
         [("a", "Planting a row of bushes"), ("b", "Building a fence around a site"), ("c", "Using a contract or instrument to reduce the risk of exchange rate moves"), ("d", "Paying only in cash")], "c"),
        ("What is a cross-border grant?",
         [("a", "A grant paid across national borders"), ("b", "A wall built on a border"), ("c", "A sea route between two ports"), ("d", "A passport for travel")], "a"),
        ("What are conversion costs?",
         [("a", "The costs of running a shop"), ("b", "The costs of religious conversion"), ("c", "Fees and spreads paid when money is changed from one currency to another"), ("d", "The cost of a car")], "c"),
        ("Why choose a reporting currency?",
         [("a", "Because it is fun to use"), ("b", "So that accounts and reports are consistent and comparable"), ("c", "To hide losses from the funder"), ("d", "Because it is the cheapest one available")], "b"),
    ],
}
