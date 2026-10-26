"""Files and Folders: named bundles of data, the folders that hold them, the paths that find them, and the copies that keep them safe."""
CODE = "computing2_files"
BOOK = {
    "title": "Files and Folders",
    "subtitle": "Named bundles of data, the folders that hold them, and the paths that find them",
    "chapters": [
        ("A file is a bundle",
         "A file is a named bundle of data kept on storage, such as a text document, a picture or a saved game. Every file has a name and a size, and it stays on the disk until someone deletes it. Files are the usual way programs keep information between uses."),
        ("Folders hold files",
         "A folder, sometimes called a directory, is a container for files and for other folders. Folders nest, one inside another, to keep things in order. Most computers arrange them as a tree that starts from one top folder."),
        ("Paths",
         "A path is the full address of a file, listing each folder on the way, such as documents/notes/week1.txt. A short name is not enough when two files share a name in different folders. The path tells the computer exactly which file is meant."),
        ("File formats",
         "The format of a file is the set of rules for arranging its bytes. A plain text file, a picture and a spreadsheet are each stored in their own format. Opening a file in the wrong program often shows garbled text, because the program reads the bytes by the wrong rules."),
        ("Flash and spinning disks",
         "Many storage devices use flash memory, which keeps data with no power by trapping tiny electric charges. Older hard drives keep data on spinning magnetic disks, read by a head that moves across them. Both keep data when the power goes off, but flash has no moving parts."),
        ("Copies and backups",
         "Copying a file makes a second, separate file, so a change to one does not change the other. A backup is a copy kept somewhere safe, so a broken drive does not mean lost work. A good habit is at least two copies in two places."),
    ],
    "test": [
        ("What is a path in a file system?",
         [("a", "A kind of picture format"), ("b", "The number of bytes in a file"), ("c", "The speed of a disk"), ("d", "The full address of a file, listing each folder on the way")], "d"),
        ("Why is a path needed when two files share the same name?",
         [("a", "Because the computer cannot read names"), ("b", "Because it tells the computer exactly which file, in which folder, is meant"), ("c", "Because names are always deleted"), ("d", "Because files with the same name merge")], "b"),
        ("What is a file format?",
         [("a", "A way of printing a page"), ("b", "A folder that holds files"), ("c", "The set of rules for arranging a file's bytes"), ("d", "The number of files on a disk")], "c"),
        ("What can happen if you open a file in a program that expects a different format?",
         [("a", "The text may look garbled, because the bytes are read by the wrong rules"), ("b", "The computer prints it at once"), ("c", "The file turns into a folder"), ("d", "The file gains more bytes")], "a"),
        ("Why is a backup useful?",
         [("a", "It makes the file smaller"), ("b", "It keeps a separate copy, so a broken drive does not mean lost work"), ("c", "It stops anyone reading the file"), ("d", "It speeds up the computer")], "b"),
    ],
}
