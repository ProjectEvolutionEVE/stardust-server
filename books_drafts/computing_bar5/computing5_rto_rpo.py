"""Recovery Time and Recovery Point Objectives: tolerable downtime, data loss windows, design choices, testing, costs and agreement with the business."""
CODE = 'computing5_rto_rpo'
BOOK = {
    "title": 'Recovery Time and Recovery Point Objectives',
    "subtitle": 'How long you can be down, and how much you can afford to lose',
    "chapters": [
        ('Two questions',
         'When a system fails, two questions matter. How long can the service stay down? And how much recent data can be lost? The first is the recovery time objective, or RTO. The second is the recovery point objective, or RPO.'),
        ('Tolerable downtime',
         'The RTO is the longest outage the business can accept before serious harm follows. A shop checkout may need minutes; an archive may tolerate days. Setting the figure is a business decision, not only a technical one.'),
        ('Data loss windows',
         'The RPO measures how far back in time the recovered data may be. If backups run once a day, a failure can lose up to a day of work. A shorter RPO usually needs more frequent copying of data.'),
        ('Design choices',
         'Lower targets cost more. Options include keeping a standby copy in another place, copying data continuously, or writing a clear runbook so that people can restore service quickly. Each choice trades money for speed and safety.'),
        ('Testing the plan',
         'A recovery plan that has never been tried is a guess. Teams rehearse restores on a schedule and measure the time they actually take. The rehearsal often finds gaps that no document revealed.'),
        ('Agreement with the business',
         'The targets should be written down and agreed with the people who own the service and the costs. When the business and the technical team share one understanding, spending goes where it is needed, and no one is surprised in a crisis.'),
    ],
    "test": [
        ('What does the recovery time objective (RTO) measure?',
         [('a', 'The longest outage the business can accept'), ('b', 'The number of backup copies'), ('c', 'The speed of the network cable'), ('d', 'How many staff are on call')], 'a'),
        ('What does the recovery point objective (RPO) measure?',
         [('a', 'The colour of the backup disks'), ('b', 'How far back in time recovered data may be'), ('c', 'The cost of the office'), ('d', 'The size of the screen')], 'b'),
        ('If backups run once a day, how much work might one failure lose?',
         [('a', 'Nothing at all, ever'), ('b', 'Up to about a day of work'), ('c', 'Only the work of one minute'), ('d', 'Exactly one hour of work')], 'b'),
        ('Why is a recovery plan that has never been tested a risk?',
         [('a', 'Tests always cost more than disasters'), ('b', 'It is only a guess until it has been rehearsed'), ('c', 'Plans must be kept secret'), ('d', 'Restores never take any time')], 'b'),
        ('Who should agree the recovery targets?',
         [('a', 'Only the people who design the logo'), ('b', 'No one; they are chosen by chance'), ('c', 'The people who own the service and the costs, with the technical team'), ('d', 'Only the newest member of staff')], 'c'),
    ],
}
