"""Headcount Planning and Cost per Hire: how many people a team needs, how long hiring takes, and what each new hire really costs."""
CODE = "computing5_headcount_planning"
BOOK = {
    "title": "Headcount Planning and Cost per Hire",
    "subtitle": "Planning how many people are needed, and what each hire really costs",
    "chapters": [
        ("Capacity demand",
         "Capacity demand is the amount of work the team must do in a period, measured in hours or in units of output. Compare it with the hours the team can really give. The gap shows how many people are needed."),
        ("Hiring lead times",
         "Lead time is the gap between deciding to hire and having someone at work. It often runs for several months, including advertising, interviews and notice periods. Start hiring early enough for the work to be covered."),
        ("Cost per hire",
         "Cost per hire adds up the money spent to bring one person in, such as advertising, recruiter fees and the time of interviewers. Divide the total by the number of hires. The figure helps compare options fairly."),
        ("Ramp-up cost",
         "A new hire is not fully productive at once. Ramp-up time is the period before they reach full output, and it has a real cost in the time of others who help them. Include it when comparing a hire with a longer-term option."),
        ("Attrition",
         "Attrition is the rate at which people leave. Each departure creates a new hiring need and a ramp-up cost. Plans should assume some attrition, based on past figures."),
        ("Annual plans",
         "An annual headcount plan links the expected work, hiring timing and budget. Review it each quarter and change it when the work changes. A plan that is never checked against reality quickly becomes wrong."),
    ],
    "test": [
        ("What is capacity demand?",
         [("a", "The number of chairs in the office"), ("b", "The amount of work the team must do in a period"), ("c", "The fine for missing a deadline"), ("d", "The price of a laptop")], "b"),
        ("What is lead time in hiring?",
         [("a", "The time a candidate waits for a coffee"), ("b", "The length of a contract signed by a vendor"), ("c", "The time spent on a break"), ("d", "The gap between deciding to hire and having someone at work")], "d"),
        ("What does cost per hire include?",
         [("a", "The money spent to bring one person in, such as advertising and interviews"), ("b", "Only the salary of the new person"), ("c", "The price of a building"), ("d", "Only the cost of training courses")], "a"),
        ("Why must ramp-up cost be counted?",
         [("a", "New hires are fully productive on their first day"), ("b", "Ramp-up is a tax that must be paid"), ("c", "New hires are not fully productive at once, and others help them"), ("d", "Ramp-up only affects managers")], "c"),
        ("What is attrition?",
         [("a", "The time spent on training"), ("b", "The rate at which people leave"), ("c", "The cost of office space"), ("d", "A type of software licence")], "b"),
    ],
}
