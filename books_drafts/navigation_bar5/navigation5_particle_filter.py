"""Particle Filters for Localisation: sample sets, weights, resampling, degeneracy and the use of maps."""
CODE = "navigation5_particle_filter"
BOOK = {
    "title": "Particle Filters for Localisation",
    "subtitle": "Tracking a position with many sample guesses",
    "chapters": [
        ("Samples instead of formulas", "A particle filter represents a belief with many sample points, called particles. Each particle is one possible state of the vehicle."),
        ("Weights", "Each particle gets a weight based on how well it matches the measurements. Heavier particles count for more."),
        ("Resampling", "Resampling copies the heavy particles and drops the light ones. This keeps the particles focused on the likely states."),
        ("Degeneracy", "Over time, one particle can end up carrying almost all of the weight. This is called degeneracy, and it weakens the filter."),
        ("Map use", "Particle filters are often used with maps, such as when a robot locates itself against a building plan. The map helps weight each particle by how well it fits."),
        ("Costs", "More particles give better results but cost more computing. Designers choose a number that suits their hardware."),
    ],
    "test": [
        ("What are the samples in a particle filter?",
         [("a", "Paints"), ("b", "Bread"), ("c", "Particles, each a possible state"), ("d", "Trees")], "c"),
        ("What decides a particle's weight?",
         [("a", "How well it matches the measurements"), ("b", "Its colour"), ("c", "Its size on paper"), ("d", "Its name")], "a"),
        ("What does resampling do?",
         [("a", "Prints maps"), ("b", "Copies heavy particles and drops light ones"), ("c", "Stops the clock"), ("d", "Cuts paper")], "b"),
        ("What is degeneracy?",
         [("a", "A loud sound"), ("b", "A new colour"), ("c", "A map title"), ("d", "One particle carries almost all the weight")], "d"),
        ("What role does a map play here?",
         [("a", "It cooks food"), ("b", "It helps weight particles by how well they fit"), ("c", "It is a printer"), ("d", "It counts sheep")], "b"),
    ],
}
