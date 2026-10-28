"""Architecture Evaluation with ATAM: a structured review that tests a design against the qualities the system must have."""
CODE = 'computing5_atam'
BOOK = {
    "title": 'Architecture Evaluation with ATAM',
    "subtitle": 'Testing a design against the qualities it must deliver',
    "chapters": [
        ('What ATAM is',
         'The Architecture Tradeoff Analysis Method is a structured review, developed at the Software Engineering Institute at Carnegie Mellon University. It tests whether an architecture meets its key quality goals. It also shows where those goals pull against each other.'),
        ('Quality attribute scenarios',
         "A quality attribute scenario describes a stimulus, the system's environment, its response and a measure. For example, a user requests a report and it appears within two seconds on a normal day. Concrete scenarios make quality goals testable."),
        ('Utility trees',
         'A utility tree breaks the quality goals into specific scenarios, ranked by importance and by how hard they are to achieve. It helps the team focus the review on what matters most. The tree is built with stakeholders in the room.'),
        ('Sensitivity and trade-off points',
         'A sensitivity point is a design decision that strongly affects one quality. A trade-off point affects two or more qualities in opposite directions. Naming these points is the heart of the review.'),
        ('Risks and non-risks',
         'A risk is a decision that may fail to meet a goal, and a non-risk is one that is judged safe. Recording both shows the team what it has checked. Risks are followed up with owners and actions.'),
        ('Running a review and follow-up',
         'A review runs in phases with stakeholders, using scenarios, analysis and discussion. Its output is a set of documented decisions, risks and trade-offs. Follow-up work turns those findings into changes and checks.'),
    ],
    "test": [
        ('Where was the ATAM method developed?',
         [('a', 'A printing company in Paris'), ('b', 'The Software Engineering Institute at Carnegie Mellon University'), ('c', 'A film studio in London'), ('d', 'A bank in Tokyo')], 'b'),
        ('What does a quality attribute scenario include?',
         [('a', 'A list of printers'), ('b', 'A colour for each screen'), ('c', "A user's birthday"), ('d', 'A stimulus, the environment, a response and a measure')], 'd'),
        ('What is a utility tree?',
         [('a', 'A breakdown of quality goals into ranked, specific scenarios'), ('b', 'A map of the office car park'), ('c', 'A list of software licences'), ('d', 'A diagram of the coffee machine')], 'a'),
        ('What is a trade-off point?',
         [('a', 'A point where the power goes off'), ('b', 'A date set for a meeting'), ('c', 'A decision that affects two or more qualities in opposite directions'), ('d', 'A corner of the room')], 'c'),
        ('What is a risk in an ATAM review?',
         [('a', 'A type of coffee'), ('b', 'A prize for the best diagram'), ('c', 'An email signature'), ('d', 'A decision that may fail to meet a quality goal')], 'd'),
    ],
}
