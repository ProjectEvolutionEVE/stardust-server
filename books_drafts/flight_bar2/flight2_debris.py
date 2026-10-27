"""Flying Among the Debris: field sizes, how the autopilot parks you, and working a field safely."""
CODE = "flight2_debris"
BOOK = {
    "title": "Flying Among the Debris",
    "subtitle": "Field sizes, where the autopilot parks you, and working a field safely",
    "chapters": [
        ("Four sizes of field",
         "Fields come in four sizes: large, medium, small and tiny. A bigger field holds more pieces, so it is worth more time. A tiny field has only a few pieces, and it is quiet to find."),
        ("Pieces have real sizes",
         "Every piece is a rock with a real size and shape, and bigger pieces fill more of your hold. A field usually mixes large and small rocks. Check the hold bar before you start, so you know how much room you have left."),
        ("Where the autopilot parks you",
         "When you double-tap a field, the autopilot parks you in front of it, outside its edge. From there the whole field stays in view while you work it. Working from outside lets you see the field before you commit to it."),
        ("Fog and distance",
         "Distant pieces fade into the dust and the fog, so a far-off field can look thinner than it is. Move in closer before you judge a field. Seeing it up close is the surest way to know what is there."),
        ("Going in slowly",
         "Flying into a field fast is the easiest way to lose control. Slow down before you enter, and keep your speed low enough that you can stop in the space you have. Use small, steady inputs, as you would on any tight approach."),
        ("Stay in the band",
         "Fields lie inside a ring's band. If you drift out of it, Inara warns you that you are out of the band and how far outside you are. Turn back toward the debris, and the warning clears."),
    ],
    "test": [
        ("Where does the autopilot park you when you double-tap a field?",
         [("a", "Inside the field, among the rocks"), ("b", "On top of the Starship"), ("c", "In front of the field, outside its edge, so the whole field is in view"), ("d", "At the Sun")], "c"),
        ("What happens to distant pieces in the view?",
         [("a", "They get louder"), ("b", "They turn gold"), ("c", "They vanish from the hold"), ("d", "They fade into the dust and the fog")], "d"),
        ("Why should you slow down before you enter a field?",
         [("a", "So the scanner can rest"), ("b", "Flying in fast is the easiest way to lose control"), ("c", "The hold fills faster at speed"), ("d", "Only slow craft are allowed in")], "b"),
        ("Which field size holds the most pieces?",
         [("a", "Tiny"), ("b", "Small"), ("c", "Large"), ("d", "All four hold the same")], "c"),
        ("What does Inara's warning mean when you drift out of a ring's band?",
         [("a", "The hold is full"), ("b", "Turn back toward the debris, you are outside the band"), ("c", "You must unload at once"), ("d", "The Sun is too close")], "b"),
    ],
}
