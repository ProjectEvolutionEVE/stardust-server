"""Procurement Strategy for Heavy Equipment: sourcing, supplier panels, total cost, risk, negotiation and performance."""
CODE = 'mining5_procure'
BOOK = {
    "title": "Procurement Strategy for Heavy Equipment",
    "subtitle": "Sourcing, supplier panels, total cost and negotiation",
    "chapters": [
        ("Buying big machines well",
         "Heavy equipment is costly, long-lived and critical to the work. A poor purchase can cost for decades. Procurement strategy sets how the company buys, not only what it buys."),
        ("Sourcing",
         "Sourcing is the search for the right supplier for a need. Look beyond the first supplier you know, and compare options on the same terms. A clear specification makes the comparison fair."),
        ("Supplier panels",
         "A supplier panel is a group of pre-approved suppliers for a category of work. A panel saves time on each purchase and keeps standards high. Panels should be reviewed regularly, so that weak suppliers are replaced."),
        ("Total cost of ownership",
         "Total cost of ownership adds the purchase price to running, fuel, maintenance, parts and disposal over the life of the machine. A cheap machine can be the most costly over its life. Always compare on the whole cost."),
        ("Risk and negotiation",
         "Procurement weighs risks such as delivery delays, spare parts and supplier health. Negotiation aims for a fair deal both sides can keep. Squeezing a supplier until it fails leaves you without support when you need it."),
        ("Performance",
         "Track supplier performance against agreed service levels, quality and delivery. Share the results with the supplier, and act on the trends. Good performance records make the next negotiation fairer."),
    ],
    "test": [
        ("What is total cost of ownership?",
         [("a", "Only the purchase price"), ("b", "The price paid to the seller only"), ("c", "The purchase price plus running, maintenance and disposal costs over the life of the machine"), ("d", "The cost of the sales team")], "c"),
        ("What is a supplier panel?",
         [("a", "A pre-approved group of suppliers for a category of work"), ("b", "A solar panel on the office roof"), ("c", "A television display in the lobby"), ("d", "A single supplier with no competition")], "a"),
        ("Why is relying on a single source risky?",
         [("a", "It is always cheaper"), ("b", "It has no risk at all"), ("c", "It removes the need for contracts"), ("d", "If it fails, there is no quick alternative")], "d"),
        ("What should supplier performance be tracked against?",
         [("a", "The weather"), ("b", "Agreed service levels, quality and delivery"), ("c", "The supplier's favourite colour"), ("d", "The number of emails sent")], "b"),
        ("What is a good aim in supplier negotiation?",
         [("a", "Squeezing the supplier until it fails"), ("b", "Hiding the true need"), ("c", "A fair deal that both sides can keep"), ("d", "Signing the first offer")], "c"),
    ],
}
