"""Break-Even in Units (Manager, bar 3, part A): fixed costs, what each unit earns, and how many you must sell to cover them."""
CODE = "business3a_breakeven_units"
BOOK = {
    "title": "Break-Even in Units",
    "subtitle": "Fixed costs, what each unit earns, and how many you must sell to cover them",
    "chapters": [
        ("Two kinds of cost",
         "Fixed costs stay the same whether you sell a little or a lot, such as the rent on a plant or a loan payment. Variable costs rise with each unit you make or sell, such as materials. Break-even analysis works with the two kinds of cost separately."),
        ("What each unit contributes",
         "Each unit sold brings in its price. Take away the variable cost of that unit, and what is left is its contribution. The contribution goes first toward paying the fixed costs. Once they are covered, each further unit adds its contribution to profit."),
        ("The break-even formula",
         "Break-even units equal the fixed costs divided by the contribution per unit. The answer is the number of units that covers every cost, and no more. Sell that many, and you have made neither a profit nor a loss."),
        ("A worked example",
         "Suppose fixed costs are 1,200 credits a week, each unit sells for 20 and costs 14 to make. The contribution is 6 per unit, so the break-even is 1,200 divided by 6: 200 units a week. Sell 201, and you have made 6 credits more than the costs."),
        ("Why it helps",
         "Break-even shows how much you must sell before any profit appears. If that number is far above what you can realistically sell, the plan needs a lower fixed cost, a higher price or a lower variable cost before it can work."),
        ("The limits",
         "The calculation assumes that the price and the variable cost per unit stay the same. Real prices move, so run the sum again whenever they do. Break-even is a planning tool, not a promise of what will sell."),
    ],
    "test": [
        ("Which cost stays the same whatever the number of units sold?",
         [("a", "A fixed cost, such as rent or a loan payment"), ("b", "Materials for each unit"), ("c", "Packaging for each unit"), ("d", "The price of one unit")], "a"),
        ("A unit sells for 20 and costs 14 to make. What is its contribution?",
         [("a", "34 credits"), ("b", "14 credits"), ("c", "6 credits"), ("d", "20 credits")], "c"),
        ("Fixed costs are 1,200 credits a week and each unit contributes 6. How many units break even?",
         [("a", "6 units"), ("b", "120 units"), ("c", "1,206 units"), ("d", "200 units")], "d"),
        ("Why does the contribution go first toward the fixed costs?",
         [("a", "Because fixed costs are optional"), ("b", "Because fixed costs must be paid whatever you sell"), ("c", "Because the Bank sets the price"), ("d", "Because the market sets fixed costs each day")], "b"),
        ("What is the main limit of a break-even calculation?",
         [("a", "It assumes price and variable cost stay the same, so it must be rerun when they change"), ("b", "It never works for a plan with fixed costs"), ("c", "It counts profit before costs"), ("d", "It only applies to loans")], "a"),
    ],
}
