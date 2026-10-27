"""Speech Recognition Pipelines: how spoken sound becomes text, from acoustic features to a final, checked transcript."""
CODE = 'computing5_speech_recognition'
BOOK = {
    "title": 'Speech Recognition Pipelines',
    "subtitle": 'From sound waves to text, and where it goes wrong',
    "chapters": [
        ('From sound to features',
         'Speech is a pressure wave, sampled many thousands of times a second. The system turns short slices of that signal into acoustic features, numbers that describe the pitch and energy of each slice. Those features are what the rest of the pipeline reads.'),
        ('The acoustic model',
         'The acoustic model estimates which speech sounds, or units close to them, are most likely in each part of the signal. Modern systems use neural networks for this. Their output is a series of likely sounds, with some uncertainty.'),
        ('Decoding',
         'The decoder searches for the best word sequence that fits the acoustic evidence. It works through many candidate paths and keeps the most likely ones. The search must run fast enough for the speaker.'),
        ('The language model',
         "A language model scores how natural a word sequence is, so the system can choose between words that sound alike. Knowing that a phrase is common helps it choose correctly. The language model also pulls in some of the training text's habits, good and bad."),
        ('Measuring errors',
         'The usual measure is the word error rate: the number of substituted, deleted and inserted words, divided by the number of words in the correct text. A low figure on a test set does not guarantee the same figure in daily use. Real audio is noisier and more varied.'),
        ('Streaming, accents and fairness',
         'Streaming recognition must give partial text while the person is still speaking, which trades speed against accuracy. Accents, dialects and speaking styles can lead to higher error rates for some groups. Testing across many speakers and conditions is part of responsible design.'),
    ],
    "test": [
        ('What does an acoustic model estimate?',
         [('a', 'The price of the microphone'), ('b', 'The battery level of the phone'), ('c', 'The colour of the sound wave'), ('d', 'Which speech sounds are likely in each part of the signal')], 'd'),
        ('What is the job of the decoder?',
         [('a', 'To record the sound'), ('b', 'To search for the most likely word sequence that fits the evidence'), ('c', 'To delete background noise forever'), ('d', 'To translate text into video')], 'b'),
        ('What does a language model add to recognition?',
         [('a', 'It makes the microphone louder'), ('b', 'It counts the speakers in the room'), ('c', 'It scores how natural a word sequence is'), ('d', 'It stores the audio file')], 'c'),
        ('What does the word error rate count?',
         [('a', 'Substitutions, deletions and insertions, relative to the correct text'), ('b', 'The number of microphones used'), ('c', 'The length of the recording in minutes'), ('d', 'The number of languages supported')], 'a'),
        ('What is the trade-off in streaming recognition?',
         [('a', 'Accuracy is perfect but nothing appears until the end'), ('b', 'Partial text arrives quickly, but accuracy can be lower'), ('c', 'Audio must be recorded in colour'), ('d', 'Only one word can be recognised at a time')], 'b'),
    ],
}
