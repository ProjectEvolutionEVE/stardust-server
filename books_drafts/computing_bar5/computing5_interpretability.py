"""Interpretability Methods: ways to ask a model why it made a decision, and the honest limits of those answers."""
CODE = 'computing5_interpretability'
BOOK = {
    "title": 'Interpretability Methods',
    "subtitle": 'Asking a model why, and how far the answer can be trusted',
    "chapters": [
        ('Why ask why',
         'A model that makes decisions about loans, health or safety should be able to explain itself. Interpretability methods try to show which inputs mattered and how. They help engineers debug and help people decide whether to trust a result.'),
        ('Attribution and saliency',
         'Attribution methods assign a score to each input feature, such as a pixel or a word, based on its effect on the output. Saliency maps are a common picture of those scores. Different methods can highlight different things for the same answer.'),
        ('Feature importance',
         'Feature importance ranks the input features across many decisions. Permuting a feature and measuring the loss in accuracy is one simple approach. It shows what the model relies on, not necessarily what is true in the world.'),
        ('Probing',
         'Probing trains a small test model to read some property from the inner activity of a larger network. If the probe succeeds, that information is present inside. Probing does not prove the network uses that information.'),
        ('Limits of explanations',
         'An explanation is a simplified story about a complex model. Two good explanations can disagree, and a plausible one can be wrong. Explanations can also be gamed, so they are not proof of fairness or safety.'),
        ('Explanations for people',
         'A useful explanation depends on the reader. Engineers need detail, while people affected by a decision need a clear reason and a route to appeal. Testing explanations with real users shows whether they are understood.'),
    ],
    "test": [
        ('What do attribution methods assign to each input?',
         [('a', 'A random colour'), ('b', 'A score for its effect on the output'), ('c', 'A date of birth'), ('d', 'A storage location')], 'b'),
        ('What does a saliency map show?',
         [('a', 'The total cost of the model'), ('b', 'The weather forecast'), ('c', 'The number of layers in the network'), ('d', 'A picture of which inputs the method scored as important')], 'd'),
        ('What does a successful probe show?',
         [('a', 'The information is present inside the network'), ('b', 'The network definitely uses that information'), ('c', 'The network was trained on paper'), ('d', 'The network is fair')], 'a'),
        ('Why are explanations not proof of safety or fairness?',
         [('a', 'They are always perfect copies of the model'), ('b', 'They cannot be written down'), ('c', 'They are simplified stories that can be wrong or gamed'), ('d', 'They only show the screen size')], 'c'),
        ('What do people affected by a decision usually need most?',
         [('a', 'The full model weights'), ('b', "The training server's address"), ('c', 'A list of every chip used'), ('d', 'A clear reason and a way to appeal')], 'd'),
    ],
}
