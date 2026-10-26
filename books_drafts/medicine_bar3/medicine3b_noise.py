"""Medicine, bar 3 (Senior Doctor), part B: Noise and Hearing at Work. How loud noise damages hearing, why the decibel scale matters, and how workplaces protect people."""
CODE = "medicine3b_noise"
BOOK = {
    "title": "Noise and Hearing at Work",
    "subtitle": "How loud noise damages hearing, why the decibel scale matters, and how workplaces protect people",
    "chapters": [
        ("How we hear",
         "Sound travels as waves of pressure. The ear turns those waves into signals, and tiny hair cells in the inner ear send them along the hearing nerve. Hair cells in humans do not grow back once they are badly damaged."),
        ("The decibel scale",
         "Loudness is measured in decibels, and the scale is logarithmic. Every increase of 10 decibels means about ten times the sound power, and people hear it as roughly twice as loud. That is why a small rise in the number can mean a large rise in danger."),
        ("How noise damages hearing",
         "Loud sound for long enough can damage hair cells and cause permanent hearing loss. Damage can also bring ringing or buzzing in the ears, called tinnitus. The harm depends on both how loud a sound is and how long it lasts."),
        ("Limits used at work",
         "Safety bodies set limits on daily exposure. A common guide is that an average of about 85 decibels over an eight-hour day is the level at which protection is expected. Louder sounds call for much shorter exposure."),
        ("Protecting the ears",
         "Protection starts with the work itself. Engineers reduce noise at the source, put barriers between people and the noise, and limit the time spent near loud machines. Ear defenders and plugs are the last line of defence, and they only work when worn correctly and checked regularly."),
        ("Noise on a ship",
         "A ship has machines that run all day. Quiet zones for rest, and loud equipment placed well away from living areas, protect both sleep and hearing. Money spent on quieter machines or good barriers often saves more in health costs later."),
    ],
    "test": [
        ("Which tiny cells in the inner ear does loud noise damage?",
         [("a", "Hair cells"), ("b", "Bone cells"), ("c", "Skin cells"), ("d", "Red blood cells")], "a"),
        ("On the decibel scale, what does an increase of 10 decibels roughly mean for sound power?",
         [("a", "About one more"), ("b", "Exactly the same"), ("c", "About ten times more"), ("d", "About half")], "c"),
        ("Which condition is ringing or buzzing in the ears caused by noise?",
         [("a", "Anaemia"), ("b", "Tinnitus"), ("c", "Scurvy"), ("d", "Tendinitis")], "b"),
        ("What is the common guide for daily noise exposure at work?",
         [("a", "Any level is fine"), ("b", "Only at night"), ("c", "About 200 decibels all day"), ("d", "About 85 decibels averaged over an eight-hour day")], "d"),
        ("What is the best first step to protect hearing?",
         [("a", "Turn the machine up to drown out the noise"), ("b", "Wear plugs and forget them"), ("c", "Reduce noise at the source"), ("d", "Ignore it")], "c"),
    ],
}
