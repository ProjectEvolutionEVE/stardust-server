"""Project Finance and Loan Terms: how lenders size a loan for a mine or plant, and the promises that come with it."""
CODE = 'mining4_project_finance'
BOOK = {
    "title": 'Project Finance and Loan Terms',
    "subtitle": 'How lenders size a loan, and the promises it carries',
    "chapters": [
        ('Lenders and covenants',
         'Lenders lend to a project on the strength of its cash flow. Covenants are promises the borrower makes, such as keeping certain financial ratios or not taking on other debt without consent.'),
        ('Debt sizing',
         "Lenders size the loan so the project's expected cash can cover the repayments with some margin to spare. A project with steady, reliable income can carry more debt."),
        ('Repayment schedules',
         'A repayment schedule sets the amount and date of each payment over the life of the loan. Regular payments make the cash plan predictable for the borrower and the lender.'),
        ('Debt service cover',
         'The debt service cover ratio divides the cash available by the payments due in a period. A ratio above one means the project can pay its debt from its own cash.'),
        ('Default',
         'Default is failing to meet a payment or a covenant. It can trigger penalties, a demand for early repayment or a change in who controls the project. Lenders try to prevent it early.'),
        ('Refinancing',
         'Refinancing replaces an old loan with a new one, often to get a lower rate or longer terms. It can ease the repayments, but it also brings new costs and conditions to agree.'),
    ],
    "test": [
        ('What is a covenant in a loan?',
         [('a', 'A type of ore'), ('b', 'A pair of gloves'), ('c', 'A promise the borrower makes, such as keeping certain ratios'), ('d', 'A map of the town')], 'c'),
        ('How do lenders size a project loan?',
         [('a', 'So the expected cash can cover repayments with some margin'), ('b', 'By the size of the logo'), ('c', 'By the colour of the office'), ('d', 'By the number of cups of tea')], 'a'),
        ('What does a repayment schedule set?',
         [('a', 'The shape of the mine gate'), ('b', 'The name of the mine'), ('c', 'The number of bolts'), ('d', "The amount and date of each payment over the loan's life")], 'd'),
        ('What does a debt service cover ratio above one mean?',
         [('a', 'The project has no debt at all'), ('b', 'The project can pay its debt from its own cash'), ('c', 'The project will close tomorrow'), ('d', 'The project is painted green')], 'b'),
        ('What is refinancing?',
         [('a', 'Melting down old coins'), ('b', 'Cleaning a furnace'), ('c', 'Replacing an old loan with a new one, often on different terms'), ('d', 'Selling the staff uniforms')], 'c'),
    ],
}
