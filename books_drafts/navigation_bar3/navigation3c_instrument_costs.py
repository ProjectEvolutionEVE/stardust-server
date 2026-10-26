"""Navigation Instruments and Their Costs: what each instrument costs to buy, keep and replace, and how to choose the right one for the job."""
CODE = "navigation3c_instrument_costs"
BOOK = {
    "title": "Navigation Instruments and Their Costs",
    "subtitle": "What each instrument costs to buy, keep and replace, and how to choose the right one for the job",
    "chapters": [
        ("Every instrument has a price",
         "A navigation instrument costs money in three places: buying it, keeping it working, and replacing it when it wears out or fails. A cheap instrument can cost more over its life than a dearer one, if it needs frequent repair or checks."),
        ("Accuracy costs",
         "Better accuracy usually costs more. A sensor that is twice as precise may need better parts, more calibration and more care. Ask whether the extra accuracy will change a decision. If it will not, a cheaper instrument may be the right choice."),
        ("Spares and backups",
         "A backup instrument adds cost, but it can save a voyage. A craft with one sensor has no safety net, while two or three sensors cost more and give a way out when one fails. Weigh the price of a spare against the cost of losing the sensor."),
        ("Power and weight",
         "Every instrument uses power and adds mass. Power comes from a limited supply, and mass costs fuel to move. Choose instruments for the job, not for the features on the box."),
        ("Budgeting for navigation",
         "Plan a yearly budget for navigation that covers purchase, checks, spare parts and training. Keep a reserve for the unexpected. An instrument that is never checked is a cost that will arrive later, usually at the worst time."),
        ("Owning or leasing",
         "Some craft are leased rather than owned, with instruments included in a regular price. Compare the total cost over the time you will really use the craft, not the price of one period. A lease can be cheaper for a short job and dearer for a long one."),
    ],
    "test": [
        ("Where does a navigation instrument cost money?",
         [("a", "Only when it is first bought"), ("b", "Only when it is switched on"), ("c", "In buying it, keeping it working and replacing it"), ("d", "Only in the hold")], "c"),
        ("Why might a cheap instrument cost more overall?",
         [("a", "It cannot be used at all"), ("b", "It never needs checking"), ("c", "It is always the best choice"), ("d", "It may need frequent repair and checks, which add up")], "d"),
        ("When is extra accuracy worth paying for?",
         [("a", "Always, whatever the cost"), ("b", "When it changes a decision that matters"), ("c", "Never"), ("d", "Only on a Sunday")], "b"),
        ("Why is a backup instrument sometimes worth its cost?",
         [("a", "It gives a way out if the main sensor fails"), ("b", "It replaces the crew"), ("c", "It makes the hull shine"), ("d", "It cancels fuel costs")], "a"),
        ("What is a sensible part of a navigation budget?",
         [("a", "Buying as many instruments as possible"), ("b", "Keeping nothing in reserve"), ("c", "Saving for checks, spares and unexpected repairs"), ("d", "Ignoring costs until something fails")], "c"),
    ],
}
