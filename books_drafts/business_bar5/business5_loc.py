"""Letters of Credit: how a bank's promise lets strangers trade, the documents, the steps, the costs and the fraud risks."""
CODE = 'business5_loc'
BOOK = {
    "title": 'Letters of Credit',
    "subtitle": 'A bank promise that lets strangers trade safely',
    "chapters": [
        ('Trust between strangers',
         'A seller in one country may not know a buyer in another, and the buyer may not trust the seller to ship. A letter of credit solves this by putting a bank in the middle. The bank promises to pay the seller if the seller presents the right papers.'),
        ('The people involved',
         "There are usually four parties: the buyer, who is the applicant; the buyer's bank, which issues the letter; the seller, who is the beneficiary; and often a bank in the seller's country that advises and checks the letter. Each one has its own duties."),
        ('The documents are the deal',
         'The bank pays against documents, not against the goods themselves. Typical papers are the invoice, a bill of lading and an insurance certificate. If the papers match the letter exactly, the bank must pay, even if the buyer later complains.'),
        ('The steps',
         'The buyer asks its bank to open the letter. The seller ships the goods and presents the documents to the bank. The bank checks them, and if they match, it pays. The buyer then pays the bank back, often on a set date.'),
        ('Costs',
         'Banks charge fees for opening, amending and paying under a letter, and they may charge for confirming it. These costs are real, so letters are most common for large or risky trades between parties who do not know each other well. Compare the fee with the risk it removes.'),
        ('Fraud risks',
         'Because the bank deals in papers, a crook can try to forge documents or ship empty boxes. Courts in many countries will refuse to pay if they find clear fraud, but this is a hard exception to prove. Check every document and deal only with banks you know.'),
    ],
    "test": [
        ('What does a letter of credit mainly promise?',
         [('a', 'That the goods will be perfect'), ('b', 'That a bank will pay the seller when the right documents are presented'), ('c', 'That the buyer will never change the order'), ('d', 'That shipping is free')], 'b'),
        ('Who is the beneficiary in a letter of credit?',
         [('a', 'The buyer'), ('b', 'The bank that opens the letter'), ('c', 'The seller'), ('d', 'The shipping company')], 'c'),
        ('What does the bank pay against?',
         [('a', "The buyer's opinion of the goods"), ('b', 'A photo of the warehouse'), ('c', "The seller's promise alone"), ('d', 'The documents, which must match the letter')], 'd'),
        ('What is a main cost of a letter of credit?',
         [('a', 'Fees for opening, amending and paying under it'), ('b', 'A fee for each word in the letter'), ('c', 'A tax paid to the seller'), ('d', 'Nothing at all, ever')], 'a'),
        ('Why is fraud a risk even with a bank involved?',
         [('a', 'Banks never check papers'), ('b', 'Forged or empty-shipment papers can look correct to a bank that deals only in papers'), ('c', 'Letters of credit are spoken, not written'), ('d', 'Sellers always cheat')], 'b'),
    ],
}
