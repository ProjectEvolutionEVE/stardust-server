"""Variables and Types: names that hold values, and why the kind of value decides what you can do with it."""
CODE = "computing2_variables"
BOOK = {
    "title": "Variables and Types",
    "subtitle": "Names that hold values, and the kinds of values they hold",
    "chapters": [
        ("A named box",
         "A variable is a name that holds a value, like a labelled box. You put a value in the box, look at it later, and swap in a new value whenever you need to. The program uses the name to find the value again."),
        ("Kinds of values",
         "Every value has a type, which tells the computer what sort of thing it is. Whole numbers, decimal numbers, text and true-or-false values are the most common types. The type decides what you can do with a value: you can add two numbers, but you cannot add a number to a picture."),
        ("Numbers and text",
         "The number 3 and the text '3' look alike, but they behave differently. Adding the numbers 3 and 4 gives 7. Adding the text '3' to the text '4' joins them into '34'. Many bugs come from mixing these two up."),
        ("Decimals are close, not exact",
         "A decimal number such as 0.3 is stored in a form that can be very slightly off. So a program may show 0.30000000000000004 where you expected 0.3. This is normal. Programs round the result before they show it to people."),
        ("Assigning replaces",
         "Putting a new value into a variable replaces the old one; it does not add to it. If a variable holds 10 and you assign it 15, it now holds 15 and the 10 is gone. To add to a total, you write the new total back into the same variable, as in total = total + 5."),
        ("Name things well",
         "A good name says what the value means, such as hold_mass_kg rather than x. Names cannot contain spaces, so programmers join words with underscores or capitals. Clear names make a program easier to read, and easier to fix when something goes wrong."),
    ],
    "test": [
        ("What is a variable, in plain words?",
         [("a", "A fixed value that can never change"), ("b", "A type of screen"), ("c", "A name that holds a value the program can read and change"), ("d", "A place where only text can be stored")], "c"),
        ("What do you get from adding the text '3' to the text '4'?",
         [("a", "7"), ("b", "'34', the two pieces of text joined together"), ("c", "'12'"), ("d", "An error every time")], "b"),
        ("Why can a computer show 0.30000000000000004 where you expected 0.3?",
         [("a", "The computer is broken"), ("b", "The computer adds a random number"), ("c", "The number was typed in wrongly"), ("d", "Decimal numbers are stored in a form that can be very slightly off")], "d"),
        ("A variable holds 10, and you assign it 15. What does it hold now?",
         [("a", "15, and the old 10 is gone"), ("b", "25"), ("c", "10 and 15 together"), ("d", "Nothing")], "a"),
        ("Which name is the clearest for a variable that holds the mass of a load?",
         [("a", "x"), ("b", "q2"), ("c", "hold_mass_kg"), ("d", "thing")], "c"),
    ],
}
