"""Model-Driven Engineering: using models and transformations to generate software, and the honest limits of that approach."""
CODE = 'computing5_model_driven'
BOOK = {
    "title": 'Model-Driven Engineering',
    "subtitle": 'Generating software from models, and its honest limits',
    "chapters": [
        ('What model-driven means',
         "Model-driven engineering treats models as the main design artefacts, from which code and documents are generated. The Object Management Group's Model Driven Architecture is one well-known approach. The goal is less repetitive work and more consistency."),
        ('Metamodels',
         'A metamodel defines the rules for what a model may contain, much as a grammar defines a language. Models are then written in terms of the metamodel. Clear metamodels make tools and checks possible.'),
        ('Transformations',
         'A transformation converts one model into another model or into code. Transformations are written as rules that can be run again and again. Their correctness must be tested like any other software.'),
        ('Code generation and the limits of UML',
         'Generated code can be consistent and quick to produce. Many teams found UML diagrams hard to keep current, and drawings alone rarely captured the full behaviour. Generation works best where the rules are simple and well understood.'),
        ('Tooling',
         'Modelling tools provide editors, checkers and generators. Their quality strongly affects how useful the approach is. Teams must also keep tools, models and generated code in step.'),
        ('Adoption barriers',
         'Adoption is held back by cost, the learning curve and the risk of lock-in to a tool. Engineers may also distrust code they did not write by hand. Starting with a small, well-defined area is the usual route to success.'),
    ],
    "test": [
        ('What is a metamodel?',
         [('a', 'A type of computer mouse'), ('b', 'A hat for a model railway'), ('c', 'A catalogue of paper sizes'), ('d', 'A set of rules defining what a model may contain')], 'd'),
        ('What does a transformation do?',
         [('a', 'It melts metal'), ('b', 'It converts one model into another model or into code'), ('c', 'It moves a server to a new room'), ('d', 'It changes the screen size')], 'b'),
        ('Which organisation created the Model Driven Architecture approach?',
         [('a', 'The Royal Navy'), ('b', 'A national football league'), ('c', 'The Object Management Group'), ('d', 'A chocolate company')], 'c'),
        ('Why did many teams find UML diagrams hard to use?',
         [('a', 'They were hard to keep current with the real system'), ('b', 'They were too small to read'), ('c', 'They could only be drawn in pencil'), ('d', 'They were banned by law')], 'a'),
        ('What is a common barrier to adopting model-driven engineering?',
         [('a', 'Too many tools that all work perfectly'), ('b', 'Cost, the learning curve and the risk of tool lock-in'), ('c', 'Models that never change'), ('d', 'Engineers who never write code')], 'b'),
    ],
}
