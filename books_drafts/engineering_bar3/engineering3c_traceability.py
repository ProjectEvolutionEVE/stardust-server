"""Requirements Traceability: linking each requirement to the design that meets it and the test that proves it."""
CODE = 'engineering3c_traceability'
BOOK = {
    "title": 'Requirements Traceability: Every Need Has a Test',
    "subtitle": 'Linking each requirement to the design that meets it and the test that proves it',
    "chapters": [
        ('Requirements as a list',
         "A requirement says what the build must do, with a number wherever possible. Lift 50 kilograms is a requirement; strong enough is not. Give each requirement its own number, so that it can be followed through the whole project."),
        ('Linking to the design',
         "Each requirement is linked to the part of the design that meets it. A requirement with no design behind it is a gap. A design part with no requirement behind it may be extra weight or extra cost."),
        ('Linking to a test',
         "Each requirement also needs a test that proves it is met. The test states the setup, the pass mark and the result. A requirement with no test is only a hope."),
        ('The traceability matrix',
         "A traceability matrix is a table. Requirements run down one side, and designs and tests run across the top. Each row shows where a requirement lives and how it was proved. Gaps stand out at once when the table is filled in."),
        ('Changes ripple',
         "When a requirement changes, follow its links to find every design part and test it touches. A change to a lift figure may affect the motor, the frame and the brake tests. Good links stop those changes being missed."),
        ('Keeping it honest',
         "Update the matrix as the build changes, and review it before each stage. Keep it short enough to read, and treat it as a living record. An out-of-date matrix is worse than none, because it still looks true."),
    ],
    "test": [
        ('What makes a good requirement?',
         [('a', 'It is vague, like strong enough'), ('b', 'It states what the build must do, with a number where possible'), ('c', 'It gives the colour of the design'), ('d', 'It is written after the build')], 'b'),
        ('What does a requirement with no design behind it show?',
         [('a', 'A finished part'), ('b', 'A cheap build'), ('c', 'A spare part'), ('d', 'A gap in the design')], 'd'),
        ('Besides the design, what must each requirement be linked to?',
         [('a', 'A paint sample'), ('b', 'A price list'), ('c', 'A test that proves it is met'), ('d', 'A holiday schedule')], 'c'),
        ('What is a traceability matrix?',
         [('a', 'A table showing where each requirement lives and how it was proved'), ('b', 'A type of motor'), ('c', 'A map of the hold'), ('d', 'A list of crew names')], 'a'),
        ('Why must you follow the links when a requirement changes?',
         [('a', 'To find the price'), ('b', 'To find every design part and test that the change touches'), ('c', 'To repaint the drawings'), ('d', 'To delete the requirement')], 'b'),
    ],
}
