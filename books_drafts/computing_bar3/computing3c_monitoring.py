"""Metrics, Alerts and Dashboards: watching a running system with numbers, and knowing when to act."""
CODE = "computing3c_monitoring"
BOOK = {
    "title": "Metrics, Alerts and Dashboards",
    "subtitle": "Watching a running system with numbers, and knowing when to act",
    "chapters": [
        ("Watching while it runs",
         "Monitoring means keeping an eye on a running system through measurements taken over time. A metric is one such number, such as requests per minute or the share of requests that failed. Measured over time, numbers show whether things are getting better or worse."),
        ("Four things to watch",
         "A widely used set is latency, traffic, errors and saturation. Latency is how long requests take, traffic is how many arrive, errors are how many fail, and saturation is how full the machines are. Watching these four gives a quick view of most problems."),
        ("Averages can hide trouble",
         "An average response time can look fine while a few users wait a very long time. Look at the slowest tenth, or the slowest one percent, too. These slower measures are called percentiles."),
        ("Dashboards",
         "A dashboard puts the key metrics on one screen, so a person can see the health of the system at a glance. Keep it small. Too many charts make the real problem hard to find."),
        ("Alerts",
         "An alert tells a person when a metric crosses a set line, such as errors rising above a set share for five minutes. Alerts should be rare and clear, because an alert that rings all the time gets ignored. A good alert says what is wrong and what to check first."),
        ("Watching the budget too",
         "Monitoring costs money to run and store, so keep the metrics you actually use. Treat the cost of monitoring like any other line in the budget. Review it now and then, and drop what nobody reads."),
    ],
    "test": [
        ("What is a metric?",
         [("a", "A unit of weight"), ("b", "A kind of screen"), ("c", "A measurement taken over time, such as requests per minute"), ("d", "A player's name")], "c"),
        ("What are the four things a common monitoring set watches?",
         [("a", "Paint, paper, pens and glue"), ("b", "Latency, traffic, errors and saturation"), ("c", "Speed, weight, colour and cost"), ("d", "Sound, light, heat and power")], "b"),
        ("Why can an average response time mislead?",
         [("a", "It always shows the true worst case"), ("b", "It is always zero"), ("c", "It can look fine while a few users wait a very long time"), ("d", "It hides every error")], "c"),
        ("What is an alert?",
         [("a", "A new colour for the screen"), ("b", "A player's message"), ("c", "A sound effect"), ("d", "A notice that tells a person when a metric crosses a set line")], "d"),
        ("Why should alerts be rare?",
         [("a", "Because an alert that rings all the time gets ignored"), ("b", "Because alerts cost nothing"), ("c", "Because alerts are sent to the moon"), ("d", "Because a rare alert is always wrong")], "a"),
    ],
}
