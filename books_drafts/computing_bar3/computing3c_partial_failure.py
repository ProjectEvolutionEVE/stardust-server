"""When Part of the System Fails: timeouts, retries, and not knowing whether the work was done."""
CODE = "computing3c_partial_failure"
BOOK = {
    "title": "When Part of the System Fails",
    "subtitle": "Timeouts, retries and not knowing whether the work was done",
    "chapters": [
        ("Two machines, one network",
         "When two machines talk over a network, messages can be lost, delayed or arrive twice. A machine can be perfectly healthy and still look silent. Part of a system can fail while the rest carries on."),
        ("The silent reply",
         "When a request gets no reply, the sender cannot tell what happened. The message may never have arrived, the other side may have crashed, or it may have done the work and lost its reply on the way back. The honest answer is unknown, not no."),
        ("Timeouts",
         "A timeout is how long a sender waits before it gives up. A timeout that is too short gives up on work that was going well. A timeout that is too long leaves the user waiting. Pick a time that fits the job, and show a clear message when it runs out."),
        ("Retries",
         "A common answer is to try again. A retry helps when the first message was lost. But if the first try did the work, a retry may do it a second time, so retries need care. Limit how many times you retry."),
        ("Backing off",
         "Waiting a little longer before each retry, called exponential backoff, stops a crowd of retries from flooding a system that is already struggling. Adding a little random variation helps too, so that many senders do not retry at the same instant."),
        ("Plan for the unknown",
         "Assume that any call might fail after doing its work. Design the next step so the system stays correct when that happens. Good planners expect partial failure rather than hoping it will not happen."),
    ],
    "test": [
        ("Why can a sender not tell what happened when no reply comes?",
         [("a", "Because replies are never sent"), ("b", "Because the message may be lost, or the other side may have done the work and its reply was lost"), ("c", "Because networks print messages"), ("d", "Because timeouts are always right")], "b"),
        ("What is a timeout?",
         [("a", "A break for lunch"), ("b", "A kind of cable"), ("c", "A rule for money"), ("d", "The longest time a sender waits before it gives up")], "d"),
        ("Why can a retry cause trouble?",
         [("a", "It always makes the system faster"), ("b", "It stops replies from being sent"), ("c", "It may do the same work twice if the first try had worked"), ("d", "It uses no network at all")], "c"),
        ("What is exponential backoff?",
         [("a", "Waiting a longer time between each retry"), ("b", "Trying faster each time"), ("c", "Sending every retry at once"), ("d", "Turning off the network")], "a"),
        ("What is the safest assumption about a call that failed?",
         [("a", "It did nothing at all, always"), ("b", "It may have done its work, so the next step must still be correct"), ("c", "It was never sent"), ("d", "It was sent twice on purpose")], "b"),
    ],
}
