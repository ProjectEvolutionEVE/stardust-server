"""The Cash Flow Statement: where the actual money came from and where it went, which profit alone cannot show."""
CODE = 'flight5_m_cashflow_stmt'
BOOK = {
    'title': 'The Cash Flow Statement',
    'subtitle': 'Where the money really came from and went',
    'chapters': [
        ('Cash is not profit', 'A business can show a profit and still run out of cash. Profit counts sales when they are made, not when the money arrives. The cash flow statement follows the real money.'),
        ('Operating cash flow', 'Operating cash flow is the cash from the day-to-day business: customers paying in, suppliers and wages paid out. A business that does not earn cash from its work is in trouble.'),
        ('Investing cash flow', 'Investing cash flow covers money spent on long-term items, such as craft and equipment, and money received from selling them. Heavy spending here is normal for a growing business.'),
        ('Financing cash flow', 'Financing cash flow covers money from loans and owners, and money paid back in loan repayments and dividends. It shows how the business is funded.'),
        ('Free cash flow', 'Free cash flow is operating cash flow minus the spending needed to keep the business running. It is the cash left to repay debt, pay owners or grow. Many lenders watch it closely.'),
        ('Warning signs', 'Watch for a business that keeps borrowing to pay running costs, or whose operating cash flow is negative for a long time. Profit that never turns into cash is a warning sign.'),
    ],
    'test': [
        ('Why can a business show a profit and still run out of cash?', [('a', 'Profit counts sales when made, not when the money arrives'), ('b', 'Profit is always cash'), ('c', 'Cash is never needed'), ('d', 'Profit is measured in paint')], 'a'),
        ('What is operating cash flow?', [('a', 'Cash in a locked box'), ('b', 'Cash from the sale of the family ship'), ('c', 'Cash from the day-to-day business'), ('d', 'Cash given to charity')], 'c'),
        ('What does investing cash flow cover?', [('a', 'Daily snacks'), ('b', 'Long-term items such as craft and equipment'), ('c', 'Gifts for the crew'), ('d', 'Fees for a parking space')], 'b'),
        ('What is free cash flow?', [('a', 'Cash given away for nothing'), ('b', 'The total of all bills'), ('c', 'The price of a sale'), ('d', 'Operating cash flow minus the spending needed to keep the business running')], 'd'),
        ('What is a warning sign on this statement?', [('a', 'Steady cash from customers'), ('b', 'Loan repayments made on time'), ('c', 'Borrowing to pay running costs for a long time'), ('d', 'Cash that grows each year')], 'c'),
    ],
}
