"""The Capital Asset Pricing Model: market risk, beta and the price of risk."""
CODE = "business4_capm"
BOOK = {
    "title": "The Capital Asset Pricing Model",
    "subtitle": "Market risk, beta and the price of risk",
    "chapters": [
        ("Two kinds of risk",
         "Some risk belongs to one company, such as a factory fire or a failed product. Other risk belongs to the whole market, such as a recession or a rise in interest rates. Holding many assets spreads away the first kind. The second kind stays, and it is the risk the market pays for."),
        ("What beta means",
         "Beta measures how far an asset moves with the market. A beta of 1 means it moves about in step with the market. Above 1 it swings more, and below 1 it swings less. A beta of 0 means it does not move with the market at all."),
        ("The risk-free rate",
         "The model starts from a return with no default risk, usually taken from government bonds of a reliable country. It is the reward for waiting, before any extra risk is taken."),
        ("The security market line",
         "The model draws a straight line. Expected return equals the risk-free rate, plus beta times the extra return the market is expected to earn above that rate. In a fair market, each asset should sit on this line. The line is a price list for risk."),
        ("Finding expected return from beta",
         "Suppose the risk-free rate is 2%, the market is expected to return 8%, and an asset has a beta of 1.5. The market's extra return is 6%. The asset's expected return is 2% plus 1.5 times 6%, which is 11%. In this model, a higher beta means a higher expected return."),
        ("Where it falls short",
         "Real markets show effects the model does not explain well. Small firms, and some cheap shares, have often returned more than beta predicts. Beta also changes over time, and it depends on the period and the index used. The model is a useful starting point, not a full picture."),
    ],
    "test": [
        ("Which risk does holding many assets remove?",
         [("a", "Market risk"), ("b", "Company-specific risk"), ("c", "Inflation"), ("d", "The price of gold")], "b"),
        ("What does a beta of 1.5 mean?",
         [("a", "The asset never moves with the market"), ("b", "The asset is free of risk"), ("c", "The asset tends to move about one and a half times as much as the market"), ("d", "The asset has no link to the market")], "c"),
        ("What is the risk-free rate in the model?",
         [("a", "The return on a random stock"), ("b", "The return on a loan to a friend"), ("c", "The return from an asset with no default risk, such as a reliable government bond"), ("d", "The profit of the biggest company")], "c"),
        ("In the security market line, what gives expected return?",
         [("a", "The risk-free rate, plus beta times the market's extra return"), ("b", "Beta divided by the market return"), ("c", "The price of the asset"), ("d", "The number of shares issued")], "a"),
        ("Which is a known limit of the model?",
         [("a", "It proves every stock is fairly priced"), ("b", "Some effects, such as small firms returning more than beta predicts, do not fit it well"), ("c", "It has no use at all"), ("d", "It needs no data")], "b"),
    ],
}
