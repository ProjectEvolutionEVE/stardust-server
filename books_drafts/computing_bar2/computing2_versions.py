"""Version Control: a history of every change, with snapshots, diffs, branches and merges."""
CODE = "computing2_versions"
BOOK = {
    "title": "Version Control",
    "subtitle": "Snapshots, history, branches and merging",
    "chapters": [
        ("A history of every change",
         "Version control keeps a record of every change made to a set of files, so you can see what changed, when, and why. Without it, people end up with files named final, final2 and really-final. A version control system keeps one history instead."),
        ("Commits are snapshots",
         "A commit is a saved snapshot of the files at one moment, with a short message describing the change. Good messages say what changed and why, so someone reading the history later understands it. Each commit can be looked at, compared or undone."),
        ("Comparing changes",
         "A diff shows exactly which lines were added, removed or changed between two versions. Reading the diff before saving a change catches mistakes that are easy to miss by eye. Many reviews of code are simply a close look at the diff."),
        ("Branches",
         "A branch is a separate line of work, so you can try an idea without disturbing the main version. If the idea works, it can be joined back in; if it does not, the branch can be left behind. Most teams keep one main line that is always in a working state."),
        ("Merging",
         "Merging combines the changes from one branch into another. When two people changed the same line in different ways, the system stops and asks someone to decide which version to keep. Such a clash is called a conflict."),
        ("Undo, safely",
         "Version control makes undoing a mistake safer, because the old version is still in the history. Good practice is to make small commits often, so each one is easy to understand and to reverse. The game's own code is kept in a Git repository, which keeps this history."),
    ],
    "test": [
        ("What is version control?",
         [("a", "A way to print many copies"), ("b", "A record of every change to a set of files, so changes can be seen and undone"), ("c", "A kind of screen"), ("d", "A password system")], "b"),
        ("What is a commit?",
         [("a", "A kind of virus"), ("b", "A printed page"), ("c", "A list of every player"), ("d", "A saved snapshot of the files at one moment, with a message about the change")], "d"),
        ("What does a diff show?",
         [("a", "The lines added, removed or changed between two versions"), ("b", "The number of players online"), ("c", "The colour of the screen"), ("d", "The size of the disk")], "a"),
        ("Why use a branch?",
         [("a", "To delete the history"), ("b", "To print the files"), ("c", "To try an idea without disturbing the main version"), ("d", "To stop anyone else reading the code")], "c"),
        ("What is a merge conflict?",
         [("a", "A power failure during saving"), ("b", "A file that cannot be opened"), ("c", "A branch that has no commits"), ("d", "A clash where two changes touch the same part and someone must decide which to keep")], "d"),
    ],
}
