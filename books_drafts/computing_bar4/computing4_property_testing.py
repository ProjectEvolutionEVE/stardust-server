"""Property-Based Testing: stating rules that must always hold, and letting a tool search for counterexamples."""
CODE = 'computing4_property_testing'
BOOK = {
    "title": 'Property-Based Testing',
    "subtitle": 'Stating rules that must always hold, and letting a tool search for the cases that break them',
    "chapters": [
        ('From examples to properties',
         'A normal test checks one example, such as sorting the list three, one, two. A property states a rule that must hold for every input, such as the output of a sort having the same items as the input. Properties cover many more cases than one hand-picked example.'),
        ('Random input generators',
         'A property-based tool creates many random inputs and checks the rule for each one. The generator must produce inputs that are realistic and varied. A poor generator misses the strange cases where real bugs hide.'),
        ('Shrinking failures',
         'When the tool finds a failing input, it tries to shrink it into the smallest example that still fails. A short failing case is far easier to understand than a long random one. Shrinking turns a confusing crash into a clear clue.'),
        ('Stateful models',
         'Some systems change over time, such as a queue or a bank account. A stateful test runs a random sequence of actions and compares the real system with a simple model of what should happen. Differences show where the design has gone wrong.'),
        ('Finding edge cases',
         'Properties are good at finding edge cases, such as empty inputs, very large numbers or repeated actions. Many bugs live at these edges. Writing a property forces the author to think clearly about what the code promises.'),
        ('Properties for real code',
         'Start with simple properties, such as round trips, where encoding and decoding must return the original. Then add rules about ordering, limits and idempotence. Keep the tests fast enough to run often, and keep the rules readable.'),
    ],
    "test": [
        ('What is a property in this kind of testing?',
         [('a', 'A piece of furniture in the office'), ('b', 'A single hand-picked example'), ('c', 'A bug report'), ('d', 'A rule that must hold for every input')], 'd'),
        ('What does shrinking do?',
         [('a', 'Makes the screen smaller'), ('b', 'Reduces a failing input to the smallest example that still fails'), ('c', 'Deletes the tests'), ('d', 'Removes all errors')], 'b'),
        ('What is a round trip property?',
         [('a', 'A test that runs around the office'), ('b', 'A flight plan for a craft'), ('c', 'Encoding then decoding must return the original value'), ('d', 'A test that never ends')], 'c'),
        ('What is a stateful model used for?',
         [('a', 'Comparing a changing real system with a simple model of what should happen'), ('b', 'Painting the code'), ('c', 'Choosing a licence'), ('d', 'Sending email')], 'a'),
        ('Where do many real bugs hide, according to this book?',
         [('a', 'In the middle of ordinary inputs only'), ('b', 'At the edges, such as empty or very large inputs'), ('c', 'In the company logo'), ('d', 'Nowhere at all')], 'b'),
    ],
}
