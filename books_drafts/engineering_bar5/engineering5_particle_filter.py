"""Particle Filters for Nonlinear Estimation: particle sampling, weighting, resampling, degeneracy and when to use particles."""
CODE = "engineering5_particle_filter"
BOOK = {
    "title": "Particle Filters for Nonlinear Estimation",
    "subtitle": "Tracking a state with a cloud of guesses",
    "chapters": [
        ("Why particles",
         "A Kalman filter assumes a simple, bell-shaped uncertainty and a straight-line model. Many real systems break these rules. A particle filter handles nonlinear models and odd shapes of uncertainty by using many guesses instead."),
        ("Particle sampling",
         "Each particle is one possible value of the state. The filter starts with many particles spread over the possible states. Each particle is moved forward using the model, with a little random noise added."),
        ("Weighting",
         "When a measurement arrives, each particle is given a weight. A particle that agrees well with the measurement gets a high weight, and one that disagrees gets a low weight. The weights show which guesses are most likely to be right."),
        ("Resampling",
         "Particles with tiny weights are dropped, and particles with large weights are copied. This keeps the cloud focused on the likely states. The cloud then moves on to the next measurement."),
        ("Degeneracy",
         "Over time, weight can collect on one or two particles, leaving the rest useless. This is called degeneracy, and it wastes the filter's effort. Engineers fight it with enough particles and by resampling at the right times."),
        ("When to use particles",
         "Particle filters suit problems with strange models or uncertainty that is not bell-shaped. They need more computing power than a Kalman filter. Engineers choose them when the simpler methods clearly fail."),
    ],
    "test": [
        ("What does each particle represent?",
         [("a", "A grain of sand"), ("b", "A part of the paint"), ("c", "One possible value of the state"), ("d", "A unit of money")], "c"),
        ("What does a particle with a high weight mean?",
         [("a", "It agrees well with the latest measurement"), ("b", "It has been painted"), ("c", "It is heavy"), ("d", "It has left the cloud")], "a"),
        ("What does resampling do?",
         [("a", "It removes all particles"), ("b", "It changes the colour of the cloud"), ("c", "It stops the sensor"), ("d", "It keeps likely particles and drops unlikely ones")], "d"),
        ("What is degeneracy in a particle filter?",
         [("a", "The filter becomes too cheap"), ("b", "The weight collects on one or two particles, leaving the rest useless"), ("c", "The particles are painted"), ("d", "The model is written in a different language")], "b"),
        ("When would a particle filter be chosen over a Kalman filter?",
         [("a", "When the sensor is painted red"), ("b", "When there is no computer"), ("c", "When the model is strongly nonlinear or the uncertainty is not bell-shaped"), ("d", "When the task is painting walls")], "c"),
    ],
}
