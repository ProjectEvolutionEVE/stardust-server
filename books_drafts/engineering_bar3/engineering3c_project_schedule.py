"""Project Schedules and the Critical Path: ordering the tasks of a build and finding the chain that sets the finish date."""
CODE = 'engineering3c_project_schedule'
BOOK = {
    "title": 'Project Schedules and the Critical Path',
    "subtitle": 'Ordering the tasks of a build, and finding the chain that sets the finish date',
    "chapters": [
        ('Break the job into tasks',
         "A build is a set of tasks, and each task has a time and a cost. List every task and say which ones must come first. A clear list is the start of any schedule."),
        ('Dependencies',
         "Some tasks depend on others. The frame must stand before the panels go on. Drawing these links shows the order, and shows which tasks can run side by side. Tasks with no link between them can share the work."),
        ('The critical path',
         "The critical path is the longest chain of dependent tasks from start to finish. It sets the earliest finish date for the whole build. A delay on the critical path moves the end date by the same amount."),
        ('Slack',
         "A task off the critical path has slack, which is the time it can slip without moving the end date. Slack shows where you can borrow people or time without harm. Tasks on the critical path have no slack, so watch them most closely."),
        ('Milestones',
         "A milestone is a checkpoint with no work of its own, such as frame passed inspection. Milestones show progress to the team and to the people who pay for the work. Set them where a problem would be expensive to find late."),
        ('The cost of delay',
         "Every day a build runs late costs money in wages, rent and sales that wait. Work out the cost of a day's delay before you cut corners to save time. Time is a budget too, and often the most expensive one."),
    ],
    "test": [
        ('What is a task dependency?',
         [('a', 'A task that has no cost'), ('b', 'A paint colour'), ('c', 'The name of the team'), ('d', 'A link showing that one task must come before another')], 'd'),
        ('What is the critical path?',
         [('a', 'The longest chain of dependent tasks from start to finish'), ('b', 'The shortest task'), ('c', "The team's route to work"), ('d', 'The list of all parts')], 'a'),
        ('What happens when a task on the critical path is delayed?',
         [('a', 'Nothing, since it is not important'), ('b', 'The price of paint falls'), ('c', 'The whole project end date moves by the same amount'), ('d', 'The project finishes early')], 'c'),
        ('What is slack?',
         [('a', 'Time spent resting'), ('b', 'How long a task off the critical path can slip without moving the end date'), ('c', 'A type of screw'), ('d', 'The cost of paint')], 'b'),
        ('What is a milestone?',
         [('a', 'A checkpoint with no work of its own, such as frame passed inspection'), ('b', 'A large stone'), ('c', 'The task that costs the most'), ('d', 'A measure of distance')], 'a'),
    ],
}
