"""Compound Interest in Depth: the rule of 72, how often interest is added, long runs, and how debt compounds against you."""
CODE = "flight5_m_compound"
BOOK = {
    "title": "Compound Interest in Depth",
    "subtitle": "The rule of 72, how often it adds up, and how debt grows too",
    "chapters": [
        ("Interest on interest",
         "Compound interest is interest paid on the money you saved and on the interest it already earned. Each period, the base grows a little, so the next gain is a little larger. Simple interest pays only on the original sum."),
        ("The rule of 72",
         "To estimate how long money takes to double, divide 72 by the yearly rate. At 6% a year, money doubles in about 12 years. It is a quick estimate, not an exact sum, but it is useful for comparing choices."),
        ("How often it is added",
         "Interest may be added yearly, monthly or daily. The more often it is added, the faster the balance grows, though the difference is small at low rates. Always compare the yearly rate, called the annual percentage yield, when choosing an account."),
        ("Long runs",
         "Most of the growth in a long saving plan arrives late. The final years of a 40-year plan can add more than all the early years together. This is why time is the saver's strongest tool."),
        ("Debt works the same way",
         "Interest on a loan compounds too, but it works against the borrower. An unpaid card balance can grow quickly when interest is added to it. Paying debt off early stops that growth."),
        ("Using it well",
         "Start early, keep costs low and avoid high-cost debt that compounds against you. Check how often interest is added before you open any account or take any loan."),
    ],
    "test": [
        ("What is compound interest?",
         [("a", "Interest paid only on the first sum saved"), ("b", "A fee paid to a bank"), ("c", "Interest paid on both the original sum and the interest already earned"), ("d", "A tax on savings")], "c"),
        ("Using the rule of 72, about how long does money take to double at 6% a year?",
         [("a", "About 6 years"), ("b", "About 12 years"), ("c", "About 72 years"), ("d", "About 36 years")], "b"),
        ("Why does a higher yearly rate help a saver?",
         [("a", "It shortens the year"), ("b", "It lowers taxes"), ("c", "It removes risk"), ("d", "It makes the balance grow faster from one period to the next")], "d"),
        ("How does compound interest work against a borrower?",
         [("a", "The debt shrinks each month"), ("b", "Loans never carry interest"), ("c", "Interest is added to the debt, so the balance can grow"), ("d", "It has no effect")], "c"),
        ("Why is paying off debt early useful?",
         [("a", "It keeps the interest from growing on the balance"), ("b", "It doubles the debt"), ("c", "It stops all taxes"), ("d", "It removes the need for savings")], "a"),
    ],
}
