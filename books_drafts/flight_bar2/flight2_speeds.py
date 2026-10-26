"""Reading Speeds and Distances: metres a second, kilometres an hour, and judging how long a trip really takes."""
CODE = "flight2_speeds"
BOOK = {
    "title": "Reading Speeds and Distances",
    "subtitle": "Metres a second, kilometres an hour, and how long a trip really takes",
    "chapters": [
        ("Metres a second",
         "The info line shows your speed in metres per second. Ten metres a second is 36 kilometres an hour, a speed you already know from the road. Learn a few benchmarks, so a number on the screen means something to you at once."),
        ("Converting the units",
         "To change metres per second into kilometres per hour, multiply by 3.6. To go the other way, divide by 3.6. A kilometre a second is 1,000 metres a second, so it is 3,600 kilometres an hour. Doing the sum in your head helps you judge a trip."),
        ("Time is distance over speed",
         "The time a trip takes equals the distance divided by the speed. As a sum, a craft holding 900 metres a second would need about 38 days to cover 3 million kilometres. Check this kind of sum before you plan a long flight."),
        ("Speeds in real spaceflight",
         "Real spacecraft speeds are often given in kilometres a second. A craft in low Earth orbit moves at about 7.8 kilometres a second, which is roughly 28,000 kilometres an hour. Use the conversion to set the game's numbers beside the real ones."),
        ("Distances on the screen",
         "Short distances are shown in metres or kilometres, and long ones switch to astronomical units. The approach number is the distance still to fly to what the scanner is tracking. If it is falling, you are closing in."),
        ("Reading the Sun's distance",
         "The info line shows your distance from the Sun in AU, to three decimal places. Compare two readings a little apart to tell whether you are moving inward or outward. The third decimal place shows changes that the first two hide."),
    ],
    "test": [
        ("How many kilometres an hour is 10 metres a second?",
         [("a", "10 km/h"), ("b", "36 km/h"), ("c", "100 km/h"), ("d", "3.6 km/h")], "b"),
        ("To change metres a second into kilometres an hour, what do you do?",
         [("a", "Divide by 3.6"), ("b", "Multiply by 3.6"), ("c", "Add 1,000"), ("d", "Square the number")], "b"),
        ("About how many kilometres an hour is 7.8 kilometres a second?",
         [("a", "About 780 km/h"), ("b", "About 28,000 km/h"), ("c", "About 7.8 km/h"), ("d", "About 2,800 km/h")], "b"),
        ("At a steady 900 metres a second, roughly how long would 3 million kilometres take?",
         [("a", "About 38 days"), ("b", "About 38 hours"), ("c", "About 38 minutes"), ("d", "About 3 hours")], "a"),
        ("What does a shrinking approach number tell you?",
         [("a", "You are moving away"), ("b", "The Sun is growing"), ("c", "The hold is emptying"), ("d", "You are closing on what the scanner tracks")], "d"),
    ],
}
