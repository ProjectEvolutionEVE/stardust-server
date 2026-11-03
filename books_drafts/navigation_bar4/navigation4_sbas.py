"""Satellite-Based Augmentation: wide-area corrections, integrity messages and aviation approaches."""
CODE = "navigation4_sbas"
BOOK = {
    "title": "Satellite-Based Augmentation",
    "subtitle": "Wide-area corrections and the safety of aviation",
    "chapters": [
        ("Wide-area corrections", "A satellite-based augmentation system, or SBAS, sends corrections over a wide area. The corrections improve the accuracy of GPS positions. A receiver uses them to get a better fix."),
        ("Geostationary broadcasts", "SBAS satellites sit in geostationary orbit. They broadcast the corrections to users below. Their fixed position makes the signal easy to receive."),
        ("WAAS and EGNOS", "WAAS covers North America and EGNOS covers Europe. Other regions have their own systems, such as MSAS in Japan and GAGAN in India. Each system serves its own region."),
        ("Integrity messages", "SBAS sends integrity messages. These warn users when a signal is not safe to use. This is a key feature for safety-critical work."),
        ("Aviation approaches", "SBAS supports aircraft approaches to airports. The system allows precise guidance down to low heights. Pilots rely on it for safe landings."),
        ("Limits", "SBAS works only where its signals reach. Some places have poor coverage. A receiver must be able to receive the SBAS signal to use it."),
    ],
    "test": [
        ("What does SBAS do?",
         [("a", "Cooks food"), ("b", "Paints boats"), ("c", "Sends corrections over a wide area"), ("d", "Counts fish")], "c"),
        ("Where do SBAS satellites sit?",
         [("a", "On the ground"), ("b", "In geostationary orbit"), ("c", "Under the sea"), ("d", "On the Moon")], "b"),
        ("Which of these systems covers Europe?",
         [("a", "WAAS"), ("b", "EGNOS"), ("c", "MSAS"), ("d", "GAGAN")], "b"),
        ("What do integrity messages do?",
         [("a", "Warn users when a signal is not safe to use"), ("b", "Play music"), ("c", "Print maps"), ("d", "Count birds")], "a"),
        ("Which use does SBAS support strongly?",
         [("a", "Ice fishing"), ("b", "Tennis"), ("c", "Gardening"), ("d", "Aircraft approaches to airports")], "d"),
    ],
}
