"""Fraud Losses and Controls: the main kinds of online fraud, how detection rules work, and how to weigh friction against loss."""
CODE = 'computing4_fraud_losses'
BOOK = {
    "title": 'Fraud Losses and Controls',
    "subtitle": 'The main kinds of online fraud, and how to weigh friction against loss',
    "chapters": [
        ('Fraud types',
         'Common online fraud includes stolen card details, account takeover, fake accounts and refund abuse. Each type has its own signs. Knowing the types helps a team choose which controls matter most.'),
        ('Detection rules',
         'A detection rule flags a transaction that looks unusual, such as a large order to a new address. Rules are simple to explain but can be evaded. Many teams combine rules with scoring that weighs several signals at once.'),
        ('Friction trade-offs',
         'Each extra check, such as a code sent to a phone, slows down honest customers and may lose some sales. Too little checking allows fraud. The right level balances the cost of friction against the expected loss from fraud.'),
        ('Losses per transaction',
         'Measure fraud losses as a share of transactions, and also as money lost per transaction. A low share can still hide large losses in a few big orders. Track both measures to see the true picture.'),
        ('Control costs',
         'Controls cost money to build and run, including staff who review cases. Compare the control cost with the losses it prevents. A control that costs more than the losses it stops is a poor choice.'),
        ('Reviewing outcomes',
         'Review how cases ended, including false alarms and missed fraud. Use the results to tune rules and to remove checks that no longer help. Regular review keeps the controls matched to the threats.'),
    ],
    "test": [
        ('Which is a common kind of online fraud?',
         [('a', 'Account takeover'), ('b', 'Choosing a new font'), ('c', 'Writing a poem'), ('d', 'Painting a logo')], 'a'),
        ('What is a detection rule?',
         [('a', 'A rule about desk tidiness'), ('b', 'A rule about lunch breaks'), ('c', 'A rule that flags an unusual transaction'), ('d', 'A rule about holidays')], 'c'),
        ('What is friction in this context?',
         [('a', 'Heat from a server'), ('b', 'Extra checks that slow honest customers down'), ('c', 'A dispute with a supplier'), ('d', 'A problem with the printer')], 'b'),
        ('Why measure losses both as a share and per transaction?',
         [('a', 'Only one measure is ever meaningful'), ('b', 'Both measures are always identical'), ('c', 'Neither measure can be calculated'), ('d', 'A low share can hide large losses in a few big orders')], 'd'),
        ('When is a control a poor choice?',
         [('a', 'When it costs more than the losses it prevents'), ('b', 'When it prevents any loss at all'), ('c', 'When it is reviewed each year'), ('d', 'When customers like it')], 'a'),
    ],
}
