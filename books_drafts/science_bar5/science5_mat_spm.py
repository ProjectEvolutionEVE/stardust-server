"""Scanning Probe Microscopy: sharp tips that feel or sense a surface one atom at a time, and the artefacts to watch for."""
CODE = "science5_mat_spm"
BOOK = {
    "title": "Scanning Probe Microscopy",
    "subtitle": "Feeling a surface with a tip sharp enough to reach single atoms",
    "chapters": [
        ("A tiny tip", "Scanning probe microscopes move a sharp tip over a surface, very close to it. The tip can end in a single atom or a few. Each scan builds a map of the surface one point at a time."),
        ("Tunnelling current", "In a scanning tunnelling microscope, electrons tunnel across a tiny gap between the tip and the sample. The current depends very strongly on the distance. This sensitivity lets the tool see individual atoms."),
        ("Atomic force", "In an atomic force microscope, the force between the tip and the surface bends a tiny cantilever. The bending is measured with a laser. The force signal builds an image of the surface."),
        ("Imaging", "The tip scans line by line across the surface. Each line adds to the image, which builds up over minutes. Careful control keeps the tip at a steady distance."),
        ("Spectroscopy modes", "Scanning probes can also measure local properties, such as electrical or chemical responses. These modes show how the surface behaves in small areas. They go beyond simply showing shape."),
        ("Artefacts", "Tip shape, drift and vibration can all distort an image. A blunt or damaged tip can show copies of features that are not really there. Careful scientists check their images for these artefacts."),
    ],
    "test": [
        ("What is the tunnelling current used for in a scanning tunnelling microscope?",
         [("a", "Heating a sample"), ("b", "Lighting a room"), ("c", "Sensing a surface at atomic distances"), ("d", "Moving a car")], "c"),
        ("What does an atomic force microscope measure?",
         [("a", "The force between the tip and the surface"), ("b", "Sound"), ("c", "Smell"), ("d", "Ink")], "a"),
        ("Why does the tip shape matter?",
         [("a", "It has no effect"), ("b", "It only changes colour"), ("c", "It stops the scan"), ("d", "It can distort the image and create artefacts")], "d"),
        ("How is an image built in scanning probe microscopy?",
         [("a", "By a single flash"), ("b", "By scanning line by line across the surface"), ("c", "By listening to the surface"), ("d", "By freezing the surface")], "b"),
        ("What can scanning probe spectroscopy modes measure?",
         [("a", "Weight"), ("b", "Local electrical or chemical properties of the surface"), ("c", "The shape of clouds"), ("d", "Birdsong")], "b"),
    ],
}
