"""The Habits of Good Pilots: plan first, fly gently, keep rest in view, and learn from every flight."""
CODE = "flight2_habits"
BOOK = {
    "title": "The Habits of Good Pilots",
    "subtitle": "Plan first, fly gently, rest well, and learn from every flight",
    "chapters": [
        ("Plan before you fly",
         "A good pilot knows the destination, the route and the stopping point before moving. Planning takes a minute and saves far more time than it costs. Say the plan to yourself before you go."),
        ("Fly gently, check often",
         "Gentle inputs and frequent checks are the core of good flying. You will rarely go wrong by slowing down a little. When in doubt, ease off the throttle and look again."),
        ("Rest is part of the job",
         "Tired pilots make slow and careless errors. Rest in your bed, and fly when your bars are healthy. The game warns you when you are pushing past good habits and proper rest, so take the warning seriously."),
        ("Listen to the Tower",
         "Keep the Tower's calls in mind while you fly, and act on what they tell you. Good pilots work as part of a crew, not as lone heroes. A calm, shared picture keeps everyone safer."),
        ("Practise the basics",
         "Even expert pilots keep practising the simple moves: small corrections, clean stops and steady scans. Doing the basics well keeps the hard moves manageable. Practice never really ends."),
        ("Learn from each flight",
         "After each flight, ask what went well, what did not, and what you will do differently next time. Keep those notes short, and read them before your next flight. A pilot who reviews their own flying improves quickly."),
    ],
    "test": [
        ("What does a good pilot do before moving?",
         [("a", "Plans the destination, the route and the stopping point"), ("b", "Turns the radar off"), ("c", "Warps at once"), ("d", "Empties the hold")], "a"),
        ("What does the game warn you about when you push past healthy limits?",
         [("a", "That the Sun is too bright"), ("b", "That your hold is full of gold"), ("c", "That a field is empty"), ("d", "That your body is past good habits and proper rest")], "d"),
        ("Why do good pilots keep practising the basic moves?",
         [("a", "So the basics stay sharp and the hard moves stay manageable"), ("b", "Because the basics can never change"), ("c", "To impress the Tower"), ("d", "Because basic moves cost no time")], "a"),
        ("What should a pilot do after each flight?",
         [("a", "Forget it at once"), ("b", "Delete all notes"), ("c", "Ask what went well, what did not, and what to do differently"), ("d", "Fly straight back out")], "c"),
        ("A bar has fallen below 65%. What is the sensible step?",
         [("a", "Keep flying at full speed"), ("b", "Turn the bars off"), ("c", "Sell the hold"), ("d", "Rest, ideally in your bed")], "d"),
    ],
}
