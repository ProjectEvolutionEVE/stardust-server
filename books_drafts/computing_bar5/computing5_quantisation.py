"""Model Compression and Quantisation: making large models smaller and faster, and checking what is lost along the way."""
CODE = 'computing5_quantisation'
BOOK = {
    "title": 'Model Compression and Quantisation',
    "subtitle": 'Fewer bits, smaller models, and the accuracy you must test for',
    "chapters": [
        ('Why compress a model',
         'A large model needs a lot of memory and power to run. Compression aims to keep most of its skill while making it smaller and faster. Phones, cars and small servers all gain from this.'),
        ('Fewer bits per weight',
         'Quantisation stores each weight, the numbers inside a model, with fewer bits, such as 8 instead of 16 or 32. Fewer bits mean less memory to move, which often speeds up inference. The rounding it causes is the source of any accuracy loss.'),
        ('Pruning',
         'Pruning removes weights or whole channels that contribute little to the output. Sparse models need special hardware or software support to run faster. Pruning is often followed by a short retraining step.'),
        ('Distillation',
         "In distillation a small student model learns to copy the outputs of a larger teacher model. The student keeps much of the teacher's behaviour in a smaller form. It usually needs its own training run and careful checking."),
        ('Accuracy loss and testing',
         'Every compression step can change answers, sometimes in ways average scores do not show. Teams test on a wide range of inputs, including rare and difficult ones. They compare the compressed model with the original on the same tests.'),
        ('Hardware speedups',
         'The real gain depends on the hardware. Some chips run low-bit arithmetic much faster, while others gain little. Speed should be measured on the device where the model will run, not assumed from the bit count.'),
    ],
    "test": [
        ("What does quantisation do to a model's weights?",
         [('a', 'It deletes the whole model'), ('b', 'It makes them into photographs'), ('c', 'It moves them to another country'), ('d', 'It stores them with fewer bits')], 'd'),
        ('What is the source of accuracy loss in quantisation?',
         [('a', 'The colour of the server rack'), ('b', 'The rounding of values to fewer bits'), ('c', 'The number of keyboard keys'), ('d', "The model's name")], 'b'),
        ('What does pruning remove?',
         [('a', "The user's data"), ('b', 'The training schedule'), ('c', 'Weights or channels that contribute little to the output'), ('d', 'The network cable')], 'c'),
        ('In distillation, what does the student model learn to do?',
         [('a', 'Copy the outputs of a larger teacher model'), ('b', "Replace the teacher's name"), ('c', 'Forget every example'), ('d', 'Run only on paper')], 'a'),
        ('Why should speed be measured on the target device?',
         [('a', 'Speed never changes between devices'), ('b', 'Some hardware gains a lot from low-bit maths and some gains little'), ('c', 'Only the screen size matters'), ('d', 'Compressed models cannot be measured')], 'b'),
    ],
}
