"""Valuing a Business by Discounted Cash Flow: what a company's future cash is worth today."""
CODE = "business4_dcf"
BOOK = {
    "title": "Valuing a Business by Discounted Cash Flow",
    "subtitle": "What a company's future cash is worth today",
    "chapters": [
        ("Cash, not profit",
         "Discounted cash flow values a business by the cash it will generate for its owners over time. Accounting profit can differ from cash, because of depreciation, timing and investment. Cash is what pays the owners in the end."),
        ("Forecast the cash",
         "Begin with a forecast of free cash flow for several years, usually five to ten. Free cash flow is the cash left after running costs and the investment needed to keep and grow the business. The forecast is often the largest source of error, so it needs care."),
        ("Choose a rate",
         "Future cash is discounted at a rate that reflects risk, often the company's cost of capital. A riskier business gets a higher rate, so its future cash is worth less today."),
        ("The terminal value",
         "A business is expected to last beyond the forecast years. The terminal value estimates all the cash after that point, often using a steady long-run growth rate. It is often the largest part of the total, so its assumptions matter a great deal."),
        ("Add and discount",
         "Discount each year's forecast cash, and the terminal value, back to today's money. Add them together to get the estimated value of the business. Then subtract debt and add cash to reach the value for the owners."),
        ("Sensitivity and a sanity check",
         "Small changes in the rate or the growth rate can move the answer a lot. Test a range of guesses and see how far the value moves. Compare the result with what similar businesses sell for, as a check on the model."),
    ],
    "test": [
        ("What does discounted cash flow value?",
         [("a", "The paint on the building"), ("b", "The cash a business will generate over time, in today's money"), ("c", "The number of staff"), ("d", "The share price last year")], "b"),
        ("What is free cash flow?",
         [("a", "Cash left after running costs and needed investment"), ("b", "Any money a bank lends"), ("c", "Only the profit on paper"), ("d", "The total of all debts")], "a"),
        ("Why is the terminal value important?",
         [("a", "It is always zero"), ("b", "It is often the largest part of the total value"), ("c", "It counts only last year's cash"), ("d", "It is the tax rate")], "b"),
        ("Why is a riskier business discounted at a higher rate?",
         [("a", "It removes debt"), ("b", "Riskier firms pay no tax"), ("c", "It lowers the forecast"), ("d", "Its future cash is discounted more heavily, so it is worth less today")], "d"),
        ("What should you do after adding the discounted values?",
         [("a", "Ignore debt"), ("b", "Double the total"), ("c", "Subtract debt and add cash to reach the value for the owners"), ("d", "Divide by the number of staff")], "c"),
    ],
}
