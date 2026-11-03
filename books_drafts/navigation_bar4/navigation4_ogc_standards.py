"""Open Geospatial Standards: interoperability, web map and feature services, file formats, metadata, adoption and governance."""
CODE = "navigation4_ogc_standards"
BOOK = {
    "title": "Open Geospatial Standards",
    "subtitle": "Shared rules that let different map systems work together",
    "chapters": [
        ("Interoperability", "Interoperability means different systems can share map data without breaking. Open standards make this possible. A standard sets out how data is named, described and sent."),
        ("Web map and feature services", "A web map service sends a picture of a map. A web feature service sends the features themselves, such as roads or buildings, that a program can use. Each service follows a published standard."),
        ("File formats", "Standards also cover file formats. A format that many programs can read is much easier to share. Open formats help keep data usable for years."),
        ("Metadata", "Metadata is the description of a dataset: who made it, when, how and with what accuracy. Standard metadata lets others judge whether the data fits their need."),
        ("Adoption", "A standard is useful only when people use it. Adoption grows when software supports the standard and when users ask for it. A good standard is kept simple enough to be widely built."),
        ("Governance", "Standards are kept up by a governing body. Changes go through a public process, with members and users able to comment. This keeps a standard fair and stable."),
    ],
    "test": [
        ("What does interoperability mean?", [("a", "Different systems can share map data"), ("b", "Only one system can open a map"), ("c", "Maps must be printed"), ("d", "Maps have no names")], "a"),
        ("What does a web feature service send?", [("a", "Only a picture of a map"), ("b", "The features themselves, such as roads or buildings"), ("c", "Weather reports only"), ("d", "Music files")], "b"),
        ("What is metadata?", [("a", "A song about maps"), ("b", "A paper map cover"), ("c", "A description of a dataset, such as who made it and how accurate it is"), ("d", "A type of ship")], "c"),
        ("Why does an open file format help?", [("a", "It can only be read by one program"), ("b", "It hides the data"), ("c", "Many programs can read it"), ("d", "It stops all sharing")], "c"),
        ("What keeps a standard fair and stable?", [("a", "Changes made behind closed doors by one person"), ("b", "Ignoring user needs"), ("c", "Never updating anything"), ("d", "A public process with members and users able to comment")], "d"),
    ],
}
