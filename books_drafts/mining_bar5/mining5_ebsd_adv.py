"""Electron Backscatter Diffraction in Practice: reading grain orientation maps from a polished sample, and knowing where the method falls short."""
CODE = "mining5_ebsd_adv"
BOOK = {
    "title": "Electron Backscatter Diffraction in Practice",
    "subtitle": "Reading the orientation of every grain on a polished surface",
    "chapters": [
        ("Diffraction from the surface", "An electron beam hits a tilted, polished sample inside a scanning electron microscope. Electrons scatter from the crystal planes and form a pattern of bands, called a Kikuchi pattern."),
        ("Reading the pattern", "Software reads each band pattern and works out the grain orientation. Each point on the sample gets a colour that shows its orientation, and the result is an orientation map."),
        ("Grain boundaries", "The map shows where neighbouring grains meet and how far their orientations differ. This lets the user pick out special boundaries and measure their share."),
        ("Strain maps", "Small changes in the pattern show the local strain in the grain. Software can build a map of kernel average misorientation, which marks zones of bending."),
        ("Sample preparation", "The surface must be polished flat and free of strain from earlier cutting. A poor surface gives weak patterns and wrong results. The sample is tilted, usually to about seventy degrees."),
        ("Limits", "The method probes only a very thin layer at the surface, so it sees a small depth. Large scans take time, and very small grains or heavily worked metals can be hard to index."),
    ],
    "test": [
        ("What does the electron beam scatter from in this method?",
         [("a", "Plastic cups"), ("b", "Crystal planes"), ("c", "Water drops"), ("d", "Clouds")], "b"),
        ("What is an orientation map?",
         [("a", "A map of roads"), ("b", "A map of sea depth"), ("c", "A map of the sky"), ("d", "A map of how each grain points")], "d"),
        ("Why must the sample surface be polished well?",
         [("a", "It makes the sample taste better"), ("b", "It makes the sample heavier"), ("c", "Poor surfaces give weak patterns and wrong results"), ("d", "It stops the beam from working at all")], "c"),
        ("What does the method probe?",
         [("a", "Only a very thin layer at the surface"), ("b", "The whole inside of a mountain"), ("c", "The air above the sample"), ("d", "The microscope lens")], "a"),
        ("What does a strain map show?",
         [("a", "Where the sun rises"), ("b", "The weight of a sample"), ("c", "Zones of bending in the grains"), ("d", "The price of metal")], "c"),
    ],
}
