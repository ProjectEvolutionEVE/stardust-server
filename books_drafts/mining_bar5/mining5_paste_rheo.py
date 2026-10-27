"""Paste Backfill Rheology: how a thick mix of tailings, water and binder flows, sets and fills the voids left by mining."""
CODE = "mining5_paste_rheo"
BOOK = {
    "title": "Paste Backfill Rheology",
    "subtitle": "Yield stress, pipe flow, segregation, binder content and the slump test",
    "chapters": [
        ("Filling the voids",
         "After ore is mined, the empty space can be filled with paste backfill. Paste is a thick mix of tailings, water and a small amount of binder. Filling the voids makes mines safer and more stable."),
        ("Yield stress",
         "Paste is a stiff material that does not flow until a certain stress is reached. That minimum stress is the yield stress. Once it is passed, the paste flows, and the flow then slows as the mix thickens."),
        ("Pipe flow",
         "Paste is pumped through pipes to reach the stopes. The pressure needed depends on the yield stress and the pipe size. Engineers design the pipes and pumps together so the paste keeps moving."),
        ("Segregation",
         "Heavy particles can settle out of a paste while it sits in a pipe or a stope. This is called segregation, and it leaves a weak layer. Good mixes and flow rates reduce the risk."),
        ("Binder content",
         "A binder such as cement gives the paste its strength once it sets. More binder gives more strength, but it also costs more. Engineers choose the binder content that gives enough strength at a fair price."),
        ("Slump test and plant operation",
         "The slump test measures how far a cone of fresh paste sags when lifted. It is a quick check of consistency on site. Plant operators use results like this to adjust water and binder during the shift."),
    ],
    "test": [
        ("What is paste backfill made of?",
         [("a", "Pure gold"), ("b", "Sand only, dry"), ("c", "Tailings, water and a small amount of binder"), ("d", "Ice cubes")], "c"),
        ("What is yield stress?",
         [("a", "The number of workers needed"), ("b", "The colour of the paste"), ("c", "The price of the pump"), ("d", "The minimum stress before a paste starts to flow")], "d"),
        ("What is segregation in paste?",
         [("a", "Paste splitting into two colours"), ("b", "Heavy particles settling out and leaving a weak layer"), ("c", "Paste being sold in bags"), ("d", "Paste drying in the sun")], "b"),
        ("What does binder give the paste once it sets?",
         [("a", "Strength"), ("b", "A bad smell"), ("c", "Extra water"), ("d", "A new name")], "a"),
        ("What does the slump test measure?",
         [("a", "How far a cone of fresh paste sags when lifted"), ("b", "How loud the pump is"), ("c", "How deep the stope is"), ("d", "How many trucks arrive")], "a"),
    ],
}
