"""Nuclear Binding Energy and Fission: why some nuclei release energy when split, how reactors use that energy, and how they are kept safe."""
CODE = "science4_phys_nuclear_binding"
BOOK = {
    "title": "Nuclear Binding Energy and Fission",
    "subtitle": "Why heavy nuclei can split and release energy",
    "chapters": [
        ("The binding energy curve",
         "Binding energy per nucleon rises steeply for light nuclei, peaks near iron, and then falls slowly for heavier ones. Nuclei near the peak are the most tightly bound. Energy is released when nuclei move toward that peak."),
        ("Mass defect",
         "A nucleus has a little less mass than the sum of its separate protons and neutrons. The missing mass is the mass defect, and it is converted into the binding energy. The relation E equals mc squared links the two."),
        ("Fission",
         "Fission is the splitting of a heavy nucleus, such as uranium-235, into two lighter nuclei. The two pieces have less total mass than the original, so energy is released. Fission also releases a few neutrons."),
        ("Chain reactions",
         "The neutrons from one fission can cause further fissions, starting a chain reaction. In a reactor the chain is kept steady, with each fission leading to about one more on average. In a bomb it grows without control."),
        ("Reactor principles",
         "A reactor uses controlled fission to heat water into steam, which turns turbines to make electricity. Control rods absorb neutrons to set the pace of the chain reaction. Coolant carries the heat away safely."),
        ("Nuclear safety basics",
         "Reactors have several layers of protection, including control systems, cooling backups and containment buildings. Waste is handled carefully, because some products remain radioactive for a long time. Safety rules are set by independent regulators."),
    ],
    "test": [
        ("Where does binding energy per nucleon peak?",
         [("a", "Near iron"), ("b", "Near hydrogen"), ("c", "Near lead"), ("d", "At the very heaviest nuclei")], "a"),
        ("What is the mass defect?",
         [("a", "The missing mass of a nucleus compared with its separate parts"), ("b", "The mass of the electrons only"), ("c", "The weight of a reactor"), ("d", "The mass of air")], "a"),
        ("What is fission?",
         [("a", "The joining of two light nuclei"), ("b", "The splitting of a heavy nucleus into lighter pieces"), ("c", "The cooling of a metal"), ("d", "The burning of coal")], "b"),
        ("What do control rods do in a reactor?",
         [("a", "Absorb neutrons to set the pace of the chain reaction"), ("b", "Heat the water directly"), ("c", "Make new uranium"), ("d", "Generate sound")], "a"),
        ("What does containment in a reactor do?",
         [("a", "Makes the reactor heavier"), ("b", "Makes electricity directly"), ("c", "Adds protection against leaks from the reactor"), ("d", "Stops the reactor from being built")], "c"),
    ],
}
