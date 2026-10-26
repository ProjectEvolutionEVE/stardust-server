"""Internal Rate of Return: the rate at which a project's value reaches zero."""
CODE = "business4_irr"
BOOK = {
    "title": "Internal Rate of Return",
    "subtitle": "The rate at which a project's value reaches zero",
    "chapters": [
        ("The rate that balances",
         "The internal rate of return is the discount rate at which a project's net present value equals zero. Put another way, it is the return the project earns on the money tied up in it. Managers find it easy to understand."),
        ("Calculating it",
         "For most projects there is no simple formula. The rate is found by trial: try a rate, compute the net present value, adjust, and repeat. Spreadsheets do this quickly."),
        ("Comparing with NPV",
         "Net present value gives a sum of value in money. IRR gives a percentage. For a single project with ordinary cash flows, the two usually agree on whether to accept it. For choosing between projects, the sum of value is usually the better guide."),
        ("Multiple answers",
         "A project whose cash flows change sign more than once can have more than one IRR. Then the figure is hard to read. In such cases, net present value at a stated rate is more reliable."),
        ("Mutually exclusive projects",
         "When only one of several projects can be chosen, a higher IRR does not always mean more value. A smaller project with a high IRR may add less total value than a larger project with a lower IRR. Compare the net present values."),
        ("The modified version",
         "The modified internal rate of return assumes that cash received is reinvested at a stated rate, often the cost of capital. This fixes some of the problems of the standard measure. It is still a percentage, so check the size of the project too."),
    ],
    "test": [
        ("What is the internal rate of return?",
         [("a", "The rate at which net present value equals zero"), ("b", "The tax rate"), ("c", "The interest on a bank account"), ("d", "The price of a share")], "a"),
        ("What can happen when cash flows change sign more than once?",
         [("a", "The project has no cash"), ("b", "The project can have more than one IRR"), ("c", "The IRR is always zero"), ("d", "The project becomes a bond")], "b"),
        ("Why might a higher IRR not be better for mutually exclusive projects?",
         [("a", "IRR is measured in dollars"), ("b", "IRR leaves out taxes"), ("c", "IRR cannot be calculated"), ("d", "A small project with a high IRR may add less total value")], "d"),
        ("What does net present value give?",
         [("a", "A percentage"), ("b", "A date"), ("c", "A sum of value in money"), ("d", "A list of staff")], "c"),
        ("What does the modified IRR assume about cash received?",
         [("a", "It is spent at once"), ("b", "It is reinvested at a stated rate"), ("c", "It is lost"), ("d", "It is hidden")], "b"),
    ],
}
