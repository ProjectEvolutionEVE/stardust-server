"""Cloud Data Transfer Economics: why moving data out of a cloud costs money, and how to plan for it."""
CODE = "computing5_cloud_egress"
BOOK = {
    "title": "Cloud Data Transfer Economics",
    "subtitle": "What data transfer costs, and how design choices change the bill",
    "chapters": [
        ("Egress pricing",
         "Egress means data leaving a cloud provider's network, sent to a user or to another company. Many providers charge for each gigabyte that leaves, and they usually do not charge for data coming in. Egress can become a large share of a cloud bill."),
        ("Inter-region fees",
         "Regions are separate data-centre areas run by a provider. Moving data between regions often carries its own charge, even when both ends belong to the same company. Keep data and the services that use it in the same region where that makes sense."),
        ("Caching to save transfer",
         "A cache keeps a copy of data closer to the people who use it. When a copy is served from the cache, less data crosses the paid link. Caching is useful for content that is read often and changes rarely."),
        ("Architecture choices",
         "Design choices change how much data moves. Sending only the changed part of a file costs less than sending the whole file again. Placing compute close to its data also reduces transfer."),
        ("Measuring transfer",
         "Measure where data really goes before making changes. Billing reports and traffic logs show which services and which destinations use the most. Good numbers prevent effort being spent on the wrong fix."),
        ("Forecasts",
         "A forecast of transfer costs should follow expected use, not just the current bill. Growth in users or features raises transfer in step with it. Update the forecast when plans change, and compare it with the real bill each month."),
    ],
    "test": [
        ("What does egress mean in cloud pricing?",
         [("a", "Data entering the network only"), ("b", "Data leaving a provider's network"), ("c", "The cost of storing files"), ("d", "The price of electricity")], "b"),
        ("How can caching reduce data transfer costs?",
         [("a", "It sends the same data again every time"), ("b", "It deletes data that is still needed"), ("c", "It doubles the size of the bill"), ("d", "It keeps copies closer to users so less data crosses paid links")], "d"),
        ("What is an inter-region fee?",
         [("a", "A charge for moving data between regions of a provider"), ("b", "A discount for staff"), ("c", "A sign-up bonus"), ("d", "A tax on screens")], "a"),
        ("Why measure data transfer before forecasting it?",
         [("a", "To avoid paying at all"), ("b", "To remove the logs"), ("c", "To base forecasts on real usage rather than guesses"), ("d", "To stop users from connecting")], "c"),
        ("Which is a good first step to reduce egress costs?",
         [("a", "Delete all backups"), ("b", "Find which data moves most and why"), ("c", "Turn off all monitoring"), ("d", "Move everything to paper records")], "b"),
    ],
}
