"""Managing an Exploration Portfolio: project lists, stage gates, budget splits, kill decisions, metrics and reporting."""
CODE = 'mining5_portfolio'
BOOK = {
    "title": "Managing an Exploration Portfolio",
    "subtitle": "Project lists, stage gates, budget splits, kill decisions and metrics",
    "chapters": [
        ("A portfolio, not a single bet",
         "An exploration company rarely has one project. It holds a portfolio of many, each at a different stage. Managing the set as a whole is the job, because the best returns come from the mix."),
        ("The project list",
         "The portfolio starts with a clear list of every project, with its stage, its cost to date and its next step. The list is updated often. A project that is not on the list is not being managed."),
        ("Stage gates",
         "Each project must pass a review, called a stage gate, before it moves on. At each gate, the team checks clear criteria such as results, costs and risks. A project that fails a gate is paused or changed, not allowed to drift on."),
        ("Budget splits",
         "The budget is split across projects so that no single failure sinks the whole portfolio. Most of the money goes to the strongest projects, with a smaller share kept for new ideas. The split is reviewed as results come in."),
        ("Kill decisions",
         "A kill decision stops a project that no longer earns its place. Stopping early is a good result when the evidence is weak, because it frees money for better projects. Teams that never stop projects usually end up spreading money too thin."),
        ("Metrics and reporting",
         "Useful metrics include the expected value per dollar spent, the time to each gate and the share of projects that meet their targets. Reports to leaders should show clear status, the main risks and the decisions needed. Hidden problems cost more than bad news."),
    ],
    "test": [
        ("What is a stage gate in a portfolio?",
         [("a", "A fence around the site"), ("b", "A review point where a project must meet clear criteria to go on"), ("c", "A type of drill bit"), ("d", "A payment to a landowner")], "b"),
        ("What is a kill decision?",
         [("a", "An accident on site"), ("b", "A penalty for late reports"), ("c", "A decision to double the budget"), ("d", "A decision to stop a project that no longer earns its place")], "d"),
        ("Why split a budget across several projects?",
         [("a", "To spread risk so one failure does not sink the whole portfolio"), ("b", "To pay less tax"), ("c", "To avoid reporting"), ("d", "To hide losses")], "a"),
        ("Which is a useful portfolio metric?",
         [("a", "The colour of the reports"), ("b", "The number of meetings held"), ("c", "Expected value per dollar spent"), ("d", "The number of staff photos")], "c"),
        ("What should a report to leaders show?",
         [("a", "Only the best news"), ("b", "Hidden problems"), ("c", "Long lists of raw data only"), ("d", "Clear status, main risks and the decisions needed")], "d"),
    ],
}
