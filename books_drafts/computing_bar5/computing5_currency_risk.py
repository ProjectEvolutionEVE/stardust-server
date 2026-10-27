"""Currency Risk for Global Teams: how exchange rates move team costs, customer prices and reported results, and how to plan for it."""
CODE = "computing5_currency_risk"
BOOK = {
    "title": "Currency Risk for Global Teams",
    "subtitle": "How exchange rates change costs, prices and reported results",
    "chapters": [
        ("Exchange-rate exposure",
         "Exposure is the part of a business whose value changes with exchange rates. A team paid in one currency but spending in another carries exposure. Find each place where two currencies meet."),
        ("Hedging basics",
         "Hedging means using a financial agreement to fix a future exchange rate. It limits losses from rate moves but can also give up gains. Decide on a policy before the need arises."),
        ("Pricing in currencies",
         "A price set in one currency must be converted for customers in other places. Frequent rate changes can make prices look unstable. Review prices on a regular schedule."),
        ("Payroll across countries",
         "Staff paid in different countries need care with pay rates, tax rules and currency conversion. Changes in rates can shift real pay. Be clear about which currency a pay promise is made in."),
        ("Reporting",
         "Reported results must be converted into one currency for the accounts. Exchange gains and losses appear in those results. Explain these clearly so they are not mistaken for operating performance."),
        ("Planning",
         "Plan with a range of exchange rates, not a single rate. Show how costs and income change if the rate moves. Revisit the plan when a rate moves far from the one assumed."),
    ],
    "test": [
        ("What is exchange-rate exposure?",
         [("a", "A fear of the dark"), ("b", "The part of a business whose value changes with exchange rates"), ("c", "A type of visa stamp"), ("d", "A new office")], "b"),
        ("What does hedging do?",
         [("a", "Removes all currency in the bank"), ("b", "Makes rates move faster"), ("c", "Changes the staff pay"), ("d", "Fixes a future exchange rate through an agreement, limiting losses from moves")], "d"),
        ("Why plan with a range of exchange rates?",
         [("a", "Rates move, so one rate can mislead"), ("b", "Rates never change"), ("c", "Ranges are cheaper to print"), ("d", "Only one rate is ever allowed")], "a"),
        ("Why must a pay promise say which currency it uses?",
         [("a", "Because pay is never converted"), ("b", "Because currencies have no value"), ("c", "Because changing rates can shift the real value of pay"), ("d", "Because staff choose the currency each day")], "c"),
        ("What appears in reported results from currency moves?",
         [("a", "The weather"), ("b", "Exchange gains and losses"), ("c", "The office plants"), ("d", "The team's favourite colour")], "b"),
    ],
}
