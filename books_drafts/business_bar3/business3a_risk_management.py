"""Risk Management (Manager, bar 3, part A): find the risks, measure them, and choose how to answer each one."""
CODE = "business3a_risk_management"
BOOK = {
    "title": "Risk Management",
    "subtitle": "Find the risks, measure them, and choose how to answer each one",
    "chapters": [
        ("Find the risks",
         "A risk is something that could go wrong and cost you. Start by listing the risks to your business: a price falling, a buyer not paying, a machine breaking, a loan rate rising. Write them all in one place, so none is forgotten."),
        ("Likelihood and impact",
         "For each risk, estimate how likely it is and how much it would cost if it happened. Multiply the two, and the result is the expected cost. A 25% chance of losing 800 credits has an expected cost of 200 credits. Rank your risks by that number."),
        ("Four answers",
         "There are four common answers to a risk. You can avoid it by not taking it on. You can reduce it, for example by keeping a reserve. You can transfer it, for example by buying insurance. Or you can accept it, when the cost is small and you have set money aside for it."),
        ("Keep a reserve",
         "A reserve is money set aside for a risk you have chosen to accept. It turns a surprise into a planned cost. Size it to the risks on your list, not to hope that nothing goes wrong."),
        ("Watch and update",
         "Risks change. Review the list every week or so, and add any new risk, such as a new loan or a new rule. A risk you dealt with earlier may need checking again after a while."),
        ("Protect the business first",
         "Some risks could end the business, even when their chance is small. Those come first. Avoid them, or transfer them, rather than hoping for the best. A small risk that is easy to recover from is a different matter."),
    ],
    "test": [
        ("What is a risk, in business?",
         [("a", "A guaranteed profit"), ("b", "A sale that has already been paid"), ("c", "Something that could go wrong and cost you"), ("d", "A kind of loan")], "c"),
        ("A risk has a 25% chance of costing 800 credits. What is its expected cost?",
         [("a", "200 credits"), ("b", "800 credits"), ("c", "25 credits"), ("d", "2,000 credits")], "a"),
        ("Which answer to a risk means choosing not to take it on at all?",
         [("a", "Reduce"), ("b", "Transfer"), ("c", "Accept"), ("d", "Avoid")], "d"),
        ("Which answer to a risk is buying insurance?",
         [("a", "Avoid"), ("b", "Transfer"), ("c", "Reduce"), ("d", "Accept")], "b"),
        ("Which risk should you deal with first?",
         [("a", "The one that is easiest to ignore"), ("b", "The smallest, however likely"), ("c", "The one that could end the business, even if its chance is small"), ("d", "The newest one")], "c"),
    ],
}
