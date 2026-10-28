"""Rainflow Counting of Load History: turning a messy load record into cycles that can be counted for damage."""
CODE = "engineering5_rainflow"
BOOK = {
    "title": "Rainflow Counting of Load History",
    "subtitle": "Turning a messy load record into cycles that can be counted for damage",
    "chapters": [
        ("A messy load record",
         "A real load history rises and falls in an irregular way. Fatigue needs to know how many cycles of each size it contains."),
        ("Reversals",
         "A reversal is a peak or a valley in the record. The rainflow method works from these turning points and ignores points where the load does not turn."),
        ("The rainflow algorithm",
         "The method takes the record, finds closed loops within it, and counts each loop as one cycle of a given range. The name comes from imagining the load as rain running down the roofs of a pagoda."),
        ("Load spectra",
         "The counted cycles form a load spectrum, a table of how many cycles of each size occur. This spectrum is the input to a damage calculation."),
        ("Damage summation",
         "Miner's rule adds up the damage from each size of cycle, as a fraction of the life at that size. Failure is expected when the total reaches about one, which is a simple estimate that works well in many cases."),
        ("Reading field data",
         "Measured records are often long and noisy. Clean the data, keep the reversals, and check that the counted cycles match the total time of the record."),
    ],
    "test": [
        ("What is a reversal?",
         [("a", "A paint layer"), ("b", "A reverse gear"), ("c", "A heat wave"), ("d", "A peak or valley in the load record")], "d"),
        ("What does rainflow counting produce?",
         [("a", "A colour chart"), ("b", "A count of cycles of each size"), ("c", "A price list"), ("d", "A weather report")], "b"),
        ("What is a load spectrum?",
         [("a", "A rainbow"), ("b", "A list of suppliers"), ("c", "A table of how many cycles of each size occur"), ("d", "A map")], "c"),
        ("What does Miner's rule add up?",
         [("a", "The damage from each size of cycle, as a fraction of its life"), ("b", "Paint"), ("c", "Hours of sleep"), ("d", "Prices")], "a"),
        ("What should you check when counting cycles?",
         [("a", "That the counted cycles match the total time of the record"), ("b", "That the paint is dry"), ("c", "That the price is low"), ("d", "That the sun is up")], "a"),
    ],
}
