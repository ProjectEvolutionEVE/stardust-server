"""Procurement and Purchase Controls: how purchases are requested, approved, matched and audited so spending stays honest."""
CODE = "computing5_procurement_controls"
BOOK = {
    "title": "Procurement and Purchase Controls",
    "subtitle": "How purchases are requested, approved, matched and checked",
    "chapters": [
        ("Purchase requests",
         "A purchase request says what is needed, why, how much it costs and who will use it. It starts the buying process in a visible way. A request without a clear reason is a warning sign."),
        ("Approvals",
         "Approvals are the sign-off that a purchase is allowed. Authority depends on the amount, and no one should approve their own purchase. Written approval rules make the process fair and consistent."),
        ("Three-way matching",
         "Three-way matching checks that the purchase order, the goods or service received and the supplier's invoice all agree. Payment is made only when all three match. This stops paying for things never ordered or never delivered."),
        ("Spend limits",
         "Spend limits cap how much a person or team may commit without higher approval. They keep large decisions in front of the right people. Limits should be reviewed as budgets change."),
        ("Vendor onboarding",
         "Before paying a new supplier, check its identity, bank details and basic standing. Changes to bank details should be verified through a separate route. This blocks fake suppliers."),
        ("Audits",
         "Audits sample past purchases and check that the controls were followed. Findings should go to those who can fix the process. Repeated findings signal that a control is not working."),
    ],
    "test": [
        ("What does a purchase request say?",
         [("a", "The weather forecast"), ("b", "What is needed, why, how much it costs and who will use it"), ("c", "The name of a holiday destination"), ("d", "A list of staff birthdays")], "b"),
        ("What does three-way matching compare?",
         [("a", "Three different office colours"), ("b", "Three staff salaries"), ("c", "Three weather reports"), ("d", "The purchase order, what was received and the supplier's invoice")], "d"),
        ("Why should no one approve their own purchase?",
         [("a", "Self-approval can hide poor or unauthorised spending"), ("b", "It makes the form longer"), ("c", "It is required for coffee"), ("d", "It is never a problem")], "a"),
        ("What do spend limits do?",
         [("a", "Remove all budgets"), ("b", "Pay suppliers early"), ("c", "Cap how much can be committed without higher approval"), ("d", "Stop all purchases forever")], "c"),
        ("Why verify changes to a supplier's bank details separately?",
         [("a", "To make the bank busier"), ("b", "To block fake suppliers and payment fraud"), ("c", "To slow down every payment on purpose"), ("d", "To remove the supplier")], "b"),
    ],
}
