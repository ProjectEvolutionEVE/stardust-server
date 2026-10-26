"""Safety Factors: the spare strength a design carries, and why it is never zero."""
CODE = 'engineering3a_safety_factor'
BOOK = {
    "title": 'Safety Factors',
    "subtitle": 'How much spare strength a design carries, and why it is never zero',
    "chapters": [
        ('Spare strength on purpose',
         'A safety factor is the strength of a part divided by the load it will really carry. A factor of 2 means the part is twice as strong as its working load. The factor is a deliberate margin, and it is a mark of good design, not of poor design.'),
        ('Why a margin is needed',
         'No load is known exactly. Winds gust, machines are run harder than planned, and cargo sometimes shifts. Materials also vary a little from batch to batch, and a tiny flaw can weaken a part far more than its size suggests.'),
        ('Yield or ultimate',
         'For a part that must not change shape, engineers compare the working stress with the yield strength. For a part that must not break at all, they compare it with the ultimate strength. Choose the right one for the job, because the two can differ a lot.'),
        ('Choosing the number',
         'The right factor depends on what happens if the part fails and on how well its loads are known. A part whose failure could hurt someone gets a larger factor than one that is cheap to replace. Write down the reason for the number you choose.'),
        ('Too much margin costs',
         'Extra margin means extra material, extra weight and extra cost. A part far stronger than it needs to be wastes mass that a ship must carry. The aim is enough margin to be safe, and no more.'),
        ('Test what you can',
         'Where you can, test the finished part under its real load, or test a sample to failure. Real tests show things a calculation can miss. Record the factor you designed to, next to the result of each test.'),
    ],
    "test": [
        ('A part has a strength of 600 newtons and carries a working load of 300 newtons. What is its safety factor?',
         [('a', '0.5'), ('b', '300'), ('c', '2'), ('d', '900')], 'c'),
        ('Why do engineers build in a margin of spare strength?',
         [('a', 'Because loads, materials and flaws are never known exactly'), ('b', 'Because heavier parts are always better'), ('c', 'Because it makes parts cheaper'), ('d', 'Because it stops parts from being tested')], 'a'),
        ('Which two things should guide the choice of a safety factor?',
         [('a', 'The colour and the finish'), ('b', 'The name of the designer'), ('c', 'How many bolts the part has'), ('d', 'What happens on failure, and how well the loads are known')], 'd'),
        ('What is the main drawback of far too much margin?',
         [('a', 'The part is always too weak'), ('b', 'It adds extra weight and cost'), ('c', 'It makes the part melt'), ('d', 'It stops the part from being inspected')], 'b'),
        ('Why is it worth testing a finished part under load?',
         [('a', 'Because tests show things a calculation may miss'), ('b', 'Because tests replace the drawings'), ('c', 'Because tests make the part lighter'), ('d', 'Because tests are never needed again')], 'a'),
    ],
}
