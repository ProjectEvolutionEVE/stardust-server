"""Model Checking with TLA+: describing a system's design precisely and exploring every state it can reach."""
CODE = 'computing4_model_checking'
BOOK = {
    "title": 'Model Checking with TLA+',
    "subtitle": 'Describing a design precisely, then exploring the states it can reach',
    "chapters": [
        ('Specifying systems',
         'A specification describes what a system is allowed to do, written in precise mathematics rather than in code. TLA+ is a language created by Leslie Lamport for this purpose. Writing the spec forces a team to decide exactly what the design means.'),
        ('State exploration',
         'A model checker starts from the initial state of the spec and explores every state the system can reach. For small models, it checks all of them, which can reveal problems that testing would almost never find. Larger models need limits on size.'),
        ('Invariants and liveness',
         'An invariant is a rule that must be true in every reachable state, such as no two servers holding the same lock. Liveness is a promise that something good eventually happens, such as a request always getting an answer. Both are checked by the tool.'),
        ('Counterexamples',
         'When a rule is broken, the checker produces a counterexample: a step-by-step path from the start to the failure. These traces are often long but very clear. Reading them carefully is the main skill of model checking.'),
        ('Modelling concurrency',
         'Concurrent systems are hard because many things can happen in any order. A model lets the checker try every interleaving of steps. This reveals race conditions that rarely appear in ordinary testing.'),
        ('Practical adoption',
         'Teams usually begin with one hard design, such as a replication protocol, and model only its key parts. Engineers often find value before the spec is complete. The spec is best kept with the design and updated as the design changes.'),
    ],
    "test": [
        ('What is a specification in this book?',
         [('a', 'A list of office supplies'), ('b', 'A photograph of the server room'), ('c', 'A precise description of what a system is allowed to do'), ('d', 'A user manual for a printer')], 'c'),
        ('What does a model checker do?',
         [('a', 'Explores every state the system can reach, for small models'), ('b', 'Writes the final product for you'), ('c', 'Sends emails to customers'), ('d', 'Only changes colours')], 'a'),
        ('What is an invariant?',
         [('a', 'A type of plant'), ('b', 'A bug that never appears'), ('c', 'A fixed price'), ('d', 'A rule that must be true in every reachable state')], 'd'),
        ('What is a counterexample?',
         [('a', 'A test that always passes'), ('b', 'A path of steps from the start to a broken rule'), ('c', 'A copy of the spec'), ('d', 'A prize for finding bugs')], 'b'),
        ('Why is modelling concurrency valuable?',
         [('a', 'It removes all threads from the system'), ('b', 'It makes the system slower on purpose'), ('c', 'It tries every order of steps, revealing race conditions'), ('d', 'It stops all requests')], 'c'),
    ],
}
