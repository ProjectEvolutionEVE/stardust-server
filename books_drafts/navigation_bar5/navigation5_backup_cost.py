"""Cost-Effective Backup Navigation: backups for satellite services, their costs, risk reduction, choosing among options and maintenance."""
CODE = "navigation5_backup_cost"
BOOK = {
    "title": "Cost-Effective Backup Navigation",
    "subtitle": "Planning for the day the main service fails",
    "chapters": [
        ("Backups for satellites",
         "A backup is a system ready to take over if the main satellite service fails. It may be another satellite, a ground system or an older method. A backup is a form of insurance against loss."),
        ("Their costs",
         "Backups cost money to build, launch and maintain. The cost has to be weighed against the risk the backup reduces. Costs should be counted over the whole life of the backup."),
        ("Risk reduction",
         "A backup reduces risk by lowering the chance that a service is lost for a long time. The reduction is measured as a lower expected loss. Good planning shows how much risk is removed."),
        ("The choice",
         "Choosing a backup means comparing options by cost and effectiveness. The cheapest option is not always the best, and the most expensive is not always needed. Clear criteria guide the choice."),
        ("Maintenance",
         "Backups must be maintained and tested regularly to be useful. An untested backup can fail when it is needed most. Regular checks keep it ready."),
        ("Lessons",
         "The best backup is affordable, tested and matched to the real risk. Overbuilding wastes money, just as underbuilding leaves the risk open. Balance is the aim."),
    ],
    "test": [
        ("What is a backup for a satellite service?",
         [("a", "A system ready to take over if the main service fails"), ("b", "A sail"), ("c", "A painting"), ("d", "A fish")], "a"),
        ("What must the cost of a backup be weighed against?",
         [("a", "The colour of the box"), ("b", "The risk the backup reduces"), ("c", "The weather"), ("d", "The sea")], "b"),
        ("What does a backup reduce?",
         [("a", "The price of stars"), ("b", "The sky"), ("c", "The chance a service is lost for a long time"), ("d", "The wind")], "c"),
        ("Which statement about the cheapest backup is true?",
         [("a", "It is always the best"), ("b", "It is always the most expensive"), ("c", "It is never worth it"), ("d", "It is not always the best")], "d"),
        ("Why must backups be tested?",
         [("a", "To paint them"), ("b", "Because an untested backup can fail when it is needed"), ("c", "To lose them"), ("d", "To sell them")], "b"),
    ],
}
