"""Case Study: Phobos-Grunt, 2011. An ambitious plan, a spacecraft stuck in orbit, and a fall back to Earth."""
CODE = "flight5_phobos_grunt"
BOOK = {
    "title": "Case Study: Phobos-Grunt",
    "subtitle": "An ambitious plan, a spacecraft stuck in orbit, and a fall back to Earth",
    "chapters": [
        ("An ambitious plan",
         "Phobos-Grunt was a Russian mission launched in 2011 to land on Phobos, one of the moons of Mars, and bring a sample back to Earth. It was a bold plan with many parts. The spacecraft had to do a long and precise job."),
        ("Stuck in orbit",
         "After launch, the craft did not fire its engine as planned to leave Earth orbit. It stayed in a low orbit around the Earth and could not start its trip to Mars. Efforts to recover it did not succeed."),
        ("A likely cause",
         "A fault in the probe's onboard computer systems stopped its engine burn. Russia's inquiry blamed radiation damage to computer chips; others pointed to weak design and testing. The findings were not all made public. What is clear is that a single fault in a complex system can stop a whole mission."),
        ("The fall",
         "The craft slowly lost height and fell back to Earth in January 2012. Most of it burned up on the way down, and the remaining pieces fell into the ocean. No one was hurt."),
        ("The review",
         "Reviews looked at how the software was tested and how the mission was run. The findings pointed to gaps in testing and in the checking of how systems worked together. Changes to processes followed."),
        ("Lessons",
         "A complex mission needs testing for the whole system, not just its parts. The hardest bugs are often the ones that appear only when the pieces meet. A captain who asks how each system will be tested will catch many problems early."),
    ],
    "test": [
        ("What was Phobos-Grunt's planned target?",
         [("a", "The Moon"), ("b", "Venus"), ("c", "Phobos, a moon of Mars"), ("d", "Jupiter")], "c"),
        ("What went wrong just after launch?",
         [("a", "The craft did not fire its engine to leave Earth orbit"), ("b", "The craft landed on the launch pad"), ("c", "The solar panels were painted"), ("d", "The sample was lost in the lab")], "a"),
        ("Where did the fault that stranded the probe lie?",
         [("a", "A bird strike"), ("b", "In its onboard computer systems"), ("c", "A late lunch"), ("d", "Too much sunlight")], "b"),
        ("What happened to the craft in the end?",
         [("a", "It reached Mars safely"), ("b", "It is still orbiting Venus"), ("c", "It landed on the Moon"), ("d", "It fell back to Earth in January 2012")], "d"),
        ("What does the case show about complex missions?",
         [("a", "Only the parts need testing, not the whole"), ("b", "Software never fails"), ("c", "A single fault can stop a whole mission"), ("d", "Long plans are always safe")], "c"),
    ],
}
