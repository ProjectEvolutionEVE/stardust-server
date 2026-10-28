"""Selling Data Responsibly: what it takes to sell data products fairly, with consent, honest anonymisation and clear contracts."""
CODE = "computing5_selling_data"
BOOK = {
    "title": "Selling Data Responsibly",
    "subtitle": "Selling data products with consent, honest contracts and realistic promises",
    "chapters": [
        ("Data products",
         "A data product is information packaged for others to use, such as reports, feeds or summaries. Its value depends on accuracy, timeliness and clear documentation. Define exactly what is being sold."),
        ("Consent",
         "People who supply data must agree to how it will be used, and those terms must be honest. Consent given for one purpose does not cover another. Check the terms before each new sale."),
        ("Limits of anonymisation",
         "Removing names does not always make data anonymous. Combining several details can re-identify people. Treat anonymisation as a reduction of risk, not a guarantee."),
        ("Contracts",
         "Contracts for data should state permitted uses, security duties, retention limits and what happens at the end. Vague contracts lead to misuse and disputes. Read the terms before signing."),
        ("Pricing",
         "Price data by the value it gives buyers, the cost of producing it and the legal limits on use. Avoid prices that rest on selling personal details. Keep the pricing rules written down."),
        ("Reputational risk",
         "A data scandal can damage trust far beyond any single sale. Ask whether customers and the public would accept the sale. If the answer is unclear, do not proceed."),
    ],
    "test": [
        ("What is a data product?",
         [("a", "A type of printer ink"), ("b", "Information packaged for others to use, such as reports or feeds"), ("c", "A staff uniform"), ("d", "A kitchen appliance")], "b"),
        ("Why must consent be checked before each new sale?",
         [("a", "Consent is never needed"), ("b", "Consent only matters for printing"), ("c", "Consent expires at lunch"), ("d", "Consent for one purpose does not cover another")], "d"),
        ("Why is removing names not always enough to anonymise data?",
         [("a", "Combining several details can re-identify people"), ("b", "Names are the only personal detail"), ("c", "Anonymised data is always public"), ("d", "Names are required by law to stay")], "a"),
        ("What should a data contract state?",
         [("a", "The name of the office cat"), ("b", "The weather on the signing day"), ("c", "Permitted uses, security duties and retention limits"), ("d", "A promise of unlimited use")], "c"),
        ("What is a sensible test before a sale?",
         [("a", "Whether the price is round"), ("b", "Whether customers and the public would accept it"), ("c", "Whether the logo is blue"), ("d", "Whether the sale is on a Monday")], "b"),
    ],
}
