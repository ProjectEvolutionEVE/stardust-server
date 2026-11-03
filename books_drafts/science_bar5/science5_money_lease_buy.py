"""Leasing Versus Buying Scientific Instruments: comparing the total cost of each option and when each one makes sense."""
CODE = "science5_money_lease_buy"
BOOK = {
    "title": "Leasing Versus Buying Scientific Instruments",
    "subtitle": "Lease terms, total cost comparison, residual values, utilisation break-even, service and decision rules",
    "chapters": [
        ("What a lease is", "A lease is a contract to use equipment for a set period, in exchange for regular payments. At the end, the equipment may be returned, renewed or bought. Buying means paying the full price up front or by loan, and owning the equipment outright."),
        ("Total cost comparison", "A fair comparison adds up every cost of each option over the same period. That includes payments, interest, service, consumables, insurance and any end payments. Comparing only the monthly figure can give the wrong answer."),
        ("Residual value", "Residual value is the estimated worth of an instrument at the end of its use. A purchase keeps some of that value, and a lease usually does not. The residual value affects which option is cheaper overall."),
        ("Utilisation break-even", "Utilisation break-even is the level of use at which owning or leasing costs the same as renting time or sending samples out. If the instrument will be used more than that level, owning often makes sense. If use is low, renting time is usually cheaper."),
        ("Service inclusion", "Some leases include service and repairs, and some do not. Repair and servicing can add large costs over an instrument's life. Checking exactly what is covered changes which option is cheaper."),
        ("Decision rules", "Set a rule before you compare: for example, lease equipment that changes quickly and buy equipment that stays useful for years. Write down the assumptions about use, lifetime and service. Then compare total costs, and revisit the decision when use changes."),
    ],
    "test": [
        ("What is a lease?",
         [("a", "A gift of equipment from a supplier"), ("b", "A permanent sale of equipment"), ("c", "A loan of cash for any purpose"), ("d", "A contract to use equipment for regular payments over a set time")], "d"),
        ("What is a total cost comparison?",
         [("a", "Adding up every cost, including service, over the same period, for each option"), ("b", "Comparing only the monthly payment"), ("c", "Comparing only the colour of each instrument"), ("d", "Ignoring interest and fees")], "a"),
        ("What is a residual value?",
         [("a", "The cost of cleaning an instrument"), ("b", "The food left in the staff room"), ("c", "The estimated worth of an instrument at the end of its use"), ("d", "A tax on scientific equipment")], "c"),
        ("What is a utilisation break-even point?",
         [("a", "The point at which the instrument is never used"), ("b", "The level of use at which owning or leasing costs the same as renting time or sending samples out"), ("c", "The day the lease begins"), ("d", "A test of the software")], "b"),
        ("Why check whether service is included?",
         [("a", "Because service is never needed"), ("b", "Because service is always free"), ("c", "Because repair and service costs can change which option is cheaper"), ("d", "Because it only matters for software")], "c"),
    ],
}
