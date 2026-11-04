"""Net Present Value of a Satellite Constellation: capital costs, launch and operations, revenue streams, discount rates, risk and the decision rule."""
CODE = "navigation5_constellation_npv"
BOOK = {
    "title": "Net Present Value of a Satellite Constellation",
    "subtitle": "Deciding whether a fleet of satellites is worth building",
    "chapters": [
        ("Capital costs",
         "A constellation needs large spending up front on satellites, ground stations and launches. These costs come before any revenue arrives. Estimating them carefully matters a great deal."),
        ("Launch and operations",
         "Launch costs are significant, and operations need ground control and staff for many years. These running costs continue through the life of the satellites. Operations are part of the total cost."),
        ("Revenue streams",
         "Revenue may come from selling services, data, subscriptions or fees. Each stream has its own timing and its own risk. Revenue forecasts are often uncertain."),
        ("Discount rates",
         "Net present value discounts future cash flows, because money now is worth more than the same money later. The discount rate reflects the time value of money and the risk. A higher rate lowers the present value of distant cash."),
        ("Risk",
         "Satellites can fail and launches can go wrong, so risk affects value. Risk can be reflected in the cash flows or in the discount rate. Analysts test how sensitive the result is to the key assumptions."),
        ("The decision rule",
         "A project with a positive net present value adds value at the chosen discount rate. A project with a negative value usually should not go ahead on financial grounds alone. The rule is simple, but its inputs need care."),
    ],
    "test": [
        ("What comes first for a constellation?",
         [("a", "Revenue"), ("b", "Large spending up front"), ("c", "Rest"), ("d", "Fees")], "b"),
        ("Which costs continue through the life of the satellites?",
         [("a", "None"), ("b", "Only the paint"), ("c", "Operations and ground staff"), ("d", "Only the launch")], "c"),
        ("Which of these is one revenue stream?",
         [("a", "Rain"), ("b", "Rocks"), ("c", "Wind"), ("d", "Subscriptions or data fees")], "d"),
        ("What does a higher discount rate do?",
         [("a", "Raises the value of distant cash"), ("b", "Lowers the present value of distant cash"), ("c", "Doubles revenue"), ("d", "Removes risk")], "b"),
        ("What is the decision rule?",
         [("a", "Accept a project with a positive net present value"), ("b", "Accept any project"), ("c", "Reject all projects"), ("d", "Toss a coin")], "a"),
    ],
}
