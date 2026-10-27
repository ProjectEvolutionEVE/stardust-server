"""Causal inference: correlation versus cause, causal graphs, the do-operator, instrumental variables, natural experiments and pitfalls."""
CODE = 'computing5_causal_inference'
BOOK = {
    "title": 'Causal Inference',
    "subtitle": 'Telling cause from correlation, and designing studies that can',
    "chapters": [
        ('Correlation is not cause',
         'Two things can move together because one causes the other, because both share a common cause, or by chance. Correlation alone cannot tell these apart.'),
        ('Causal graphs',
         'A directed graph draws arrows from causes to effects. The graph shows which variables must be considered to answer a causal question.'),
        ('The do-operator',
         "Judea Pearl's do-operator asks what happens if we set a variable ourselves. Do-calculus gives rules for working this out from observational data where possible."),
        ('Instrumental variables',
         'An instrument affects the outcome only through the thing we study. It can help estimate a cause when a direct comparison is biased.'),
        ('Natural experiments',
         'Sometimes nature or policy splits people into groups almost at random. Comparing those groups can reveal a cause without a lab trial.'),
        ('Common pitfalls',
         'Controlling for the wrong variable can create bias, such as conditioning on a collider. Selection bias and hidden confounders also mislead many studies.'),
    ],
    "test": [
        ('Why can two things be correlated without one causing the other?',
         [('a', 'Correlation always means cause'), ('b', 'They are both on paper'), ('c', 'They may share a common cause'), ('d', 'They have the same colour')], 'c'),
        ('What do arrows in a causal graph show?',
         [('a', 'Which variable affects which'), ('b', 'Where the printer is'), ('c', 'The date of a meeting'), ('d', 'The price of paper')], 'a'),
        ('What does the do-operator ask?',
         [('a', 'What colour is the data'), ('b', 'Who is the author'), ('c', 'How long a file is'), ('d', 'What happens if we set a variable ourselves')], 'd'),
        ('What does an instrumental variable need to do?',
         [('a', 'Be printed in red'), ('b', 'Affect the outcome only through the studied cause'), ('c', 'Be the outcome itself'), ('d', 'Be random text')], 'b'),
        ('What is a collider?',
         [('a', 'A car crash'), ('b', 'A type of cable'), ('c', 'A variable that two causes both lead into'), ('d', 'A brand of paper')], 'c'),
    ],
}
