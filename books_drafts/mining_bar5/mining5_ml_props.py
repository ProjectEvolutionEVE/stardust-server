"""Machine Learning for Material Properties: teaching a computer to predict how a material behaves."""
CODE = 'mining5_ml_props'
BOOK = {
    "title": 'Machine Learning for Material Properties',
    "subtitle": 'Teaching a computer to predict how a material behaves',
    "chapters": [
        ('Feature design', 'A model needs inputs that describe each material, called features or descriptors. Choosing good features, such as atomic size or electron count, is often the hardest part. Poor features give poor predictions, however clever the model.'),
        ('Training data', 'A model learns from examples where the answer is already known. The data must be accurate, varied and large enough to cover the cases the model will meet. Missing or wrong data quietly weakens every prediction.'),
        ('Model choice', 'Many kinds of model can be used, from simple linear fits to deep neural networks. Simple models are easier to understand and check. More complex models can fit more patterns but need more data and care.'),
        ('Uncertainty', 'A good model reports how sure it is, not just a single number. Uncertainty tells a researcher when a prediction can be trusted and when a lab test is needed. Ignoring uncertainty is a common mistake.'),
        ('Validation', 'A model is tested on data it has never seen, called held-out data. If it does well there, it has learned something real rather than memorising. Validation should match how the model will be used in practice.'),
        ('Practice', 'Machine learning is a tool that works alongside physics and chemistry, not in place of them. Teams check predictions against experiments and keep notes on where the model fails. Honest checking is what makes a model useful.'),
    ],
    "test": [
        ('What are features in a materials model?', [('a', 'Decorations on a computer screen'), ('b', 'Descriptions of each material that the model uses as inputs'), ('c', 'The final lab report'), ('d', 'Parts of a furnace')], 'b'),
        ('Why does training data need to be accurate?', [('a', 'Because accurate data is always smaller'), ('b', 'Because the model prints it'), ('c', 'Because it helps the colour of the screen'), ('d', 'Because wrong data quietly weakens every prediction')], 'd'),
        ('What is held-out data used for?', [('a', 'To test the model on examples it has never seen'), ('b', 'To heat the lab'), ('c', 'To store old reports'), ('d', 'To give the model a new name')], 'a'),
        ("Why is a model's stated uncertainty important?", [('a', 'It makes the model run faster'), ('b', 'It removes the need for features'), ('c', 'It shows when a prediction can be trusted and when a lab test is needed'), ('d', "It changes the material's colour")], 'c'),
        ('Which is a simple kind of model mentioned here?', [('a', 'A steam engine'), ('b', 'A glass lens'), ('c', 'A ladder'), ('d', 'A linear fit')], 'd'),
    ],
}
