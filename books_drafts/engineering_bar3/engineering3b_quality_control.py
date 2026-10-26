"""Quality control: sampling, defect rates and control charts, for checking parts and spotting when a process drifts."""
CODE = 'engineering3b_quality_control'
BOOK = {
    "title": 'Quality Control: Sampling and Control Charts',
    "subtitle": 'Checking parts without checking every one forever, and spotting when a process starts to drift',
    "chapters": [
        ('Why check at all',
         'Quality control finds parts that do not meet the drawing before they reach a customer or a ship. Every defect costs something: the material, the time, and the cost of scrap or rework. Checking early is much cheaper than fixing or replacing a part later.'),
        ('Check all, or sample',
         'Checking every part is called 100 per cent inspection. It catches every defect, but it takes time. For large batches, sampling checks a set number of parts and accepts or rejects the whole batch by the result. Use full checks for safety-critical parts and sampling for the rest.'),
        ('Defects and defect rate',
         'A defect is a flaw that makes a part fail its drawing. The defect rate is the number of defective parts divided by the number checked, often given per hundred or per million. A low rate in a big run can still mean many bad parts, so count them.'),
        ('Average and spread',
         'Two numbers tell you a lot about a process. The average shows where the process sits, and the spread shows how far the parts vary around it. A process can have the right average and still be too spread out to fit.'),
        ('Control charts',
         'A control chart plots measurements in order over time, with a centre line at the average and limits set about three standard deviations either side. Points inside the limits are normal variation. A point beyond a limit, or a long run of points rising or falling together, warns that something has changed.'),
        ('Act on the signal',
         'When a chart warns, stop and find the cause before making more parts. Worn tools, a new batch of material and a changed setting are common causes. Write down what you found and what you changed, so the next check starts from a clear record.'),
    ],
    "test": [
        ('What is 100 per cent inspection?',
         [('a', 'Checking one part in a hundred'), ('b', 'Checking no parts at all'), ('c', 'Checking only the first part of a batch'), ('d', 'Checking every part')], 'd'),
        ('What is the defect rate?',
         [('a', 'The weight of the defects'), ('b', 'Defective parts divided by the number checked'), ('c', 'The price of each part'), ('d', 'The number of workers on shift')], 'b'),
        ('What do the limits on a control chart show?',
         [('a', 'The normal range of variation for the process'), ('b', 'The price the parts may sell for'), ('c', 'The number of workers allowed'), ('d', 'The height of the chart paper')], 'a'),
        ('What does the spread of a process tell you?',
         [('a', 'The colour of the parts'), ('b', 'The price of the materials'), ('c', 'How far the parts vary around the average'), ('d', 'How many workers are on shift')], 'c'),
        ('What should you do when a control chart gives a warning?',
         [('a', 'Ignore it if the parts look fine'), ('b', 'Stop and find the cause before making more parts'), ('c', 'Make more parts quickly'), ('d', 'Change the drawing')], 'b'),
    ],
}
