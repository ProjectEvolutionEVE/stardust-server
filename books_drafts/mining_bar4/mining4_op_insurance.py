"""Insurance for Mine Operations: what insurance covers at a mine, and how much risk a miner chooses to keep."""
CODE = 'mining4_op_insurance'
BOOK = {
    "title": 'Insurance for Mine Operations',
    "subtitle": 'What cover protects, and how much risk to keep',
    "chapters": [
        ('Property cover',
         'Property cover pays to repair or replace buildings, plant and equipment damaged by an insured event, such as fire or flood. It protects the physical assets of the mine.'),
        ('Business interruption',
         'If a mine stops because of an insured event, business interruption cover pays the income lost while it is shut. This keeps the loan payments and wages covered during the stop.'),
        ('Premiums',
         'The premium is the regular price paid for insurance. It depends on the risk of the site, its history and the level of cover. Safer operations usually pay less.'),
        ('Deductibles',
         'A deductible is the amount the insured pays on each claim before the insurer pays. A higher deductible lowers the premium, but it means more money is needed on hand when something goes wrong.'),
        ('Claims',
         "Making a claim means reporting the loss quickly, showing the damage and the cost, and working with the insurer's assessor. Good records make a claim faster and smoother."),
        ('Risk retention',
         'Some miners keep part of their risk themselves rather than insure it. This is called risk retention, and it suits small, predictable losses. Large or rare losses are usually insured.'),
    ],
    "test": [
        ('What does property cover pay for?',
         [('a', "The owner's holiday"), ('b', 'New clothes for the staff'), ('c', 'Repair or replacement of buildings and equipment damaged by an insured event'), ('d', 'Advertising')], 'c'),
        ('What does business interruption cover pay?',
         [('a', 'Income lost while the mine is shut by an insured event'), ('b', 'The cost of a new car'), ('c', 'Tea and biscuits'), ('d', 'A gift for the town')], 'a'),
        ('What is a deductible?',
         [('a', 'A bonus paid to the insurer'), ('b', 'A type of drill'), ('c', 'The cost of a map'), ('d', 'The amount the insured pays on each claim before the insurer pays')], 'd'),
        ('What is risk retention?',
         [('a', 'Losing all records'), ('b', 'Keeping part of a risk yourself rather than insuring it'), ('c', 'Buying the insurance company'), ('d', 'Forgetting the risk')], 'b'),
        ('Why keep good records when making a claim?',
         [('a', 'They make the claim void'), ('b', 'They stop the mine from working'), ('c', 'They make the claim faster and smoother'), ('d', 'They change the weather')], 'c'),
    ],
}
