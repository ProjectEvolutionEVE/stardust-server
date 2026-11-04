"""Telescopes and Detectors: aperture and light gathering, angular resolution, mirrors and lenses, CCD detectors, spectrographs and observing sites."""
CODE = "science4_astro_telescopes"
BOOK = {
    "title": "Telescopes and Detectors",
    "subtitle": "Light gathering, resolution, mirrors, detectors and sites",
    "chapters": [
        ("Light gathering", "A telescope's aperture is the diameter of its main light-collecting part. A larger aperture gathers more light, so fainter objects become visible."),
        ("Angular resolution", "Angular resolution is the smallest angle between two objects that a telescope can tell apart. A larger aperture gives finer detail. Turbulence in the atmosphere can blur that detail on the ground."),
        ("Mirrors and lenses", "Telescopes use lenses or mirrors to focus light. Large research telescopes are usually reflectors. A mirror can be made very large, and it avoids the colour problems that lenses suffer from."),
        ("CCD detectors", "A CCD is a light-sensitive chip that turns light into electric charge. CCDs record images far more efficiently than photographic film, and they can measure faint light precisely."),
        ("Spectrographs", "A spectrograph spreads starlight into its colours to make a spectrum. The lines in a spectrum reveal a star's temperature, its chemical makeup and how it moves."),
        ("Observing sites", "Dark, dry, high sites with steady air make the best locations for telescopes. Light pollution from cities and turbulent air both blur and hide faint objects."),
    ],
    "test": [
        ("What does a telescope's aperture describe?",
         [("a", "Its colour"), ("b", "The diameter of its main light-collecting part"), ("c", "The length of its tube"), ("d", "The number of eyepieces")], "b"),
        ("What is angular resolution?",
         [("a", "How bright an image appears"), ("b", "How far away the telescope can see"), ("c", "How many lenses it has"), ("d", "The smallest angle between two objects a telescope can separate")], "d"),
        ("What does a CCD do?",
         [("a", "It stores starlight in a jar"), ("b", "It cools the telescope mirror"), ("c", "It turns light into electric charge"), ("d", "It moves the telescope on its mount")], "c"),
        ("Why are large research telescopes usually reflectors?",
         [("a", "A mirror can be made very large and avoids colour problems that lenses have"), ("b", "Mirrors are cheaper than paper"), ("c", "Lenses are too light"), ("d", "Reflectors can see through clouds")], "a"),
        ("What does a spectrograph do?",
         [("a", "Spreads starlight into colours to show a spectrum"), ("b", "Makes stars appear larger"), ("c", "Measures the weight of a planet"), ("d", "Cools a detector")], "a"),
    ],
}
