"""Capital Planning for a Research Facility: deciding which large purchases come first, how they are paid for and what they cost over their life."""
CODE = "science5_money_capex_plan"
BOOK = {
    "title": "Capital Planning for a Research Facility",
    "subtitle": "Asset lists, investment priorities, funding sources, phased purchases, lifecycle costs and the approval process",
    "chapters": [
        ("Why plan big purchases", "Capital items are large, long-lived assets such as buildings, major instruments and heavy equipment. They cost much more than everyday supplies and they last for years. A capital plan lays out what will be bought, when and why."),
        ("The asset list", "An asset list records the major equipment and buildings a facility owns, with their condition. It shows what is due for repair or replacement. Without it, planning relies on memory and guesswork."),
        ("Investment priorities", "Investment priorities rank the needs so the most important items are funded first. A ranking should weigh safety, science value, running cost and how many people the item serves. A clear ranking helps decisions stay consistent over time."),
        ("Funding and phased purchases", "Money for capital can come from grants, reserves, loans or the host institution. Phased purchases spread the cost over several stages, and each stage can be checked before the next starts. Phasing lowers the risk of buying something that no longer fits the need."),
        ("Lifecycle costs", "The lifecycle cost of an asset is the full cost over its life. It includes the purchase price, running costs, energy, maintenance, staff time and eventual disposal. The cheapest purchase is often the most expensive over its life."),
        ("The approval process", "Capital spending is checked and authorised by the right people before it goes ahead. Approval gives the funder and the institution confidence that the money is well spent. A clear process also keeps decisions open to review."),
    ],
    "test": [
        ("What is an asset list?",
         [("a", "A list of staff holidays"), ("b", "A list of journal titles"), ("c", "A record of the major equipment and buildings a facility owns, with their condition"), ("d", "A list of open grant applications")], "c"),
        ("What does an investment priority do?",
         [("a", "Chooses the paint colour for the building"), ("b", "Lets everyone buy whatever they like"), ("c", "Ranks needs so the most important items are funded first"), ("d", "Removes the need for any budget")], "c"),
        ("Why do phased purchases help?",
         [("a", "They spread the cost and let each stage be checked before the next"), ("b", "They always cost more in total"), ("c", "They stop the equipment from being used"), ("d", "They remove the need for a plan")], "a"),
        ("What are lifecycle costs?",
         [("a", "Only the price on the invoice"), ("b", "The cost of the staff party after installation"), ("c", "Only the cost of the building itself"), ("d", "The full cost over the asset's life, including running, maintenance, energy and disposal")], "d"),
        ("What does the approval process ensure?",
         [("a", "That the purchase is approved by nobody at all"), ("b", "That the spending is checked and authorised by the right people before it goes ahead"), ("c", "That the money is spent in secret"), ("d", "That all spending is delayed indefinitely")], "b"),
    ],
}
