"""Package Managers and Dependency Resolution: libraries, version ranges and lock files."""
CODE = "computing4_dependencies"
BOOK = {
    "title": "Package Managers and Dependency Resolution",
    "subtitle": "Libraries, version ranges and lock files",
    "chapters": [
        ("Libraries as dependencies", "Most programs use libraries written by others. A dependency is a library your project needs, and a package manager fetches it for you. Using well-tested parts saves time, but every part is also code you must trust."),
        ("Version ranges", "A project may say it accepts any version from 2.1 up to, but not including, 3.0. Ranges let fixes arrive without editing the code by hand. A range that is too loose can pull in a change that breaks the build."),
        ("Solving the graph", "Each library may need others, and together they form a web of requirements. The resolver searches for one version of each library that satisfies every rule at once. Sometimes no such set exists, and the resolver must report the conflict."),
        ("Lock files", "A lock file records the exact version chosen for each dependency. Anyone who installs from it gets the same versions, so the build behaves the same everywhere. Lock files are updated on purpose, not by accident."),
        ("Version conflicts", "Two libraries may need different versions of a third one. Teams fix this by upgrading, pinning or waiting for a library to update. Reading the conflict message carefully usually shows which rule is in the way."),
        ("Supply risks", "Many small packages mean many people you must trust. A single compromised package can reach many projects. Teams review new dependencies, keep their number small and watch for unexpected updates."),
    ],
    "test": [
        ("What is a lock file for?",
         [("a", "Locking the player out of the game"), ("b", "Storing the price of libraries"), ("c", "Recording the exact versions chosen so builds match"), ("d", "Making the screen dark")], "c"),
        ("What does a version range allow?",
         [("a", "A single version forever"), ("b", "A set of versions that fit a stated rule"), ("c", "Any colour of code"), ("d", "Versions with no numbers")], "b"),
        ("What is the job of a dependency resolver?",
         [("a", "To find one version of each library that meets every rule"), ("b", "To write new libraries"), ("c", "To print the project"), ("d", "To remove all dependencies")], "a"),
        ("What is a supply risk with many small packages?",
         [("a", "The packages become too bright"), ("b", "Small packages cannot be installed"), ("c", "Every package must be a game"), ("d", "A single compromised package can reach many projects")], "d"),
        ("What is a version conflict?",
         [("a", "Two libraries need incompatible versions of the same third library"), ("b", "A player argues with the Captain"), ("c", "Two screens show the same picture"), ("d", "A library has no name")], "a"),
    ],
}
