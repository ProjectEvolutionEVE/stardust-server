"""Error-correcting Codes: how extra bits let a receiver fix damaged messages, from simple parity to Reed-Solomon."""
CODE = "flight4_coding"
BOOK = {
    "title": "Error-correcting Codes",
    "subtitle": "Extra bits that repair damaged messages",
    "chapters": [
        ("Why bits flip", "Radio noise and cosmic rays can flip a bit, turning a one into a zero or the reverse. A deep space message may pass through a lot of noise before it reaches Earth."),
        ("Parity", "The simplest code adds one extra bit, a parity bit, so that the count of ones is always even. A single flipped bit breaks the count, so the receiver knows something went wrong, but it cannot always say which bit."),
        ("Reed-Solomon", "Reed-Solomon codes add more check symbols to a block of data. They can find and repair several damaged symbols in the block. Deep space and disc players have both used this kind of code."),
        ("Convolutional codes", "Convolutional codes spread each message bit across several coded bits, and the receiver picks the most likely message from the pattern. They work well when the noise is steady and weak."),
        ("Voyager's recoveries", "Voyager used a combined code, a convolutional code with a Reed-Solomon code on top. This combination helped Voyager's data come home clearly from billions of kilometres away."),
        ("Modern codes", "Newer codes, such as low-density parity-check codes, come very close to the best limit that theory allows. They are now used in many fast data links, including some satellite systems."),
    ],
    "test": [
        ("What does a single parity bit tell the receiver?", [("a", "The weather"), ("b", "The name of the craft"), ("c", "That something went wrong, though not always which bit"), ("d", "Nothing at all")], "c"),
        ("What does Reed-Solomon do?", [("a", "Finds and repairs several damaged symbols in a block"), ("b", "Paints the message"), ("c", "Stops the radio"), ("d", "Makes the signal louder")], "a"),
        ("What do convolutional codes do with each message bit?", [("a", "Delete it"), ("b", "Print it on paper"), ("c", "Send it twice in the same place"), ("d", "Spread it across several coded bits")], "d"),
        ("What did Voyager use to bring its data home?", [("a", "Only a paper note"), ("b", "A convolutional code combined with Reed-Solomon"), ("c", "No code at all"), ("d", "A telephone line")], "b"),
        ("What do modern codes come close to?", [("a", "The colour of the Sun"), ("b", "The speed of a car"), ("c", "The best limit that theory allows"), ("d", "The depth of the sea")], "c"),
    ],
}
