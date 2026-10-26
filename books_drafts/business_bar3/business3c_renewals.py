"""Renewals and Cancellation (Business, bar 3, part C): auto-renewing contracts, the end date, and how to stop before the next payment."""
CODE = "business3c_renewals"
BOOK = {
    "title": "Renewals and Cancellation",
    "subtitle": "Auto-renewing contracts: knowing the end date, and how to stop before the next payment",
    "chapters": [
        ("Read the end date",
         "Every contract has a start and an end. Before you sign, find out when the current term ends and what happens then. Write the date in your records, so it does not catch you by surprise."),
        ("Automatic renewal",
         "Many contracts renew by themselves unless you cancel. A renewal can be sensible for a service you use every week, but a payment that repeats without your attention can add up quietly."),
        ("The craft lease",
         "The craft lease is a weekly lease of 500 credits, taken four weeks at a time, and it renews automatically unless you turn auto-renew off. Check the setting before each term ends, and decide whether you still want the craft."),
        ("Cancel in time",
         "Most agreements set a notice period. Cancel before the renewal date, not after, and keep proof that you did. A late cancellation can cost you a full term."),
        ("Compare the cost of staying",
         "Work out what the next term costs in total, and what you will actually get from it. If you would not use it, the whole term is a loss."),
        ("Watch for changes",
         "A contract that renews at a higher price can change your budget. Check the renewal price each time, not only the first one you signed."),
    ],
    "test": [
        ("What should you do first with a new contract?",
         [("a", "Sign before reading it"), ("b", "Find the end date and what happens when it ends"), ("c", "Pay the whole term in advance"), ("d", "Give it to a friend to hold")], "b"),
        ("What is automatic renewal?",
         [("a", "A payment that stops on its own"), ("b", "A contract that never starts"), ("c", "A contract that continues by itself unless you cancel"), ("d", "A fee for signing a contract")], "c"),
        ("How is the craft lease described in this book?",
         [("a", "500 credits a week, taken four weeks at a time, renewing unless auto-renew is turned off"), ("b", "50 credits an hour, with no renewal"), ("c", "A fixed fee for ever"), ("d", "A free lease with no end")], "a"),
        ("Why cancel before the renewal date?",
         [("a", "Because cancelling after renewal is illegal"), ("b", "Because the Bank requires it"), ("c", "Because it doubles the price"), ("d", "Because most agreements set a notice period that must be met before renewal")], "d"),
        ("Why check the renewal price each time?",
         [("a", "Because renewal prices never change"), ("b", "Because a renewal can cost more and change your budget"), ("c", "Because the first price is the right one for ever"), ("d", "Because renewals are free")], "b"),
    ],
}
