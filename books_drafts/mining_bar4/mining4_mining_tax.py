"""Depreciation and Mining Tax Allowances: how spreading the cost of equipment and resources changes the tax bill."""
CODE = 'mining4_mining_tax'
BOOK = {
    "title": 'Depreciation and Mining Tax Allowances',
    "subtitle": 'Spreading the cost of equipment and resources over time',
    "chapters": [
        ('Straight-line depreciation',
         "Straight-line depreciation spreads an asset's cost in equal amounts over its useful life. A machine costing 100,000 over ten years is written down by 10,000 each year."),
        ('Declining balance',
         'Declining balance depreciation takes a larger share in the early years and less later. It gives a bigger deduction when the asset is new, which can help cash flow in the first years.'),
        ('Tax losses',
         'When a mine loses money in a year, the loss can often be carried forward to reduce tax in later profitable years. The rules differ by country, so local advice is needed.'),
        ('Depletion allowances',
         'A depletion allowance recognises that a mineral deposit is used up as it is mined. It lets the owner deduct part of the value of the resource as it leaves the ground.'),
        ('Tax timing',
         'When a deduction is taken matters as much as its size. An earlier deduction lowers tax sooner, which frees cash, while a later one spreads the benefit out.'),
        ('After-tax cash flow',
         'After-tax cash flow is the cash left once tax is paid. Planners look at this number, not the profit on paper, when they judge whether a mine is worth building.'),
    ],
    "test": [
        ('What does straight-line depreciation do?',
         [('a', 'Makes the asset free'), ('b', 'Sells the asset for scrap at once'), ('c', 'Spreads the cost of an asset in equal amounts over its life'), ('d', 'Ignores the asset completely')], 'c'),
        ('Why does declining balance help cash flow in early years?',
         [('a', 'It gives a bigger deduction when the asset is new'), ('b', 'It delays all deductions to the end'), ('c', 'It removes tax for ever'), ('d', 'It doubles the price of the asset')], 'a'),
        ('What is a depletion allowance?',
         [('a', 'A payment for lost keys'), ('b', 'A fee for parking'), ('c', 'A grant for paint'), ('d', 'A deduction for the value of a resource used up as it is mined')], 'd'),
        ('What does tax timing change?',
         [('a', 'The colour of the tax form'), ('b', 'When tax is lowered, which affects cash, not only its size'), ('c', 'The number of staff'), ('d', 'The height of the mine')], 'b'),
        ('What is after-tax cash flow?',
         [('a', 'The profit shown on paper before tax'), ('b', 'The price of a machine'), ('c', 'The cash left once tax is paid'), ('d', 'The number of payments due')], 'c'),
    ],
}
