"""Capitalising Software and Depreciation: how a company records software it builds, and how that affects reported profit."""
CODE = 'computing4_capitalising_software'
BOOK = {
    "title": 'Capitalising Software and Depreciation',
    "subtitle": 'How a company records software it builds, and how that changes reported profit',
    "chapters": [
        ('Development stages',
         'Software work usually moves through stages, such as research, planning, building and testing. Early research is normally expensed. Later building work may be recorded as an asset, depending on the accounting rules. The stage matters.'),
        ('Capitalisation rules',
         'Capitalising means recording a cost as an asset on the balance sheet, rather than as an expense at once. Accounting standards give conditions that must be met first, such as technical feasibility and a clear intention to finish. Rules differ between frameworks.'),
        ('Amortisation periods',
         'Once an asset is in use, its cost is spread over its useful life, which is called amortisation. The period is a judgement, and it should reflect how long the software will really serve. Review it when plans change.'),
        ('Impairment',
         'If the software is no longer expected to deliver its value, its recorded amount must be reduced. This is an impairment. Abandoned projects are a common reason, and recognising them promptly keeps accounts honest.'),
        ('Effect on profit',
         'Capitalising spreads cost over several years, so profit this year looks higher than if all costs were expensed. The total profit over the life is the same. Readers of accounts should understand this timing effect.'),
        ('Accounting records',
         'Keep clear records of hours, costs and decisions for each capitalised project. Auditors often ask for evidence. Good records also help the team learn which projects delivered value.'),
    ],
    "test": [
        ('What does capitalising a cost mean?',
         [('a', 'Writing it in capital letters'), ('b', 'Paying it in cash only'), ('c', 'Recording it as an asset rather than an expense at once'), ('d', 'Deleting it from the records')], 'c'),
        ('What is amortisation?',
         [('a', 'Spreading an asset cost over its useful life'), ('b', 'A type of loan from the bank'), ('c', 'A fee paid to a lawyer'), ('d', 'A name for a bug')], 'a'),
        ('What is an impairment?',
         [('a', 'A medical injury'), ('b', 'A pay rise'), ('c', 'A new office'), ('d', 'A reduction in the recorded value of an asset that will not deliver its value')], 'd'),
        ('Why can capitalising make profit look higher this year?',
         [('a', 'Because costs are doubled'), ('b', 'Because cost is spread across several years'), ('c', 'Because sales are hidden'), ('d', 'Because accounts are never checked')], 'b'),
        ('Why keep clear records for capitalised projects?',
         [('a', 'So the records can be lost'), ('b', 'So nobody needs to read them'), ('c', 'Auditors often ask for evidence of the costs'), ('d', 'So the amounts can grow automatically')], 'c'),
    ],
}
