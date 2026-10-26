"""Functions: a named set of steps that takes inputs and gives back a result, so a job is written once and used many times."""
CODE = "computing2_functions"
BOOK = {
    "title": "Functions",
    "subtitle": "Named steps that take inputs, give back results and can be reused",
    "chapters": [
        ("A named recipe",
         "A function is a set of steps given a name, so you can use them again without writing them out each time. You write it once and call it by name whenever you need the job done. Calling a function runs its steps from the top."),
        ("Inputs and results",
         "A function can take inputs, which are called arguments or parameters, and it can give back a result, called a return value. A function that adds sales tax to a price takes the price and returns the total with tax. The same function works for any price you give it."),
        ("Write once, fix once",
         "A function keeps a program short and easy to check. If one step is repeated in five places, a mistake in it must be fixed in five places. Put the step in a function, and the fix is made once and reaches every use."),
        ("Keeping things local",
         "A variable made inside a function is usually local, which means it exists only while the function runs. This stops one part of a program from changing another part by accident. Good functions do one job and do it well."),
        ("Easy to test",
         "You can test a function by giving it inputs where you already know the right output. This is the unit testing from the earlier book on debugging. A function that gives the same output for the same input, and changes nothing else, is especially easy to trust."),
        ("Functions calling functions",
         "Functions can call other functions, so a big job is built from small named pieces. One function might read an order, another check its price, and a third write out the total. Each piece can be tested on its own."),
    ],
    "test": [
        ("What is a function?",
         [("a", "A kind of memory card"), ("b", "A named set of steps that runs whenever its name is called"), ("c", "A place where data is kept for ever"), ("d", "A screen that shows results")], "b"),
        ("What is a return value?",
         [("a", "The power a program uses"), ("b", "The name of the function"), ("c", "A copy of the whole program"), ("d", "The result a function hands back to the part that called it")], "d"),
        ("Why does fixing a bug inside a shared function help every place that uses it?",
         [("a", "Because one function is used everywhere, so one fix changes every use"), ("b", "Because a fix copies itself into the other places"), ("c", "Because bugs only ever happen on the screen"), ("d", "Because functions cannot contain bugs")], "a"),
        ("What does it mean that a local variable exists only while its function runs?",
         [("a", "It is saved to storage for ever"), ("b", "It is shared with every other function"), ("c", "It belongs to that function's work, so other parts of the program cannot change it by accident"), ("d", "It is printed on the screen")], "c"),
        ("A well-written function is given the same input twice and changes nothing else. What should happen?",
         [("a", "It gives a different answer each time"), ("b", "It gives the same output both times"), ("c", "It stops working the second time"), ("d", "It asks the user for new inputs")], "b"),
    ],
}
