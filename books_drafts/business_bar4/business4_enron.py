"""Enron: how a Houston energy firm hid its debts and fell, and what its collapse teaches about reading accounts."""
CODE = "business4_enron"
BOOK = {
    "title": "Enron and the Lessons of Its Fall",
    "subtitle": "Mark-to-market, hidden partnerships and a Houston energy firm that failed",
    "chapters": [
        ("From pipelines to trading",
         "Enron began as a natural gas company in Houston. Over time it became a trader of energy, and then of many other things. It grew quickly, and it was admired for its bold ideas about markets."),
        ("Mark-to-market accounting",
         "Under mark-to-market accounting, a firm can book the expected profit of a long contract as income today, using its own estimate of future prices. Used with care, the method can show a fair picture. Used loosely, it can show profit that has not arrived as cash and may never arrive."),
        ("Partnerships that hid debt",
         "Enron set up many partnerships, called special purpose entities, to hold certain assets and debts away from its main accounts. Some were run by Enron's own finance staff, which created clear conflicts of interest. Investors did not see how much of the risk still belonged to Enron."),
        ("The unravelling",
         "By late 2001, the true picture had come out. Lenders pulled back, investors lost trust, and Enron filed for bankruptcy in December 2001. Thousands of employees lost jobs, and many lost their savings, which were tied up in company stock."),
        ("The auditor",
         "Arthur Andersen, the accounting firm that audited Enron, had approved much of the structure. The firm later destroyed documents, and its conviction for obstruction was overturned in 2005, but by then the firm had largely collapsed."),
        ("What changed",
         "In 2002 Congress passed the Sarbanes-Oxley Act. It made top executives certify the accuracy of their accounts and set stronger rules for auditors. The lesson for anyone reading a company's books is simple: ask who benefits from a complicated structure."),
    ],
    "test": [
        ("What did mark-to-market accounting allow a firm to do?",
         [("a", "Book the expected profit of a long contract as income now"), ("b", "Pay no tax at all"), ("c", "Delay every payment for ten years"), ("d", "Avoid having any assets")], "a"),
        ("What were special purpose entities used for at Enron?",
         [("a", "To train new traders"), ("b", "To hold assets and debts away from the main accounts"), ("c", "To sell fresh water"), ("d", "To print banknotes")], "b"),
        ("When did Enron file for bankruptcy?",
         [("a", "In 1985"), ("b", "In 1995"), ("c", "In December 2001"), ("d", "In 2010")], "c"),
        ("What did Congress pass in 2002 in response?",
         [("a", "The Glass-Steagall Act"), ("b", "The Homestead Act"), ("c", "The Clayton Antitrust Act"), ("d", "The Sarbanes-Oxley Act")], "d"),
        ("What is the main lesson from the Enron story?",
         [("a", "Complicated structures can hide risk, so ask who benefits"), ("b", "Only small firms make accounting errors"), ("c", "Profit always shows up as cash on time"), ("d", "Auditors are never needed")], "a"),
    ],
}
