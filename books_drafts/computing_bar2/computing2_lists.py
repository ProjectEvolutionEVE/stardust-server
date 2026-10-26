"""Lists and Dictionaries: ordered lists of values, and dictionaries that look a value up by its key."""
CODE = "computing2_lists"
BOOK = {
    "title": "Lists and Dictionaries",
    "subtitle": "Ordered lists, and dictionaries that find things by name",
    "chapters": [
        ("Lists keep their order",
         "A list holds many values in a fixed order, like a row of numbered boxes. A shopping list and a queue of people are both lists. The order is part of the list: the first item stays first until someone changes the list."),
        ("Counting from zero",
         "In most programming languages, positions in a list start at 0, not 1. The first item sits at position 0, the second at position 1, and so on. This feels strange at first, but it is used all through computing."),
        ("Adding and removing",
         "You can add an item to the end of a list, insert one in the middle, or remove one. When an item is removed from the middle, the items after it shift along to close the gap. The list keeps its order through every change."),
        ("Dictionaries: keys and values",
         "A dictionary holds pairs, each with a key and a value. The key is the label you look up by, and the value is what is stored under it. A dictionary of item names to prices lets you ask for one item's price by its name, not by its position."),
        ("Keys are unique",
         "Each key can appear only once in a dictionary. Storing a new value under a key that already exists replaces the old value. Keys are usually text or numbers that do not change."),
        ("Choosing the right one",
         "Use a list when order matters or when you go through every item in turn. Use a dictionary when you want to find one item by its name. Many real records, such as a price list, are dictionaries of this kind."),
    ],
    "test": [
        ("In a list, what does an item's position tell you?",
         [("a", "How heavy the item is"), ("b", "How many copies exist"), ("c", "Whether the item is true"), ("d", "Where the item sits in the order")], "d"),
        ("In most programming languages, what position number does the first item of a list have?",
         [("a", "1"), ("b", "0"), ("c", "2"), ("d", "It has no position")], "b"),
        ("A list has five items, and you remove the item in the middle. What happens to the items after it?",
         [("a", "They are deleted too"), ("b", "They become a new list"), ("c", "They shift along to close the gap"), ("d", "They are copied into storage")], "c"),
        ("What is a dictionary made of?",
         [("a", "Pairs of a key and a value"), ("b", "Rows and columns only"), ("c", "Numbers only"), ("d", "Pictures")], "a"),
        ("What happens when you store a new value under a key that already exists in a dictionary?",
         [("a", "Both values are kept under that key"), ("b", "The program stops with an error"), ("c", "The key is renamed"), ("d", "The new value replaces the old one")], "d"),
    ],
}
