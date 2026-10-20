"""Assaying (10-20): finding out what an ore holds and how much metal it will give."""
import minerals as MN

CODE = "assaying"
_C, _H, _GA = MN.MINERALS["copper"], MN.MINERALS["iron"], MN.MINERALS["gold"]

BOOK = {
    "title": "Assaying",
    "subtitle": "What is in the ore, and how much metal it will give",
    "chapters": [
        ("What an assay is",
         "An assay is a test that tells you what a sample holds and how much of it. On Earth, assayers told miners "
         "whether a find was worth working, and told buyers whether metal was what the seller claimed."),
        ("Formula tells all",
         "Out here, every ore piece is pure ore mineral. So the assay is simple: the mineral's chemical formula gives "
         "its metal's share by weight. You add up the atomic weights in the formula and see what part belongs to the "
         f"metal.\n• {_H['name']} ({_H['formula']}): {MN.yield_text(_H)}.\n"
         f"• {_C['name']} ({_C['formula']}): {MN.yield_text(_C)}.\n"
         f"• {_GA['name']} ({_GA['formula']}): {MN.yield_text(_GA)}, already metal."),
        ("Density, the quick check",
         "Every mineral has its own density. Archimedes' old trick still works: weigh a sample, then find its volume "
         "by the water it pushes aside, and divide weight by volume. "
         f"{_GA['name']} at {_GA['density']:,} kg per cubic metre is far heavier than {_C['name'].lower()} at "
         f"{_C['density']:,}, so a fake is easy to spot."),
        ("Fire assay",
         "The classic test for gold and silver on Earth is the fire assay: the sample is melted with lead in a hot "
         "furnace, the lead collects the precious metal, then the lead is burned away in a small porous cup, leaving "
         "a tiny bead to weigh. It is background knowledge: the game does not run fire assays."),
        ("Why it matters aboard",
         "When you hire a smelter, the server knows the expected yield from the chemistry. If the metal handed back "
         "matches it, the bank pays the smelter, even if you forget to confirm within 48 hours. A customer who "
         "disputes a delivery gets the server's check."),
    ],
    "test": [
        ("What does an assay tell you?",
         [("a", "The weather"), ("b", "What a sample holds, and how much"), ("c", "Who owns it"), ("d", "Its price")], "b"),
        ("In our fields, what gives an ore's metal share?",
         [("a", "Its chemical formula"), ("b", "Its colour"), ("c", "A guess"), ("d", "Its size")], "a"),
        ("How do you find density?",
         [("a", "Weight divided by volume"), ("b", "Volume times price"), ("c", "Count the pieces"), ("d", "Ask Inara")], "a"),
        ("What collects the gold in a fire assay?",
         [("a", "Water"), ("b", "Lead"), ("c", "Ice"), ("d", "Sand")], "b"),
        ("How does the bank know a smelter's delivery is right?",
         [("a", "The smelter says so"), ("b", "The server checks the expected yield from the chemistry"), ("c", "It never checks"), ("d", "Another player votes")], "b"),
    ],
}
