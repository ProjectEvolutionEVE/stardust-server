"""Activity Coefficients and Non-Ideal Solutions: ionic strength, Debye-Hückel theory and correcting equilibrium constants."""
CODE = "science5_chem_activity"
BOOK = {
    "title": "Activity Coefficients and Non-Ideal Solutions",
    "subtitle": "Ionic strength, Debye-Hückel theory and activity versus concentration",
    "chapters": [
        ("Solutions are not ideal", "In dilute solutions, concentration and effective behaviour are close. In more concentrated or charged solutions, ions interact and the simple rules fail. Activity corrects for these interactions."),
        ("Activity versus concentration", "Activity is the effective concentration of a species, which equals its concentration times an activity coefficient. For ideal solutions the coefficient is one. For real ionic solutions it is often below one."),
        ("Ionic strength", "Ionic strength is a measure of the total charge in a solution. It is half the sum of each ion's concentration multiplied by the square of its charge. Higher ionic strength usually lowers activity coefficients."),
        ("Debye-Hückel theory", "Debye-Hückel theory explains how ions shield each other and reduce their effective activity. It gives a simple formula for the activity coefficient at low ionic strength. The theory works well only in dilute solutions."),
        ("Electrolyte solutions", "Electrolyte solutions contain dissolved ions that carry charge. Their behaviour depends strongly on the ionic strength. Engineers and chemists must allow for this when designing processes."),
        ("Correcting equilibrium constants", "Equilibrium constants are defined with activities. When working with concentrations, the constant must be corrected by the activity coefficients. Failing to correct gives wrong predictions of how far a reaction goes."),
    ],
    "test": [
        ("What is activity?",
         [("a", "The number of people in a lab"), ("b", "The loudness of a stirring bar"), ("c", "The colour of a flask"), ("d", "The effective concentration of a species")], "d"),
        ("For an ideal solution, what is the activity coefficient?",
         [("a", "Zero"), ("b", "A hundred"), ("c", "A large negative number"), ("d", "One")], "d"),
        ("What does ionic strength measure?",
         [("a", "The total charge in a solution"), ("b", "The total weight of the glassware"), ("c", "The colour of the indicator"), ("d", "The age of the solvent")], "a"),
        ("What does Debye-Hückel theory explain?",
         [("a", "How plants grow in sunlight"), ("b", "How clouds form in the sky"), ("c", "How ions shield each other and reduce their effective activity"), ("d", "How metal rusts in air")], "c"),
        ("Why must equilibrium constants be corrected for activity?",
         [("a", "Because constants change with the day of the week"), ("b", "Because constants are always wrong"), ("c", "Because flasks are heavy"), ("d", "Because the constants are defined using activities, not concentrations")], "d"),
    ],
}
