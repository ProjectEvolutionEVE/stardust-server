"""Type Systems in Practice: what a type promises, and where the checker helps."""
CODE = "computing4_type_systems"
BOOK = {
    "title": "Type Systems in Practice",
    "subtitle": "What a type promises, and where the checker helps",
    "chapters": [
        ("What a type promises", "A type is a label a program gives a value, such as a whole number, a piece of text or a true-or-false answer. The type makes a promise: a value of this kind will only be used in ways that suit it. Adding a number to a word breaks that promise, and a type system is the set of rules that catches the break."),
        ("Static and dynamic checking", "A static checker looks at the program before it runs and rejects mismatches it can prove. A dynamic checker waits and tests each value as the program runs, so the error appears only when that path is reached. Both catch real mistakes, but static checks find them earlier and across every path."),
        ("Generics and their limits", "Generics let one piece of code work on many types, such as a list of numbers or a list of names, while keeping each element's type known. They reduce copy-and-paste code. They cannot promise everything, and a very general type can become hard to read and hard to get right."),
        ("Type inference", "Many languages work out types from how a value is made, so the programmer does not have to write each one. Inference keeps code short while still checking it. When it guesses wrong, the error message is usually the best clue to what went wrong."),
        ("Errors caught before a run", "A good type checker catches misspelt names, wrong argument counts and mixed-up units before the program runs. These are cheap to find early and expensive to find in a live game. A checker cannot prove the logic is right, only that the parts fit together."),
        ("Choosing a discipline for a team", "Teams decide how strict their types should be. Strict checking slows the first draft but makes large changes safer. Lighter checking is quicker for small experiments. Most teams take a middle path and give clear type names to the things that matter most."),
    ],
    "test": [
        ("What does a type promise about a value?",
         [("a", "It will be printed in red"), ("b", "It will only be used in ways that suit its kind"), ("c", "It will never change its place in memory"), ("d", "It will run faster than other values")], "b"),
        ("What is the main difference between static and dynamic checking?",
         [("a", "Static checking needs a network connection"), ("b", "Dynamic checking never finds errors"), ("c", "Static checking looks before the program runs, dynamic checking while it runs"), ("d", "Static checking only works on pictures")], "c"),
        ("What do generics mainly help with?",
         [("a", "Making programs print faster"), ("b", "Letting one piece of code work on many types while keeping each type known"), ("c", "Removing the need for any testing"), ("d", "Storing values on a disk")], "b"),
        ("What does type inference do?",
         [("a", "Works out types from how values are made, so they need not all be written"), ("b", "Deletes all type errors"), ("c", "Writes the whole program for you"), ("d", "Sends types to a server")], "a"),
        ("Which error does a type checker usually catch before the program runs?",
         [("a", "A mood the player is in"), ("b", "A misspelt name or a wrong number of arguments"), ("c", "Lag on a slow phone"), ("d", "A player's favourite colour")], "b"),
    ],
}
