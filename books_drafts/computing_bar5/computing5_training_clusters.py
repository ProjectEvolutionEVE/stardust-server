"""GPU Clusters for Training: how many accelerators work together on one model, where time is lost, and how to keep them busy."""
CODE = 'computing5_training_clusters'
BOOK = {
    "title": 'GPU Clusters for Training',
    "subtitle": 'Sharing one large training job across many accelerators',
    "chapters": [
        ('Why clusters',
         'A large model can be too big, or take too long, for one accelerator. A cluster links many of them so they share the work. Coordinating them well is as important as having many of them.'),
        ('Data parallelism',
         'In data parallelism, each accelerator holds a full copy of the model and trains on a different slice of the data. After each step the gradients are averaged across all copies. This is the simplest way to scale.'),
        ('Model parallelism',
         'When the model is too large for one device, its layers or parts are split across devices. The devices must pass intermediate results between them. Careful splitting keeps each device busy.'),
        ('Communication bottlenecks',
         'Moving gradients and activations between devices takes time, and the network can become the slowest part. Faster links and better timing help. Teams often measure communication separately from computing to see where time goes.'),
        ('Checkpointing and failures',
         'Hardware fails in long runs, so training saves checkpoints of its state at regular intervals. A failed run restarts from the latest checkpoint instead of from the beginning. Checkpoints must be saved often enough to limit lost work, but not so often that saving takes over.'),
        ('Scheduling and utilisation',
         'A cluster is shared, so a scheduler decides which job runs when. Utilisation measures how much of the hardware is doing useful work. High utilisation saves money, and idle accelerators are an expensive waste.'),
    ],
    "test": [
        ('What does data parallelism give each accelerator?',
         [('a', 'Only a single pixel of the model'), ('b', 'No model at all'), ('c', 'A different keyboard'), ('d', 'A full copy of the model and a slice of the data')], 'd'),
        ('When is model parallelism needed?',
         [('a', 'When the data is printed on paper'), ('b', 'When the model is too large for one device'), ('c', 'When the screen is too bright'), ('d', 'When there are no gradients')], 'b'),
        ('What can become the slowest part of a large training run?',
         [('a', 'The colour of the rack'), ('b', 'The name of the project'), ('c', 'The communication between devices'), ('d', 'The tea break')], 'c'),
        ('Why are checkpoints saved during training?',
         [('a', 'So a failed run can restart from a recent state'), ('b', 'So the model can be printed'), ('c', 'So the data is deleted'), ('d', 'So no one needs to monitor it')], 'a'),
        ('What does utilisation measure?',
         [('a', 'How many emails were sent'), ('b', 'How much of the hardware is doing useful work'), ('c', 'How tall the cluster is'), ('d', 'How many colours the logo has')], 'b'),
    ],
}
