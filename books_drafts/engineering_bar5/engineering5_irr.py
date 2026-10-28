"""Internal Rate of Return and Its Pitfalls: the rate definition, multiple roots, reinvestment and comparison with NPV."""
CODE = 'engineering5_irr'
BOOK = {'title': 'Internal Rate of Return and Its Pitfalls',
 'subtitle': 'What the rate means, where it can mislead, and why NPV often gives the clearer answer',
 'chapters': [('What the rate means',
               'The internal rate of return, or IRR, is the discount rate at which a project’s NPV becomes '
               'zero. It gives one percentage that summarises the return of a project. Managers like it '
               'because it is easy to compare with a target rate.'),
              ('Multiple roots',
               'If a project’s cash flows change sign more than once, the IRR equation can have more than '
               'one answer. A project may then show several rates that each make the NPV zero. In that case '
               'the IRR alone does not give a clear answer.'),
              ('Reinvestment assumptions',
               'The IRR assumes that cash received during the project can be reinvested at the same rate. '
               'That may not be realistic. If the real reinvestment rate is lower, the IRR overstates the '
               'value of the project.'),
              ('Comparing with NPV',
               'NPV gives the value added in money terms at a chosen rate. When two projects differ in size, '
               'a high IRR on a small project can still add less money than a lower IRR on a large one. NPV '
               'shows the money difference directly.'),
              ('A practical rule',
               'Use IRR as a helpful signal, and check it with NPV. Look at the cash flows before trusting '
               'the single percentage. The two methods agree most of the time, and where they disagree, NPV '
               'is usually the safer guide.'),
              ('The money side of the choice',
               'The choice between IRR and NPV affects how much money a company commits. A ranking by '
               'percentage can send capital to the wrong project. Comparing the money added keeps the '
               'decision tied to what the company can actually gain.')],
 'test': [('What is the internal rate of return?',
           [('a', 'The rate of pay for the workers'),
            ('b', 'The price of steel per tonne'),
            ('c', 'The discount rate at which the NPV becomes zero'),
            ('d', 'The number of hours in a shift')],
           'c'),
          ('When can an IRR have more than one answer?',
           [('a', 'When the project is painted'),
            ('b', 'When the team is large'),
            ('c', 'When the sun is out'),
            ('d', 'When the cash flows change sign more than once')],
           'd'),
          ('What does the IRR assume about money received during a project?',
           [('a', 'That it can be reinvested at the same rate'),
            ('b', 'That it is burned'),
            ('c', 'That it is always lost'),
            ('d', 'That it is hidden in a box')],
           'a'),
          ('What does NPV show directly that IRR does not?',
           [('a', 'The colour of the project plans'),
            ('b', 'The money added by the project at a chosen rate'),
            ('c', 'The height of the building'),
            ('d', 'The name of the project lead')],
           'b'),
          ('Which is usually the safer guide when the two methods disagree?',
           [('a', 'The weather forecast'),
            ('b', 'The office coffee machine'),
            ('c', 'NPV'),
            ('d', 'A coin toss')],
           'c')]}
