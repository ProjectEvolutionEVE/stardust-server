"""Costs of Aircraft Navigation Databases: subscriptions, update cycles, database errors, fleet costs, vendor choice and contracts."""
CODE = "navigation4_aircraft_nav_db"
BOOK = {
    "title": "Costs of Aircraft Navigation Databases",
    "subtitle": "What it costs to keep an aircraft's navigation data current and correct",
    "chapters": [
        ("Subscriptions", "Aircraft navigation databases are usually supplied under a subscription. The subscription gives access to each new release. A missed release can leave an aircraft with out-of-date data."),
        ("Update cycles", "Navigation data changes on a fixed cycle. The AIRAC cycle runs every 28 days. Each cycle brings a new database that must be loaded before its effective date."),
        ("Database errors", "A database error can give a wrong waypoint or a wrong runway. Operators check the data against official sources. Errors are reported and corrected quickly."),
        ("Fleet costs", "An operator with many aircraft pays for each one. Costs grow with the size of the fleet. Managing updates across the whole fleet needs careful planning."),
        ("Vendor choice", "Operators choose a data vendor. The choice depends on quality, support and price. A vendor who is slow to correct errors is a real risk."),
        ("Contracts", "The contract sets the terms, the price and what happens if the data is wrong. Read the contract with care. Clear terms protect both sides."),
    ],
    "test": [
        ("How often does the AIRAC cycle run?", [("a", "Every hour"), ("b", "Every 100 days"), ("c", "Every 7 years"), ("d", "Every 28 days")], "d"),
        ("What is a risk of missing a database release?", [("a", "The aircraft becomes lighter"), ("b", "The paint fades"), ("c", "The aircraft may have out-of-date data"), ("d", "The flight is free")], "c"),
        ("What might a database error give?", [("a", "A wrong waypoint or runway"), ("b", "A better view"), ("c", "A new colour"), ("d", "A free meal")], "a"),
        ("What does a fleet operator's cost depend on?", [("a", "The colour of the seats"), ("b", "The weather in London"), ("c", "The size of the fleet"), ("d", "The name of the pilot")], "c"),
        ("What should a contract set out?", [("a", "Only the colour"), ("b", "The terms, the price and what happens if data is wrong"), ("c", "Nothing at all"), ("d", "The lunch menu")], "b"),
    ],
}
