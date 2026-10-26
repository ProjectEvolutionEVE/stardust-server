"""Modelling in a Spreadsheet: inputs apart from formulas, layout, checks, a famous spreadsheet error, documenting and review."""
CODE = "business5_spreadsheet"
BOOK = {
    "title": "Modelling in a Spreadsheet",
    "subtitle": "Inputs apart from formulas, layout, checks, common errors, documenting and review",
    "chapters": [
        ("Keep inputs apart", "Put every input, such as a rate or a price, in one clearly labelled place. Formulas should refer to those inputs rather than hide numbers inside them. Then changing an assumption means changing one cell."),
        ("Layout", "Arrange the model in a logical flow, usually from inputs to calculations to outputs. Use consistent rows and columns, and avoid scattering blocks across the sheet. A clear layout helps the next reader follow the logic."),
        ("Checks", "Build checks into the model, such as totals that must match or balances that must be zero. A failed check flags an error early. A good model checks itself."),
        ("A famous error", "A 2010 economics paper on debt and growth was later found to contain a spreadsheet error. A formula range left out some countries, and the mistake changed the published result. Other common errors include wrong cell references and numbers typed over formulas."),
        ("Documenting", "Write down what the model does, what each input means, and where the data came from. Notes inside the file are worth their time. A model without documentation is hard to trust."),
        ("Review", "Ask another person to review the model before anyone relies on it. A fresh pair of eyes often finds errors the author has stopped seeing. Review is a standard part of careful financial work."),
    ],
    "test": [
        ("Where should inputs sit in a model?",
         [("a", "Hidden inside formulas"), ("b", "In random cells"), ("c", "In a secret tab"), ("d", "In one clearly labelled place")], "d"),
        ("What is a check in a model?",
         [("a", "A total that must match or a balance that must be zero"), ("b", "A cheque for money"), ("c", "A pen mark"), ("d", "A picture")], "a"),
        ("What kind of error was found in a famous 2010 economics paper?",
         [("a", "A spelling mistake"), ("b", "A missing photo"), ("c", "A formula range that left out some countries"), ("d", "A wrong colour")], "c"),
        ("What does documenting a model include?",
         [("a", "Hiding the sources"), ("b", "What each input means and where the data came from"), ("c", "Deleting the notes"), ("d", "Keeping no records")], "b"),
        ("Why ask another person to review a model?",
         [("a", "To make it longer"), ("b", "To delay it"), ("c", "To remove all inputs"), ("d", "A fresh pair of eyes often finds errors the author has missed")], "d"),
    ],
}
