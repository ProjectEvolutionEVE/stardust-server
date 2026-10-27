"""Effect Systems: tracking side effects in types, so a function's reach is visible."""
CODE = 'computing5_effect_systems'
BOOK = {
    "title": 'Effect Systems',
    "subtitle": 'Side effects written into types, so a function reach is visible',
    "chapters": [
        ('What is a side effect', 'A side effect is anything a piece of code does besides giving back an answer: writing to a file, sending a message, reading the clock or raising an error. Most code does some of these. Effect systems make them visible in the type of a function.'),
        ('Effects in the type', 'An effect system adds a short list to a function type saying what it may do, such as "may write to the screen" or "may fail". A reader can see at a glance what the function touches, before reading its body.'),
        ('Handlers', 'A handler is the code that decides what an effect means. The same request to read a setting can be handled by reading a real file, by using a test value, or by a stored default. The function that asks does not change; only the handler does.'),
        ('Exceptions as effects', 'An exception is a kind of effect: the function may stop early and pass a problem upward. Treating exceptions this way lets a checker confirm that every possible problem is either handled or declared, instead of surprising a user at run time.'),
        ('Algebraic effects', 'Algebraic effects are a general form of this idea, with handlers that can pause a computation, resume it, or run it more than once. Some modern languages offer them directly, and others build similar patterns with libraries.'),
        ('Testability and trade-offs', 'Because effects are named, tests can swap a real file or network connection for a fake one without changing the main code. The trade-offs are extra writing in types and some learning. Teams usually weigh clearer code against that cost.'),
    ],
    "test": [
        ('What is a side effect?',
         [('a', 'Anything a function does besides returning a result'), ('b', 'The final answer of a function'), ('c', 'A kind of colour'), ('d', 'A bug that never happens')], 'a'),
        ('Where does an effect system show the effects?',
         [('a', 'In the screen brightness'), ('b', 'In the function type'), ('c', 'In the user hand'), ('d', 'Nowhere')], 'b'),
        ('What does a handler decide?',
         [('a', 'The price of the computer'), ('b', 'The name of the programmer'), ('c', 'Whether the sun is up'), ('d', 'What an effect actually does in a given setting')], 'd'),
        ('Why is testing easier with effects?',
         [('a', 'Tests become longer'), ('b', 'Effects stop all errors'), ('c', 'A fake version can be swapped in for a real file or network'), ('d', 'No tests are needed')], 'c'),
        ('How is an exception treated in an effect system?',
         [('a', 'As a colour'), ('b', 'As an effect'), ('c', 'As a planet'), ('d', 'As a file')], 'b'),
    ],
}
