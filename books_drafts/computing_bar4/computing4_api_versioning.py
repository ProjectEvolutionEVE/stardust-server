"""API Versioning and Compatibility: breaking changes, additive evolution, version headers and paths, deprecation windows, consumer contracts, and migration help."""
CODE = "computing4_api_versioning"
BOOK = {
    "title": "API Versioning and Compatibility",
    "subtitle": "Changing an interface without breaking the programs that use it",
    "chapters": [
        ("Breaking changes",
         "A breaking change stops existing clients from working, such as removing a field or renaming one. A breaking change needs a new version."),
        ("Additive evolution",
         "Adding optional fields or new endpoints usually keeps old clients working. This is the safer way to grow an interface."),
        ("Version headers and paths",
         "A version can appear in the URL path or in a header. Either works. Teams pick one approach and keep it consistent."),
        ("Deprecation windows",
         "Announce deprecations early, and give consumers a clear time to move, with dates and notes on how to migrate."),
        ("Consumer contracts",
         "Consumer-driven contract tests check that the API still meets what its clients expect. They catch breaking changes before release."),
        ("Migration help",
         "Provide guides, examples and tools to help clients move to the new version. Track which versions clients still use."),
    ],
    "test": [
        ("What is a breaking change?",
         [("a", "A broken cup"), ("b", "A new colour"), ("c", "One that stops existing clients from working"), ("d", "A typo in a blog")], "c"),
        ("What does additive evolution mean?",
         [("a", "Adding optional fields or endpoints"), ("b", "Removing fields"), ("c", "Renaming everything"), ("d", "Erasing old versions")], "a"),
        ("Where can a version appear?",
         [("a", "On the moon"), ("b", "In a paper form"), ("c", "In a song"), ("d", "In the URL path or a header")], "d"),
        ("What is a deprecation window?",
         [("a", "A broken window"), ("b", "A clear time for consumers to move, with dates"), ("c", "A glass"), ("d", "A holiday")], "b"),
        ("What do consumer contract tests catch?",
         [("a", "Breaking changes before release"), ("b", "Nothing"), ("c", "Colours"), ("d", "Coffee")], "a"),
    ],
}
