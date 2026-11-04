"""Budgeting a Field Expedition: costing travel, equipment, permits, contingency and team welfare for a trip into the field."""
CODE = "science5_money_expedition"
BOOK = {
    "title": "Budgeting a Field Expedition",
    "subtitle": "Travel costs, equipment transport, permits, contingency, team welfare and logistics planning",
    "chapters": [
        ("Travel costs", "Travel costs include flights, ground transport, lodging and daily allowances for each team member. Costs can change with season, route and availability. Book early where possible, and check the fares against the plan."),
        ("Equipment transport", "Equipment transport means moving instruments and supplies to the field and back. It includes packing, freight, customs fees and insurance for valuable items. Heavy or fragile kit can add a large share of the cost."),
        ("Permits", "Permits are official permissions to work, collect samples or enter a protected area. They can take months to arrange and may carry fees. Build the permit timetable into the expedition plan from the start."),
        ("Contingency", "Contingency covers the cost of delays, breakdowns, weather and other unexpected events. Field work is hard to predict, so a contingency is an essential part of the budget. Explain clearly what it covers and how it was sized."),
        ("Team welfare", "Team welfare covers the basic health, safety, food and rest that people need in the field. It includes first aid, clean water, shelter and communication. Keeping the team well protects both people and the science."),
        ("Logistics planning", "Logistics planning puts the timetable, transport, supplies and communications into one plan. It names who does what, and what happens if a link fails. A written plan, shared with the team, prevents many costly problems."),
    ],
    "test": [
        ("What kinds of costs go into the travel part of an expedition budget?",
         [("a", "Only the cost of stamps"), ("b", "Only the cost of a sandwich"), ("c", "Flights, ground transport, lodging and daily allowances"), ("d", "Only the cost of paper clips")], "c"),
        ("What is equipment transport in a field budget?",
         [("a", "Carrying people from one city to another"), ("b", "Carrying a bus"), ("c", "Carrying food for guests"), ("d", "Moving instruments and supplies, including packing, freight and fees")], "d"),
        ("What are permits for field work?",
         [("a", "Official permissions to work or collect in a place"), ("b", "Passes to a theatre"), ("c", "Driving licences for the team"), ("d", "Membership cards for a gym")], "a"),
        ("Why include a contingency in an expedition budget?",
         [("a", "So that the team can spend more money"), ("b", "To cover unexpected costs such as delays or breakdowns"), ("c", "To hide the true size of the budget"), ("d", "Because it must always be zero")], "b"),
        ("What does team welfare cover on an expedition?",
         [("a", "Golf sessions"), ("b", "Expensive dinners"), ("c", "Basic health, safety, food and rest for the team in the field"), ("d", "Holiday travel after the trip")], "c"),
    ],
}
