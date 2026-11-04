"""Ionospheric Scintillation: how the ionosphere makes satellite signals flicker, and how it is watched."""
CODE = "navigation5_scintillation"
BOOK = {
    "title": "Ionospheric Scintillation",
    "subtitle": "When the ionosphere makes signals flicker",
    "chapters": [
        ("Signal fading", "Ionospheric scintillation is rapid change in a signal's strength and phase as it passes through the ionosphere. The signal can fade, flicker or drop out."),
        ("Equatorial bubbles", "After sunset, the ionosphere over the equator can form bubbles of thin plasma. Signals that pass through them can scintillate strongly."),
        ("Polar patches", "Near the poles, patches of dense plasma can cause scintillation too. Solar storms often make these patches stronger."),
        ("Loss of lock", "Strong scintillation can break a receiver's tracking loops. The position solution can then be lost for a while."),
        ("Monitoring", "Ground stations monitor scintillation by logging signal strength and phase. The logs show when and where problems occur."),
        ("Forecasting", "Forecasts use models of the ionosphere and of space weather. They help users plan around risky times and places."),
    ],
    "test": [
        ("What is ionospheric scintillation?",
         [("a", "Rapid changes in a signal's strength and phase"), ("b", "A type of cloud"), ("c", "A printer fault"), ("d", "A loud noise")], "a"),
        ("When do equatorial bubbles most often form?",
         [("a", "At noon"), ("b", "In winter at the poles"), ("c", "After sunset"), ("d", "In the desert")], "c"),
        ("Where are polar patches found?",
         [("a", "In the deep ocean"), ("b", "In the polar ionosphere"), ("c", "On mountains"), ("d", "In deserts")], "b"),
        ("What can strong scintillation cause in a receiver?",
         [("a", "A faster battery"), ("b", "A bigger screen"), ("c", "A new map"), ("d", "Loss of lock")], "d"),
        ("What do ground stations log to monitor scintillation?",
         [("a", "Menu options"), ("b", "Signal strength and phase"), ("c", "Song titles"), ("d", "Traffic counts")], "b"),
    ],
}
