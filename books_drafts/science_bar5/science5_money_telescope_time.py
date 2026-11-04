"""The Economics of Telescope Time Allocation: how observing time is priced, shared out and judged fair among many competing astronomers."""
CODE = "science5_money_telescope_time"
BOOK = {
    "title": "The Economics of Telescope Time Allocation",
    "subtitle": "Time pricing, oversubscription rates, allocation rules, the value of observing time, user fees and fairness",
    "chapters": [
        ("Pricing observing time", "Observing time on a large telescope is valuable and limited. Some facilities put a value on it, such as a cost per hour, while others use it as a shared resource. Pricing helps decide how the facility's costs are covered."),
        ("Oversubscription", "Oversubscription happens when the time requested is greater than the time available. Most large telescopes are oversubscribed, often by several times. Oversubscription is a sign of demand, and it forces hard choices about who gets time."),
        ("Allocation rules", "Allocation rules set how time is granted. Most use peer review, scored by experts, with priority given to the strongest proposals. Rules should be published so applicants know how decisions are made."),
        ("The value of observing time", "The value of observing time is the scientific gain it could produce. It is hard to compare across proposals, because the aims differ and the outcomes are uncertain. Panels use careful judgement, supported by clear criteria."),
        ("User fees", "A user fee is a charge paid by users for access or service. Some facilities charge fees to recover running costs, while others offer free time to researchers. The choice affects who can afford to use the facility."),
        ("Allocation fairness", "Fair allocation gives different groups, institutions and countries a reasonable chance at time. Fairness also means transparent rules and clear reasons for each decision. A system seen as fair keeps the community trusting it."),
    ],
    "test": [
        ("What is time pricing for a telescope?",
         [("a", "Pricing a clock on the wall"), ("b", "Pricing an item in a shop"), ("c", "Pricing a hat"), ("d", "Putting a cost or value on observing time, such as a rate per hour or a share of allocation")], "d"),
        ("What is oversubscription?",
         [("a", "Too little demand for the facility"), ("b", "When requested observing time is greater than the time available"), ("c", "Too much cloud over the site"), ("d", "Overheating of the equipment")], "b"),
        ("What are allocation rules?",
         [("a", "Rules for parking cars"), ("b", "Rules for keeping dogs"), ("c", "Rules that set how time is granted, such as peer review and priority"), ("d", "Rules for food in the canteen")], "c"),
        ("Why is the value of observing time hard to compare?",
         [("a", "The scientific gain it could produce is hard to compare across proposals"), ("b", "Its price is written in every shop"), ("c", "It has a clear colour"), ("d", "It weighs the same in every case")], "a"),
        ("What is a user fee?",
         [("a", "A charge paid by users for access or service"), ("b", "A tip given to staff"), ("c", "A dress code for visitors"), ("d", "The price of lunch in the canteen")], "a"),
    ],
}
