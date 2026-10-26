"""Light-Time Delay: talking across the distance, when radio takes time to cross space and far craft must act on their own."""
CODE = "flight3c_light_time"
BOOK = {
    "title": "Light-Time Delay",
    "subtitle": "Radio signals take time to cross space, so far craft must act on their own",
    "chapters": [
        ("Radio takes time",
         "Radio signals travel at the speed of light. That is very fast, but it is not instant. The further a craft is from Earth, the longer a message takes to arrive, in both directions. This delay is called light-time, and it is a plain fact of distance."),
        ("Times across the Solar System",
         "A one-way message from the Earth to the Moon takes about a second and a quarter. To Mars it takes anywhere from about three minutes to over twenty, depending on where the two planets are in their orbits. Out past the giants, a single message can take hours."),
        ("Round trips",
         "A question and its answer take twice the one-way time. A craft at Mars can take well over half an hour to answer, so controllers on Earth cannot steer it moment by moment. They have to wait, and plan around the wait."),
        ("Plan ahead",
         "Because the answers are always late, a far craft needs a plan that works without help. Commands are sent in advance, and the craft checks its own readings and carries on by itself when it must. Good planning is what makes the wait safe."),
        ("The picture is old",
         "What you see from a far craft is a picture of the past. By the time the picture arrives, the craft has moved on. A careful operator keeps that in mind when judging what is happening now."),
        ("A pilot's view",
         "Short distances make talk easy, and long distances make it slow. Keep your reports short and clear, and be ready to act on your own when the answer is hours away. A good report says what you see, what you have done and what you will do next."),
    ],
    "test": [
        ("What is light-time?",
         [("a", "The glow of the Sun"), ("b", "The time a radio message takes to cross space"), ("c", "A kind of engine"), ("d", "The length of a day in orbit")], "b"),
        ("Roughly how long does a one-way message take from the Earth to the Moon?",
         [("a", "About a second and a quarter"), ("b", "About an hour"), ("c", "About three days"), ("d", "Instant")], "a"),
        ("Why must a far craft act on its own?",
         [("a", "Its radio is broken"), ("b", "Controllers are asleep"), ("c", "Space is too quiet"), ("d", "Answers come back too late for moment-by-moment steering")], "d"),
        ("How long does a question to Mars and back take, compared with the one-way time?",
         [("a", "Half the one-way time"), ("b", "The same as one way"), ("c", "Twice the one-way time"), ("d", "Ten times longer")], "c"),
        ("Why is a picture from a far craft a picture of the past?",
         [("a", "The cameras are old"), ("b", "Light and radio take time to arrive, so the craft has moved on"), ("c", "Pictures fade in space"), ("d", "The Sun paints them")], "b"),
    ],
}
