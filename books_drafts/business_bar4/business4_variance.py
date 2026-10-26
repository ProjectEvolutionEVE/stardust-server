"""Variance Analysis: budget against actual, price variance, quantity variance, reading causes, reports that lead to action, and avoiding blame."""
CODE = 'business4_variance'
BOOK = {
    "title": 'Variance Analysis',
    "subtitle": 'Comparing what was planned with what happened, and asking why',
    "chapters": [
        ('Budget against actual',
         'A budget is a plan for money and quantities. Variance analysis compares that plan with what actually happened. The difference is the variance. A variance is not a verdict on its own; it is a signal that something needs a closer look.'),
        ('Price variance',
         'Price variance shows how much more or less was paid for an input than planned. If the budget assumed a cost of five per kilogram and the firm paid six, the price variance is unfavourable. Causes might include supplier price rises, rush orders or a poor deal.'),
        ('Quantity variance',
         'Quantity variance shows how much more or less of an input was used than planned for the output achieved. Using extra material to make the same product is an unfavourable quantity variance. Causes might include waste, poor skills or equipment faults.'),
        ('Reading causes',
         'A good analyst looks behind each variance. Price and quantity effects can cancel each other out, so both must be examined. Timing differences, one-off events and errors in the budget itself can also explain a gap. The aim is to find the true cause.'),
        ('Reports that lead to action',
         'A variance report is useful only if it leads someone to act. It should show the biggest differences first, explain the likely cause in plain language, and name who will look into it and by when. Long tables of numbers with no comment rarely change anything.'),
        ('Avoiding blame',
         'When variances are used to punish people, staff hide problems and reports become fiction. Managers do better to ask what the variance tells them about the process, and to treat it as a shared question. Honest reporting is worth more than a clean-looking number.'),
    ],
    "test": [
        ('What is variance analysis?',
         [('a', 'Choosing a new office colour'), ('b', 'Comparing the budget plan with what actually happened'), ('c', 'Writing a company song'), ('d', 'Setting the national interest rate')], 'b'),
        ('If a firm pays more per kilogram than planned, which variance is affected?',
         [('a', 'Quantity variance only'), ('b', 'Brand variance'), ('c', 'Price variance'), ('d', 'Weather variance')], 'c'),
        ('What does quantity variance measure?',
         [('a', 'The number of colours in the office'), ('b', 'The height of the building'), ('c', 'The interest rate on a loan'), ('d', 'How much more or less of an input was used than planned for the output achieved')], 'd'),
        ('Why must price and quantity effects both be examined?',
         [('a', 'Because they can cancel each other out'), ('b', 'Because one of them is always zero'), ('c', 'Because the law demands it'), ('d', 'Because they are always the same')], 'a'),
        ('What makes a variance report useful?',
         [('a', 'It is as long as possible'), ('b', 'It leads someone to act on the biggest differences'), ('c', 'It names someone to blame'), ('d', 'It contains no explanation')], 'b'),
    ],
}
