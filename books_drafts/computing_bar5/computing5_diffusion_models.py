"""Diffusion Models: how image and sound generators learn to turn noise into a clear result, step by step."""
CODE = 'computing5_diffusion_models'
BOOK = {
    "title": 'Diffusion Models',
    "subtitle": 'Adding noise, removing it, and paying for every step',
    "chapters": [
        ('The core idea',
         'A diffusion model learns by practising on damage. Training data is gradually covered with random noise until nothing recognisable is left. The model then learns to reverse one small step of that process.'),
        ('The forward process',
         'Adding noise is simple and fixed. Each step mixes in a little more random static, following a schedule chosen by the designer. By the final step the picture is almost pure noise.'),
        ('The denoising network',
         'A neural network is trained to predict the noise that was added at each step, or the cleaner image underneath it. Most modern systems use a network shaped like a U, which sees the picture at several scales. The same network is used at every step.'),
        ('Sampling and steps',
         'To generate something new, the model starts from random noise and removes a little at a time. More steps usually give finer detail but take more computing time. Faster samplers reach a good result in fewer steps.'),
        ('Guidance',
         'Guidance steers the output toward a prompt or a label. Classifier-free guidance blends a prompted prediction with an unprompted one, so the result follows the request more closely. Stronger guidance can make images sharper but less varied.'),
        ('The cost of generation',
         'Each sampling step runs the whole network again, so generation time grows with the step count. Training needs large datasets and long runs on many accelerators. Good results are therefore a matter of both design and budget.'),
    ],
    "test": [
        ('What does the forward process of a diffusion model do?',
         [('a', 'It removes noise from a finished picture'), ('b', 'It compresses the picture into a single number'), ('c', 'It adds random noise to training data step by step'), ('d', 'It labels each pixel with a colour name')], 'c'),
        ('What does the denoising network learn to predict?',
         [('a', 'The noise added at a step, or the cleaner image beneath it'), ('b', 'The total file size of the image'), ('c', 'The name of the photographer'), ('d', 'The screen brightness setting')], 'a'),
        ('What usually happens when a sampler uses more steps?',
         [('a', 'Less detail and no extra cost'), ('b', 'The model forgets its training'), ('c', 'The output becomes audio'), ('d', 'Finer detail, but more computing time')], 'd'),
        ('What is the main job of guidance?',
         [('a', 'To make training data smaller'), ('b', 'To steer the output toward a prompt or label'), ('c', 'To switch the model off'), ('d', 'To count the pixels')], 'b'),
        ('Why does generation cost grow with the step count?',
         [('a', 'The screen must be redrawn once per step'), ('b', 'Noise must be paid for in advance'), ('c', 'The network is run again at every sampling step'), ('d', 'Each step doubles the number of colours')], 'c'),
    ],
}
