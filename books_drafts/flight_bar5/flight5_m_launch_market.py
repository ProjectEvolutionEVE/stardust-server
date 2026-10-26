"""The Launch Market: providers, prices, contracts, rideshare missions, insurance and competition."""
CODE = "flight5_m_launch_market"
BOOK = {
    "title": "The Launch Market",
    "subtitle": "Who sends things to space, and at what price",
    "chapters": [
        ("Providers",
         "A launch provider is a company that sends payloads into orbit. Some are government agencies and some are private firms. Each has its own rockets, sites and customers, and each competes on price, reliability and schedule."),
        ("Prices",
         "Launch prices vary widely with rocket size, the orbit and how much is carried. Reusable rockets, which land and fly again, have lowered the price per launch for many customers. Prices are often quoted per mission, not per kilogram."),
        ("Contracts",
         "A launch contract sets the date, the orbit, the price, the penalties for delay and who insures the payload. Customers should read the terms closely. Schedules often slip, so contracts usually allow for delays."),
        ("Rideshare missions",
         "A rideshare mission carries several small satellites on one rocket. It lets small customers reach orbit for less than booking a whole launch. The schedule and orbit are set by the main customer, so small payloads must fit."),
        ("Insurance",
         "Launches are insured, because rockets can fail. The insurance cost depends on the rocket's record and the value of the payload. A failure can cost a lot, so the premium is a real part of the price."),
        ("Competition",
         "More providers and cheaper launches widen choice. Competition pushes prices down and encourages new designs. A market with few providers can leave customers with fewer options and higher prices."),
    ],
    "test": [
        ("What is a launch provider?",
         [("a", "A shop that sells rockets toys"), ("b", "A bank for satellites"), ("c", "A company or agency that sends payloads into orbit"), ("d", "A type of orbit")], "c"),
        ("What does a rideshare mission do?",
         [("a", "Carries one person to the Moon"), ("b", "Carries several small satellites on one rocket"), ("c", "Stops satellites from launching"), ("d", "Lands rockets on water only")], "b"),
        ("What do launch contracts usually set?",
         [("a", "The colour of the rocket"), ("b", "The menu for the crew"), ("c", "The name of the pilot's school"), ("d", "The date, the orbit, the price and the penalties for delay")], "d"),
        ("Why are launches insured?",
         [("a", "The law forbids launches without insurance for all payloads"), ("b", "Insurers launch rockets"), ("c", "Rockets can fail, and a failure can be very costly"), ("d", "Insurance pays for holidays")], "c"),
        ("What does more competition usually do to launch prices?",
         [("a", "It tends to push prices down"), ("b", "It always raises prices"), ("c", "It removes all choice"), ("d", "It has no effect")], "a"),
    ],
}
