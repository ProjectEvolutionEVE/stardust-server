"""Radio Link Budgets: adding up the power, the gains and the losses that decide whether a radio signal can be heard."""
CODE = "flight4_link_budget"
BOOK = {
    "title": "Radio Link Budgets",
    "subtitle": "Power, gain, loss and margin in one sum",
    "chapters": [
        ("A list of gains and losses", "A link budget is a ledger for a radio signal. It starts with the power sent, adds the gains of the antennas, and subtracts the losses along the way. What is left decides whether the signal can be heard."),
        ("Power out", "The transmitter sets how much power leaves the craft. More power gives a stronger signal, but power costs weight, heat and energy, so it has to be chosen with care."),
        ("Spreading loss", "A radio wave spreads out as it travels. Over billions of kilometres it is spread very thin, and most of the power is lost in that spreading. This is the biggest loss in a deep space link."),
        ("Antenna gain", "A big dish focuses the signal like a torch beam. Gain is the boost from that focus. A larger dish or a higher frequency gives more gain, but it also needs more accurate pointing."),
        ("Noise", "Every receiver adds some noise of its own, and the sky adds some too. The signal must be stronger than this noise to be read. Cold receivers add less noise, so they hear faint signals better."),
        ("Bits per second and margin", "The data rate, in bits per second, is set so that the signal can still be decoded. Engineers always keep a margin, an extra safety amount, so the link still works when things go a little wrong."),
    ],
    "test": [
        ("What is a link budget?", [("a", "A list of crew wages"), ("b", "A ledger that adds the power, gains and losses of a radio signal"), ("c", "A map of stars"), ("d", "A shopping list")], "b"),
        ("What is spreading loss?", [("a", "A spilled cup of tea"), ("b", "A broken window"), ("c", "Crew sleep time"), ("d", "Power lost as the radio wave spreads out over distance")], "d"),
        ("What does a bigger dish give the link?", [("a", "More gain, as the signal is focused"), ("b", "Less signal"), ("c", "No change"), ("d", "A louder crew")], "a"),
        ("What must a signal be to be read?", [("a", "Quieter than a whisper"), ("b", "The same colour as the sky"), ("c", "Stronger than the noise"), ("d", "Hidden under paint")], "c"),
        ("What is the margin in a link budget?", [("a", "A mistake to remove"), ("b", "An extra safety amount so the link still works when things go wrong"), ("c", "The edge of the paper"), ("d", "A type of antenna")], "b"),
    ],
}
