"""Return on an Aircraft Navigation Upgrade: upgrade costs, savings, approach access, payback, risk and decisions."""
CODE = 'navigation5_nav_upgrade_roi'
BOOK = {
    "title": 'Return on an Aircraft Navigation Upgrade',
    "subtitle": 'Whether a new navigation system pays for itself',
    "chapters": [
        ('Upgrade costs',
         'The cost of an upgrade is more than the purchase price. Add installation, training, certification, and the time the aircraft is out of service. Count all of them, or the return will look better than it is.'),
        ('Savings',
         'Savings can come from less fuel burned, shorter routes, fewer diversions and lower maintenance. Estimate each one separately and say how sure you are of it.'),
        ('Approach access',
         'New equipment can open more approach paths and let an aircraft land in poor weather. That access has value, because flights that would have been cancelled can still arrive on time.'),
        ('Payback',
         'Payback is the time it takes the savings to repay the cost. A short payback is attractive, but it is only one measure. Also look at the total return over the life of the equipment.'),
        ('Risk',
         'Ask what happens if the upgrade is late, or if the savings fall short. Test the case with lower savings and longer delays. A plan that still pays back under those tests is a stronger plan.'),
        ('Decisions',
         'Compare the upgrade with the other options, including doing nothing. Choose the plan with the best return that the operator can accept, in cost, in risk and in the time it takes to bring in.'),
    ],
    "test": [
        ('Which of these is an upgrade cost?',
         [('a', 'The colour of the cabin walls'), ('b', 'Installation and training'), ('c', 'The weather on the day of delivery'), ('d', 'The name of the airline website')], 'b'),
        ('What is payback?',
         [('a', 'The price of the upgrade'), ('b', 'The distance flown'), ('c', 'The time taken for savings to repay the cost'), ('d', 'The number of pilots aboard')], 'c'),
        ('What can new approach equipment offer?',
         [('a', 'Heavier aircraft'), ('b', 'Less light on the instruments'), ('c', 'Fewer runways in the world'), ('d', 'Access to more approach paths in poor weather')], 'd'),
        ('What does a risk check look at?',
         [('a', 'What happens if the upgrade is late or the savings fall short'), ('b', 'What the cabin paint costs'), ('c', 'The colour of the manual'), ('d', 'Nothing, since risks cannot be counted')], 'a'),
        ('What is the purpose of comparing options in an upgrade decision?',
         [('a', 'To pick the most expensive option'), ('b', 'To avoid making any choice'), ('c', 'To choose the plan with the best return the operator can accept'), ('d', 'To delay the decision forever')], 'c'),
    ],
}
