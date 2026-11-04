"""Capital Budgeting for a Survey Fleet: vessel purchase, utilisation, lifetime costs, financing, sensitivity and timing."""
CODE = 'navigation5_survey_fleet_capex'
BOOK = {
    "title": 'Capital Budgeting for a Survey Fleet',
    "subtitle": 'Deciding whether, when and how to buy a survey vessel',
    "chapters": [
        ('Vessel purchase',
         'The purchase price is only the start. Crew, fuel, insurance, repairs and dry-docking all follow the purchase. A sound budget counts every one of them, not just the first cheque.'),
        ('Utilisation',
         'A vessel that sits idle earns nothing and still costs money. Plan how many days a year it will work, and check that the plan is realistic. Utilisation often decides whether a purchase pays.'),
        ('Lifetime costs',
         'Add up all the costs over the vessel working life. Compare that total with the expected earnings or the value of the work it will do. This gives a fair picture of the whole investment.'),
        ('Financing',
         'Buying, leasing and sharing a vessel each carry different costs and risks. Compare them on the same basis, including interest, obligations and what happens at the end of the term.'),
        ('Sensitivity',
         'Test how the result changes if use or costs turn out differently. If a small change in use wipes out the gain, the decision is fragile, and the risk should be stated clearly.'),
        ('Timing',
         'A good time to buy can matter as much as the choice of vessel. Prices, demand and availability all change. Consider when the purchase should happen, not only whether it should.'),
    ],
    "test": [
        ('Why is the purchase price only the start of a vessel budget?',
         [('a', 'Vessels are free after purchase'), ('b', 'Crew, fuel and repairs follow over the working life'), ('c', 'Purchase prices are never really paid'), ('d', 'The price already includes the weather')], 'b'),
        ('Why does utilisation matter?',
         [('a', 'A vessel that sits idle earns nothing'), ('b', 'Idle vessels always earn more'), ('c', 'Use has no effect on cost'), ('d', 'Only the paint matters')], 'a'),
        ('What should a lifetime cost analysis do?',
         [('a', 'Count only the first year'), ('b', 'Ignore repairs'), ('c', 'Add up all the costs over the working life'), ('d', 'Count the crew hobbies')], 'c'),
        ('What is sensitivity analysis used for in fleet budgeting?',
         [('a', 'Choosing the colour of the hull'), ('b', 'Setting staff holidays'), ('c', 'Naming the vessel'), ('d', 'Testing how the result changes when use or costs change')], 'd'),
        ('What can the timing of a vessel purchase affect?',
         [('a', 'The cost and value of the investment'), ('b', 'The name of the vessel'), ('c', 'The language of the manual'), ('d', 'Nothing at all')], 'a'),
    ],
}
