"""Bernoulli, Pressure and Lift: what the simple flow model explains, where it stops, and the wrong ideas to drop."""
CODE = 'engineering4_bernoulli'
BOOK = {
    "title": "Bernoulli, Pressure and Lift",
    "subtitle": "What the simple flow model explains, where it stops, and the wrong ideas to drop",
    "chapters": [
        ("Energy in a flowing fluid",
         "Bernoulli's principle says that in a steady flow along a streamline, pressure energy, speed energy and height energy add up to a constant. Where the flow is faster, the pressure is usually lower."),
        ("Venturi meters",
         "A venturi narrows a pipe. The faster flow in the narrow part has lower pressure, and that pressure difference measures the flow rate."),
        ("Lift from pressure",
         "A wing turns the air downward, and the pressure difference between its underside and its top gives lift. The pressure difference and the turning of the air are two views of the same physics, not a race between two halves of the flow."),
        ("Limits of the simple model",
         "Bernoulli's principle assumes steady, frictionless, incompressible flow along a streamline. Flows with friction, turbulence or shocks need more detailed models."),
        ("Wrong explanations to avoid",
         "The equal transit time idea is wrong. Air over a wing does not have to reach the trailing edge at the same time as air below it. Lift comes from the whole flow pattern."),
        ("Using the idea well",
         "Use Bernoulli for quick estimates, and check its limits before trusting it. A simple model is a tool, not the whole truth."),
    ],
    "test": [
        ("What does Bernoulli's principle say about the energies in a steady flow?",
         [("a", "They multiply"), ("b", "Pressure, speed and height energy add to a constant along a streamline"), ("c", "They vanish"), ("d", "They are always zero")], "b"),
        ("How does a venturi meter measure flow?",
         [("a", "By its colour"), ("b", "By its weight"), ("c", "By its sound"), ("d", "By the pressure difference between the wide and narrow parts")], "d"),
        ("Which explanation of lift is wrong?",
         [("a", "Air over the wing must reach the back at the same time as air underneath"), ("b", "The wing pushes the air down"), ("c", "The wing turns the air"), ("d", "Pressure differs above and below the wing")], "a"),
        ("What does Bernoulli's principle assume?",
         [("a", "Turbulent, sticky, compressible flow"), ("b", "Noisy flow"), ("c", "Steady, frictionless, incompressible flow along a streamline"), ("d", "A painted wall")], "c"),
        ("A simple model is best described as:",
         [("a", "The whole truth"), ("b", "A tool that must be checked against its limits"), ("c", "A painting"), ("d", "A law of the weather")], "b"),
    ],
}
