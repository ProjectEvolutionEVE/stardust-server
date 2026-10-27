"""Safety and Assurance Cases: structured arguments, backed by evidence, that a system is safe enough for its use."""
CODE = 'computing5_assurance_cases'
BOOK = {
    "title": 'Safety and Assurance Cases',
    "subtitle": 'Claims, arguments and evidence, set out so others can check them',
    "chapters": [
        ('What an assurance case is',
         'An assurance case is a documented argument that a system is acceptably safe or secure for its use. It sets out what is claimed, why it is believed and what proves it. Regulators and independent reviewers often read them.'),
        ('Claims, arguments and evidence',
         'A claim is a statement, such as the brake system will stop the vehicle in time. An argument explains why the claim follows from smaller claims. Evidence, such as test results and analysis, supports the lowest-level claims.'),
        ('Goal Structuring Notation',
         'Goal Structuring Notation, or GSN, is a graphical way to show claims, strategies, context and evidence. Its goal-and-strategy tree makes the reasoning easy to follow. It helps reviewers see where the argument is weak.'),
        ('Confidence',
         'Confidence describes how strongly the evidence supports each claim. Some claims rest on tested evidence, while others rest on assumptions. Making assumptions explicit shows where more work is needed.'),
        ('Review',
         'Independent review tests whether the argument is complete and the evidence is relevant. Reviewers ask what would make the claims false. Honest review finds gaps before the system is used.'),
        ('Links to certification',
         'Many certification schemes ask for evidence that a system meets its requirements. An assurance case gathers that evidence into one structure. It does not replace the standards, but it helps show how they were met.'),
    ],
    "test": [
        ('What is an assurance case?',
         [('a', 'A case for carrying a laptop'), ('b', 'A documented argument that a system is acceptably safe or secure'), ('c', 'A box for spare cables'), ('d', 'A legal case about a car park')], 'b'),
        ('What does a claim do in an assurance case?',
         [('a', 'It sets the price of the product'), ('b', 'It chooses the office colour'), ('c', 'It counts the staff'), ('d', 'It states something the system must achieve')], 'd'),
        ('What is Goal Structuring Notation?',
         [('a', 'A graphical way to show claims, strategies, context and evidence'), ('b', 'A written code for musical notes'), ('c', 'A shorthand for shopping lists'), ('d', 'A map key for hiking trails')], 'a'),
        ('What does confidence describe?',
         [('a', 'How loud the alarm is'), ('b', 'How many engineers are on holiday'), ('c', 'How strongly the evidence supports each claim'), ('d', 'The price of the steel')], 'c'),
        ('What do independent reviewers look for?',
         [('a', 'Pictures of the team'), ('b', 'The age of the office chairs'), ('c', 'The number of coffee cups'), ('d', 'Gaps in the argument and evidence that is not relevant')], 'd'),
    ],
}
