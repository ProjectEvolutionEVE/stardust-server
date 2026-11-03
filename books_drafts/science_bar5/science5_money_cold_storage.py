"""Cold Storage and Facility Running Costs: keeping samples frozen safely, and what it really costs to run a cold store over time."""
CODE = "science5_money_cold_storage"
BOOK = {
    "title": "Cold Storage and Facility Running Costs",
    "subtitle": "Freezer energy, backup power, monitoring, maintenance contracts, storage planning and cost per sample stored",
    "chapters": [
        ("Freezer energy", "A freezer must keep samples at a low temperature all day and night, so it uses power constantly. Energy is often the largest running cost of cold storage. Newer, well-maintained freezers use less power for the same job."),
        ("Backup power", "Backup power keeps freezers running during a mains power cut. Without it, samples can warm and be lost in hours. The cost of a backup system is small compared with the value of the samples it protects."),
        ("Monitoring", "Continuous temperature monitoring alerts staff when a freezer drifts out of range. It catches a fault early, before samples are lost. Alarms should reach someone who can act at any hour."),
        ("Maintenance contracts", "A maintenance contract covers scheduled servicing and repairs of equipment for an agreed price. It spreads the cost of upkeep and reduces surprise breakdowns. Read the terms to see what is and is not included."),
        ("Storage planning", "Storage planning matches the space and the freezers to the samples held and the length of time they are kept. Clear plans prevent overcrowding and wasted energy. Regular reviews remove samples that no longer need to be kept."),
        ("Cost per sample stored", "Cost per sample stored is the total storage cost divided by the number of samples held over a period. It allows fair comparisons between storage options. The figure depends heavily on how full the freezers are kept."),
    ],
    "test": [
        ("What is the largest running cost of most freezers?",
         [("a", "Paint for the walls"), ("b", "Keeping samples at a low temperature continuously, which uses power all the time"), ("c", "The door handles"), ("d", "The sample labels")], "b"),
        ("What does backup power do for cold storage?",
         [("a", "Keeps the lights on at parties"), ("b", "Adds to the electricity bill"), ("c", "Keeps freezers running during a mains power cut"), ("d", "Heats the room")], "c"),
        ("Why monitor freezer temperature continuously?",
         [("a", "To catch a fault early, before samples are lost"), ("b", "To make the reports longer"), ("c", "To count the stock on the shelves"), ("d", "To heat the freezer")], "a"),
        ("What does a maintenance contract cover?",
         [("a", "Staff lunches"), ("b", "Staff holidays"), ("c", "Paint for the building"), ("d", "Scheduled servicing and repairs of equipment for an agreed price")], "d"),
        ("What is cost per sample stored?",
         [("a", "The price of one sample"), ("b", "The weight of one sample"), ("c", "The total storage cost divided by the number of samples held over a period"), ("d", "The cost of a flight to a conference")], "c"),
    ],
}
