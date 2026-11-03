"""Real Options for Mapping Projects: waiting, staged investment, option value, decision trees, estimates and limits."""
CODE = 'navigation5_real_options'
BOOK = {
    "title": 'Real Options for Mapping Projects',
    "subtitle": 'Keeping choices open when the future is uncertain',
    "chapters": [
        ('The option to wait',
         'Many mapping projects do not have to start today. Waiting keeps a choice open until better information arrives. That freedom has real value, and a good planner counts it before spending money.'),
        ('Staged investment',
         'Spend in small stages instead of all at once. Each stage gives you new information. After each one you can stop, continue, or change course, which keeps your losses small if the plan goes wrong.'),
        ('What option value means',
         'Option value is the worth of keeping a choice open. It grows when the future is uncertain and when a bad outcome can be avoided. A plan that can be changed is often worth more than a fixed one.'),
        ('Decision trees',
         'A decision tree draws your choices and the chance events as branches. Start at the end branches, work back to the start, and compare the expected values at each choice point. The best first decision often becomes clear this way.'),
        ('Estimates and their limits',
         'Cost and benefit estimates are never exact. Show them as ranges, and note which numbers matter most to the result. A small change in one key figure can change the whole decision.'),
        ('Know the limits',
         'Real options help, but they do not solve everything. Do not invent options that are not really there. Keep the analysis simple enough that the people who must decide can follow it.'),
    ],
    "test": [
        ('What is the option to wait?',
         [('a', 'Paying all costs before the work starts'), ('b', 'Keeping a choice open until more is known'), ('c', 'Selling the project at once'), ('d', 'Ignoring the risk of delay')], 'b'),
        ('What does staged investment mean?',
         [('a', 'Spending the whole budget on day one'), ('b', 'Borrowing before a plan exists'), ('c', 'Hiring a second team for the same job'), ('d', 'Spending in steps, with a check after each step')], 'd'),
        ('When is option value highest?',
         [('a', 'When the future is uncertain and a bad outcome can be avoided'), ('b', 'When the future is fully known'), ('c', 'When no decision can be changed'), ('d', 'When costs are zero')], 'a'),
        ('What is a decision tree?',
         [('a', 'A list of project staff'), ('b', 'A map of rainfall'), ('c', 'A diagram of choices and chance events drawn as branches'), ('d', 'A type of survey instrument')], 'c'),
        ('Why are cost and benefit estimates often shown as ranges?',
         [('a', 'Ranges are always more exact'), ('b', 'Estimates are never exact, and a range shows the uncertainty'), ('c', 'Every law requires ranges'), ('d', 'Ranges remove the need for any decision')], 'b'),
    ],
}
