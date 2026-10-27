"""Procedural Noise and Generation: smooth random patterns and rule sets that build landscapes, textures and worlds from a seed."""
CODE = 'computing5_procedural_noise'
BOOK = {
    "title": 'Procedural Noise and Generation',
    "subtitle": 'Smooth randomness and seeded rules for building worlds',
    "chapters": [
        ('Smooth randomness',
         'Pure random numbers look like static, which is no use for a mountain or a cloud. Gradient noise, such as Perlin noise, gives values that change smoothly from place to place. That smoothness makes it suitable for natural-looking patterns.'),
        ('Perlin and simplex noise',
         'Perlin noise was introduced in the 1980s, and simplex noise is a later method that uses fewer calculations in higher dimensions. Both create smooth fields from random gradients on a grid. Simplex noise has fewer visible grid artefacts.'),
        ('Fractal sums',
         'Adding noise layers at increasing frequency and decreasing strength creates a fractal pattern. The result has rough detail at every scale, much like real terrain. Each added layer is called an octave.'),
        ('Grammars',
         "A grammar is a set of rules that replace one symbol with several others. Applying the rules repeatedly builds structures such as roads, buildings or plants. The rules keep the results consistent with the designer's intent."),
        ('Seeded generation',
         'A seed is a starting number that sets the whole random sequence. The same seed always produces the same world, which lets players share places and lets developers reproduce bugs. Seeds make generation repeatable.'),
        ('Quality control and tooling',
         'Generated content must be checked, because rules can produce odd or unplayable results. Tools let designers preview, adjust and reject outputs. Good tools turn the generator into a partner for the artist rather than a source of surprises.'),
    ],
    "test": [
        ('Why is pure random noise poor for a mountain?',
         [('a', 'It cannot be stored in memory'), ('b', 'It is always blue'), ('c', 'It looks like static and changes too abruptly'), ('d', 'It only works in sound')], 'c'),
        ('What does a fractal sum add to the noise?',
         [('a', 'Layers of detail at increasing frequency and decreasing strength'), ('b', 'A single flat colour'), ('c', 'A list of player names'), ('d', 'A rule for paying tax')], 'a'),
        ('What is a grammar in procedural generation?',
         [('a', 'A spelling checker'), ('b', 'A type of camera lens'), ('c', 'A sound file format'), ('d', 'A set of rules that replace symbols to build structures')], 'd'),
        ('What does a seed do?',
         [('a', 'It plants a real tree'), ('b', 'It sets the random sequence, so the same seed gives the same world'), ('c', 'It deletes the world'), ('d', 'It changes the screen colour at random')], 'b'),
        ('Why must generated content be checked?',
         [('a', 'Generated content is always perfect'), ('b', 'Checking is only needed for music'), ('c', 'Rules can produce odd or unplayable results'), ('d', 'Content cannot be seen')], 'c'),
    ],
}
