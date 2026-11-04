"""Photochemistry and Excited States: how light excites molecules, and what happens next."""
CODE = "science5_chem_photochem"
BOOK = {
    "title": "Photochemistry and Excited States",
    "subtitle": "Electronic excitation, Jablonski diagrams and energy transfer",
    "chapters": [
        ("Light drives change", "Photochemistry studies chemical change caused by light. A molecule absorbs a photon and jumps to an excited electronic state. Its behaviour then depends on what happens next."),
        ("Jablonski diagrams", "A Jablonski diagram shows energy levels for singlet and triplet states and the transitions between them. Arrows show absorption, fluorescence, phosphorescence and other steps. The diagram is a map of possible fates for an excited molecule."),
        ("Fluorescence and phosphorescence", "Fluorescence is light emitted quickly from a singlet excited state. Phosphorescence is light emitted much more slowly from a triplet state. Phosphorescence can last from a fraction of a second to many seconds or longer."),
        ("Energy transfer", "An excited molecule can pass its energy to a nearby molecule without emitting light. This is energy transfer, and it is important in many photochemical systems. Some sensitisers are chosen for their ability to transfer energy efficiently."),
        ("Photoreactions", "An excited molecule can also react chemically, for example by breaking a bond or rearranging its atoms. These photoreactions can give products that are hard to make in the dark. Photochemistry is used in some industrial processes."),
        ("Solar energy conversion", "Solar energy conversion captures sunlight to make fuels or electricity. Light-harvesting dyes and catalysts are studied for this purpose. Good designs use excited states efficiently and avoid wasting energy."),
    ],
    "test": [
        ("What does a molecule do when it absorbs a photon?",
         [("a", "It turns into a metal"), ("b", "It jumps to an excited electronic state"), ("c", "It falls through the floor"), ("d", "It makes a sound only")], "b"),
        ("What is a Jablonski diagram?",
         [("a", "A list of plant names"), ("b", "A picture of a cloud"), ("c", "A chart of tide heights"), ("d", "A map of energy levels and the transitions between them")], "d"),
        ("How does fluorescence differ from phosphorescence?",
         [("a", "Fluorescence is slow and phosphorescence is quick"), ("b", "Both are the same thing"), ("c", "Fluorescence is quick, from a singlet state; phosphorescence is slower, from a triplet state"), ("d", "Phosphorescence only happens in the dark for a year")], "c"),
        ("What is energy transfer in photochemistry?",
         [("a", "An excited molecule passing its energy to a nearby molecule"), ("b", "Sunlight moving to the Moon"), ("c", "Water being turned into ice"), ("d", "Glass being broken by heat")], "a"),
        ("What can an excited molecule do in a photoreaction?",
         [("a", "Vanish from the universe"), ("b", "Turn into a plant seed"), ("c", "Stop existing at once"), ("d", "Break a bond or rearrange its atoms")], "d"),
    ],
}
