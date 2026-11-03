"""Cost-Benefit of Tsunami Warning Systems: lives and damage, warning reliability, costs, discounting, uncertainty and results."""
CODE = 'navigation5_tsunami_bca'
BOOK = {
    "title": 'Cost-Benefit of Tsunami Warning Systems',
    "subtitle": 'Weighing the lives and damage a warning can save against what it costs',
    "chapters": [
        ('Lives and damage',
         'The main benefit of a tsunami warning is the lives saved and the damage avoided. Both are hard to value, so count them with care and say how you did it. Do not leave them out because they are difficult.'),
        ('Warning reliability',
         'A warning system is worth only as much as it is accurate and fast. False alarms also carry costs, such as evacuations, lost trade and public doubt. Reliability must be part of the calculation.'),
        ('Costs',
         'Costs include sensors such as buoys, communications, staff and upkeep. Upkeep often lasts for many years, so add the whole life of the system, not just the first purchase.'),
        ('Discounting',
         'Benefits and costs in the future are usually weighed less than those in the present, at a chosen discount rate. The rate you pick can change the answer, so show the effect of different rates.'),
        ('Uncertainty',
         'Show ranges for the key inputs, and test how the result changes when they change. A result that holds across a wide range of assumptions is much more trustworthy than one that depends on a single guess.'),
        ('Results',
         'State the net benefit and the assumptions behind it. Show the trade-offs clearly, so the people who decide can see what they are buying and what risks remain.'),
    ],
    "test": [
        ('What is the main benefit of a tsunami warning system?',
         [('a', 'Lower taxes for everyone'), ('b', 'Fewer ships at sea'), ('c', 'Lives saved and damage avoided'), ('d', 'A better colour for the charts')], 'c'),
        ('Why do false alarms matter in this analysis?',
         [('a', 'They have no cost at all'), ('b', 'They carry costs, so reliability matters'), ('c', 'They make the system faster'), ('d', 'They are required by law')], 'b'),
        ('What does discounting do?',
         [('a', 'Weighs future costs and benefits less than present ones, at a chosen rate'), ('b', 'Makes future costs larger'), ('c', 'Removes all uncertainty'), ('d', 'Doubles the budget')], 'a'),
        ('What is a good way to handle uncertainty in a cost-benefit study?',
         [('a', 'Ignore the key inputs'), ('b', 'Use one exact number only'), ('c', 'Hide the assumptions'), ('d', 'Show ranges and test how the result changes')], 'd'),
        ('What should a results section state?',
         [('a', 'Only the best case'), ('b', 'The net benefit and the assumptions behind it'), ('c', 'The name of the designer'), ('d', 'Nothing about costs')], 'b'),
    ],
}
