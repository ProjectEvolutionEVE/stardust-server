"""Managing a Core Research Facility: service portfolio, staffing models, quality control, user access, facility reporting and closing or expanding services."""
CODE = "science5_lab_facility"
BOOK = {
    "title": "Managing a Core Research Facility",
    "subtitle": "Running shared equipment and services that many labs depend on",
    "chapters": [
        ("What a core facility is",
         "A core facility is a shared service that gives many research groups access to expensive equipment or expertise. It saves each group from buying and running everything itself. Its value depends on being reliable and fairly run."),
        ("Service portfolio",
         "The service portfolio lists what the facility offers, at what price and to whom. Review it each year. Services that few people use may be worth stopping, and new demand may justify adding one."),
        ("Staffing models",
         "A staffing model sets how the facility's people are organised, such as dedicated technicians for each instrument or a shared pool. Choose the model that fits the workload and the skills needed. Plan for cover during leave."),
        ("Quality control and user access",
         "Quality control keeps the results trustworthy, through regular checks and documented procedures. User access rules say who may use which equipment, after what training. Clear rules protect both the instruments and the results."),
        ("Facility reporting",
         "Facility reports show usage, income, downtime and user numbers. They help funders and managers see whether the facility is worth its cost. Honest reporting includes the problems as well as the successes."),
        ("Closing or expanding services",
         "A decision to close or expand a service should use the portfolio review, the demand data and the costs. Give users notice and an alternative where possible. Expansions should be checked against staffing and space first."),
    ],
    "test": [
        ("What is a core research facility?",
         [("a", "A private office for one scientist"), ("b", "A shared service giving many groups access to equipment or expertise"), ("c", "A warehouse for old furniture"), ("d", "A bus stop")], "b"),
        ("What does a service portfolio list?",
         [("a", "The staff's favourite music"), ("b", "The services offered, their prices and who they serve"), ("c", "The lunch menu"), ("d", "The parking spaces")], "b"),
        ("What do user access rules decide?",
         [("a", "Who may use which equipment, after what training"), ("b", "Which colour the walls should be"), ("c", "Which journal to publish in"), ("d", "How long the lunch break lasts")], "a"),
        ("What do facility reports show?",
         [("a", "Only the best results"), ("b", "Usage, income, downtime and user numbers"), ("c", "The price of the building"), ("d", "The staff's holiday photos")], "b"),
        ("What should guide a decision to close a service?",
         [("a", "A coin toss"), ("b", "Only the most recent complaint"), ("c", "The portfolio review, demand data and costs"), ("d", "The colour of the sign")], "c"),
    ],
}
