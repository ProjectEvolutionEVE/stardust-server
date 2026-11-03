"""Robust Estimation with M-Estimators: how to keep one bad measurement from spoiling the whole answer."""
CODE = 'navigation5_robust_m'
BOOK = {
    "title": 'Robust Estimation with M-Estimators',
    "subtitle": 'Outliers, the Huber loss, weights, breakdown points, trade-offs and practice',
    "chapters": [
        ('When bad data appears',
         'Real measurements sometimes include wild values, such as a reflection that makes a range reading far too long. A few such outliers can pull a simple average far off course. Robust methods are built to hold steady when that happens.'),
        ('The Huber loss',
         'The Huber loss treats small errors as squared errors and large errors as straight-line errors. Small errors are still counted carefully. Large errors grow only slowly, so one bad value cannot take over the answer.'),
        ('Weights',
         'A robust estimator gives each measurement a weight. Points that fit the model well get a high weight, and points far off get a low one. The weights are recalculated as the estimate improves.'),
        ('Breakdown points',
         'The breakdown point is the share of bad data an estimate can take before it can be pushed anywhere at all. The plain mean has a breakdown point of zero, since one bad value can ruin it. The median can handle up to half the data being bad.'),
        ('Trade-offs',
         'Robust methods give up a little accuracy when the data is clean. In return they stay sensible when it is not. Choosing the threshold is a balance between the two.'),
        ('Putting it into practice',
         'Plot your residuals and look for clusters of large errors. Set the threshold from your sensor\'s known noise. Then compare the robust answer with the plain one to see what the outliers were doing.'),
    ],
    "test": [
        ('What is an outlier?',
         [('a', 'A measurement that fits the model exactly'), ('b', 'The most common value in the data'), ('c', 'A measurement far from where the rest of the data points'), ('d', 'A measurement taken with a clock')], 'c'),
        ('What is the main idea of the Huber loss?',
         [('a', 'It treats large errors more gently than squared errors'), ('b', 'It counts every error the same way'), ('c', 'It removes all noise from a signal'), ('d', 'It sets the time of each measurement')], 'a'),
        ('Which estimator has a breakdown point of zero?',
         [('a', 'The median'), ('b', 'The Huber estimate'), ('c', 'The robust weighted fit'), ('d', 'The plain mean')], 'd'),
        ('What does a weight do in a robust estimator?',
         [('a', 'It sets the colour of each point'), ('b', 'It sets how much a measurement counts'), ('c', 'It sets the time of the reading'), ('d', 'It names the sensor')], 'b'),
        ('What is the trade-off of robust methods?',
         [('a', 'They always fail with clean data'), ('b', 'They need no computer'), ('c', 'They may lose a little accuracy on clean data'), ('d', 'They ignore all data')], 'c'),
    ],
}
