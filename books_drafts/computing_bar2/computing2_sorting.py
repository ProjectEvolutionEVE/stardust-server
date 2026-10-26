"""Sorting Compared: selection, insertion and merge sort side by side, and why the method matters as lists grow."""
CODE = "computing2_sorting"
BOOK = {
    "title": "Sorting Compared",
    "subtitle": "Selection, insertion and merge sort, and why the method matters",
    "chapters": [
        ("Many ways to sort",
         "The earlier book introduced bubble sort. Other methods put a list in order in different ways, and some are much faster on big lists. Comparing them shows why the choice of method matters."),
        ("Selection sort",
         "Selection sort finds the smallest item in the list, moves it to the front, then repeats the same job on the rest. It is easy to follow. But it checks the rest of the list again and again, so it slows down quickly as lists grow."),
        ("Insertion sort",
         "Insertion sort works like sorting a hand of playing cards: take the next card and slide it into place among the cards already sorted. It is quick on a list that is nearly in order already, and slow on a list that is in reverse."),
        ("Merge sort",
         "Merge sort cuts a list in half, sorts each half, then merges the two sorted halves into one. Merging two sorted lists is quick, because you only ever compare the front items. This approach handles very large lists far better than the simple methods."),
        ("Speed on paper",
         "On a list of a million items, a method that needs about a trillion steps (a million squared) takes far longer than one that needs about 20 million. Real times depend on the computer, but the pattern is the same: the method matters more as the list grows."),
        ("Stable sorts",
         "A stable sort keeps items that are equal in the same order they were in before. If two orders have the same price, a stable sort keeps them in their original sequence. Insertion sort and merge sort are stable. Some fast methods are not."),
    ],
    "test": [
        ("Which method finds the smallest item, moves it to the front, then repeats on the rest?",
         [("a", "Insertion sort"), ("b", "Selection sort"), ("c", "Merge sort"), ("d", "Binary search")], "b"),
        ("What does merge sort do first?",
         [("a", "It compares each item with every other item"), ("b", "It deletes the largest item"), ("c", "It cuts the list into halves and sorts each half"), ("d", "It checks the middle name first")], "c"),
        ("Which method is quick on a list that is already nearly in order?",
         [("a", "Insertion sort"), ("b", "Selection sort"), ("c", "Random shuffling"), ("d", "Binary search")], "a"),
        ("What is a stable sort?",
         [("a", "One that uses no memory"), ("b", "One that never finishes"), ("c", "One that works only on numbers"), ("d", "One that keeps equal items in the order they were in before")], "d"),
        ("Roughly how many steps does a method that needs n times n steps take on a list of 1,000 items?",
         [("a", "About 1,000"), ("b", "About 1,000,000"), ("c", "About 100"), ("d", "About 10")], "b"),
    ],
}
