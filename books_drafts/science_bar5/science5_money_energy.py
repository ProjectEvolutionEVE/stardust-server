"""Energy Costs and Efficiency in Laboratories: where lab energy goes, how to measure it and which upgrades pay back."""
CODE = "science5_money_energy"
BOOK = {
    "title": "Energy Costs and Efficiency in Laboratories",
    "subtitle": "Energy audits, fume hood loads, equipment standby, efficiency upgrades, payback periods and metering",
    "chapters": [
        ("Energy audits", "An energy audit is a survey of how a building uses energy, to find where savings are possible. It looks at heating, cooling, lighting, ventilation and equipment. The audit gives a list of changes ranked by cost and benefit."),
        ("Fume hoods", "Fume hoods draw large volumes of air out of the lab to keep people safe. That air must be heated or cooled, which makes hoods one of the largest energy loads in a lab. Closing sashes when hoods are not in use saves energy and keeps the air safer."),
        ("Equipment standby", "Standby load is the power drawn by equipment that is switched on but idle. Many instruments and computers keep drawing power overnight and at weekends. Switching off or using sleep modes can reduce this waste."),
        ("Efficiency upgrades", "Efficiency upgrades replace old equipment or systems with models that use less energy for the same work. Examples include efficient freezers, LED lighting and better controls. Each upgrade should be judged by its full cost and savings."),
        ("Payback periods", "A payback period is the time for savings to repay the cost of an upgrade. Short payback periods make an upgrade attractive. Payback should be checked against the expected life of the equipment."),
        ("Metering", "Metering measures how much energy each part of a building or each piece of equipment uses. It shows where the energy goes and whether savings are real. Without meters, savings are hard to prove."),
    ],
    "test": [
        ("What is an energy audit?",
         [("a", "A check of tax returns"), ("b", "A financial audit of the accounts only"), ("c", "A review of staff performance"), ("d", "A survey of how a building uses energy, to find where savings are possible")], "d"),
        ("Why do fume hoods use so much energy?",
         [("a", "They move large volumes of air, which must be heated or cooled"), ("b", "They run on coal"), ("c", "They have no motor at all"), ("d", "They emit light")], "a"),
        ("What is standby load?",
         [("a", "A stand for lab coats"), ("b", "A shelf for spare parts"), ("c", "Power drawn by equipment left on but idle"), ("d", "A safety rule for the lab")], "c"),
        ("What is a payback period?",
         [("a", "The time needed to repay a credit card bill"), ("b", "The time a machine sits idle"), ("c", "A type of holiday"), ("d", "The time for savings to repay the cost of an upgrade")], "d"),
        ("Why meter energy use?",
         [("a", "So you can see where the energy goes and check that savings are real"), ("b", "To hide the bills"), ("c", "Because meters are never useful"), ("d", "To predict the weather")], "a"),
    ],
}
