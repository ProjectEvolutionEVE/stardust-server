"""Project Planning and the Critical Path: tasks and dependencies, a network diagram, the critical path, slack, Gantt charts, and crashing a schedule."""
CODE = 'business4_cpm'
BOOK = {
    "title": 'Project Planning and the Critical Path',
    "subtitle": 'Finding the chain of tasks that sets how soon a project can finish',
    "chapters": [
        ('Tasks and dependencies',
         'A project is a set of tasks, and some tasks must wait for others. A dependency says that one task cannot start until another is finished. Listing the tasks and their dependencies is the first step in planning any project, from a house to a software release.'),
        ('A network diagram',
         'A network diagram draws the tasks as boxes or arrows and links them by their dependencies. It shows the whole project as a map. Each task is shown with its duration, so the planner can work out the earliest start and finish for every step.'),
        ('The critical path',
         'The critical path is the longest chain of dependent tasks through the network. Its total length sets the shortest time the whole project can take. A delay on any task of the critical path delays the project, unless that delay is recovered elsewhere.'),
        ('Slack',
         'Slack, or float, is how long a task can be delayed without delaying the project. Tasks on the critical path have no slack. Tasks off it have some, and a manager can move people from tasks with slack to those on the critical path when needed.'),
        ('Gantt charts',
         "A Gantt chart shows tasks as bars along a timeline, with each bar's length matching its duration. Dependencies are shown as links between bars. Henry Gantt developed these charts in the early 1900s, and they remain a common way to show a schedule."),
        ('Crashing a schedule',
         'Crashing means spending more to shorten the project, for example by adding workers or paying for overtime on critical tasks. It is worth doing only on the critical path, since shortening other tasks does not finish the project sooner. The extra cost must be weighed against the value of the time saved.'),
    ],
    "test": [
        ('What does a dependency mean in a project plan?',
         [('a', 'One task cannot start until another is finished'), ('b', 'Two tasks must always be done by the same person'), ('c', 'A task has no duration'), ('d', 'A task is paid in advance')], 'a'),
        ('What is the critical path?',
         [('a', 'The path to the car park'), ('b', 'The longest chain of dependent tasks, which sets the shortest project time'), ('c', 'The shortest task in a project'), ('d', 'A list of unpaid invoices')], 'b'),
        ('What is slack in a schedule?',
         [('a', 'A type of loose fabric'), ('b', 'The cost of a new computer'), ('c', 'How long a task can be delayed without delaying the project'), ('d', 'The number of meetings held')], 'c'),
        ('Who developed the Gantt chart in the early 1900s?',
         [('a', 'Henry Ford'), ('b', 'Adam Smith'), ('c', 'Robert Owen'), ('d', 'Henry Gantt')], 'd'),
        ('What is crashing a schedule?',
         [('a', 'Spending more to shorten the project, usually on critical tasks'), ('b', 'Stopping a project forever'), ('c', 'Deleting every task at once'), ('d', 'Moving the deadline without telling anyone')], 'a'),
    ],
}
