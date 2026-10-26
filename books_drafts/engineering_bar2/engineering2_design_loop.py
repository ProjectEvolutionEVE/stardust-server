"""The Design Loop: requirements, prototype, test and improve, the cycle by which a design gets better."""
CODE = 'engineering2_design_loop'
BOOK = {
    "title": 'The Design Loop',
    "subtitle": 'Requirements, prototype, test and improve: how a design gets better',
    "chapters": [
        ('Write the requirements first',
         "A requirement is something the finished design must do, or stay within: its load, size, weight, power, cost, and the conditions "
         "it must survive. Write each one as a number or a test, not as a hope. A design that meets its requirements is done; one that "
         "is only pleasant to look at is not."),
        ('Sketch several ideas',
         "Make several rough ideas, not one. Compare each against the requirements, and cross out any that fail. Keep the best two or "
         "three for the next step, because the first idea is seldom the best one."),
        ('Build a prototype',
         "A prototype is a cheap, quick model that tests an idea. It might be cardboard, a rough model, a printed part or a small section. "
         "Build only enough to answer the question you have, and mark clearly which parts are real and which are stand-ins."),
        ('Test against each requirement',
         "Test the prototype the way it will really be used, and measure it against each requirement. Write down the numbers. A test that "
         "does not match real conditions tells you little. Test one spare part to failure, to find where its limit lies."),
        ('Find the failure, then improve',
         "When a part fails, find out how and why before you change it. Change one thing, test again, and compare the results. Each turn "
         "of the loop should make the design better, and it should show why."),
        ('Stop at good enough',
         "A design is finished when it meets every requirement, not when it is perfect. Record the requirements, the tests and the changes, "
         "so that a builder or a reviewer can see why the design is what it is."),
    ],
    "test": [
        ("What is a requirement?",
         [('a', 'A drawing of the part'), ('b', 'Something the design must do or stay within, written as a number or a test'), ('c', 'A paint colour'), ('d', 'A serial number')], 'b'),
        ("What is the purpose of a prototype?",
         [('a', 'To sell the first copy'), ('b', 'To be the final build'), ('c', 'To replace the requirements'), ('d', 'To test an idea cheaply before the full build')], 'd'),
        ("Why sketch several rough ideas instead of one?",
         [('a', 'Ideas are cheap, so there is no need to compare them'), ('b', 'One idea always fails'), ('c', 'The first idea is rarely the best, so compare the rough ideas against the requirements'), ('d', 'Only ten ideas are allowed')], 'c'),
        ("When a part fails a test, what should you do first?",
         [('a', 'Find out how and why it failed, before you change it'), ('b', 'Replace it with a bigger one'), ('c', 'Hide the result'), ('d', 'Test it again at once without changing anything')], 'a'),
        ("When is a design finished?",
         [('a', 'When it looks good'), ('b', 'When it is the most expensive option'), ('c', 'When it meets every requirement'), ('d', 'When the first prototype is built')], 'c'),
    ],
}
