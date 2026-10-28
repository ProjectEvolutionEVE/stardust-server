"""Two-Phase Flow Regimes: how gas and liquid arrange themselves in a pipe, and why the pattern matters for pressure and measurement."""
CODE = "engineering5_two_phase"
BOOK = {
    "title": "Two-Phase Flow Regimes",
    "subtitle": "Bubble, slug, churn and annular flow, and flow maps",
    "chapters": [
        ("Gas and liquid together", "When gas and liquid flow together in a pipe, they form patterns called flow regimes. The pattern depends on the flow rates of both fluids and on the pipe."),
        ("Bubble and slug", "Bubble flow has small bubbles spread through the liquid. Slug flow has large bubbles that fill most of the pipe, separated by slugs of liquid."),
        ("Churn and annular", "Churn flow is chaotic and unsteady. Annular flow has gas in the core of the pipe, with the liquid forming a film on the wall."),
        ("Flow maps", "A flow map shows which regime is expected for given gas and liquid flow rates. It is a quick guide for design and for reading test data."),
        ("Pressure drop", "Each regime has its own pressure drop. This matters for choosing pumps and compressors and for predicting the energy the system needs."),
        ("Void fraction", "Void fraction is the share of the pipe filled by gas at a given place. It is measured with several methods, and each method has its own limits."),
    ],
    "test": [
        ("What is bubble flow?", [("a", "A sheet of ice over water"), ("b", "Small bubbles spread through a liquid"), ("c", "A dry road surface"), ("d", "A solid steel bar")], "b"),
        ("What is slug flow?", [("a", "A snail moving along a pipe"), ("b", "A coin dropped in a pipe"), ("c", "A paint mixing process"), ("d", "Large bubbles that fill most of the pipe")], "d"),
        ("What is annular flow?", [("a", "Gas in the core with liquid as a film on the wall"), ("b", "A ring of ice on a pipe"), ("c", "A bolt used in pipe joints"), ("d", "A seal for a valve")], "a"),
        ("What is a flow map?", [("a", "A chart showing the expected regime for given flow rates"), ("b", "A street map of a city"), ("c", "A map of the moon"), ("d", "A menu for the canteen")], "a"),
        ("What is void fraction?", [("a", "The price of gas per cubic metre"), ("b", "The colour of the pipe"), ("c", "The speed of the pump"), ("d", "The share of the pipe filled by gas")], "d"),
    ],
}
