"""The Dataflow Model: processing endless streams of data by event time, windows and triggers."""
CODE = 'computing5_dataflow_model'
BOOK = {
    "title": 'The Dataflow Model',
    "subtitle": 'Processing endless streams of data by event time, windows and triggers',
    "chapters": [
        ('Unbounded data', 'Many data sources never end: sensors, clicks and payments keep arriving. The dataflow model treats such data as an unbounded stream, and asks how to compute answers over it that stay correct as data keeps coming.'),
        ('Windows and triggers', 'A window groups events into a span of time, such as an hour. A trigger decides when to output the result for a window, possibly more than once. This gives early answers, and updates them as more data arrives.'),
        ('Event time versus processing time', 'Event time is when something happened; processing time is when the system handles it. The two can differ, because messages arrive late or out of order. The model lets programs work by event time, which gives more meaningful answers.'),
        ('Watermarks', 'A watermark is the system estimate of how far event time has progressed. Events older than the watermark are considered late. Watermarks are estimates, but they give the system a way to know when a window is probably complete.'),
        ('Late data', 'Late events do arrive sometimes. The model lets a program decide how long to wait, and whether to update a window answer when a late event comes in. Each choice trades speed against completeness.'),
        ('The Beam model', 'Google published the model in 2015, and it became the basis of Apache Beam, which lets one program run on several engines. The aim is to keep the meaning of a computation separate from the system that runs it.'),
    ],
    "test": [
        ('What is unbounded data?',
         [('a', 'Data in a box'), ('b', 'Data with no numbers'), ('c', 'Data that is empty'), ('d', 'Data that never ends as it keeps arriving')], 'd'),
        ('What does a window do?',
         [('a', 'Opens a house'), ('b', 'Groups events into a span of time'), ('c', 'Cleans the screen'), ('d', 'Counts users in a room')], 'b'),
        ('What does a trigger decide?',
         [('a', 'The colour of the chart'), ('b', 'The price of a server'), ('c', 'When to output a window result, possibly more than once'), ('d', 'Who the user is')], 'c'),
        ('What is event time?',
         [('a', 'When something happened'), ('b', 'The time the printer is off'), ('c', 'Lunch time'), ('d', 'The clock on the wall')], 'a'),
        ('What is a watermark?',
         [('a', 'The system estimate of how far event time has progressed'), ('b', 'A stain on paper'), ('c', 'A brand logo'), ('d', 'A kind of pen')], 'a'),
    ],
}
