"""Incident Response and Forensics: preparing responders, containment, evidence collection, timelines, log analysis, and lessons and reports."""
CODE = "computing4_incident_forensics"
BOOK = {
    "title": "Incident Response and Forensics",
    "subtitle": "Responding calmly to a security incident, and learning from it",
    "chapters": [
        ("Preparing responders",
         "Teams prepare before an incident happens. They write response plans, agree who does what, and make sure logs and contact lists are ready when they are needed."),
        ("Containment",
         "Containment limits the damage. Teams isolate affected systems, disable compromised accounts and block harmful traffic, while taking care to keep the evidence."),
        ("Evidence collection",
         "Collect copies of logs, disk images and memory where possible, in a way that leaves the originals unchanged. Keep a record of who collected what, and when."),
        ("Timelines",
         "A timeline puts the events in order, using logs and reports. It shows the team what happened and in what sequence."),
        ("Log analysis",
         "Logs from many sources must be lined up by time, and checked for gaps. Accurate clocks on every system matter for this."),
        ("Lessons and reports",
         "After the incident, a blameless review explains the cause, the response, and the changes that will prevent a repeat."),
    ],
    "test": [
        ("Why prepare responders in advance?",
         [("a", "To delay"), ("b", "For fun"), ("c", "So no one needs to respond"), ("d", "So roles, plans and logs are ready before an incident")], "d"),
        ("What does containment do?",
         [("a", "Deletes evidence"), ("b", "Ignores damage"), ("c", "Limits damage while keeping evidence"), ("d", "Sends emails to everyone")], "c"),
        ("What should evidence collection keep?",
         [("a", "Edited copies"), ("b", "Unchanged copies, with a record of who collected them"), ("c", "Nothing"), ("d", "Only screenshots of colours")], "b"),
        ("What is a timeline?",
         [("a", "Events placed in order, from logs and reports"), ("b", "A calendar of holidays"), ("c", "A ruler"), ("d", "A clock on the wall")], "a"),
        ("Why do accurate clocks matter?",
         [("a", "Clocks make coffee"), ("b", "Clocks are decorative"), ("c", "They keep the server cool"), ("d", "Logs from many sources must line up by time")], "d"),
    ],
}
