"""Discounting Future Research Returns: why money later is worth less than money now, and how the discount rate is chosen."""
CODE = "science5_money_discounting"
BOOK = {
    "title": "Discounting Future Research Returns",
    "subtitle": "Present value, discount rates, time preference, uncertainty, social discount rates and choosing a rate",
    "chapters": [
        ("Present value", "Present value is what a future sum of money is worth today. A pound or a dollar received in ten years is worth less now than one in hand. Present value lets very different timings be compared on one scale."),
        ("Discount rates", "A discount rate is the rate used to reduce future money to its value today. A higher rate shrinks distant amounts more. The choice of rate often decides which projects look worthwhile."),
        ("Time preference", "Time preference is the tendency to value money now more than the same money later. People and organisations usually prefer benefits sooner. This is one reason why discounting is used at all."),
        ("Uncertainty", "Future returns are less certain than present costs, so they are often discounted more heavily. A discovery may take longer than planned, or never pay off. Discounting is one way to reflect that risk."),
        ("Social discount rates", "A social discount rate is used in public decisions to value benefits and costs over time for society as a whole. It can be lower than a private rate, because public projects often serve long-term goals. Choosing it is a value judgement as well as a technical one."),
        ("Choosing a rate", "Choose a rate that fits the decision, the risk and the setting, and state it clearly. Test how the answer changes across a range of rates. A result that holds across reasonable rates is more trustworthy than one that depends on a single number."),
    ],
    "test": [
        ("What is present value?",
         [("a", "The value today of money to be received later, after allowing for time and risk"), ("b", "Money spent in the past on equipment"), ("c", "The colour of a machine"), ("d", "The total of all bills received this year")], "a"),
        ("What is a discount rate?",
         [("a", "The percentage off in a shop sale"), ("b", "A tax on scientific income"), ("c", "A payment that applies only to loans"), ("d", "The rate used to reduce future money to its value today")], "d"),
        ("What is time preference?",
         [("a", "A preference for a particular shape of graph"), ("b", "A rule about the time of day for meetings"), ("c", "A choice of holiday dates"), ("d", "The tendency to value money now more than the same money later")], "d"),
        ("Why does uncertainty affect discounting?",
         [("a", "It does not affect discounting at all"), ("b", "Future returns are less certain, so they are often discounted more heavily"), ("c", "Uncertainty makes money worth more later"), ("d", "Only banks face uncertainty")], "b"),
        ("What is a social discount rate?",
         [("a", "A rate offered by one shop to its customers"), ("b", "A bank's profit margin"), ("c", "A rate used in public decisions to value benefits and costs over time for society"), ("d", "A fixed tax on research")], "c"),
    ],
}
