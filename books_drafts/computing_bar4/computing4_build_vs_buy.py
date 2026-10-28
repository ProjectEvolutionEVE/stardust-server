"""Build or Buy: The Money Test: comparing the cost of making a system yourself with buying one from a vendor."""
CODE = 'computing4_build_vs_buy'
BOOK = {
    "title": 'Build or Buy: The Money Test',
    "subtitle": 'Comparing the cost of making a system yourself with buying one',
    "chapters": [
        ('Build costs and maintenance',
         'Building means paying for design, development, testing and years of maintenance. The first version is only the start. Count the ongoing work of fixing, updating and securing the code, because that is where most of the cost lies.'),
        ('Vendor fees',
         'Buying means paying licence or subscription fees, often every year. Fees may rise with usage or with the number of users. Read the pricing carefully and model the cost as the company grows.'),
        ('Switching risk',
         'Once a system is bought, moving away from it can be expensive and slow. Data formats, contracts and training all tie you in. Weigh this lock-in as a real cost, not a footnote.'),
        ('Strategic value',
         'Some systems are close to what makes your business different. Building those may be worth the cost, because control matters. Buying common systems, such as email or accounting, often makes better sense.'),
        ('A decision matrix',
         'A decision matrix scores each option against the criteria that matter, such as cost, risk, speed and control. Weight the criteria honestly, and show the scores in the open. A matrix helps a team argue about the reasons, not about the winner.'),
        ('Revisiting the choice',
         'A build or buy decision is not forever. Market prices, vendor terms and your own needs all change. Review the choice every year or two, and be willing to change direction when the facts change.'),
    ],
    "test": [
        ('What are the main ongoing costs of building a system?',
         [('a', 'Fixing, updating and securing the code'), ('b', 'Only the cost of the first version'), ('c', 'The price of the office coffee'), ('d', 'Nothing after launch')], 'a'),
        ('What is switching risk?',
         [('a', 'The risk of changing office'), ('b', 'The risk of changing the logo'), ('c', 'The cost and difficulty of moving away from a bought system'), ('d', 'The chance of a power cut')], 'c'),
        ('When might building be worth it?',
         [('a', 'When it is a common system like email'), ('b', 'When the system is close to what makes your business different'), ('c', 'When nobody has time to read'), ('d', 'When the vendor is free')], 'b'),
        ('What does a decision matrix do?',
         [('a', 'Paints the decision on a wall'), ('b', 'Picks a winner by chance'), ('c', 'Sends the decision to customers'), ('d', 'Scores each option against the criteria that matter')], 'd'),
        ('Why revisit a build or buy choice?',
         [('a', 'Prices, terms and needs all change over time'), ('b', 'Because decisions are illegal'), ('c', 'Because it is never possible to change'), ('d', 'Because the first choice is always right')], 'a'),
    ],
}
