"""Exoplanet Atmospheric Retrievals: how scientists work backward from a planet's light to the gases, clouds and temperatures in its air."""
CODE = 'science5_astro_retrieval'
BOOK = {
    "title": 'Exoplanet Atmospheric Retrievals',
    "subtitle": 'Reading an alien sky from its light',
    "chapters": [
        ('Working backward',
         'A retrieval starts with a measured spectrum and works back to the atmosphere that made it. It is the reverse of predicting a spectrum from a known atmosphere. The job is like guessing a recipe from the taste.'),
        ('Spectral models',
         'A spectral model is a calculation that predicts what light spectrum an atmosphere would produce. It includes gases, temperatures and clouds. Each choice of settings gives a different predicted spectrum.'),
        ('Bayesian retrieval',
         'Bayesian retrieval compares the measured spectrum with many model spectra. It gives a range of likely properties with their uncertainties. The answer is a set of possibilities, not one exact value.'),
        ('Degeneracies',
         'A degeneracy happens when different atmospheres give nearly the same spectrum. The data cannot tell them apart, so the answer stays uncertain. Recognising degeneracies is part of honest science.'),
        ('Clouds and hazes',
         'Clouds and hazes can hide spectral features that tell us about the gases below. They make the atmosphere harder to read. Including them in the model is important.'),
        ('Retrieval validation',
         'Retrieval methods are tested on simulated data where the true answer is known. If the method recovers the truth, it is more trusted on real data. This check protects against false claims.'),
    ],
    "test": [
        ('What is a spectral model in a retrieval?',
         [('a', 'A model airplane'), ('b', 'A map of rivers'), ('c', 'A calculation that predicts what light spectrum an atmosphere would produce'), ('d', 'A grocery list')], 'c'),
        ('What does Bayesian retrieval produce?',
         [('a', 'One exact answer with no error'), ('b', 'A painting of the planet'), ('c', 'A list of comets'), ('d', 'A range of likely atmosphere properties with their uncertainties')], 'd'),
        ('What is a degeneracy in retrieval?',
         [('a', 'Two planets of the same size'), ('b', 'Different atmospheres that give nearly the same spectrum, so they cannot be told apart'), ('c', 'A broken telescope'), ('d', 'A type of cloud on Earth')], 'b'),
        ('How do clouds and hazes affect a retrieval?',
         [('a', 'They can hide features in the spectrum, making the atmosphere harder to read'), ('b', 'They make the planet larger'), ('c', 'They turn the star off'), ('d', 'They have no effect at all')], 'a'),
        ('What is retrieval validation?',
         [('a', 'Checking the price of a telescope'), ('b', 'Testing the method on simulated data where the true answer is known'), ('c', 'Painting the answer on a wall'), ('d', 'Ignoring the results')], 'b'),
    ],
}
