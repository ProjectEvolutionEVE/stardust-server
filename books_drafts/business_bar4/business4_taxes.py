"""How Income Tax Works: marginal and average rates, brackets and planning."""
CODE = "business4_taxes"
BOOK = {
    "title": "How Income Tax Works",
    "subtitle": "Marginal and average rates, brackets and planning",
    "chapters": [
        ("Income and tax",
         "Most countries tax income in some form, and the system is set by law. Income tax is paid on earnings after allowances. Knowing the rules helps you plan, and the rules differ from country to country."),
        ("Marginal against average",
         "The marginal rate is the rate paid on the next unit of income. The average rate is the total tax divided by total income. Because brackets rise, the average rate is usually lower than the top marginal rate."),
        ("Brackets",
         "In a bracket system, income is taxed in slices, and each slice has its own rate. Earning more does not push all of your income into a higher rate. Only the part that falls within the higher slice is taxed at that higher rate."),
        ("Deductions and credits",
         "A deduction reduces taxable income. A credit reduces the tax bill itself, by its full amount. So a deduction is worth less than the same amount as a credit, because its value depends on your rate."),
        ("Withholding and capital gains",
         "Employers often withhold tax from wages before they are paid. Gains from selling assets, such as shares, may be taxed as capital gains, often at different rates. The rules on timing and on losses matter."),
        ("Tax planning without tricks",
         "Use the allowances and reliefs the law provides, keep good records, and plan the timing where the rules allow. Avoid schemes that promise too much. Tax rules change, so check current official guidance, and seek a qualified adviser for your own situation."),
    ],
    "test": [
        ("What is the marginal tax rate?",
         [("a", "The rate on the next unit of income"), ("b", "The average of all rates"), ("c", "The rate on savings only"), ("d", "The bank's rate")], "a"),
        ("In a bracket system, what happens when you earn more?",
         [("a", "All income moves to the higher rate"), ("b", "Tax falls"), ("c", "Only the part in the higher slice is taxed at that rate"), ("d", "Tax is paid in advance only")], "c"),
        ("What does a tax credit do?",
         [("a", "Reduces taxable income"), ("b", "Adds to income"), ("c", "Sets the bracket"), ("d", "Reduces the tax bill directly by its amount")], "d"),
        ("What is withholding?",
         [("a", "Tax taken by the employer from wages before they are paid"), ("b", "A tax refund"), ("c", "A type of loan"), ("d", "A tax on gifts")], "a"),
        ("What is the best approach to tax planning, according to this chapter?",
         [("a", "Use the allowances and reliefs the law provides, and keep records"), ("b", "Join any scheme that promises a lot"), ("c", "Hide income"), ("d", "Never file")], "a"),
    ],
}
