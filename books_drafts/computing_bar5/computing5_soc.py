"""Security operations centres: round-the-clock monitoring, triage tiers, playbooks, escalation, metrics and staffing."""
CODE = 'computing5_soc'
BOOK = {
    "title": 'Security Operations Centres',
    "subtitle": 'The teams that watch systems around the clock and respond to alerts',
    "chapters": [
        ('Watching all day and night',
         "A security operations centre, or SOC, watches an organisation's computers and networks around the clock. Its staff look at alerts from many tools and decide which ones matter."),
        ('Triage tiers',
         'Work is often split into tiers. The first tier sorts alerts and closes the ones that are false alarms. Higher tiers investigate harder cases and hunt for threats that have not triggered an alert yet.'),
        ('Playbooks',
         'A playbook is a written set of steps for a common type of alert, such as a suspicious login. Playbooks help new staff act the same way as experienced ones and keep response quick.'),
        ('Escalation',
         'When an alert looks serious, it moves up to a higher tier or to managers, who may bring in outside help or tell the people in charge. Clear rules say when to escalate.'),
        ('Measuring the work',
         'Two common measures are how long it takes to detect a problem and how long it takes to respond. Teams also track how many alerts are false, since too many false alarms wear people out.'),
        ('Staffing and outsourcing',
         'A round-the-clock team needs shifts and enough people to cover them. Many firms pay an outside company to run part or all of the SOC, which spreads the cost but still needs clear rules.'),
    ],
    "test": [
        ('How long does a SOC watch its systems?',
         [('a', 'Only during office hours'), ('b', 'Only on weekends'), ('c', 'Around the clock'), ('d', 'Once a year')], 'c'),
        ('What does the first tier usually do?',
         [('a', 'Design the building'), ('b', 'Sort alerts and close false alarms'), ('c', "Write the company's accounts"), ('d', 'Sell the software')], 'b'),
        ('What is a playbook?',
         [('a', 'A toy for training'), ('b', 'A written set of steps for a common type of alert'), ('c', 'A sales report'), ('d', 'A list of passwords')], 'b'),
        ('Why do teams track false alarms?',
         [('a', 'False alarms are free to handle'), ('b', 'False alarms are always the most serious'), ('c', 'False alarms help the printer'), ('d', 'Too many false alarms wear people out')], 'd'),
        ('What is escalation?',
         [('a', 'Turning the network off'), ('b', 'Lowering the lights'), ('c', 'Moving a serious alert up to higher tiers or managers'), ('d', 'Hiring a new building')], 'c'),
    ],
}
