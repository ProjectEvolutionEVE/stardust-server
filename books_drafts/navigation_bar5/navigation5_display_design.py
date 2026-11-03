"""Display Design for Navigators: information layout, colour, clutter, alarms, testing with users and standards."""
CODE = "navigation5_display_design"
BOOK = {
    "title": "Display Design for Navigators",
    "subtitle": "Showing the right information at the right time",
    "chapters": [
        ("Information layout",
         "Information should sit where users look for it, in a logical order. Grouping related items helps the eye. A clear layout saves time under pressure."),
        ("Colour",
         "Colour can signal status, but it should never be the only cue. Some people have colour vision differences, so shapes and labels help. Keep the palette small."),
        ("Clutter",
         "Clutter means too much on a screen. It hides what matters and slows reading. Remove whatever is not needed."),
        ("Alarms",
         "Alarms should be used sparingly and should say clearly what is wrong. Too many alarms teach people to ignore them. Good design ranks alarms by urgency."),
        ("Testing",
         "Displays should be tested with real users in realistic conditions. Testing finds confusing parts before they cause errors. The results guide redesign."),
        ("Standards",
         "Standards set agreed rules for displays, so that users can move between systems with ease. They draw on research and experience. Following them lowers the risk of error."),
    ],
    "test": [
        ("What should information layout do?",
         [("a", "Hide things"), ("b", "Be random"), ("c", "Change every minute"), ("d", "Put information where users look for it, in a logical order")], "d"),
        ("Why should colour never be the only cue?",
         [("a", "Because colour is expensive"), ("b", "Because colour is dull"), ("c", "Because some people have colour vision differences"), ("d", "Because colour fades")], "c"),
        ("What is clutter?",
         [("a", "Too much on a screen"), ("b", "A type of cloud"), ("c", "A naval rank"), ("d", "A colour")], "a"),
        ("What happens when there are too many alarms?",
         [("a", "People use them more"), ("b", "People learn to ignore them"), ("c", "The ship sails faster"), ("d", "The screen grows")], "b"),
        ("What do standards give users?",
         [("a", "Random rules"), ("b", "Confusion"), ("c", "Agreed rules so they can move between systems easily"), ("d", "Higher prices")], "c"),
    ],
}
