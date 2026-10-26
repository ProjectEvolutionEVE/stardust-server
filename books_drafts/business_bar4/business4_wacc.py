"""The Cost of Capital: the blended return a business must earn."""
CODE = "business4_wacc"
BOOK = {
    "title": "The Cost of Capital",
    "subtitle": "The blended return a business must earn",
    "chapters": [
        ("Why capital has a cost",
         "Money has a cost, even when it is your own. Lenders want interest, and owners want a return for taking risk. A business must earn at least the blended return its funders expect, or it destroys value."),
        ("Cost of debt",
         "The cost of debt is the interest rate the firm pays on new borrowing, after any tax deduction on interest. It is usually lower than the cost of equity, because lenders are paid first if the firm fails."),
        ("Cost of equity",
         "The cost of equity is the return owners expect for the risk of holding the shares. It is harder to measure. Models such as CAPM are often used to estimate it. It is usually higher than the cost of debt."),
        ("The weights",
         "The weights are the shares of debt and equity in total funding, measured at market values. More debt puts more weight on the cheaper source. But more debt also raises the risk, and so raises the cost of equity."),
        ("The blended rate",
         "The weighted average cost of capital blends the two costs by their weights. A firm funded 40% by debt at 4% after tax, and 60% by equity at 10%, has a blended rate of 1.6 plus 6, which is 7.6%."),
        ("Hurdle rates",
         "A project's expected return is compared with the blended cost, often called a hurdle rate. Projects that beat the hurdle add value. Projects that fall short take value away, even if they make a profit."),
    ],
    "test": [
        ("Why must a business earn at least its cost of capital?",
         [("a", "To pay no tax"), ("b", "To avoid losing value for its funders"), ("c", "To avoid all risk"), ("d", "To borrow more")], "b"),
        ("Why is the cost of debt usually lower than the cost of equity?",
         [("a", "Lenders are paid first if the firm fails"), ("b", "Debt has no risk"), ("c", "Equity is free"), ("d", "Interest is never paid")], "a"),
        ("What are the weights in the cost of capital?",
         [("a", "The mass of the factory"), ("b", "The staff numbers"), ("c", "The age of the company"), ("d", "The shares of debt and equity in total funding, at market values")], "d"),
        ("A firm is 40% debt at 4% after tax and 60% equity at 10%. What is the blended rate?",
         [("a", "6%"), ("b", "14%"), ("c", "7.6%"), ("d", "10%")], "c"),
        ("What is a hurdle rate?",
         [("a", "The rate a project must beat to add value"), ("b", "A tax on loans"), ("c", "The rate paid to staff"), ("d", "A type of share")], "a"),
    ],
}
