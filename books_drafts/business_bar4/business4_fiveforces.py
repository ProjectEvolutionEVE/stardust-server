"""Porter's Five Forces: rivals, new entrants, substitutes, buyers, suppliers, and how to read an industry."""
CODE = 'business4_fiveforces'
BOOK = {
    "title": "Porter's Five Forces",
    "subtitle": 'Five pressures that decide how much profit an industry can keep',
    "chapters": [
        ('Rivals',
         'The first force is the competition among firms already in the industry. When rivals are many, similar and fighting over the same customers, prices and profits tend to fall. When there are few rivals with clear advantages, profits are easier to keep.'),
        ('New entrants',
         'New firms can join an industry and add capacity. High barriers, such as large start-up costs, patents, strong brands or licences, make entry harder and protect the profit of those already inside. Low barriers invite more competition.'),
        ('Substitutes',
         'A substitute meets the same need in a different way. Email can replace a letter, and a bus ride can replace a taxi. The more good substitutes there are, and the cheaper they are, the less room a firm has to raise its prices.'),
        ('Buyers',
         'Powerful buyers can press prices down. They are strong when they buy in large volumes, when switching is cheap, or when the product is a small share of their costs. A firm with many small buyers usually has more room to earn profit.'),
        ('Suppliers',
         "Suppliers are strong when only a few sell the input, or when switching to another input is costly. A firm that depends on one scarce supplier may find its costs rising at the supplier's whim. Good relations and several sources can weaken this force."),
        ('Reading an industry',
         'Michael Porter introduced the five forces in 1979. To use the model, list each force, rate how strong it is, and ask what the firm can do to reduce the pressure. The aim is not to predict everything, but to see where the profit in an industry tends to go.'),
    ],
    "test": [
        ("Which of these is one of Porter's five forces?",
         [('a', 'Government spending'), ('b', 'The weather'), ('c', 'Interest on the national debt'), ('d', 'New entrants')], 'd'),
        ('What makes entry into an industry harder?',
         [('a', 'High barriers such as large start-up costs'), ('b', 'Many small firms with cheap products'), ('c', 'Low costs of switching suppliers'), ('d', 'Falling demand for the product')], 'a'),
        ('What is a substitute?',
         [('a', 'A worker who fills in for someone on leave'), ('b', 'A product that meets the same need in a different way'), ('c', 'A kind of bank loan'), ('d', 'A payment made in advance')], 'b'),
        ('When are buyers most powerful?',
         [('a', 'When there are thousands of tiny buyers'), ('b', 'When the product is their only choice'), ('c', 'When they buy in large volumes and switching is cheap'), ('d', 'When they never compare prices')], 'c'),
        ('In what year did Michael Porter introduce the five forces model?',
         [('a', '1949'), ('b', '1999'), ('c', '2009'), ('d', '1979')], 'd'),
    ],
}
