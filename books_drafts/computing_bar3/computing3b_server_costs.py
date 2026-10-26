"""The Cost of Running Servers: what a server bill is made of, which costs grow with players, and how to plan and watch them."""
CODE = "computing3b_server_costs"
BOOK = {
    "title": "The Cost of Running Servers",
    "subtitle": "What a server bill is made of, and how costs grow with players",
    "chapters": [
        ("What you pay for",
         "Running a server costs money in several ways. You pay for the computer that runs the program, for the database, for storage and backups, and for the data sent out. Some services, such as text messages and email, also charge for each message. Each cost may be billed by the month, by the hour or by the amount used."),
        ("Costs that stay and costs that grow",
         "Some costs stay the same, such as a basic server kept running all month. Others grow with use. More players mean more requests, more stored records and more data sent out. A good budget keeps the two kinds of cost on separate lines."),
        ("Paying per message",
         "Some services charge for each message they send. A text-message sign-in code costs a small amount every time it is sent. Limits on how many codes a person can request are therefore a money control as well as a security one."),
        ("Storage and backups add up",
         "Every stored record takes space, and backups keep extra copies of it. A small cost per record can become a large bill when records pile up for years. Deleting data that is no longer needed saves money as well as reducing privacy risk."),
        ("Plan and measure",
         "Watch the usage and the bill every month, and set an alert before the bill passes the plan. Compare the cost per player over time. If the cost per player rises, something needs fixing, even when the total still looks small."),
        ("Money in the budget",
         "Build a simple budget with a fixed line for servers, a line for each per-use service, and a reserve for surprises. Compare the total with what the project earns or what its users pay. Good planning turns a surprise into a known number."),
    ],
    "test": [
        ("Which of these is a fixed cost of running a server?",
         [("a", "A basic server kept running all month"), ("b", "Each text message sent"), ("c", "Each record sent out to a player"), ("d", "Each new player who joins")], "a"),
        ("Why can a per-message service cost grow as players grow?",
         [("a", "Because each message costs a little, so more messages mean a bigger bill"), ("b", "Because messages become heavier over time"), ("c", "Because messages are always free"), ("d", "Because the players pay the bill directly")], "a"),
        ("Why do limits on sign-in codes also matter for money?",
         [("a", "Because limits make the servers cheaper to rent"), ("b", "Because codes are printed on paper"), ("c", "Because each code sent costs money, so limits stop the bill being drained"), ("d", "Because limits make the database larger")], "c"),
        ("What do backups do to the cost of stored data?",
         [("a", "They make storage free"), ("b", "They remove the need to pay for storage"), ("c", "They halve every bill"), ("d", "They keep extra copies, so storage costs more")], "d"),
        ("What is a good way to catch rising costs early?",
         [("a", "Watch usage and bills every month, and set an alert before the bill passes the plan"), ("b", "Wait until the bill arrives after a year"), ("c", "Turn off the monitoring to save money"), ("d", "Ask players to pay more without looking at the numbers")], "a"),
    ],
}
