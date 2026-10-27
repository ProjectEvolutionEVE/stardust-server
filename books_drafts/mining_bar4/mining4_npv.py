"""Net Present Value of a Mine: discounting future cash flows to decide whether a project is worth doing."""
CODE = 'mining4_npv'
BOOK = {
    "title": 'Net Present Value of a Mine',
    "subtitle": 'Discounting future cash to decide whether a project is worth doing',
    "chapters": [
        ('Money later is worth less',
         'Money received in the future is worth less than the same money today, because it could be invested in the meantime. Discounting turns future cash into its value today.'),
        ('Capital and operating costs',
         'A mine has big up-front capital costs for building, and then steady operating costs while it runs. Revenue from metal sales comes in over the years, and all these flows are counted.'),
        ('Choosing a discount rate',
         'The discount rate reflects the time value of money and the risk of the project. A riskier project is usually discounted at a higher rate, so its later cash counts for less.'),
        ('NPV versus payback',
         "Payback time counts how long until the money is recovered, and ignores what happens later. Net present value adds up every year's discounted cash, so it captures the full life of the mine."),
        ('Sensitivity',
         'Analysts test how the NPV changes if the metal price, the grade of ore or the costs change. A project that stays positive across the likely range is more solid.'),
        ('Decisions',
         'A project with a positive net present value at the chosen rate adds value. A negative one destroys it. The number helps compare options, but it is one input among several.'),
    ],
    "test": [
        ('What does discounting do to future cash?',
         [('a', 'Doubles it every year'), ('b', 'Hides it from the books'), ('c', 'Turns it into its value today'), ('d', 'Moves it to the next country')], 'c'),
        ('What is an up-front capital cost?',
         [('a', 'The large cost of building the mine before it earns'), ('b', 'The cost of a single pencil'), ('c', 'A fee paid after the mine closes'), ('d', 'A gift to the workers')], 'a'),
        ('What does a riskier project usually get?',
         [('a', 'A lower discount rate, always'), ('b', 'No discount at all'), ('c', 'A free ride'), ('d', 'A higher discount rate')], 'd'),
        ('Why is NPV preferred to payback time?',
         [('a', 'It ignores all costs'), ('b', 'It counts the whole life of the mine, not only the early years'), ('c', 'It is easier to say aloud'), ('d', 'It needs no numbers')], 'b'),
        ('What is sensitivity analysis?',
         [('a', 'Measuring how loud the mill is'), ('b', 'Checking the temperature of the office'), ('c', 'Testing how the NPV changes when prices, grade or costs change'), ('d', 'Counting the staff')], 'c'),
    ],
}
