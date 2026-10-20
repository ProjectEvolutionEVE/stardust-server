"""Contracts & Services (10-20): paying for work through the bank. Built on rules 8 and 25 (the smelting service).
The smelting service is settled by rule but NOT built yet; the book says so."""
CODE = "contracts"
BOOK = {
    "title": "Contracts & Services",
    "subtitle": "Paying for skilled work, with the bank in the middle",
    "chapters": [
        ("What a contract is",
         "A contract is a promise: you do this work, I pay this price. A good contract says what will be done, for how "
         "much, and by when. On Earth, people often used a trusted middleman, called escrow, to hold the money until "
         "the work was done."),
        ("The bank is the middleman",
         "Aboard the Starship, players never talk to each other and never see each other's names. So services work "
         "like the market: the Starship bank stands in the middle as custodian and broker. Nobody has to trust a "
         "stranger; everyone trusts the bank."),
        ("The first service: smelting",
         "Smelting turns ore into metal. A player who hasn't learned Metallurgy can pay a skilled smelter to do it. The "
         "smelter lists the service: which ores, the fee, and how long it takes. The smelter designs their own furnace "
         "as a blueprint; the Starship has no smelting bay. This service is decided but not built yet."),
        ("How a job will run",
         "You fill a cart with the ore to be smelted and drop it off. The bank holds the whole fee and tells the smelter "
         "the money is there in full, so smelting begins. When the metal comes back, you confirm with the bank that "
         "you're satisfied, and the bank pays the smelter."),
        ("If something goes wrong",
         "If you don't confirm within 48 hours and the delivery matches the expected yield, the bank pays the smelter "
         "automatically: the server knows the right yield from real chemistry. If you dispute a delivery, the server "
         "checks it. If the smelter misses the stated time, you may cancel and get your ore and your full fee back."),
        ("Fees and receipts",
         "For now the bank charges no broker's fee: it holds the money for free. Both sides get receipts. And no "
         "messages, ever: the listing, the cart and the bank say everything that needs saying."),
    ],
    "test": [
        ("Who stands in the middle of a service job?",
         [("a", "Nobody"), ("b", "The Starship bank"), ("c", "The fastest player"), ("d", "The Captain")], "b"),
        ("When does the bank pay the smelter?",
         [("a", "Before any work"), ("b", "When you confirm you're satisfied"), ("c", "Never"), ("d", "When the smelter asks")], "b"),
        ("You don't confirm within 48 hours and the yield is right. What happens?",
         [("a", "The fee is lost"), ("b", "The bank pays the smelter automatically"), ("c", "The ore is sold"), ("d", "The job restarts")], "b"),
        ("The smelter misses the stated time. What can you do?",
         [("a", "Nothing"), ("b", "Message the smelter"), ("c", "Cancel and get your ore and full fee back"), ("d", "Pay double")], "c"),
        ("What broker's fee does the bank charge for now?",
         [("a", "None"), ("b", "2.5%"), ("c", "10%"), ("d", "100 credits")], "a"),
    ],
}
