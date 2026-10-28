"""Team Topologies in Practice: designing teams around the flow of work, and how they interact."""
CODE = "computing5_team_topologies"
BOOK = {
    "title": "Team Topologies in Practice",
    "subtitle": "Teams built around the flow of work, and how they work together",
    "chapters": [
        ("Why team shape matters",
         "A software team's structure shapes the software it builds. When the people who build a service sit in one team, the service tends to match that team's boundaries. Team Topologies is a practical guide to designing teams on purpose."),
        ("Four kinds of team",
         "The book names four basic team types. A stream-aligned team owns one flow of work for the business, such as a customer journey. An enabling team helps others learn a new skill, a complicated-subsystem team looks after a part that needs deep specialist knowledge, and a platform team offers tools that other teams use themselves."),
        ("How teams interact",
         "Teams work together in a small set of interaction modes. In collaboration two teams work closely for a time, in X-as-a-service one team uses another's offer with little close contact, and in facilitating one team helps another get unstuck. Naming the mode makes clear what each side should expect."),
        ("Cognitive load",
         "Every team can only hold so much in its head at once. A team that owns too many systems, tools and rules is overloaded, and its work slows down. Good design keeps each team's load within what its people can really manage."),
        ("Boundaries change",
         "Team boundaries should change as the business and its software change. A boundary drawn for last year's product may be wrong this year. Review the shape of teams on a set rhythm, and move boundaries when the work moves."),
        ("Measuring the fit",
         "A design is working when teams can deliver without constant waiting on each other. Look at how often work crosses team boundaries, how long handoffs take, and whether teams feel overloaded. Use these signs together to judge the design, not a single number."),
    ],
    "test": [
        ("How many basic team types does Team Topologies describe?",
         [("a", "Two"), ("b", "Four"), ("c", "Seven"), ("d", "Twelve")], "b"),
        ("Which team owns one flow of work for the business?",
         [("a", "Platform team"), ("b", "Enabling team"), ("c", "Stream-aligned team"), ("d", "Complicated-subsystem team")], "c"),
        ("What does a cognitive load limit mean for a team?",
         [("a", "The team's pay ceiling"), ("b", "The most a team can reasonably hold in mind"), ("c", "The number of meetings allowed"), ("d", "The team's office size")], "b"),
        ("In which interaction mode does one team use another team's service with little close contact?",
         [("a", "Collaboration"), ("b", "Facilitating"), ("c", "Shadowing"), ("d", "X-as-a-service")], "d"),
        ("Which sign suggests a team design is working?",
         [("a", "Teams wait on each other often"), ("b", "Handoffs keep getting longer"), ("c", "Teams deliver without constant waiting on each other"), ("d", "Teams take on more systems each quarter")], "c"),
    ],
}
