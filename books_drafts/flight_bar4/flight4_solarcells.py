"""Solar Cells: how sunlight becomes electricity in space, the stacked cells that do better, and what radiation and heat take away."""
CODE = "flight4_solarcells"
BOOK = {
    "title": "Solar Cells",
    "subtitle": "Turning sunlight into electricity in space",
    "chapters": [
        ("How a cell works", "A solar cell absorbs light and frees electrons inside a semiconductor. The electrons flow through a circuit, and that flow is electricity. Many cells joined together make a panel."),
        ("Efficiency", "Efficiency is the share of sunlight that becomes electricity. Typical cells turn only part of the light into power, and the rest becomes heat. Better designs turn a larger share."),
        ("Multi-junction cells", "A multi-junction cell stacks layers that each respond to a different part of the sunlight. Together they catch more of the light than a single layer could. These cells cost more, so they are chosen for missions where power per kilogram matters most."),
        ("Radiation damage", "Space is full of charged particles that slowly damage a cell's crystal. Over years the cell gives less power. Designers allow for this drop when they size the array."),
        ("Temperature effects", "A hotter cell makes less electricity. Craft in close to the Sun run hot, so their arrays need cooling or a design that can handle the heat."),
        ("Array shape", "Panels are arranged in arrays that face the Sun. Some arrays fold for launch and unfold in space. The shape is chosen to keep the panels pointed at the Sun while the craft moves."),
    ],
    "test": [
        ("What does a solar cell do?", [("a", "Turns light into electricity inside a semiconductor"), ("b", "Makes sound"), ("c", "Cooks food"), ("d", "Prints pictures")], "a"),
        ("What is efficiency in a solar cell?", [("a", "The number of cells in a row"), ("b", "The price of the panel"), ("c", "The share of sunlight that becomes electricity"), ("d", "The colour of the frame")], "c"),
        ("Why do multi-junction cells catch more light?", [("a", "They are painted white"), ("b", "They are always dark"), ("c", "They face the wrong way"), ("d", "Their stacked layers each respond to a different part of the sunlight")], "d"),
        ("What does radiation do to a solar cell over time?", [("a", "It makes the cell bigger"), ("b", "It slowly damages the crystal and lowers the power"), ("c", "It stops all light"), ("d", "It makes the cell sing")], "b"),
        ("What happens to a cell's output when it gets hotter?", [("a", "It makes more electricity"), ("b", "It makes the Sun brighter"), ("c", "It makes less electricity"), ("d", "Nothing changes ever")], "c"),
    ],
}
