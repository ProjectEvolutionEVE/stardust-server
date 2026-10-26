"""User Interfaces: the screens people touch, the feedback they get, and the event loop that answers them."""
CODE = "computing2_interfaces"
BOOK = {
    "title": "User Interfaces",
    "subtitle": "The screens people touch, and how they respond",
    "chapters": [
        ("The part people touch",
         "A user interface is the part of a program that people see and use: buttons, menus, text fields and screens. The rules and data behind it work out of sight. A good interface makes the program's power easy to reach."),
        ("Input and feedback",
         "A user interface takes input from taps, clicks, keys and the mouse, and answers with output on the screen. A good interface always shows what happened after an action. A button that gives no sign it was pressed leaves people wondering whether it worked."),
        ("Waiting for events",
         "Most interfaces run in an event loop: the program waits for something to happen, such as a tap, then responds and waits again. Every tap is an event. The screen is redrawn as needed, so the display keeps up with what the user is doing."),
        ("Clear labels",
         "Users should be able to tell what each control does from its label and its place on the screen. Words such as Buy now or Sell now say exactly what will happen. Vague labels make people guess, and guesses lead to mistakes."),
        ("Consistency",
         "Things that work the same way should look the same and sit in the same places. Once a user learns that one screen has its main action at the bottom right, other screens should follow that pattern. Consistency lets people use new parts of a program without starting again."),
        ("Undoing and checking",
         "Good interfaces make mistakes easy to reverse, and they ask for a second look before anything big or costly happens. A confirm step before a sale is final is a simple example. Designing for mistakes is part of designing for people."),
    ],
    "test": [
        ("What is a user interface?",
         [("a", "The power cable of a computer"), ("b", "The rules and data kept out of sight"), ("c", "The part of a program people see and use, such as buttons, menus and screens"), ("d", "A file on storage")], "c"),
        ("Why does a good interface show feedback after an action?",
         [("a", "So the user knows the action happened"), ("b", "To make the screen brighter"), ("c", "To use less memory"), ("d", "To replace the labels")], "a"),
        ("What is an event loop?",
         [("a", "A cable that loops back to the power"), ("b", "A list of all the users"), ("c", "A kind of file format"), ("d", "A program waiting for something to happen, such as a tap, then responding and waiting again")], "d"),
        ("Why are clear labels such as 'Sell now' valuable?",
         [("a", "They make the screen bigger"), ("b", "They say exactly what will happen, so people need not guess"), ("c", "They replace the need for a power cable"), ("d", "They hide the control")], "b"),
        ("What does consistency in an interface mean?",
         [("a", "Things that work the same way look the same and sit in the same place"), ("b", "Every screen uses a different colour"), ("c", "Each control does a random job"), ("d", "Only one button is ever shown")], "a"),
    ],
}
