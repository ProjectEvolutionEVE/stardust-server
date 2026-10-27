"""Nanoindentation and Local Hardness: measuring hardness on a scale too small to see with the eye."""
CODE = "engineering5_nanoindent"
BOOK = {
    "title": "Nanoindentation and Local Hardness",
    "subtitle": "Measuring hardness on a scale too small to see with the eye",
    "chapters": [
        ("Pressing a tiny point",
         "Nanoindentation presses a very sharp diamond tip into a surface with a small, controlled load. The depth of the mark is recorded while the load is applied and removed."),
        ("Indenter geometry",
         "The tip is usually a sharp pyramid, such as the Berkovich shape, so the contact area can be worked out from its geometry. This lets the hardness be calculated."),
        ("Load-displacement curves",
         "The curve of depth against load, recorded while loading and unloading, shows how the surface yields and springs back. The shape of the unloading part carries information about stiffness."),
        ("Oliver-Pharr analysis",
         "The Oliver-Pharr method uses the top of the unloading curve to find the contact depth and the stiffness. It is the standard way to turn the curve into hardness and modulus."),
        ("Thin film hardness",
         "For a thin film, the indent must be shallow enough that it does not feel the substrate under the film. Rules of thumb set the maximum depth as a fraction of the film thickness."),
        ("Size effects",
         "At very small depths, measured hardness can rise, because deformation becomes harder in tiny volumes. Results must be read with the size of the indent in mind."),
    ],
    "test": [
        ("What does nanoindentation measure?",
         [("a", "Paint thickness"), ("b", "Price"), ("c", "Hardness with a small controlled load and a sharp tip"), ("d", "Weight")], "c"),
        ("Why is the contact area known?",
         [("a", "Because the tip has a known shape"), ("b", "Because the surface is painted"), ("c", "Because it is guessed"), ("d", "Because it is always round")], "a"),
        ("What does a load-displacement curve record?",
         [("a", "Sound levels"), ("b", "Sales"), ("c", "Colours"), ("d", "How the surface yields and springs back")], "d"),
        ("Which method turns the unloading curve into hardness and modulus?",
         [("a", "Newton's cradle"), ("b", "Oliver-Pharr"), ("c", "A paint code"), ("d", "A price rule")], "b"),
        ("Why must indents on a thin film be shallow?",
         [("a", "So they do not feel the substrate under the film"), ("b", "To paint them"), ("c", "To make them louder"), ("d", "To count holes")], "a"),
    ],
}
