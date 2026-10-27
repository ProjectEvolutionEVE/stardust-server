"""Invar and Low-Expansion Alloys: iron-nickel alloys that barely grow when warmed, used where precision must survive temperature change."""
CODE = "mining5_inv_alloys"
BOOK = {
    "title": "Invar and Low-Expansion Alloys",
    "subtitle": "Metals that hardly change size when they warm up",
    "chapters": [
        ("Most metals grow when warm", "Nearly all metals expand when heated and shrink when cooled. For a precision instrument, even a small change in length can throw off its readings. Engineers therefore look for metals that barely change size."),
        ("The discovery", "Charles Edouard Guillaume found that an alloy of about 36% nickel in iron shows almost no expansion near room temperature. He received the Nobel Prize in Physics in 1920 for his work on these alloys."),
        ("The magnetovolume effect", "In Invar, the atoms shrink slightly as the magnetism in the alloy weakens during heating. This shrinkage cancels out the normal expansion, so the total change in size is very small."),
        ("Other compositions", "Adjusted versions, such as super Invar, add a little cobalt and change the nickel share to tune the expansion. Each version is chosen for its temperature range."),
        ("Limits", "Invar keeps its small expansion only in a limited temperature band. Above that band the magnetism changes and the expansion rises. Designers keep parts in the range the alloy was made for."),
        ("Uses", "Low expansion alloys are used in watch and clock parts, measuring tapes, precision gauges and some shadow masks for displays. They are also used in tanks that hold very cold liquid gas."),
    ],
    "test": [
        ("What does Invar hardly do when warmed?",
         [("a", "Change its size"), ("b", "Change its colour"), ("c", "Shine"), ("d", "Make sound")], "a"),
        ("Roughly how much nickel is in the classic Invar alloy?",
         [("a", "About 3%"), ("b", "About 90%"), ("c", "About 36%"), ("d", "None at all")], "c"),
        ("Who discovered the low-expansion effect in Invar and received a Nobel Prize for it?",
         [("a", "Isaac Newton"), ("b", "Charles Edouard Guillaume"), ("c", "Marie Curie"), ("d", "Galileo Galilei")], "b"),
        ("What is the magnetovolume effect?",
         [("a", "Magnets becoming heavier"), ("b", "Sound made by metal"), ("c", "Metal turning into paper"), ("d", "Atoms shrink as magnetism weakens, cancelling normal expansion")], "d"),
        ("Where is Invar used?",
         [("a", "In paper cups"), ("b", "In watch parts and measuring tapes"), ("c", "In ceramic plates"), ("d", "In fruit juice bottles")], "b"),
    ],
}
