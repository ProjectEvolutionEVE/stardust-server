"""Audio Synthesis: building sound from oscillators, shaping it over time, and avoiding the aliasing that spoils digital tones."""
CODE = 'computing5_audio_synthesis'
BOOK = {
    "title": 'Audio Synthesis',
    "subtitle": 'Making sound from waves, shaped over time',
    "chapters": [
        ('Oscillators',
         "An oscillator produces a repeating waveform, such as a sine, square, sawtooth or triangle wave. The shape of the wave strongly affects the sound's tone. Oscillators are the raw source of most synthesised sound."),
        ('Additive and subtractive synthesis',
         'Additive synthesis builds a sound by adding sine waves at chosen frequencies and volumes. Subtractive synthesis starts with a rich waveform and removes frequencies with a filter. Both are standard ways to shape tone.'),
        ('Frequency modulation',
         'Frequency modulation changes the pitch of one oscillator with another oscillator running at audio speed. This creates rich sidebands and complex tones from a few simple parts. It was developed in the 1970s and became famous in digital instruments.'),
        ('Envelopes',
         "An envelope sets how a sound's volume or filter changes over time, from the first attack to the decay and release. A piano and a violin differ greatly in their envelopes. Envelopes give a sound its shape in time."),
        ('Sampling',
         'Sampling plays back recorded sounds, often changed in pitch and length. Good sample playback needs careful looping and layered recordings. Samples are a practical route to realistic instruments.'),
        ('Aliasing',
         'A digital system that generates harmonics above half the sample rate produces aliasing, which sounds like harsh, false tones. Oversampling and band-limited waveforms reduce it. Avoiding aliasing is one of the main quality tasks in synthesis.'),
    ],
    "test": [
        ('What does an oscillator produce?',
         [('a', 'A printed page'), ('b', 'A repeating waveform'), ('c', 'A photograph'), ('d', 'A video stream')], 'b'),
        ('What does additive synthesis do?',
         [('a', 'It adds more paper to a score'), ('b', 'It removes all sound'), ('c', 'It sends sound by post'), ('d', 'It adds sine waves at chosen frequencies and volumes')], 'd'),
        ('What is an envelope in synthesis?',
         [('a', "How a sound's volume or filter changes over time"), ('b', 'A paper packet for a CD'), ('c', 'A type of microphone'), ('d', 'A password for the studio')], 'a'),
        ('What is aliasing?',
         [('a', 'A type of speaker cable'), ('b', 'A kind of sheet music'), ('c', 'Harsh, false tones from frequencies above half the sample rate'), ('d', 'A name for a music genre')], 'c'),
        ('What does frequency modulation use to change pitch?',
         [('a', 'A paintbrush'), ('b', 'A pair of scissors'), ('c', 'A sheet of glass'), ('d', 'Another oscillator running at audio speed')], 'd'),
    ],
}
