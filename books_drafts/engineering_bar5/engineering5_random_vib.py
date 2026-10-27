"""Random Vibration and Power Spectral Density: how engineers describe shaking that is random, and how to estimate the response of a structure to it."""
CODE = "engineering5_random_vib"
BOOK = {
    "title": "Random Vibration and Power Spectral Density",
    "subtitle": "Describing unpredictable shaking and how structures respond to it",
    "chapters": [
        ("Random shaking", "Much real vibration is random. Road roughness, wind gusts and rocket noise cannot be predicted exactly. Engineers describe them with statistics instead of a single exact curve."),
        ("Power spectral density", "The power spectral density, or PSD, shows how the power of a random signal is spread across frequency. It is measured in units such as g squared per hertz. A peak in the PSD shows a frequency with lots of energy."),
        ("Response to random input", "A structure with a natural frequency responds most strongly near that frequency. Its response can be found from the input PSD and the structure's frequency response. The result gives the expected root mean square level."),
        ("Miles' equation", "Miles' equation gives a quick estimate of the response of a single-mode system to a random input. The root mean square response is the square root of pi over two, times the natural frequency, times the quality factor, times the PSD at that frequency. It is a fast first check."),
        ("Test specifications", "Products are tested on shakers with a set PSD, called a test specification. The test shows whether the product survives the expected environment. Specifications are based on measured or predicted conditions for the real use."),
        ("Keeping it honest", "Random vibration results are estimates, not exact values. Engineers add margins and check their assumptions. Long tests and measured data make the estimate more reliable."),
    ],
    "test": [
        ("What does a power spectral density show?", [("a", "The colour of a sensor"), ("b", "How the power of a random signal is spread across frequency"), ("c", "The weight of a bolt"), ("d", "The number of cables")], "b"),
        ("In what units is PSD often measured?", [("a", "Metres"), ("b", "Litres"), ("c", "Kilograms per cubic metre"), ("d", "g squared per hertz")], "d"),
        ("What does Miles' equation estimate?", [("a", "The price of a machine"), ("b", "The number of workers needed"), ("c", "The response of a single-mode system to a random input"), ("d", "The colour of a test chamber")], "c"),
        ("Which factors appear in Miles' equation?", [("a", "Natural frequency, quality factor and the PSD at that frequency"), ("b", "The paint and the label"), ("c", "The room temperature only"), ("d", "The name of the test engineer")], "a"),
        ("What is a test specification?", [("a", "A list of staff names"), ("b", "A catalogue of paints"), ("c", "A bill of sale"), ("d", "A set PSD used to shake a product in a test")], "d"),
    ],
}
