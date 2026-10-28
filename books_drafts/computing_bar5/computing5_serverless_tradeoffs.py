"""Serverless Architecture Trade-offs: functions as units, cold starts, per-request pricing, state, vendor coupling and observability."""
CODE = 'computing5_serverless_tradeoffs'
BOOK = {
    "title": 'Serverless Architecture Trade-offs',
    "subtitle": 'Functions as units, and what the convenience costs',
    "chapters": [
        ('What serverless means',
         'In a serverless design the cloud provider runs the machines, and the team deploys small functions that run when something calls them. The team does not manage the operating systems or the capacity for those functions. The name is misleading, because servers still exist; they are simply hidden from the people who write the code.'),
        ('Cold starts',
         'A function that has been idle may need time to start up the next time it is called. This delay is called a cold start. It can add noticeable waiting for a user, so teams measure it and sometimes keep a few copies running.'),
        ('Paying per request',
         'Serverless billing usually charges for each request and for the time a function runs. This suits uneven or light traffic, because nothing is charged while the system is idle. At steady, very high volume the same work can cost more than a dedicated server would.'),
        ('State and design limits',
         'Functions are usually short-lived and do not keep memory between calls. Any lasting data must live in an outside store such as a database or cache. Designs that assume local files or long sessions need rethinking.'),
        ('Vendor coupling',
         'Each provider has its own triggers, limits and service interfaces. The more a system depends on those details, the harder it is to move to another provider. Many teams keep the business rules in plain code and isolate the provider-specific parts.'),
        ('Observability',
         'Many small functions make it harder to follow one request from start to finish. Tracing, structured logs and a shared request ID restore that view. Without them, finding a fault becomes guesswork.'),
    ],
    "test": [
        ('What does the cloud provider take care of in a serverless design?',
         [('a', 'Writing the business rules for the team'), ('b', 'Running the machines beneath the functions'), ('c', 'Choosing the name of the product'), ('d', 'Approving every release by hand')], 'b'),
        ('What is a cold start?',
         [('a', 'A server that has been switched off for good'), ('b', 'A delay when an idle function must start up again'), ('c', 'A failed login attempt'), ('d', 'A cheap way to store files')], 'b'),
        ('Why can per-request billing be a poor fit for steady, very high traffic?',
         [('a', 'Providers never charge for requests'), ('b', 'Each request is free after the first one'), ('c', 'The same work can cost more than a dedicated server'), ('d', 'It only works in one country')], 'c'),
        ('Where should a serverless function keep data that must last between calls?',
         [('a', 'In its own memory only'), ('b', 'In an outside store such as a database'), ('c', 'On the user\'s web browser alone'), ('d', 'Nowhere, since the data is not needed')], 'b'),
        ('What helps a team follow one request across many small functions?',
         [('a', 'Tracing and a shared request ID'), ('b', 'Turning the logs off'), ('c', 'Making every function much larger'), ('d', 'Removing all monitoring')], 'a'),
    ],
}
