"""Data Governance for Operations: ownership, quality, master data, access, standards and audits."""
CODE = 'mining5_data_gov'
BOOK = {
    "title": "Data Governance for Operations",
    "subtitle": "Ownership, quality, master data and access",
    "chapters": [
        ("Why data needs rules",
         "Operations run on data: production figures, maintenance records and supplier details. Bad data leads to bad decisions and wasted money. Data governance sets the rules for who looks after the data and how."),
        ("Data ownership",
         "A data owner is the person accountable for a set of data and its quality. Owners decide who may use the data and what it means. Without an owner, errors are nobody's job to fix."),
        ("Master data",
         "Master data is the core shared data, such as site, asset and supplier records, used across many systems. Keep one trusted version of each record. Duplicates in master data cause errors that spread everywhere."),
        ("Quality",
         "Good data is complete, accurate and consistent across systems. Quality rules check these things automatically at entry. Regular checks catch problems before they reach a report."),
        ("Access",
         "Access rules control who can see and change the data. People should have only the access their job needs. Logs of changes show what happened, and who did it."),
        ("Standards and audits",
         "Common standards for names, units and codes make data easy to share. Audits check that the data is still accurate and used properly. Findings lead to clear fixes with owners and dates."),
    ],
    "test": [
        ("Who is a data owner?",
         [("a", "The person who types the data in"), ("b", "The person accountable for a set of data and its quality"), ("c", "The IT vendor"), ("d", "Any visitor to the site")], "b"),
        ("What is master data?",
         [("a", "A recording of the boss's speeches"), ("b", "The core shared data, such as site or supplier records, used across systems"), ("c", "A backup of personal files"), ("d", "A list of old emails")], "b"),
        ("Why control who can access data?",
         [("a", "So nobody can use the data"), ("b", "So reports are never written"), ("c", "So data is always deleted"), ("d", "So only the right people see and change the data")], "d"),
        ("Which is a sign of good data quality?",
         [("a", "Many duplicate records"), ("b", "Records with no owner"), ("c", "Values that are complete, accurate and consistent"), ("d", "Data stored in no system")], "c"),
        ("Why audit data?",
         [("a", "To find ways to avoid reporting"), ("b", "To check the data is still accurate and used properly"), ("c", "To delete every record"), ("d", "To replace all staff")], "b"),
    ],
}
