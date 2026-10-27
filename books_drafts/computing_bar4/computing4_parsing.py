"""Parsing and Grammars: turning text into a tree the program can understand."""
CODE = "computing4_parsing"
BOOK = {
    "title": "Parsing and Grammars",
    "subtitle": "Turning text into a tree the program can understand",
    "chapters": [
        ("Tokens", "Before a program can understand text, it splits the text into tokens: the smallest meaningful pieces, such as a number, a name, an operator or a bracket. This step is called lexing or tokenising. Spaces and comments are usually skipped."),
        ("Grammar rules", "A grammar is a set of rules that say which token sequences are valid. For example, a sum may be a number, then a plus sign, then another number. Grammars describe the shape a valid program must take."),
        ("Syntax trees", "A parser builds a tree that shows how the pieces fit together, with the operations near the top. The tree lets later steps check meaning and run the program. Two different trees for the same text can mean two different things."),
        ("Recursive descent", "A common hand-written method has one function for each grammar rule, and each function calls the others for smaller parts. It reads tokens from left to right and is easy to follow. It works well for many everyday languages."),
        ("Reporting syntax errors well", "A good parser points to the exact place where it got confused and says what it expected. It can keep going after the error to report more problems at once. Clear messages save far more time than clever ones."),
        ("Parsers in everyday tools", "Parsers are inside spreadsheets, web browsers, code editors and many settings files. Every time a formula or a web page is read, a parser runs. Learning them shows how such tools understand the text you type."),
    ],
    "test": [
        ("What is a token?",
         [("a", "The smallest meaningful piece of text, such as a number or an operator"), ("b", "A coin used in the game"), ("c", "A kind of lock"), ("d", "The final answer of a program")], "a"),
        ("What does a grammar describe?",
         [("a", "The colour of the screen"), ("b", "The speed of the processor"), ("c", "Which token sequences are valid"), ("d", "The price of a ship")], "c"),
        ("What does a syntax tree show?",
         [("a", "How the pieces of the text fit together"), ("b", "How many words a page has"), ("c", "The fastest route on a map"), ("d", "Which player is online")], "a"),
        ("What is recursive descent?",
         [("a", "A way to delete tokens"), ("b", "A method with one function per grammar rule"), ("c", "A kind of save file"), ("d", "A map of the galaxy")], "b"),
        ("What makes a good syntax error message?",
         [("a", "It says where the parser got confused and what it expected"), ("b", "It is written in a secret code"), ("c", "It only says the word error"), ("d", "It hides the line number")], "a"),
    ],
}
