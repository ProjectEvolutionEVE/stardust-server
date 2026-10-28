"""Cost indices and escalation: index construction, inflation, contract clauses, forecasts, benchmarks and sensitivity."""
CODE = 'mining5_cost_index'
BOOK = {
    'title': 'Cost Indices and Escalation',
    'subtitle': 'Allowing for prices that rise and fall over a long project',
    "chapters": [
        ('Costs change', 'The prices of fuel, steel, labour and power change over time. A long project must allow for this.'),
        ('Building an index', 'A cost index tracks the price of a basket of goods and services against a base year. A value of 100 in the base year is a common starting point.'),
        ('Inflation', 'Inflation is a general rise in prices. Escalation is the part of a cost change that a contract adjusts for.'),
        ('Contract clauses', 'Escalation clauses let a price rise or fall with an index. Both sides share the risk of price change this way.'),
        ('Forecasts and benchmarks', 'Cost forecasts are checked against benchmarks from similar projects. A forecast far from the benchmarks needs a reason.'),
        ('Sensitivity', 'Sensitivity analysis asks how much the project changes when one cost moves. It shows which costs matter most.'),
    ],
    "test": [
        ('What does a cost index track?', [('a', 'The number of workers each year'), ('b', 'The price of a basket of goods and services against a base year'), ('c', 'The height of the headframe'), ('d', 'The weight of the ore')], 'b'),
        ('What is inflation?', [('a', 'A fall in the price of one item'), ('b', 'A new kind of drill'), ('c', 'A general rise in prices'), ('d', 'A change in the shift pattern')], 'c'),
        ('What do escalation clauses do?', [('a', 'Fix the price forever'), ('b', 'Cancel the contract'), ('c', 'Pay the workers twice'), ('d', 'Adjust a price with an index so both sides share the risk')], 'd'),
        ('What are cost forecasts checked against?', [('a', 'Benchmarks from similar projects'), ('b', 'The weather on the day'), ('c', 'The colour of the office walls'), ('d', 'Guesses from the canteen')], 'a'),
        ('What does sensitivity analysis ask?', [('a', 'Who the project manager is'), ('b', 'How many pens are in stock'), ('c', 'How much the project changes when one cost moves'), ('d', 'Which shirt the crew prefers')], 'c'),
    ],
}
