"""Mining (10-20): real-world basics of mining, and how collecting ore works aboard."""
import minerals as MN

CODE = "mining"
_G, _GA = MN.MINERALS["galena"], MN.MINERALS["gold"]
_I = MN.MINERALS["water-ice"]

BOOK = {
    "title": "Mining",
    "subtitle": "Collecting ore from the debris fields, and the basics of mining",
    "chapters": [
        ("What mining is",
         "Mining is taking useful minerals out of the place they are found. On Earth, miners dug open pits or tunnels "
         "into rock. Out here there is no ground to dig: the ore is already broken into pieces, drifting in the "
         "debris fields. Mining aboard means finding a field and collecting the pieces worth having."),
        ("Ore as it is found",
         "Debris fields hold ores, not refined metal. Each piece is pure ore mineral, so its formula tells you what "
         "it holds. Turning ore into metal is smelting, which is a separate skill (Metallurgy)."),
        ("Weight matters",
         "Every piece weighs its size times its real density. Heavy and light ores differ a lot: "
         f"{_G['name'].lower()} is {_G['density']:,} kg per cubic metre and {_GA['name'].lower()} "
         f"{_GA['density']:,}, while {_I['name'].lower()} is only {_I['density']:,}. "
         "Two pieces the same size can weigh very different amounts."),
        ("Nothing is unlimited",
         "Your ship's hold has a size, and a piece only comes aboard if its shape fits with room left. Pick pieces "
         "that are worth the space. When you unload, the ore goes to your own space in the Starship's cargo hold, "
         "which also has a fixed size."),
        ("A receipt for every load",
         "Every time goods move, you get a receipt with a code anyone can check. Your receipts are kept in the log "
         "in your filing cabinet, and you can save a copy to your own device."),
        ("Selling in lots",
         "The market trades ore in lots, and one lot is the smallest order: iron and copper ore 100 kg, silver ore "
         "10 kg, gold and diamond 1 kg. Ore under one lot waits in the hold until you have a full lot."),
        ("Real time, real rest",
         "Mining runs in real time. A long run can continue while you are offline, and your character's health bars "
         "keep draining while it works. Come back rested: below 65% your abilities decline severely, and below 50% extremely."),
    ],
    "test": [
        ("What do debris fields hold?",
         [("a", "Refined metal bars"), ("b", "Ores, as they were found"), ("c", "Only ice"), ("d", "Finished parts")], "b"),
        ("How is a piece's weight worked out?",
         [("a", "Its size times its density"), ("b", "Every piece weighs 1 kg"), ("c", "By its colour"), ("d", "You choose it")], "a"),
        ("When does a piece come aboard?",
         [("a", "Always"), ("b", "Only if it is gold"), ("c", "When its shape fits your hold, with room left"), ("d", "Only on Tuesdays")], "c"),
        ("What do you get every time goods move?",
         [("a", "A receipt with a code anyone can check"), ("b", "Nothing"), ("c", "A message from another player"), ("d", "A free lot")], "a"),
        ("What is the smallest order of iron ore on the market?",
         [("a", "1 kg"), ("b", "10 kg"), ("c", "100 kg"), ("d", "1 tonne")], "c"),
    ],
}
