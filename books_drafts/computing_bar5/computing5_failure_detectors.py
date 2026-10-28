"""Failure Detector Theory: deciding a machine may be down, when you can never be certain."""
CODE = 'computing5_failure_detectors'
BOOK = {
    "title": 'Failure Detector Theory',
    "subtitle": 'Deciding a machine may be down, when you can never be certain',
    "chapters": [
        ('Suspicion without certainty', 'A machine that stops answering may have crashed, or may just be slow or cut off. A failure detector gives a judgement of suspicion, not a fact. Because of this, it will sometimes be wrong.'),
        ('Completeness and accuracy', 'Chandra and Toueg described failure detectors with two promises. Completeness means every crashed machine is eventually suspected. Accuracy means healthy machines are not suspected, at least for a while. Different classes of detectors give different mixes of the two.'),
        ('Phi accrual detection', 'The phi accrual detector, from Hayashibara and colleagues, gives a level of suspicion as a number rather than a yes or no. It learns the usual gaps between heartbeats, and the level rises as a late heartbeat becomes less likely. Systems set a threshold for action.'),
        ('Partial synchrony', 'Failure detectors can be made correct under partial synchrony, where delays are unknown but eventually bounded. Under that assumption, the detector can eventually stop making mistakes about healthy machines. It is a useful and realistic model.'),
        ('False positives', 'A false positive is a healthy machine wrongly suspected, which can trigger an unnecessary failover. Such errors cost time and sometimes data safety. Designers must treat false alarms as a normal part of the system.'),
        ('Tuning', 'Timeouts and thresholds control the trade-off. Short timeouts find crashes fast but cause more false alarms. Long timeouts are calmer but slow to react. Teams tune these settings using their own network behaviour.'),
    ],
    "test": [
        ('What does a failure detector give?',
         [('a', 'A paint job'), ('b', 'A bill'), ('c', 'A guaranteed diagnosis'), ('d', 'A judgement of suspicion, not certain fact')], 'd'),
        ('What does completeness promise?',
         [('a', 'Every crashed machine is eventually suspected'), ('b', 'No machine is ever suspected'), ('c', 'Machines never crash'), ('d', 'Messages are never lost')], 'a'),
        ('What does the phi accrual detector output?',
         [('a', 'A colour'), ('b', 'A password'), ('c', 'A tune'), ('d', 'A level of suspicion as a number')], 'd'),
        ('What is a false positive?',
         [('a', 'A correct alarm'), ('b', 'A healthy machine wrongly suspected'), ('c', 'A broken machine not noticed'), ('d', 'A perfect network')], 'b'),
        ('What does a short timeout do?',
         [('a', 'Finds crashes fast but causes more false alarms'), ('b', 'Stops all crashes'), ('c', 'Makes the network faster'), ('d', 'Removes the need for tuning')], 'a'),
    ],
}
