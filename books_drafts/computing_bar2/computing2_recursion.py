"""Recursion: a function that calls itself on a smaller version of the same problem, and the base case that stops it."""
CODE = "computing2_recursion"
BOOK = {
    "title": "Recursion",
    "subtitle": "A function that calls itself on a smaller version of the same problem",
    "chapters": [
        ("A function that calls itself",
         "Recursion is when a function calls itself to solve a smaller version of the same problem. It sounds strange at first, but it is a clear way to describe jobs that have parts inside parts. Each call takes on a little less than the one before."),
        ("The base case",
         "Every recursive function needs a base case: a simple case it can answer directly, without calling itself again. Without a base case the function calls itself for ever. The base case is what makes the recursion end."),
        ("Counting down",
         "Imagine counting down from 3. Say the number, then count down from one less, until you reach zero and stop. Each call handles one number and leaves the rest to the next call, which is the same shape as a recursive function."),
        ("Factorial",
         "The factorial of a number is that number multiplied by every whole number below it. So 4 factorial is 4 times 3 times 2 times 1, which is 24. A recursive version says: the factorial of n is n times the factorial of n minus 1, and the factorial of 1 is 1."),
        ("Folders inside folders",
         "A folder can hold files and other folders, and those can hold more of both. To add up the size of everything in a folder, you add up its files and then do the same job for each folder inside it. That is a natural task for recursion."),
        ("When to use it",
         "Recursion is clear when a problem is made of smaller copies of itself. Each call uses a little memory to remember where it was, so very deep recursion can run out of room. For simple lists, a loop often does the same job and is easier to follow."),
    ],
    "test": [
        ("What is recursion?",
         [("a", "Repeating a step a fixed number of times with a counter"), ("b", "Storing a list inside a dictionary"), ("c", "A function that calls itself to work on a smaller version of the same problem"), ("d", "A kind of storage that fills up")], "c"),
        ("What is the base case in a recursive function?",
         [("a", "The simple case that is answered directly, with no further calls"), ("b", "The largest possible input"), ("c", "The first line of the program"), ("d", "The name of the function")], "a"),
        ("What is 4 factorial?",
         [("a", "10"), ("b", "8"), ("c", "16"), ("d", "24")], "d"),
        ("What happens to a recursive function that has no base case?",
         [("a", "It returns the answer at once"), ("b", "It calls itself again and again without ending"), ("c", "It deletes its own code"), ("d", "It switches to a dictionary")], "b"),
        ("Why is a folder full of folders a good example for recursion?",
         [("a", "Each folder is the same kind of thing as the whole, so the same steps can be applied to each part"), ("b", "Because folders cannot be counted"), ("c", "Because recursion only works on pictures"), ("d", "Because files are always the same size")], "a"),
    ],
}
