"""Functional Programming and Immutability: pure functions and data that does not change."""
CODE = "computing4_functional_style"
BOOK = {
    "title": "Functional Programming and Immutability",
    "subtitle": "Pure functions and data that does not change",
    "chapters": [
        ("Pure functions", "A pure function gives the same result for the same inputs and changes nothing else. It does not read a clock, write to the screen or change a shared variable. Because of this, you can call it again and again and trust the answer."),
        ("Immutable data", "Immutable data cannot be changed once it is made. To change something, you make a new copy with the change included. This removes a whole class of bugs, where one part of a program alters data that another part is still using."),
        ("Map, filter and fold", "Map applies one step to every item in a list. Filter keeps only the items that pass a test. Fold combines a whole list into a single result, such as a total. Together these three replace many hand-written loops."),
        ("Pushing side effects to the edges", "Real programs must read input and write output, and these are side effects. A common plan keeps most of the code pure and places the reading and writing at the outer edges. The pure middle is then easy to test on its own."),
        ("Function values and closures", "A function can be passed around like a number, stored in a variable or handed to another function. A closure is a function that remembers the values around it when it was made. These tools let short pieces of logic be reused in many places."),
        ("Why pure code is easy to test", "A pure function needs no setup beyond its inputs. You give it values and check the answer, with no mocks and no shared state. Tests become short, and a failure points straight at the function that caused it."),
    ],
    "test": [
        ("What makes a function pure?",
         [("a", "It always writes to a file"), ("b", "The same inputs always give the same result and nothing else changes"), ("c", "It runs on a server"), ("d", "It is written in a short language")], "b"),
        ("What happens when immutable data needs to change?",
         [("a", "It is edited in place"), ("b", "It is deleted"), ("c", "It is sent to the player"), ("d", "A new copy is made with the change")], "d"),
        ("What does fold do?",
         [("a", "Combines a whole list into a single result"), ("b", "Keeps items that pass a test"), ("c", "Applies a step to each item"), ("d", "Sorts a list by colour")], "a"),
        ("Where do side effects usually sit in a well-planned program?",
         [("a", "At the outer edges"), ("b", "Spread through every function"), ("c", "Inside the pure middle"), ("d", "Nowhere at all")], "a"),
        ("Why is pure code easy to test?",
         [("a", "It needs only its inputs, with no shared state to set up"), ("b", "It runs faster than all other code"), ("c", "It never has any bugs"), ("d", "It uses no memory")], "a"),
    ],
}
