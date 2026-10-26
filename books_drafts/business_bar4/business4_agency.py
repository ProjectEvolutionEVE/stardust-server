"""The Principal-Agent Problem: owners and managers, misaligned goals, the cost of monitoring, incentive design, stock options, and the limits of contracts."""
CODE = 'business4_agency'
BOOK = {
    "title": 'The Principal-Agent Problem',
    "subtitle": 'When the person acting for you has different goals',
    "chapters": [
        ('Owners and managers',
         'In a large firm, owners (the principals) hire managers (the agents) to run the business day to day. The owners want the firm to be worth more. The managers may want a comfortable job, a larger team or an easier life. This gap is the core of the principal-agent problem.'),
        ('Misaligned goals',
         "When an agent's goals differ from the principal's, the agent may take actions that help the agent more than the owner. A manager might choose safer projects, spend on perks, or avoid hard decisions that would benefit shareholders in the long run."),
        ('The cost of monitoring',
         'Owners can watch their agents, but watching costs time and money. Reports, audits and meetings all take resources. The owner must decide how much monitoring is worth paying for, given how much could go wrong without it.'),
        ('Incentive design',
         'One answer is to tie pay to results the owner cares about, such as profit, sales or share price. The reward should match the outcome the owner wants. A poorly designed bonus can push agents to chase the measured number, even when that harms the business.'),
        ('Stock options',
         "Giving managers shares or options in the firm links their pay to the share price. This can align their interests with owners' interests, though it can also encourage short-term moves that lift the price now and harm the firm later. Options work best when they vest over several years."),
        ('The limits of contracts',
         'No contract can cover every situation, and written terms are never complete. Some goals are hard to measure, and some useful actions cannot be specified in advance. Good firms combine clear incentives, honest monitoring and a culture where agents want the firm to do well.'),
    ],
    "test": [
        ('In the principal-agent problem, who are the principals in a large firm?',
         [('a', 'The managers who run the firm'), ('b', 'The owners who hire the managers'), ('c', 'The customers'), ('d', 'The tax office')], 'b'),
        ('What creates the principal-agent problem?',
         [('a', 'Owning too much cash'), ('b', 'Using the same currency everywhere'), ('c', 'Goals that differ between the owner and the person acting for them'), ('d', 'Having a small team')], 'c'),
        ('Why is monitoring an agent costly?',
         [('a', 'Because it is always illegal'), ('b', 'Because agents never write reports'), ('c', 'Because owners cannot read'), ('d', 'Because it uses time and money')], 'd'),
        ('What is the main purpose of incentive design?',
         [('a', "To match the agent's reward to the outcome the owner wants"), ('b', "To lower every manager's pay"), ('c', 'To end all meetings'), ('d', 'To stop the firm from earning profit')], 'a'),
        ('Why can stock options encourage short-term moves?',
         [('a', 'Because they pay out only on the day they are granted'), ('b', 'Because they reward a quick lift in the share price'), ('c', 'Because they are banned by law'), ('d', 'Because they are paid in cash only')], 'b'),
    ],
}
