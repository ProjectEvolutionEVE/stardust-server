"""Auditing: what an audit is, independence, sampling, the opinion, fraud against error, and the auditor's limits."""
CODE = 'business4_auditing'
BOOK = {
    "title": 'Auditing',
    "subtitle": "How an outside check gives readers confidence in a company's accounts",
    "chapters": [
        ('What an audit is',
         "An audit is an independent examination of a company's financial statements. The auditor checks that the figures are a fair picture of the firm's position and results. The audit gives readers, such as lenders and shareholders, a reason to trust the numbers."),
        ('Independence',
         "An auditor must be independent of the company, in fact and in appearance. A firm that is paid to design a company's systems and also checks them has a conflict. Rules limit close ties, gifts and dual roles, so the auditor can give an honest view."),
        ('Sampling',
         'Auditors cannot check every transaction. Instead they select a sample, test it carefully, and use the results to judge the whole. The sample must be large and chosen well enough to give a reasonable basis for the conclusion.'),
        ('The opinion',
         'At the end of the audit, the auditor gives an opinion. A clean opinion means the statements are fairly presented in all material respects. A qualified or adverse opinion signals problems. The opinion is the main output that readers rely on.'),
        ('Fraud against error',
         'An audit looks for material misstatements, whether from error or fraud. Errors are honest mistakes. Fraud is deliberate, and it is harder to detect because it is often hidden. Auditors plan their work with both possibilities in mind, though they cannot promise to find every case.'),
        ("The auditor's limits",
         'An audit gives reasonable assurance, not a guarantee. Sampling, the limits of evidence, and the skill of those who hide wrongdoing all restrict what can be found. An audit is one part of a wider system of controls, not a complete shield against failure.'),
    ],
    "test": [
        ('What is an audit?',
         [('a', 'A sale of company shares'), ('b', 'A loan from a bank'), ('c', "An independent examination of a company's financial statements"), ('d', 'An advertising campaign')], 'c'),
        ('Why must an auditor be independent?',
         [('a', 'So the auditor can share the profits'), ('b', 'So the auditor never reads the accounts'), ('c', 'So the auditor can run the sales team'), ('d', 'So the auditor can give an honest view of the accounts')], 'd'),
        ('Why do auditors use sampling?',
         [('a', 'Because checking every transaction is not practical'), ('b', 'Because sampling is required to remove all risk'), ('c', 'Because sampling makes the accounts cheaper to print'), ('d', 'Because sampling replaces the opinion')], 'a'),
        ('What does a clean audit opinion mean?',
         [('a', 'The firm will never fail'), ('b', 'The statements are fairly presented in all material respects'), ('c', 'The firm is guaranteed to make a profit'), ('d', 'The firm has no staff')], 'b'),
        ('How does fraud differ from error?',
         [('a', 'Fraud is always accidental'), ('b', 'Error is always deliberate'), ('c', 'Fraud is deliberate, while error is an honest mistake'), ('d', 'There is no difference')], 'c'),
    ],
}
