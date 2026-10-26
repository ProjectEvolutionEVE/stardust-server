"""Medicine, bar 3 (Senior Doctor), part B: Light, Clocks and the Ship Day. How light sets the body clock, and how a ship with many sunrises keeps a steady day."""
CODE = "medicine3b_ship_clock"
BOOK = {
    "title": "Light, Clocks and the Ship Day",
    "subtitle": "How light sets the body clock, and how a ship with many sunrises keeps a steady day",
    "chapters": [
        ("Light is the main clock signal",
         "The body clock is set mostly by light that reaches the eyes. Special cells in the retina sense light and send the signal to the brain's master clock. Morning light tends to move the clock earlier, and evening light tends to move it later."),
        ("Sixteen sunrises a day",
         "The International Space Station circles Earth about every 90 minutes, so its crew sees around sixteen sunrises and sixteen sunsets each day. Without a steady plan the body clock would be confused. Crews therefore keep a fixed 24-hour schedule, whatever the window shows."),
        ("A ship that sets its own light",
         "Aboard a ship, the lighting can follow a schedule. Brighter, cooler light during the working day and dimmer, warmer light in the evening give the body clock the rhythm of a day. Lighting is one of the main tools for keeping a crew on time."),
        ("Fixed times for food and sleep",
         "Meals, exercise and sleep also send signals to the body clock. Eating at regular times and keeping a steady sleep period give the clock more cues to follow. Keeping the same times each day helps the clock stay in step."),
        ("When the clock is out of step",
         "A jump across time zones, or night work, puts the body clock out of step with the day. Symptoms can include poor sleep, tiredness, low appetite and trouble concentrating. The clock usually settles over a few days, once light and routine line up with the new day."),
        ("Planning the day as a crew",
         "A crew can plan the day as one: work blocks, rest blocks and shared meals. Clear plans make it easier to catch up after a late shift or a hard event. They also keep everyone's body clock moving in the same direction."),
    ],
    "test": [
        ("What sets the body clock most strongly?",
         [("a", "Light reaching the eyes"), ("b", "The ship's engines"), ("c", "Loud music"), ("d", "The size of meals")], "a"),
        ("Roughly how many sunrises does the crew of the International Space Station see each day?",
         [("a", "One"), ("b", "Two"), ("c", "About sixteen"), ("d", "About a thousand")], "c"),
        ("What helps a crew's body clock feel the rhythm of a day aboard a ship?",
         [("a", "Constant bright light, day and night"), ("b", "Bright light in the working day and dimmer light in the evening"), ("c", "Total darkness at all times"), ("d", "Changing the length of the day every hour")], "b"),
        ("Which way does morning light tend to move the body clock?",
         [("a", "Later"), ("b", "Not at all"), ("c", "It stops the clock completely"), ("d", "Earlier")], "d"),
        ("What helps a body clock settle into a new day?",
         [("a", "Staying in the dark all day"), ("b", "Skipping every meal"), ("c", "Light and routine that line up with the new day"), ("d", "Changing sleep times every night")], "c"),
    ],
}
