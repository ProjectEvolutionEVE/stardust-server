"""Instrument Quality Assurance and Maintenance Logs: daily checks, control charts, calibration logs, service records, failure trends and quality audits."""
CODE = "science5_lab_instrument_qa"
BOOK = {
    "title": "Instrument Quality Assurance and Maintenance Logs",
    "subtitle": "Catching instrument problems early, with records anyone can read",
    "chapters": [
        ("Why check instruments",
         "Every result depends on the instrument that produced it. A drifting or faulty machine can quietly spoil weeks of work. Regular checks catch problems before they reach the data."),
        ("Daily checks",
         "A daily check is a short routine run at the start of each day, using a known standard. It shows whether the instrument is performing as expected. Record the outcome, even when it passes."),
        ("Control charts",
         "A control chart plots a check result over time, with limits that show normal variation. A point outside the limits, or a run of points on one side, signals a problem. Charts show trends that single results can hide."),
        ("Calibration logs",
         "A calibration log records each calibration: the date, the standards used, the results and who did it. Calibration sets the instrument's readings against known values. A clear log shows the instrument was reliable when a result was made."),
        ("Service records",
         "Service records note each repair, service visit and part replaced. They show how the instrument has been looked after. Good records help decide when to replace an aging machine."),
        ("Failure trends and quality audits",
         "Failure trends show which faults recur, and how often. A quality audit is an independent check that routines are followed and records are complete. Use audit findings to improve the routines, not just to tick boxes."),
    ],
    "test": [
        ("What is a daily check on an instrument?",
         [("a", "A short routine using a known standard to show the instrument is performing as expected"), ("b", "A check of the lab's staff rota"), ("c", "A check of the car park"), ("d", "A review of the sponsor's budget")], "a"),
        ("What does a control chart show?",
         [("a", "The number of journals"), ("b", "A check result over time, with limits showing normal variation"), ("c", "The lab's opening hours"), ("d", "The temperature outside")], "b"),
        ("What does a calibration log record?",
         [("a", "The price of coffee"), ("b", "The names of visitors"), ("c", "The date, the standards used, the results and who did it"), ("d", "The colour of the walls")], "c"),
        ("What do service records note?",
         [("a", "Each repair, service visit and part replaced"), ("b", "Each lunch break"), ("c", "Each visitor's shoe size"), ("d", "Each journal's cover price")], "a"),
        ("What is a quality audit?",
         [("a", "A tax return"), ("b", "A party for the staff"), ("c", "A loan application"), ("d", "A check by an independent person that routines are followed and records are complete")], "d"),
    ],
}
