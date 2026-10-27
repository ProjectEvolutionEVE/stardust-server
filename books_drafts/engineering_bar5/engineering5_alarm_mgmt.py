"""Alarm Floods and Alarm Management: alarm rationalisation, floods, priorities, nuisance alarms and performance metrics."""
CODE = "engineering5_alarm_mgmt"
BOOK = {
    "title": "Alarm Floods and Alarm Management",
    "subtitle": "Making alarms useful instead of overwhelming",
    "chapters": [
        ("What an alarm is for",
         "An alarm tells an operator that something needs attention. A good alarm is rare, clear and leads to a useful action. A bad alarm is one the operator learns to ignore."),
        ("Alarm rationalisation",
         "Rationalisation checks each alarm for a clear reason, a clear action and a fitting priority. Alarms that fail this check are changed, merged or removed. The work is done alarm by alarm, with the people who run the plant."),
        ("Alarm floods",
         "An alarm flood is a period when operators receive far more alarms than they can handle. Floods often follow a single fault that sets off many linked alarms. During a flood, the operator may miss the most important alarm."),
        ("Priorities",
         "Alarm priority shows operators which alarms need the quickest response. Only the most urgent alarms should get the highest priority. If everything is urgent, nothing is."),
        ("Nuisance alarms",
         "A nuisance alarm goes off often without needing any action. Nuisance alarms teach operators to ignore alarms, which is dangerous. Engineers find them from the alarm log and fix the cause or the setting."),
        ("Performance metrics",
         "Alarm systems are measured with simple figures, such as the number of alarms per operator per period and the share of time spent in floods. Standards such as ISA-18.2 set out how to manage alarms and what to measure. Regular review keeps the system healthy."),
    ],
    "test": [
        ("What is alarm rationalisation?",
         [("a", "Checking each alarm for a clear reason, action and priority"), ("b", "Painting alarms"), ("c", "Turning alarms off"), ("d", "Counting bells")], "a"),
        ("What is an alarm flood?",
         [("a", "A leak in a pipe"), ("b", "A rainy day"), ("c", "A period when operators receive far more alarms than they can handle"), ("d", "A paint spill")], "c"),
        ("What is a nuisance alarm?",
         [("a", "A loud horn"), ("b", "An alarm that goes off often without needing action"), ("c", "A safety shutdown"), ("d", "A paint code")], "b"),
        ("What is alarm priority used for?",
         [("a", "Choosing the paint"), ("b", "Setting the lunch order"), ("c", "Setting the lights"), ("d", "Showing operators which alarms need the quickest response")], "d"),
        ("Which standard covers alarm management in process plants?",
         [("a", "ISA-18.2"), ("b", "ISO 9001"), ("c", "ISO 14001"), ("d", "ISO 27001")], "a"),
    ],
}
